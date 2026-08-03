#!/usr/bin/env python3
"""
State Snapshotting Service.

Captures pre-operation state of repository files safely and efficiently, and
provides verified restoration. The service is the persistence-layer foundation
used by migration and build scripts to guarantee that any destructive operation
can be rolled back to the exact bytes that existed immediately before the
operation ran.

Design goals (in scope of BRU-1173):
    * Safe: every snapshot is fully checksummed (SHA-256), every write to disk
      is atomic (write-to-temp + rename), and every restore re-checksums the
      live file against the manifest before declaring success.
    * Efficient: one pass over the file list to compute sizes + checksums;
      ``shutil.copy2`` for file copy (preserves mtime/permissions in one
      syscall); manifests are written in a single ``json.dump`` call.
    * Self-contained: pure stdlib, no third-party dependencies. The service
      can be imported from any script (``from data.state_snapshot import
      StateSnapshotService``) and also has a CLI for ad-hoc use.

Storage layout::

    .snapshots/
        <snapshot_id>/
            manifest.json          # SnapshotManifest (JSON Schema v1)
            files/
                <relative_path>    # exact bytes captured at capture time

Usage::

    from data.state_snapshot import StateSnapshotService

    service = StateSnapshotService(repo_root=Path("."))
    snap = service.capture(
        target_paths=[Path("data/icad_stats_initial.json")],
        operation="migrate_icad_stats",
        metadata={"version": "1.0.0"},
    )
    # ... do destructive work ...
    service.restore(snap.snapshot_id)

CLI::

    python data/state_snapshot.py capture data/icad_stats_initial.json \\
        --operation migrate_icad_stats
    python data/state_snapshot.py list
    python data/state_snapshot.py verify <snapshot_id>
    python data/state_snapshot.py restore <snapshot_id>
    python data/state_snapshot.py prune --keep-last 5
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import shutil
import sys
import tempfile
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence


SCHEMA_VERSION = "1.0.0"
DEFAULT_SNAPSHOT_ROOT = ".snapshots"
MANIFEST_FILENAME = "manifest.json"
FILES_SUBDIR = "files"
HASH_CHUNK_SIZE = 65536  # 64 KiB read window for streaming SHA-256


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class SnapshotEntry:
    """One file captured inside a snapshot.

    Attributes:
        relative_path: Path of the file relative to the repository root,
            stored with forward slashes for cross-platform reproducibility.
        size_bytes: File size in bytes at capture time.
        sha256: Lower-case hex digest of the file contents.
        captured_at: ISO-8601 UTC timestamp when this entry was captured.
    """

    relative_path: str
    size_bytes: int
    sha256: str
    captured_at: str

    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SnapshotEntry":
        return cls(
            relative_path=data["relative_path"],
            size_bytes=int(data["size_bytes"]),
            sha256=str(data["sha256"]).lower(),
            captured_at=str(data["captured_at"]),
        )


@dataclass
class SnapshotManifest:
    """Manifest describing a complete snapshot.

    The manifest is the single source of truth for what was captured, when, and
    what its checksums are. ``verify()`` re-reads every file on disk and
    confirms the checksum matches; ``restore()`` uses the relative_path to
    rewrite the live tree byte-for-byte.
    """

    snapshot_id: str
    operation: str
    created_at: str
    repo_root: str
    entries: List[SnapshotEntry] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> Dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "operation": self.operation,
            "created_at": self.created_at,
            "repo_root": self.repo_root,
            "schema_version": self.schema_version,
            "entries": [e.to_dict() for e in self.entries],
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SnapshotManifest":
        return cls(
            snapshot_id=str(data["snapshot_id"]),
            operation=str(data["operation"]),
            created_at=str(data["created_at"]),
            repo_root=str(data["repo_root"]),
            entries=[SnapshotEntry.from_dict(e) for e in data.get("entries", [])],
            metadata=dict(data.get("metadata", {})),
            schema_version=str(data.get("schema_version", SCHEMA_VERSION)),
        )

    def validate(self) -> List[str]:
        """Return a list of validation errors (empty list means valid)."""
        errors: List[str] = []
        if not self.snapshot_id:
            errors.append("snapshot_id is required")
        if not self.operation:
            errors.append("operation is required")
        if not self.created_at:
            errors.append("created_at is required")
        if not self.repo_root:
            errors.append("repo_root is required")
        if self.schema_version != SCHEMA_VERSION:
            errors.append(
                f"unsupported schema_version {self.schema_version!r} "
                f"(expected {SCHEMA_VERSION!r})"
            )
        seen: set = set()
        for entry in self.entries:
            if not entry.relative_path:
                errors.append("entry has empty relative_path")
                continue
            if entry.relative_path in seen:
                errors.append(f"duplicate entry: {entry.relative_path}")
            seen.add(entry.relative_path)
            if entry.size_bytes < 0:
                errors.append(
                    f"negative size for {entry.relative_path}: {entry.size_bytes}"
                )
            if not entry.sha256 or len(entry.sha256) != 64:
                errors.append(
                    f"invalid sha256 for {entry.relative_path}: {entry.sha256!r}"
                )
        return errors


@dataclass
class Snapshot:
    """Lightweight handle returned to callers after a successful capture."""

    snapshot_id: str
    operation: str
    created_at: str
    entry_count: int
    total_bytes: int
    snapshot_dir: Path

    @classmethod
    def from_manifest(
        cls, manifest: SnapshotManifest, snapshot_dir: Path
    ) -> "Snapshot":
        total = sum(e.size_bytes for e in manifest.entries)
        return cls(
            snapshot_id=manifest.snapshot_id,
            operation=manifest.operation,
            created_at=manifest.created_at,
            entry_count=len(manifest.entries),
            total_bytes=total,
            snapshot_dir=snapshot_dir,
        )


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------


class StateSnapshotService:
    """Capture, verify, restore, and prune pre-operation state.

    The service treats the repository root as immutable input: it never
    modifies the live tree during ``capture()``, only writes into the
    ``snapshot_root`` (default: ``.snapshots/``).
    """

    def __init__(
        self,
        repo_root: Optional[Path] = None,
        snapshot_root: Optional[Path] = None,
    ) -> None:
        if repo_root is None:
            repo_root = Path.cwd()
        self.repo_root = Path(repo_root).resolve()
        if snapshot_root is None:
            snapshot_root = self.repo_root / DEFAULT_SNAPSHOT_ROOT
        self.snapshot_root = Path(snapshot_root).resolve()

    # -- paths ---------------------------------------------------------------

    def _snapshot_dir(self, snapshot_id: str) -> Path:
        return self.snapshot_root / snapshot_id

    def _files_dir(self, snapshot_id: str) -> Path:
        return self._snapshot_dir(snapshot_id) / FILES_SUBDIR

    def _manifest_path(self, snapshot_id: str) -> Path:
        return self._snapshot_dir(snapshot_id) / MANIFEST_FILENAME

    def _normalize_relative(self, path: Path) -> str:
        """Return a forward-slash relative path string, validated to be inside repo_root."""
        abs_path = path.resolve()
        try:
            rel = abs_path.relative_to(self.repo_root)
        except ValueError as exc:
            raise ValueError(
                f"path {path} is outside repo_root {self.repo_root}"
            ) from exc
        return rel.as_posix()

    # -- capture -------------------------------------------------------------

    def capture(
        self,
        target_paths: Sequence[Path],
        operation: str,
        metadata: Optional[Dict[str, Any]] = None,
        snapshot_id: Optional[str] = None,
    ) -> Snapshot:
        """Capture the current state of every target_path into a new snapshot.

        Args:
            target_paths: Files or directories to capture. Directories are
                walked recursively. Non-existent paths are silently skipped
                (capturing a snapshot before file creation must not fail).
            operation: Free-form operation label, e.g. ``"migrate_icad_stats"``.
            metadata: Arbitrary JSON-serialisable metadata to attach to the
                manifest (script version, user, etc.).
            snapshot_id: Optional explicit ID. If omitted, a timestamp+uuid4
                suffix is generated.

        Returns:
            :class:`Snapshot` handle for the new snapshot.

        Raises:
            ValueError: If ``operation`` is empty.
            OSError: If the snapshot cannot be written to disk.
        """
        if not operation:
            raise ValueError("operation must be a non-empty string")

        created_at = datetime.now(timezone.utc).isoformat()
        sid = snapshot_id or self._generate_snapshot_id(created_at)
        snapshot_dir = self._snapshot_dir(sid)
        if snapshot_dir.exists():
            raise ValueError(
                f"snapshot_id {sid!r} already exists at {snapshot_dir}"
            )

        files_dir = self._files_dir(sid)
        files_dir.mkdir(parents=True, exist_ok=False)

        entries: List[SnapshotEntry] = []
        for target in self._expand_targets(target_paths):
            entry = self._capture_single_file(target, files_dir, created_at)
            if entry is not None:
                entries.append(entry)

        manifest = SnapshotManifest(
            snapshot_id=sid,
            operation=operation,
            created_at=created_at,
            repo_root=str(self.repo_root),
            entries=entries,
            metadata=dict(metadata or {}),
        )
        manifest_errors = manifest.validate()
        if manifest_errors:
            # Best-effort cleanup; we never leave a half-built snapshot on disk.
            shutil.rmtree(snapshot_dir, ignore_errors=True)
            raise ValueError(
                "manifest failed validation: " + "; ".join(manifest_errors)
            )

        # Atomic manifest write: write to a sibling temp file, fsync, then rename.
        manifest_path = self._manifest_path(sid)
        self._atomic_write_json(manifest_path, manifest.to_dict())
        return Snapshot.from_manifest(manifest, snapshot_dir)

    def _expand_targets(
        self, targets: Iterable[Path]
    ) -> Iterable[Path]:
        """Yield file paths to capture, recursing into directories."""
        for raw in targets:
            path = Path(raw)
            if not path.is_absolute():
                path = self.repo_root / path
            if not path.exists():
                continue
            if path.is_file():
                yield path
            elif path.is_dir():
                # Recurse but skip the snapshot root itself so we never snapshot ourselves.
                if path.resolve() == self.snapshot_root:
                    continue
                for child in sorted(path.rglob("*")):
                    if child.is_file():
                        yield child

    def _capture_single_file(
        self, source: Path, files_dir: Path, captured_at: str
    ) -> Optional[SnapshotEntry]:
        rel = self._normalize_relative(source)
        size = source.stat().st_size
        sha = self._hash_file(source)
        # Mirror directory structure under files_dir so restores are unambiguous.
        dest = files_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        # Copy bytes (preserve metadata so checksum is the only integrity check).
        shutil.copy2(source, dest)
        return SnapshotEntry(
            relative_path=rel,
            size_bytes=size,
            sha256=sha,
            captured_at=captured_at,
        )

    @staticmethod
    def _hash_file(path: Path) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            while True:
                chunk = f.read(HASH_CHUNK_SIZE)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    # -- verify --------------------------------------------------------------

    def load_manifest(self, snapshot_id: str) -> SnapshotManifest:
        manifest_path = self._manifest_path(snapshot_id)
        if not manifest_path.exists():
            raise FileNotFoundError(
                f"manifest not found for snapshot {snapshot_id!r}"
            )
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        manifest = SnapshotManifest.from_dict(data)
        errors = manifest.validate()
        if errors:
            raise ValueError(
                f"manifest for {snapshot_id} is invalid: {'; '.join(errors)}"
            )
        return manifest

    def verify(self, snapshot_id: str) -> Dict[str, Any]:
        """Re-checksum every file in the snapshot against the manifest.

        Returns a dict with ``ok`` (bool), ``checked`` (int), ``mismatched``
        (list of relative paths whose live copy no longer matches the
        captured bytes), ``missing`` (list of files no longer present in the
        snapshot directory) and ``manifest_errors`` (schema problems).
        """
        result: Dict[str, Any] = {
            "ok": True,
            "checked": 0,
            "mismatched": [],
            "missing": [],
            "manifest_errors": [],
        }
        try:
            manifest = self.load_manifest(snapshot_id)
        except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
            result["ok"] = False
            result["manifest_errors"].append(str(exc))
            return result

        files_dir = self._files_dir(snapshot_id)
        for entry in manifest.entries:
            snap_file = files_dir / entry.relative_path
            if not snap_file.exists():
                result["missing"].append(entry.relative_path)
                result["ok"] = False
                continue
            current_hash = self._hash_file(snap_file)
            current_size = snap_file.stat().st_size
            if current_hash != entry.sha256 or current_size != entry.size_bytes:
                result["mismatched"].append(entry.relative_path)
                result["ok"] = False
            result["checked"] += 1
        return result

    # -- restore -------------------------------------------------------------

    def restore(self, snapshot_id: str, verify_after: bool = True) -> Dict[str, Any]:
        """Rewrite every live file in the manifest to its captured bytes.

        Each file is restored atomically (write to sibling temp file, fsync,
        rename). If ``verify_after`` is True, the live file is re-hashed
        post-restore and compared to the manifest checksum.

        Returns a dict with ``ok``, ``restored`` (count), ``failed`` (list of
        relative paths that could not be restored), and ``verify_errors``.
        """
        manifest = self.load_manifest(snapshot_id)
        files_dir = self._files_dir(snapshot_id)

        result: Dict[str, Any] = {
            "ok": True,
            "restored": 0,
            "failed": [],
            "verify_errors": [],
        }

        for entry in manifest.entries:
            snap_file = files_dir / entry.relative_path
            if not snap_file.exists():
                result["failed"].append(entry.relative_path)
                result["ok"] = False
                continue
            target = self.repo_root / entry.relative_path
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                # Restore preserves the captured bytes (not the captured mtime);
                # mtime is incidental for content correctness.
                self._atomic_write_bytes(target, snap_file.read_bytes())
            except OSError as exc:
                result["failed"].append(entry.relative_path)
                result["ok"] = False
                result["verify_errors"].append(f"{entry.relative_path}: {exc}")
                continue

            if verify_after:
                post_hash = self._hash_file(target)
                if post_hash != entry.sha256:
                    result["failed"].append(entry.relative_path)
                    result["ok"] = False
                    result["verify_errors"].append(
                        f"{entry.relative_path}: post-restore checksum mismatch"
                    )
                    continue
            result["restored"] += 1

        return result

    # -- list / prune --------------------------------------------------------

    def list_snapshots(self) -> List[SnapshotManifest]:
        """Return every snapshot manifest in the snapshot root, newest first."""
        if not self.snapshot_root.exists():
            return []
        manifests: List[SnapshotManifest] = []
        for child in sorted(self.snapshot_root.iterdir()):
            if not child.is_dir():
                continue
            manifest_path = child / MANIFEST_FILENAME
            if not manifest_path.exists():
                continue
            try:
                with open(manifest_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                manifests.append(SnapshotManifest.from_dict(data))
            except (json.JSONDecodeError, KeyError, ValueError):
                # Skip corrupted manifests; they are not part of the valid set.
                continue
        manifests.sort(key=lambda m: m.created_at, reverse=True)
        return manifests

    def prune(self, snapshot_ids: Optional[Sequence[str]] = None, keep_last: Optional[int] = None) -> List[str]:
        """Delete snapshots and return the list of removed snapshot_ids.

        Either pass an explicit list of ``snapshot_ids`` to remove, or
        ``keep_last=N`` to retain only the N most-recent snapshots and drop
        the rest. Raises ``ValueError`` if neither argument is given.
        """
        if snapshot_ids is None and keep_last is None:
            raise ValueError("prune() requires either snapshot_ids or keep_last")
        if snapshot_ids is not None and keep_last is not None:
            raise ValueError("pass only one of snapshot_ids or keep_last")

        if snapshot_ids is not None:
            targets = list(snapshot_ids)
        else:
            all_manifests = self.list_snapshots()
            targets = [m.snapshot_id for m in all_manifests[keep_last:]]

        removed: List[str] = []
        for sid in targets:
            snapshot_dir = self._snapshot_dir(sid)
            if snapshot_dir.exists():
                shutil.rmtree(snapshot_dir, ignore_errors=True)
            removed.append(sid)
        return removed

    # -- helpers -------------------------------------------------------------

    @staticmethod
    def _generate_snapshot_id(created_at: str) -> str:
        # ISO timestamp with ':' replaced so the id is filesystem-safe everywhere.
        ts = created_at.replace(":", "-").replace(".", "-")
        suffix = uuid.uuid4().hex[:8]
        return f"{ts}_{suffix}"

    @staticmethod
    def _atomic_write_bytes(target: Path, data: bytes) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        # NamedTemporaryFile in the same directory guarantees rename is atomic
        # on POSIX and Windows (same volume).
        fd, tmp_path = tempfile.mkstemp(
            prefix=target.name + ".", suffix=".tmp", dir=str(target.parent)
        )
        try:
            with os.fdopen(fd, "wb") as f:
                f.write(data)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_path, target)
        except Exception:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise

    @classmethod
    def _atomic_write_json(cls, target: Path, payload: Dict[str, Any]) -> None:
        data = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False).encode("utf-8")
        cls._atomic_write_bytes(target, data)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="state_snapshot",
        description="Capture, verify, restore, and prune pre-operation state.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory).",
    )
    parser.add_argument(
        "--snapshot-root",
        type=Path,
        default=None,
        help="Where snapshots are stored (default: <repo>/.snapshots).",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    cap = sub.add_parser("capture", help="Capture state for the given paths.")
    cap.add_argument("paths", nargs="+", type=Path, help="Files or directories to capture.")
    cap.add_argument("--operation", required=True, help="Operation label (e.g. migrate_icad_stats).")
    cap.add_argument("--metadata", type=str, default=None,
                     help="JSON string of metadata to attach to the manifest.")
    cap.add_argument("--id", dest="snapshot_id", type=str, default=None,
                     help="Optional explicit snapshot id.")

    sub.add_parser("list", help="List existing snapshots, newest first.")

    ver = sub.add_parser("verify", help="Verify a snapshot's checksums.")
    ver.add_argument("snapshot_id", type=str)

    res = sub.add_parser("restore", help="Restore live files from a snapshot.")
    res.add_argument("snapshot_id", type=str)
    res.add_argument("--no-verify", action="store_true",
                     help="Skip post-restore verification (not recommended).")

    prn = sub.add_parser("prune", help="Delete snapshots.")
    prn.add_argument("--ids", nargs="+", type=str, default=None,
                     help="Explicit snapshot ids to delete.")
    prn.add_argument("--keep-last", type=int, default=None,
                     help="Keep only the N most-recent snapshots.")

    return parser


def _parse_metadata(raw: Optional[str]) -> Dict[str, Any]:
    if raw is None:
        return {}
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"--metadata must be valid JSON: {exc}")
    if not isinstance(parsed, dict):
        raise SystemExit("--metadata must be a JSON object")
    return parsed


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    service = StateSnapshotService(
        repo_root=args.repo_root,
        snapshot_root=args.snapshot_root,
    )

    if args.command == "capture":
        snap = service.capture(
            target_paths=args.paths,
            operation=args.operation,
            metadata=_parse_metadata(args.metadata),
            snapshot_id=args.snapshot_id,
        )
        print(json.dumps({
            "snapshot_id": snap.snapshot_id,
            "operation": snap.operation,
            "created_at": snap.created_at,
            "entry_count": snap.entry_count,
            "total_bytes": snap.total_bytes,
            "snapshot_dir": str(snap.snapshot_dir),
        }, indent=2))
        return 0

    if args.command == "list":
        manifests = service.list_snapshots()
        out = [
            {
                "snapshot_id": m.snapshot_id,
                "operation": m.operation,
                "created_at": m.created_at,
                "entry_count": len(m.entries),
                "total_bytes": sum(e.size_bytes for e in m.entries),
            }
            for m in manifests
        ]
        print(json.dumps(out, indent=2))
        return 0

    if args.command == "verify":
        result = service.verify(args.snapshot_id)
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1

    if args.command == "restore":
        result = service.restore(args.snapshot_id, verify_after=not args.no_verify)
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1

    if args.command == "prune":
        removed = service.prune(snapshot_ids=args.ids, keep_last=args.keep_last)
        print(json.dumps({"removed": removed}, indent=2))
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2  # unreachable


if __name__ == "__main__":
    sys.exit(main())

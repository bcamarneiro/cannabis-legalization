#!/usr/bin/env python3
"""
Tests for the State Snapshotting Service.

Run with::

    python scripts/test_state_snapshot.py

The test runner uses a minimal stdlib harness (matching the convention of
``scripts/test_persistence_operations.py``) so the suite runs anywhere Python
runs, with no extra dependencies and no pytest required.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

# Add repo root to path so `from data.state_snapshot import ...` works whether
# the script is invoked from the repo root or from inside scripts/.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from data.state_snapshot import (
    SCHEMA_VERSION,
    SnapshotEntry,
    SnapshotManifest,
    StateSnapshotService,
)


# ---------------------------------------------------------------------------
# Test fixtures
# ---------------------------------------------------------------------------


class _Workspace:
    """Isolated working tree: a tempdir acting as repo_root with a few files.

    Tracks every Path it created so tests can clean up after themselves
    without leaking tempdirs across runs.
    """

    def __init__(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="state_snapshot_test_"))
        (self.root / "data").mkdir()
        (self.root / "data" / "icad_stats_initial.json").write_text(
            json.dumps({"version": "1.0.0", "patterns": [{"id": 1}]}),
            encoding="utf-8",
        )
        (self.root / "data" / "raw_icad_stats_initial.json").write_text(
            json.dumps({"version": "1.0.0", "records": []}),
            encoding="utf-8",
        )
        (self.root / "data" / "subdir").mkdir()
        (self.root / "data" / "subdir" / "nested.txt").write_text(
            "nested content", encoding="utf-8"
        )
        # Pre-existing snapshot dir that capture() must never include in its own snapshot.
        (self.root / ".snapshots").mkdir()

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


# ---------------------------------------------------------------------------
# Unit tests: dataclass & validation
# ---------------------------------------------------------------------------


def test_snapshot_entry_roundtrip() -> None:
    entry = SnapshotEntry(
        relative_path="data/foo.json",
        size_bytes=42,
        sha256="a" * 64,
        captured_at="2026-08-04T00:00:00+00:00",
    )
    rebuilt = SnapshotEntry.from_dict(entry.to_dict())
    assert rebuilt == entry
    print("✓ test_snapshot_entry_roundtrip passed")


def test_snapshot_manifest_roundtrip() -> None:
    manifest = SnapshotManifest(
        snapshot_id="2026-08-04T00-00-00-abcdef12",
        operation="migrate_icad_stats",
        created_at="2026-08-04T00:00:00+00:00",
        repo_root="/tmp/repo",
        entries=[
            SnapshotEntry("a.txt", 1, "b" * 64, "2026-08-04T00:00:00+00:00"),
            SnapshotEntry("b.txt", 2, "c" * 64, "2026-08-04T00:00:00+00:00"),
        ],
        metadata={"version": "1.0.0"},
    )
    rebuilt = SnapshotManifest.from_dict(manifest.to_dict())
    assert rebuilt == manifest
    assert rebuilt.validate() == []
    print("✓ test_snapshot_manifest_roundtrip passed")


def test_manifest_validate_detects_problems() -> None:
    bad = SnapshotManifest(
        snapshot_id="",
        operation="",
        created_at="",
        repo_root="",
        entries=[
            SnapshotEntry("", 1, "x" * 64, ""),
            SnapshotEntry("dup.txt", -1, "short", ""),
            SnapshotEntry("dup.txt", 1, "z" * 64, ""),
        ],
        schema_version="99.0.0",
    )
    errors = bad.validate()
    assert any("snapshot_id" in e for e in errors)
    assert any("operation" in e for e in errors)
    assert any("created_at" in e for e in errors)
    assert any("repo_root" in e for e in errors)
    assert any("schema_version" in e for e in errors)
    assert any("empty relative_path" in e for e in errors)
    assert any("duplicate entry" in e for e in errors)
    assert any("negative size" in e for e in errors)
    assert any("invalid sha256" in e for e in errors)
    print("✓ test_manifest_validate_detects_problems passed")


# ---------------------------------------------------------------------------
# Integration tests: capture
# ---------------------------------------------------------------------------


def test_capture_single_file() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[ws.root / "data" / "icad_stats_initial.json"],
            operation="test_capture_single_file",
        )
        assert snap.entry_count == 1
        assert snap.total_bytes > 0
        assert (ws.root / ".snapshots" / snap.snapshot_id / "manifest.json").exists()
        # The captured file is the exact bytes that existed pre-snapshot.
        snap_file = ws.root / ".snapshots" / snap.snapshot_id / "files" / "data" / "icad_stats_initial.json"
        assert snap_file.read_bytes() == b'{"version": "1.0.0", "patterns": [{"id": 1}]}'
    finally:
        ws.cleanup()
    print("✓ test_capture_single_file passed")


def test_capture_multiple_files() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[
                ws.root / "data" / "icad_stats_initial.json",
                ws.root / "data" / "raw_icad_stats_initial.json",
                ws.root / "data" / "subdir" / "nested.txt",
            ],
            operation="test_capture_multiple_files",
        )
        assert snap.entry_count == 3
        # All three relative paths are present in the manifest.
        manifest = svc.load_manifest(snap.snapshot_id)
        rels = sorted(e.relative_path for e in manifest.entries)
        assert rels == [
            "data/icad_stats_initial.json",
            "data/raw_icad_stats_initial.json",
            "data/subdir/nested.txt",
        ]
    finally:
        ws.cleanup()
    print("✓ test_capture_multiple_files passed")


def test_capture_directory_recurses() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[ws.root / "data"],
            operation="test_capture_directory_recurses",
        )
        # 3 files under data/: icad_stats_initial.json, raw_icad_stats_initial.json, subdir/nested.txt
        assert snap.entry_count == 3
    finally:
        ws.cleanup()
    print("✓ test_capture_directory_recurses passed")


def test_capture_nonexistent_path_is_skipped() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[
                ws.root / "data" / "missing.json",
                ws.root / "data" / "icad_stats_initial.json",
            ],
            operation="test_capture_nonexistent_path_is_skipped",
        )
        assert snap.entry_count == 1
    finally:
        ws.cleanup()
    print("✓ test_capture_nonexistent_path_is_skipped passed")


def test_capture_rejects_duplicate_snapshot_id() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        sid = "fixed-id-for-test"
        svc.capture(
            target_paths=[ws.root / "data" / "icad_stats_initial.json"],
            operation="first",
            snapshot_id=sid,
        )
        try:
            svc.capture(
                target_paths=[ws.root / "data" / "icad_stats_initial.json"],
                operation="second",
                snapshot_id=sid,
            )
        except ValueError as exc:
            assert "already exists" in str(exc)
        else:
            raise AssertionError("expected ValueError for duplicate snapshot_id")
    finally:
        ws.cleanup()
    print("✓ test_capture_rejects_duplicate_snapshot_id passed")


def test_capture_rejects_empty_operation() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        try:
            svc.capture(
                target_paths=[ws.root / "data" / "icad_stats_initial.json"],
                operation="",
            )
        except ValueError as exc:
            assert "operation" in str(exc)
        else:
            raise AssertionError("expected ValueError for empty operation")
    finally:
        ws.cleanup()
    print("✓ test_capture_rejects_empty_operation passed")


def test_capture_includes_metadata() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[ws.root / "data" / "icad_stats_initial.json"],
            operation="with_metadata",
            metadata={"version": "1.0.0", "user": "aragorn"},
        )
        manifest = svc.load_manifest(snap.snapshot_id)
        assert manifest.metadata == {"version": "1.0.0", "user": "aragorn"}
        assert manifest.operation == "with_metadata"
        assert manifest.schema_version == SCHEMA_VERSION
    finally:
        ws.cleanup()
    print("✓ test_capture_includes_metadata passed")


def test_capture_excludes_snapshot_root() -> None:
    """A snapshot must never include its own bytes."""
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        # Capture everything in repo_root, then make sure no entry's relative
        # path points inside .snapshots/.
        snap = svc.capture(
            target_paths=[ws.root],
            operation="capture_root",
        )
        manifest = svc.load_manifest(snap.snapshot_id)
        for entry in manifest.entries:
            assert not entry.relative_path.startswith(".snapshots/"), (
                f"snapshot captured its own dir: {entry.relative_path}"
            )
    finally:
        ws.cleanup()
    print("✓ test_capture_excludes_snapshot_root passed")


def test_capture_manifest_is_atomic_on_disk() -> None:
    """Manifest file must end in a complete JSON document (no .tmp leftovers)."""
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[ws.root / "data" / "icad_stats_initial.json"],
            operation="atomic_check",
        )
        manifest_path = ws.root / ".snapshots" / snap.snapshot_id / "manifest.json"
        # Parse the manifest: must succeed and be valid JSON.
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert data["snapshot_id"] == snap.snapshot_id
        # No leftover temp files in the snapshot dir.
        leftovers = list((ws.root / ".snapshots" / snap.snapshot_id).glob("*.tmp"))
        assert leftovers == [], f"temp files left behind: {leftovers}"
    finally:
        ws.cleanup()
    print("✓ test_capture_manifest_is_atomic_on_disk passed")


# ---------------------------------------------------------------------------
# Integration tests: verify
# ---------------------------------------------------------------------------


def test_verify_ok_for_fresh_snapshot() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[ws.root / "data" / "icad_stats_initial.json"],
            operation="verify_ok",
        )
        result = svc.verify(snap.snapshot_id)
        assert result["ok"] is True
        assert result["checked"] == 1
        assert result["mismatched"] == []
        assert result["missing"] == []
    finally:
        ws.cleanup()
    print("✓ test_verify_ok_for_fresh_snapshot passed")


def test_verify_detects_corruption() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[ws.root / "data" / "icad_stats_initial.json"],
            operation="verify_corrupt",
        )
        # Tamper with the captured file.
        snap_file = (
            ws.root / ".snapshots" / snap.snapshot_id / "files"
            / "data" / "icad_stats_initial.json"
        )
        snap_file.write_bytes(b"corrupted")
        result = svc.verify(snap.snapshot_id)
        assert result["ok"] is False
        assert "data/icad_stats_initial.json" in result["mismatched"]
    finally:
        ws.cleanup()
    print("✓ test_verify_detects_corruption passed")


def test_verify_detects_missing_file() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[ws.root / "data" / "icad_stats_initial.json"],
            operation="verify_missing",
        )
        # Delete the captured file but leave the manifest in place.
        snap_file = (
            ws.root / ".snapshots" / snap.snapshot_id / "files"
            / "data" / "icad_stats_initial.json"
        )
        snap_file.unlink()
        result = svc.verify(snap.snapshot_id)
        assert result["ok"] is False
        assert "data/icad_stats_initial.json" in result["missing"]
    finally:
        ws.cleanup()
    print("✓ test_verify_detects_missing_file passed")


# ---------------------------------------------------------------------------
# Integration tests: restore
# ---------------------------------------------------------------------------


def test_restore_recovers_modified_file() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        target = ws.root / "data" / "icad_stats_initial.json"
        original = target.read_bytes()
        snap = svc.capture(
            target_paths=[target],
            operation="before_overwrite",
        )
        # Simulate a destructive operation.
        target.write_bytes(b'{"version": "9.9.9", "patterns": []}')
        result = svc.restore(snap.snapshot_id)
        assert result["ok"] is True
        assert result["restored"] == 1
        assert result["failed"] == []
        assert target.read_bytes() == original
    finally:
        ws.cleanup()
    print("✓ test_restore_recovers_modified_file passed")


def test_restore_creates_missing_file() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        target = ws.root / "data" / "icad_stats_initial.json"
        original = target.read_bytes()
        snap = svc.capture(
            target_paths=[target],
            operation="before_delete",
        )
        target.unlink()
        assert not target.exists()
        result = svc.restore(snap.snapshot_id)
        assert result["ok"] is True
        assert target.exists()
        assert target.read_bytes() == original
    finally:
        ws.cleanup()
    print("✓ test_restore_creates_missing_file passed")


def test_restore_is_atomic_per_file() -> None:
    """If a file is restored it must not leave a .tmp sibling."""
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        target = ws.root / "data" / "icad_stats_initial.json"
        snap = svc.capture(
            target_paths=[target],
            operation="atomic_restore",
        )
        target.write_bytes(b"junk")
        svc.restore(snap.snapshot_id)
        leftovers = list(target.parent.glob(target.name + ".*.tmp"))
        assert leftovers == [], f"temp files left after restore: {leftovers}"
    finally:
        ws.cleanup()
    print("✓ test_restore_is_atomic_per_file passed")


# ---------------------------------------------------------------------------
# Integration tests: list / prune
# ---------------------------------------------------------------------------


def test_list_snapshots_returns_all() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        ids = []
        for i in range(3):
            snap = svc.capture(
                target_paths=[ws.root / "data" / "icad_stats_initial.json"],
                operation=f"op_{i}",
            )
            ids.append(snap.snapshot_id)
        listed = svc.list_snapshots()
        assert [m.snapshot_id for m in listed] == list(reversed(ids))
        assert all(m.operation.startswith("op_") for m in listed)
    finally:
        ws.cleanup()
    print("✓ test_list_snapshots_returns_all passed")


def test_list_snapshots_empty() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        assert svc.list_snapshots() == []
    finally:
        ws.cleanup()
    print("✓ test_list_snapshots_empty passed")


def test_prune_by_explicit_ids() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snaps = [
            svc.capture(
                target_paths=[ws.root / "data" / "icad_stats_initial.json"],
                operation=f"op_{i}",
            )
            for i in range(3)
        ]
        removed = svc.prune(snapshot_ids=[snaps[0].snapshot_id, snaps[2].snapshot_id])
        assert removed == [snaps[0].snapshot_id, snaps[2].snapshot_id]
        remaining = {m.snapshot_id for m in svc.list_snapshots()}
        assert remaining == {snaps[1].snapshot_id}
    finally:
        ws.cleanup()
    print("✓ test_prune_by_explicit_ids passed")


def test_prune_keep_last_n() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        snaps = [
            svc.capture(
                target_paths=[ws.root / "data" / "icad_stats_initial.json"],
                operation=f"op_{i}",
            )
            for i in range(5)
        ]
        # Capture timestamps are monotonic; the last two created should remain.
        removed = svc.prune(keep_last=2)
        assert set(removed) == {
            snaps[0].snapshot_id,
            snaps[1].snapshot_id,
            snaps[2].snapshot_id,
        }
        remaining = {m.snapshot_id for m in svc.list_snapshots()}
        assert remaining == {snaps[3].snapshot_id, snaps[4].snapshot_id}
    finally:
        ws.cleanup()
    print("✓ test_prune_keep_last_n passed")


def test_prune_requires_argument() -> None:
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        try:
            svc.prune()
        except ValueError as exc:
            assert "snapshot_ids" in str(exc) and "keep_last" in str(exc)
        else:
            raise AssertionError("expected ValueError when no prune arg given")
    finally:
        ws.cleanup()
    print("✓ test_prune_requires_argument passed")


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------


def test_capture_unicode_filenames() -> None:
    ws = _Workspace()
    try:
        target = ws.root / "data" / "português.json"
        target.write_text('{"olá": "mundo"}', encoding="utf-8")
        svc = StateSnapshotService(repo_root=ws.root)
        snap = svc.capture(
            target_paths=[target],
            operation="unicode",
        )
        manifest = svc.load_manifest(snap.snapshot_id)
        rels = [e.relative_path for e in manifest.entries]
        assert "data/português.json" in rels
        # Round-trip via restore.
        target.unlink()
        result = svc.restore(snap.snapshot_id)
        assert result["ok"] is True
        assert target.read_text(encoding="utf-8") == '{"olá": "mundo"}'
    finally:
        ws.cleanup()
    print("✓ test_capture_unicode_filenames passed")


def test_capture_rejects_path_outside_repo() -> None:
    ws = _Workspace()
    try:
        outside = Path(tempfile.mkdtemp(prefix="outside_"))
        try:
            outside_file = outside / "evil.txt"
            outside_file.write_text("evil", encoding="utf-8")
            svc = StateSnapshotService(repo_root=ws.root)
            try:
                svc.capture(
                    target_paths=[outside_file],
                    operation="outside",
                )
            except ValueError as exc:
                assert "outside repo_root" in str(exc)
            else:
                raise AssertionError("expected ValueError for outside path")
        finally:
            shutil.rmtree(outside, ignore_errors=True)
    finally:
        ws.cleanup()
    print("✓ test_capture_rejects_path_outside_repo passed")


def test_capture_then_modify_then_restore_round_trip() -> None:
    """End-to-end: snapshot, modify three files in different ways, restore all."""
    ws = _Workspace()
    try:
        svc = StateSnapshotService(repo_root=ws.root)
        targets = [
            ws.root / "data" / "icad_stats_initial.json",
            ws.root / "data" / "raw_icad_stats_initial.json",
            ws.root / "data" / "subdir" / "nested.txt",
        ]
        originals = {t: t.read_bytes() for t in targets}

        snap = svc.capture(target_paths=targets, operation="round_trip")

        # Mutate: overwrite one, delete one, leave one alone, then corrupt another.
        targets[0].write_bytes(b"new contents for stats")
        targets[1].unlink()
        targets[2].write_bytes(b"different nested")

        result = svc.restore(snap.snapshot_id)
        assert result["ok"] is True
        assert result["restored"] == 3
        for t, original in originals.items():
            assert t.read_bytes() == original, f"file not restored: {t}"
    finally:
        ws.cleanup()
    print("✓ test_capture_then_modify_then_restore_round_trip passed")


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


ALL_TESTS = [
    test_snapshot_entry_roundtrip,
    test_snapshot_manifest_roundtrip,
    test_manifest_validate_detects_problems,
    test_capture_single_file,
    test_capture_multiple_files,
    test_capture_directory_recurses,
    test_capture_nonexistent_path_is_skipped,
    test_capture_rejects_duplicate_snapshot_id,
    test_capture_rejects_empty_operation,
    test_capture_includes_metadata,
    test_capture_excludes_snapshot_root,
    test_capture_manifest_is_atomic_on_disk,
    test_verify_ok_for_fresh_snapshot,
    test_verify_detects_corruption,
    test_verify_detects_missing_file,
    test_restore_recovers_modified_file,
    test_restore_creates_missing_file,
    test_restore_is_atomic_per_file,
    test_list_snapshots_returns_all,
    test_list_snapshots_empty,
    test_prune_by_explicit_ids,
    test_prune_keep_last_n,
    test_prune_requires_argument,
    test_capture_unicode_filenames,
    test_capture_rejects_path_outside_repo,
    test_capture_then_modify_then_restore_round_trip,
]


def main() -> None:
    print("Running state snapshotting service tests...")
    print("-" * 60)
    passed = 0
    failed = 0
    for test in ALL_TESTS:
        try:
            test()
            passed += 1
        except Exception as exc:  # noqa: BLE001 - show the test name + reason
            failed += 1
            print(f"✗ {test.__name__} FAILED: {type(exc).__name__}: {exc}")
    print("-" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    if failed > 0:
        sys.exit(1)
    print("All tests passed!")


if __name__ == "__main__":
    main()

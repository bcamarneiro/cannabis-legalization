#!/usr/bin/env python3
"""
Schema migration runner for the ICAD statistics data layer.

Discovers numbered migration files in `data/migrations/`, tracks which have
been applied in a state file, and provides ordered `up` / `down` execution
with status reporting.

State is persisted to `data/.migration_state.json` (path is configurable).

A migration file is a Python module exposing:
    VERSION     str  - 3-digit numeric, e.g. "001", "002"
    NAME        str  - short snake_case identifier
    DESCRIPTION str  - one-line human description
    TARGETS     list - relative output paths the migration creates
    up()        callable - apply the migration
    down()      callable - reverse the migration

Usage:
    from data.migrations.runner import MigrationRunner

    runner = MigrationRunner()
    runner.status()
    runner.up()
    runner.down(steps=1)
"""

import importlib.util
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, List, Optional


# Repo root is two parents up from this file (data/migrations/runner.py).
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_MIGRATIONS_DIR = REPO_ROOT / "data" / "migrations"
DEFAULT_STATE_PATH = REPO_ROOT / "data" / ".migration_state.json"

# Make repo root importable so migrations can `from data.xxx import ...`.
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@dataclass
class MigrationRecord:
    """A single recorded, applied migration in the state file."""
    version: str
    name: str
    description: str
    applied_at: str
    targets: List[str] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.version}_{self.name}"


@dataclass
class Migration:
    """A discovered migration file, ready to run."""
    version: str
    name: str
    description: str
    source_path: Path
    targets: List[str] = field(default_factory=list)
    up_fn: Optional[Callable[[], None]] = None
    down_fn: Optional[Callable[[], None]] = None
    applied_at: Optional[str] = None

    @property
    def full_name(self) -> str:
        return f"{self.version}_{self.name}"

    @property
    def is_applied(self) -> bool:
        return self.applied_at is not None

    def to_record(self) -> MigrationRecord:
        return MigrationRecord(
            version=self.version,
            name=self.name,
            description=self.description,
            applied_at=self.applied_at or datetime.now().isoformat(),
            targets=list(self.targets),
        )


class MigrationError(Exception):
    """Raised when a migration fails or is misconfigured."""


class MigrationRunner:
    """Discovers, tracks, and runs schema migrations."""

    def __init__(
        self,
        migrations_dir: Optional[Path] = None,
        state_path: Optional[Path] = None,
    ) -> None:
        self.migrations_dir = Path(migrations_dir or DEFAULT_MIGRATIONS_DIR)
        self.state_path = Path(state_path or DEFAULT_STATE_PATH)

    # ------------------------------------------------------------------ discovery
    def discover(self) -> List[Migration]:
        """Return all migrations in version order, with applied state merged in."""
        applied = self._load_state()
        migrations: List[Migration] = []
        for path in sorted(self.migrations_dir.glob("*.py")):
            if path.name.startswith("_") or path.name == "runner.py":
                continue
            migration = self._load_migration(path)
            record = applied.get(migration.full_name)
            if record:
                migration.applied_at = record.applied_at
                migration.targets = list(record.targets) or migration.targets
            migrations.append(migration)
        return migrations

    def _load_migration(self, path: Path) -> Migration:
        """Import a migration file and extract its metadata + callables."""
        spec = importlib.util.spec_from_file_location(
            f"data.migrations.{path.stem}", path
        )
        if spec is None or spec.loader is None:
            raise MigrationError(f"Could not load migration spec from {path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore[union-attr]

        for attr in ("VERSION", "NAME", "DESCRIPTION", "up", "down"):
            if not hasattr(module, attr):
                raise MigrationError(
                    f"Migration {path.name} is missing required attribute '{attr}'"
                )

        version = str(module.VERSION).strip()
        name = str(module.NAME).strip()
        if not version.isdigit() or len(version) != 3:
            raise MigrationError(
                f"Migration {path.name} VERSION must be a 3-digit string, got {version!r}"
            )
        if not name.replace("_", "").isalnum():
            raise MigrationError(
                f"Migration {path.name} NAME must be snake_case alphanumeric, got {name!r}"
            )

        return Migration(
            version=version,
            name=name,
            description=str(module.DESCRIPTION).strip(),
            source_path=path,
            targets=list(getattr(module, "TARGETS", []) or []),
            up_fn=module.up,
            down_fn=module.down,
        )

    # ------------------------------------------------------------------ state
    def _load_state(self) -> Dict[str, MigrationRecord]:
        if not self.state_path.exists():
            return {}
        try:
            raw = json.loads(self.state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise MigrationError(
                f"State file at {self.state_path} is corrupted: {exc}"
            ) from exc
        records: Dict[str, MigrationRecord] = {}
        for entry in raw.get("applied", []):
            record = MigrationRecord(
                version=entry["version"],
                name=entry["name"],
                description=entry.get("description", ""),
                applied_at=entry.get("applied_at", ""),
                targets=list(entry.get("targets", [])),
            )
            records[record.full_name] = record
        return records

    def _save_state(self, records: Dict[str, MigrationRecord]) -> None:
        payload = {
            "schema_version": 1,
            "last_updated": datetime.now().isoformat(),
            "applied": [
                {
                    "version": r.version,
                    "name": r.name,
                    "description": r.description,
                    "applied_at": r.applied_at,
                    "targets": list(r.targets),
                }
                for r in records.values()
            ],
        }
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        # Atomic write: write to .tmp then rename, so a crash mid-write
        # doesn't leave a half-written state file.
        tmp_path = self.state_path.with_suffix(self.state_path.suffix + ".tmp")
        tmp_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp_path.replace(self.state_path)

    # ------------------------------------------------------------------ commands
    def status(self) -> List[Migration]:
        """Return all migrations with applied state; never mutates anything."""
        return self.discover()

    def up(self, target: Optional[str] = None) -> List[Migration]:
        """Apply pending migrations in version order up to and including `target`.

        `target` may be either a full migration name (e.g. "001_create_icad_stats")
        or just the version (e.g. "001"). Pass None to apply every pending
        migration.

        Returns the list of migrations that were applied by this call.
        """
        migrations = self.discover()
        applied_now: List[Migration] = []
        records = self._load_state()

        for migration in migrations:
            if migration.is_applied:
                continue
            if target is not None and self._version_key(migration) > self._target_key(target, migrations):
                break
            self._apply_up(migration, records)
            applied_now.append(migration)
            print(
                f"  ✓ {migration.full_name} — {migration.description}"
            )

        if applied_now:
            self._save_state(records)
            print(
                f"Applied {len(applied_now)} migration(s); state written to {self.state_path}"
            )
        else:
            print("No pending migrations.")
        return applied_now

    def down(self, steps: int = 1) -> List[Migration]:
        """Rollback the most recently applied `steps` migrations, in reverse order."""
        if steps < 1:
            raise MigrationError("steps must be >= 1")

        migrations = self.discover()
        applied = [m for m in migrations if m.is_applied]
        to_rollback = list(reversed(applied))[:steps]
        if not to_rollback:
            print("Nothing to rollback.")
            return []

        records = self._load_state()
        rolled_back: List[Migration] = []
        for migration in to_rollback:
            self._apply_down(migration, records)
            records.pop(migration.full_name, None)
            rolled_back.append(migration)
            print(
                f"  ↶ {migration.full_name} — rolled back"
            )

        self._save_state(records)
        print(
            f"Rolled back {len(rolled_back)} migration(s); state written to {self.state_path}"
        )
        return rolled_back

    # ------------------------------------------------------------------ internals
    def _apply_up(self, migration: Migration, records: Dict[str, MigrationRecord]) -> None:
        assert migration.up_fn is not None
        try:
            migration.up_fn()
        except Exception as exc:  # noqa: BLE001
            raise MigrationError(
                f"Migration {migration.full_name} failed on up(): {exc}"
            ) from exc
        record = migration.to_record()
        record.applied_at = datetime.now().isoformat()
        records[migration.full_name] = record

    def _apply_down(self, migration: Migration, records: Dict[str, MigrationRecord]) -> None:
        assert migration.down_fn is not None
        try:
            migration.down_fn()
        except Exception as exc:  # noqa: BLE001
            raise MigrationError(
                f"Migration {migration.full_name} failed on down(): {exc}"
            ) from exc

    @staticmethod
    def _version_key(migration: Migration) -> int:
        return int(migration.version)

    @staticmethod
    def _target_key(target: str, migrations: List[Migration]) -> int:
        """Resolve a user-supplied target to its version integer."""
        target = target.strip()
        for m in migrations:
            if target == m.full_name or target == m.version:
                return int(m.version)
        raise MigrationError(
            f"Unknown migration target {target!r}; run 'status' to list available migrations"
        )


def format_status(migrations: List[Migration]) -> str:
    """Return a human-readable status table for CLI use."""
    if not migrations:
        return "No migrations found."
    lines = [f"{'VERSION':<8}{'NAME':<32}{'STATUS':<14}DESCRIPTION"]
    lines.append("-" * 90)
    for m in migrations:
        status = "applied" if m.is_applied else "pending"
        when = f" ({m.applied_at[:10]})" if m.applied_at and m.is_applied else ""
        lines.append(
            f"{m.version:<8}{m.name:<32}{status:<14}{m.description}{when}"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    # Direct execution: print status. The real CLI lives in scripts/migrate.py.
    print(format_status(MigrationRunner().status()))

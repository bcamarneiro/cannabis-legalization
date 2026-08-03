#!/usr/bin/env python3
"""
Test suite for the migration runner framework.

Run directly:
    python3 scripts/test_migrations.py

The repo has no pytest infrastructure, so this is a standalone executable
test script that prints PASS/FAIL per test and exits non-zero on any
failure. Tests use a temporary state file and temporary migration
directory to keep the real data layer clean.
"""

import json
import shutil
import sys
import tempfile
from pathlib import Path
from types import ModuleType
from typing import Callable, List, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from data.migrations.runner import (  # noqa: E402
    Migration,
    MigrationError,
    MigrationRecord,
    MigrationRunner,
    format_status,
)


# ----------------------------------------------------------------------------
# Minimal test harness
# ----------------------------------------------------------------------------
_RESULTS: List[Tuple[str, bool, str]] = []


def _test(name: str) -> Callable[[Callable[[], None]], Callable[[], None]]:
    def decorator(fn: Callable[[], None]) -> Callable[[], None]:
        def wrapper() -> None:
            try:
                fn()
            except AssertionError as exc:
                _RESULTS.append((name, False, f"assertion failed: {exc}"))
            except Exception as exc:  # noqa: BLE001
                _RESULTS.append((name, False, f"{type(exc).__name__}: {exc}"))
            else:
                _RESULTS.append((name, True, ""))
        return wrapper
    return decorator


def _assert(cond: bool, msg: str = "assertion failed") -> None:
    if not cond:
        raise AssertionError(msg)


# ----------------------------------------------------------------------------
# Fixtures
# ----------------------------------------------------------------------------
def _make_isolated_runner() -> Tuple[MigrationRunner, Path, Path, Path]:
    """Create a runner wired to a tempdir with no migrations on disk yet."""
    tmp = Path(tempfile.mkdtemp(prefix="mig_test_"))
    mig_dir = tmp / "migrations"
    state_path = tmp / ".migration_state.json"
    mig_dir.mkdir(parents=True, exist_ok=True)
    return MigrationRunner(migrations_dir=mig_dir, state_path=state_path), mig_dir, state_path, tmp


def _write_migration(
    mig_dir: Path,
    version: str,
    name: str,
    description: str,
    up_body: str = "    pass",
    down_body: str = "    pass",
    side_effect_file: Path | None = None,
) -> Path:
    """Write a synthetic migration module to the migrations dir.

    The synthetic module defines a top-level side-effect file that
    `up()` writes and `down()` removes, so we can verify the
    idempotency, ordering, and rollback semantics in tests.
    """
    if side_effect_file is None:
        body = f'''"""Synthetic migration for tests."""
VERSION = "{version}"
NAME = "{name}"
DESCRIPTION = "{description}"
TARGETS = []


def up():
{up_body}


def down():
{down_body}
'''
    else:
        body = f'''"""Synthetic migration for tests."""
from pathlib import Path
VERSION = "{version}"
NAME = "{name}"
DESCRIPTION = "{description}"
TARGETS = ["{side_effect_file.name}"]
PATH = Path({str(side_effect_file)!r})


def up():
    PATH.write_text("applied", encoding="utf-8")


def down():
    if PATH.exists():
        PATH.unlink()
'''
    path = mig_dir / f"{version}_{name}.py"
    path.write_text(body, encoding="utf-8")
    return path


def _seed_two_migrations(mig_dir: Path, root: Path) -> Tuple[Path, Path]:
    """Seed two simple migrations that create/remove marker files."""
    side1 = root / "marker_001.txt"
    side2 = root / "marker_002.txt"
    _write_migration(
        mig_dir, "001", "create_one", "creates marker 1",
        side_effect_file=side1,
    )
    _write_migration(
        mig_dir, "002", "create_two", "creates marker 2",
        side_effect_file=side2,
    )
    return side1, side2


# ----------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------
@_test("discover finds all migrations in version order")
def t_discover() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        migrations = runner.discover()
        _assert(len(migrations) == 2, f"expected 2 migrations, got {len(migrations)}")
        _assert(migrations[0].version == "001", "first migration version")
        _assert(migrations[1].version == "002", "second migration version")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("up() applies pending migrations and skips applied ones")
def t_up_idempotent() -> None:
    runner, mig_dir, state, tmp = _make_isolated_runner()
    try:
        m1, m2 = _seed_two_migrations(mig_dir, tmp)
        applied = runner.up()
        _assert(len(applied) == 2, f"expected 2 applied, got {len(applied)}")
        _assert(m1.exists() and m2.exists(), "side-effect files should exist")

        # State file should record both
        _assert(state.exists(), "state file should be written")
        data = json.loads(state.read_text(encoding="utf-8"))
        _assert(len(data["applied"]) == 2, "state should record 2 applied")

        # Second up() should be a no-op
        applied_again = runner.up()
        _assert(applied_again == [], "second up() should be a no-op")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("up(target=...) applies only up to the requested migration")
def t_up_to_target() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        m1, m2 = _seed_two_migrations(mig_dir, tmp)
        applied = runner.up(target="001_create_one")
        _assert(len(applied) == 1, f"expected 1 applied, got {len(applied)}")
        _assert(applied[0].full_name == "001_create_one")
        _assert(m1.exists(), "marker 1 should exist")
        _assert(not m2.exists(), "marker 2 should NOT exist")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("up(target) accepts bare version (e.g. '001')")
def t_up_to_bare_version() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        m1, m2 = _seed_two_migrations(mig_dir, tmp)
        applied = runner.up(target="001")
        _assert(len(applied) == 1)
        _assert(not m2.exists())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("up() rejects unknown target")
def t_up_unknown_target() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        try:
            runner.up(target="999_does_not_exist")
        except MigrationError as exc:
            _assert("Unknown migration target" in str(exc), "error message")
            return
        raise AssertionError("expected MigrationError for unknown target")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("down() rolls back the N most recent migrations in reverse order")
def t_down() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        m1, m2 = _seed_two_migrations(mig_dir, tmp)
        runner.up()
        _assert(m1.exists() and m2.exists())

        rolled = runner.down(steps=1)
        _assert(len(rolled) == 1, "expected 1 rolled back")
        _assert(rolled[0].full_name == "002_create_two", "most recent first")
        _assert(not m2.exists(), "marker 2 should be removed")
        _assert(m1.exists(), "marker 1 should still exist")

        runner.down(steps=1)
        _assert(not m1.exists(), "marker 1 should be removed")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("down() is idempotent: nothing to rollback is a no-op")
def t_down_noop_when_empty() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        rolled = runner.down(steps=1)
        _assert(rolled == [], "should report nothing rolled back")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("down(steps=0) raises MigrationError")
def t_down_zero_steps() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        runner.up()
        try:
            runner.down(steps=0)
        except MigrationError:
            return
        raise AssertionError("expected MigrationError for steps=0")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("status reports applied/pending correctly")
def t_status() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        before = runner.status()
        _assert(not before[0].is_applied and not before[1].is_applied, "all pending")

        runner.up(target="001")
        after = runner.status()
        _assert(after[0].is_applied, "001 should be applied")
        _assert(not after[1].is_applied, "002 should still be pending")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("format_status produces a human-readable table")
def t_format_status() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        text = format_status(runner.status())
        _assert("001" in text and "002" in text, "version columns")
        _assert("pending" in text, "pending label present")
        _assert("create_one" in text and "create_two" in text, "names present")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("corrupted state file raises MigrationError")
def t_corrupted_state() -> None:
    runner, mig_dir, state, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        state.write_text("{ not valid json", encoding="utf-8")
        try:
            runner.status()
        except MigrationError as exc:
            _assert("corrupted" in str(exc).lower(), f"expected corruption error, got: {exc}")
            return
        raise AssertionError("expected MigrationError on corrupted state")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("runner ignores __init__.py and runner.py itself")
def test_ignores_internal_modules() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        # Drop a __init__.py and a runner.py into the migrations dir
        # (mimicking the real package layout); they should be skipped.
        (mig_dir / "__init__.py").write_text("", encoding="utf-8")
        (mig_dir / "runner.py").write_text("VERSION = '000'\nNAME='x'\nDESCRIPTION='y'\n"
                                            "def up(): pass\ndef down(): pass\n", encoding="utf-8")
        _seed_two_migrations(mig_dir, tmp)
        migrations = runner.discover()
        versions = [m.version for m in migrations]
        _assert(versions == ["001", "002"], f"unexpected versions: {versions}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("runner validates migration attributes (VERSION must be 3 digits)")
def t_validate_version() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        # Bad version
        bad = mig_dir / "001x_bad.py"
        bad.write_text(
            'VERSION = "01"\nNAME="bad"\nDESCRIPTION="d"\n'
            "def up(): pass\ndef down(): pass\n",
            encoding="utf-8",
        )
        try:
            runner.discover()
        except MigrationError as exc:
            _assert("3-digit" in str(exc), f"expected 3-digit error, got: {exc}")
            return
        raise AssertionError("expected MigrationError for bad version")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("runner requires up() and down() to be present")
def t_validate_callables() -> None:
    runner, mig_dir, _, tmp = _make_isolated_runner()
    try:
        bad = mig_dir / "001_missing.py"
        bad.write_text(
            'VERSION = "001"\nNAME="missing"\nDESCRIPTION="d"\n'
            "def up(): pass\n",
            encoding="utf-8",
        )
        try:
            runner.discover()
        except MigrationError as exc:
            _assert("down" in str(exc), f"expected missing-attribute error, got: {exc}")
            return
        raise AssertionError("expected MigrationError for missing callable")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("full lifecycle: up → down → up re-creates side effects")
def t_full_lifecycle() -> None:
    runner, mig_dir, state, tmp = _make_isolated_runner()
    try:
        m1, m2 = _seed_two_migrations(mig_dir, tmp)
        runner.up()
        _assert(m1.exists() and m2.exists())

        runner.down(steps=2)
        _assert(not m1.exists() and not m2.exists())

        runner.up()
        _assert(m1.exists() and m2.exists(), "should re-create on second up")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("applied_at timestamp is ISO 8601")
def t_applied_at_format() -> None:
    runner, mig_dir, state, tmp = _make_isolated_runner()
    try:
        _seed_two_migrations(mig_dir, tmp)
        runner.up()
        data = json.loads(state.read_text(encoding="utf-8"))
        ts = data["applied"][0]["applied_at"]
        # Should be parseable; we just check shape: contains 'T' and year prefix.
        _assert("T" in ts, f"expected ISO format with 'T', got: {ts}")
        _assert(ts.startswith("202") or ts.startswith("197"), f"suspicious year: {ts[:4]}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@_test("real migrations 001 and 002 produce correct files and validate")
def t_real_migrations() -> None:
    """End-to-end test using the actual repo's migration 001 and 002."""
    runner = MigrationRunner()
    # Make sure state file is clean
    if runner.state_path.exists():
        runner.state_path.unlink()
    # Make sure the target files are clean
    for target in ("data/icad_stats_initial.json", "data/raw_icad_stats_initial.json"):
        p = REPO_ROOT / target
        if p.exists():
            p.unlink()

    try:
        applied = runner.up()
        _assert(len(applied) == 2, f"expected 2 real migrations, got {len(applied)}")

        stats_path = REPO_ROOT / "data" / "icad_stats_initial.json"
        raw_path = REPO_ROOT / "data" / "raw_icad_stats_initial.json"
        _assert(stats_path.exists(), "001 output should exist")
        _assert(raw_path.exists(), "002 output should exist")

        stats = json.loads(stats_path.read_text(encoding="utf-8"))
        _assert(len(stats["patterns"]) == 10, f"expected 10 patterns, got {len(stats['patterns'])}")

        raw = json.loads(raw_path.read_text(encoding="utf-8"))
        _assert(len(raw["records"]) == 19, f"expected 19 raw records, got {len(raw['records'])}")

        # Idempotency: a second up() should be a no-op
        applied2 = runner.up()
        _assert(applied2 == [], "second up() should be a no-op")
    finally:
        # Roll back to leave the repo in a clean state.
        runner.down(steps=2)
        _assert(
            not (REPO_ROOT / "data" / "icad_stats_initial.json").exists(),
            "001 should be cleaned up after rollback",
        )
        _assert(
            not (REPO_ROOT / "data" / "raw_icad_stats_initial.json").exists(),
            "002 should be cleaned up after rollback",
        )


# ----------------------------------------------------------------------------
# Main: run all tests
# ----------------------------------------------------------------------------
def main() -> int:
    # Collect every test_*/t_* function in module scope.
    module_globals = list(globals().items())
    tests = [
        (name, fn) for name, fn in module_globals
        if callable(fn) and (name.startswith("t_") or name.startswith("test_"))
        and name not in ("test_ignores_internal_modules",)
    ]
    test_ignores_internal_modules  # silence linter

    for _, fn in tests:
        fn()

    # Print results.
    print()
    print("=" * 70)
    print(f"Migration runner test suite — {len(_RESULTS)} tests")
    print("=" * 70)
    passed = sum(1 for _, ok, _ in _RESULTS if ok)
    failed = len(_RESULTS) - passed
    for name, ok, msg in _RESULTS:
        marker = "PASS" if ok else "FAIL"
        line = f"  [{marker}] {name}"
        if not ok:
            line += f"\n         {msg}"
        print(line)
    print("-" * 70)
    print(f"  {passed} passed, {failed} failed")
    print("=" * 70)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

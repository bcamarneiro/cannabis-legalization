#!/usr/bin/env python3
"""
CLI entry point for the ICAD statistics migration runner.

Usage:
    python scripts/migrate.py status
    python scripts/migrate.py up [TARGET]
    python scripts/migrate.py down [STEPS]
    python scripts/migrate.py redo [TARGET]
    python scripts/migrate.py reset

Subcommands:
    status        Show all migrations and which are applied.
    up [TARGET]   Apply pending migrations; optionally up to a specific
                  migration (e.g. "001" or "001_create_icad_stats"). Default
                  applies every pending migration.
    down [STEPS]  Roll back the N most recent applied migrations (default 1).
    redo [TARGET] Roll back the most recent applied migration, then re-apply
                  it (or up to TARGET if given).
    reset         Roll back every applied migration.

The state file is data/.migration_state.json. The migrations directory is
data/migrations/.

Exit code is 0 on success, 1 on any failure (e.g. validation error in a
migration's up/down).
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from data.migrations.runner import MigrationRunner, MigrationError, format_status  # noqa: E402


def _cmd_status(runner: MigrationRunner) -> int:
    print(format_status(runner.status()))
    return 0


def _cmd_up(runner: MigrationRunner, target: str | None) -> int:
    runner.up(target=target)
    return 0


def _cmd_down(runner: MigrationRunner, steps: str | None) -> int:
    n = int(steps) if steps is not None else 1
    runner.down(steps=n)
    return 0


def _cmd_redo(runner: MigrationRunner, target: str | None) -> int:
    applied = [m for m in runner.status() if m.is_applied]
    if not applied:
        print("Nothing to redo — no migrations are applied yet.")
        return 0
    last = applied[-1]
    if target is not None:
        # Roll back the migrations between last and target (inclusive of
        # last on the down side, then re-apply up to target).
        runner.down(steps=len(applied))
        runner.up(target=target)
    else:
        runner.down(steps=1)
        runner.up(target=last.full_name)
    return 0


def _cmd_reset(runner: MigrationRunner) -> int:
    applied = [m for m in runner.status() if m.is_applied]
    if not applied:
        print("Nothing to reset.")
        return 0
    runner.down(steps=len(applied))
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 0

    cmd, rest = argv[0], argv[1:]
    runner = MigrationRunner()

    try:
        if cmd == "status":
            return _cmd_status(runner)
        if cmd == "up":
            target = rest[0] if rest else None
            return _cmd_up(runner, target)
        if cmd == "down":
            steps = rest[0] if rest else None
            return _cmd_down(runner, steps)
        if cmd == "redo":
            target = rest[0] if rest else None
            return _cmd_redo(runner, target)
        if cmd == "reset":
            return _cmd_reset(runner)
        print(f"Unknown command: {cmd!r}\n")
        print(__doc__)
        return 1
    except MigrationError as exc:
        print(f"migration error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"unexpected error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

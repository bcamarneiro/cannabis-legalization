"""
Schema migration framework for the cannabis legalization policy document data layer.

Migrations are versioned, ordered, and tracked in a state file so the same
migration can be re-run safely (idempotent on `up`) and rolled back
deterministically.

See `data/migrations/runner.py` for the runner and the `scripts/migrate.py`
CLI entry point.
"""

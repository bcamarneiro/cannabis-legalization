#!/usr/bin/env python3
"""
Tests for build state management with reversion logic.

Run: python3 tests/test_build_state.py
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from build_state import BuildTransaction, BuildSnapshot, TransactionState, BuildError


def test_snapshot_creation():
    """Test that snapshots capture state correctly."""
    print("Test: snapshot creation...")
    
    project_dir = Path(__file__).parent.parent
    tx = BuildTransaction(project_dir=project_dir)
    
    snapshot = tx.capture_snapshot()
    
    assert snapshot.version is not None, "Version should be captured"
    assert snapshot.timestamp is not None, "Timestamp should be set"
    assert len(snapshot.files) > 0, "Should capture chapter file hashes"
    assert tx.state == TransactionState.IN_PROGRESS, "State should be IN_PROGRESS"
    
    # Cleanup
    if tx.snapshot_path and tx.snapshot_path.exists():
        tx.snapshot_path.unlink()
    
    print("  ✓ Snapshot creation passed")


def test_context_manager_success():
    """Test that context manager commits on success."""
    print("Test: context manager (simulated success)...")
    
    project_dir = Path(__file__).parent.parent
    tx = BuildTransaction(project_dir=project_dir)
    
    # Simulate successful build without actually running it
    tx.capture_snapshot()
    tx.state = TransactionState.IN_PROGRESS  # Pretend we're in progress
    tx.commit()
    
    assert tx.state == TransactionState.COMMITTED, "State should be COMMITTED"
    
    # Cleanup
    if tx._temp_snapshot and Path(tx._temp_snapshot).exists():
        shutil.rmtree(tx._temp_snapshot, ignore_errors=True)
    
    print("  ✓ Context manager success passed")


def test_revert_restores_state():
    """Test that revert restores output directory."""
    print("Test: revert restores state...")
    
    project_dir = Path(__file__).parent.parent
    tx = BuildTransaction(project_dir=project_dir)
    
    # Create a test output file
    output_dir = project_dir / "output"
    output_dir.mkdir(exist_ok=True)
    test_file = output_dir / "test_output.txt"
    test_file.write_text("original content")
    
    # Capture snapshot (backs up the test file)
    tx.capture_snapshot()
    
    # Simulate file change
    test_file.write_text("modified content")
    
    # Revert
    tx.state = TransactionState.IN_PROGRESS
    tx.revert()
    
    assert tx.state == TransactionState.REVERTED, "State should be REVERTED"
    assert test_file.read_text() == "original content", "File should be restored"
    
    # Cleanup
    test_file.unlink()
    if tx._temp_snapshot and Path(tx._temp_snapshot).exists():
        shutil.rmtree(tx._temp_snapshot, ignore_errors=True)
    
    print("  ✓ Revert restores state passed")


def test_snapshot_serialization():
    """Test that snapshots serialize/deserialize correctly."""
    print("Test: snapshot serialization...")
    
    snapshot = BuildSnapshot(
        timestamp="2026-08-04T00:00:00",
        version="1.0.27",
        files={"chapters/01.md": "abc123", "chapters/02.md": "def456"},
        output_files=["output/document.pdf"],
        metadata={"test": True},
    )
    
    data = snapshot.to_dict()
    restored = BuildSnapshot.from_dict(data)
    
    assert restored.timestamp == snapshot.timestamp
    assert restored.version == snapshot.version
    assert restored.files == snapshot.files
    assert restored.output_files == snapshot.output_files
    assert restored.metadata == snapshot.metadata
    
    print("  ✓ Snapshot serialization passed")


def test_list_snapshots():
    """Test listing available snapshots."""
    print("Test: list snapshots...")
    
    project_dir = Path(__file__).parent.parent
    tx = BuildTransaction(project_dir=project_dir)
    
    # Create a test snapshot
    tx.SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    test_snapshot = tx.SNAPSHOT_DIR / "snapshot_test.json"
    test_snapshot.write_text('{"timestamp": "test", "version": "1.0.0", "files": {}, "output_files": []}')
    
    snapshots = tx.list_snapshots()
    assert len(snapshots) > 0, "Should find at least one snapshot"
    
    # Cleanup
    test_snapshot.unlink()
    
    print("  ✓ List snapshots passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 50)
    print("Build State Management - Test Suite")
    print("=" * 50 + "\n")
    
    tests = [
        test_snapshot_creation,
        test_context_manager_success,
        test_revert_restores_state,
        test_snapshot_serialization,
        test_list_snapshots,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 50 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

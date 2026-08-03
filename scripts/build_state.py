#!/usr/bin/env python3
"""
Build State Management with Transactional Reversion.

Provides deterministic failure handling with snapshot-based reversion
for document build operations. Captures state before builds and triggers
automatic reversion upon transaction abort (build failure).

Usage:
    from build_state import BuildTransaction
    
    # Automatic rollback on failure
    with BuildTransaction() as tx:
        tx.run_build()  # rolls back automatically on exception
    
    # Manual control
    tx = BuildTransaction()
    tx.capture_snapshot()
    try:
        tx.run_build()
        tx.commit()
    except BuildError:
        tx.revert()  # restore previous state
"""

import os
import shutil
import subprocess
import sys
import tempfile
import json
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum


class TransactionState(Enum):
    """Transaction lifecycle states."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMMITTED = "committed"
    ABORTED = "aborted"
    REVERTED = "reverted"


@dataclass
class BuildSnapshot:
    """Captured state snapshot for potential reversion."""
    timestamp: str
    version: str
    files: Dict[str, str]  # path -> content hash
    output_files: List[str]  # list of output file paths
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "version": self.version,
            "files": self.files,
            "output_files": self.output_files,
            "metadata": self.metadata,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BuildSnapshot":
        return cls(
            timestamp=data["timestamp"],
            version=data["version"],
            files=data["files"],
            output_files=data["output_files"],
            metadata=data.get("metadata", {}),
        )


class BuildError(Exception):
    """Build transaction failed."""
    pass


class BuildTransaction:
    """
    Transactional build wrapper with automatic reversion on failure.
    
    Captures snapshots before builds and reverts to previous state
    if the build fails (transaction abort).
    """
    
    SNAPSHOT_DIR = Path(".hermes/build_snapshots")
    
    def __init__(self, project_dir: Optional[Path] = None):
        self.project_dir = project_dir or Path(__file__).parent.parent
        self.output_dir = self.project_dir / "output"
        self.state = TransactionState.PENDING
        self.snapshot: Optional[BuildSnapshot] = None
        self.snapshot_path: Optional[Path] = None
        self._temp_snapshot: Optional[str] = None
    
    def _hash_file(self, path: Path) -> str:
        """Compute SHA256 hash of file content."""
        import hashlib
        if not path.exists():
            return ""
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hasher.update(chunk)
        return hasher.hexdigest()[:16]
    
    def capture_snapshot(self) -> BuildSnapshot:
        """
        Capture current state snapshot before build.
        
        Records:
        - Current VERSION file
        - Hashes of all chapter files
        - List of existing output files
        """
        self.SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
        
        # Capture version
        version_file = self.project_dir / "VERSION"
        version = version_file.read_text().strip() if version_file.exists() else "unknown"
        
        # Capture chapter file hashes
        chapters_dir = self.project_dir / "chapters"
        files = {}
        if chapters_dir.exists():
            for chapter in sorted(chapters_dir.glob("*.md")):
                files[str(chapter.relative_to(self.project_dir))] = self._hash_file(chapter)
        
        # Capture references.bib hash
        bib_file = self.project_dir / "references.bib"
        if bib_file.exists():
            files["references.bib"] = self._hash_file(bib_file)
        
        # List existing output files
        output_files = []
        if self.output_dir.exists():
            for f in self.output_dir.glob("*"):
                if f.is_file():
                    output_files.append(str(f.relative_to(self.project_dir)))
        
        self.snapshot = BuildSnapshot(
            timestamp=datetime.now().isoformat(),
            version=version,
            files=files,
            output_files=output_files,
            metadata={
                "build_type": "manual",
                "python_version": f"{os.sys.version_info.major}.{os.sys.version_info.minor}",
            },
        )
        
        # Save snapshot to disk
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.snapshot_path = self.SNAPSHOT_DIR / f"snapshot_{timestamp_str}.json"
        
        # Backup output files before build
        self._temp_snapshot = tempfile.mkdtemp(prefix="build_snapshot_")
        if self.output_dir.exists():
            for f in self.output_dir.glob("*"):
                if f.is_file():
                    dest = Path(self._temp_snapshot) / f.name
                    shutil.copy2(f, dest)
        
        # Save snapshot metadata
        with open(self.snapshot_path, "w") as f:
            json.dump(self.snapshot.to_dict(), f, indent=2)
        
        self.state = TransactionState.IN_PROGRESS
        return self.snapshot
    
    def run_build(self, build_type: str = "both") -> subprocess.CompletedProcess:
        """
        Execute the build process.
        
        Args:
            build_type: "pdf", "docx", or "both"
        
        Raises:
            BuildError: If build process fails
        """
        if self.state != TransactionState.IN_PROGRESS:
            raise BuildError("Must capture snapshot before running build")
        
        build_script = self.project_dir / "scripts" / "build.sh"
        if not build_script.exists():
            raise BuildError(f"Build script not found: {build_script}")
        
        args = ["bash", str(build_script)]
        if build_type in ("pdf", "docx"):
            args.append(build_type)
        
        try:
            result = subprocess.run(
                args,
                cwd=str(self.project_dir),
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
            )
            
            if result.returncode != 0:
                raise BuildError(
                    f"Build failed with exit code {result.returncode}\n"
                    f"STDOUT: {result.stdout}\n"
                    f"STDERR: {result.stderr}"
                )
            
            return result
            
        except subprocess.TimeoutExpired:
            raise BuildError("Build timed out after 300 seconds")
        except Exception as e:
            raise BuildError(f"Build execution failed: {e}")
    
    def commit(self) -> None:
        """
        Commit the transaction - build succeeded.
        
        Cleans up temporary snapshot backup.
        """
        if self.state != TransactionState.IN_PROGRESS:
            return
        
        self.state = TransactionState.COMMITTED
        
        # Clean up temp backup
        if self._temp_snapshot and Path(self._temp_snapshot).exists():
            shutil.rmtree(self._temp_snapshot, ignore_errors=True)
        
        if self.snapshot:
            print(f"✓ Build committed successfully (version {self.snapshot.version})")
    
    def revert(self) -> None:
        """
        Revert to captured snapshot - build failed.
        
        Restores output directory to pre-build state.
        """
        if self.state not in (TransactionState.IN_PROGRESS, TransactionState.ABORTED):
            return
        
        self.state = TransactionState.REVERTED
        
        # Restore output files from temp backup
        if self._temp_snapshot and Path(self._temp_snapshot).exists():
            self.output_dir.mkdir(parents=True, exist_ok=True)
            for backup_file in Path(self._temp_snapshot).glob("*"):
                dest = self.output_dir / backup_file.name
                shutil.copy2(backup_file, dest)
            
            # Clean up temp backup
            shutil.rmtree(self._temp_snapshot, ignore_errors=True)
        
        if self.snapshot:
            print(f"✗ Build reverted to previous state (version {self.snapshot.version})")
    
    def __enter__(self) -> "BuildTransaction":
        """Context manager entry - capture snapshot."""
        self.capture_snapshot()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Context manager exit - commit or revert.
        
        Returns:
            True if exception was handled (reverted), False to propagate
        """
        if exc_type is not None:
            # Build failed - revert
            self.state = TransactionState.ABORTED
            self.revert()
            # Don't propagate BuildError - we handled it by reverting
            return isinstance(exc_type, type) and issubclass(exc_type, BuildError)
        else:
            # Build succeeded - commit
            self.commit()
        return False
    
    def list_snapshots(self) -> List[Path]:
        """List all available snapshots for potential reversion."""
        if not self.SNAPSHOT_DIR.exists():
            return []
        return sorted(self.SNAPSHOT_DIR.glob("snapshot_*.json"))
    
    def load_snapshot(self, snapshot_path: Path) -> BuildSnapshot:
        """Load a previously captured snapshot."""
        with open(snapshot_path) as f:
            data = json.load(f)
        return BuildSnapshot.from_dict(data)


def main():
    """CLI interface for build state management."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build state management with reversion")
    parser.add_argument("command", choices=["build", "list", "revert"], 
                       help="Command to execute")
    parser.add_argument("--type", choices=["pdf", "docx", "both"], default="both",
                       help="Build type (default: both)")
    parser.add_argument("--snapshot", type=Path,
                       help="Snapshot file for revert operation")
    
    args = parser.parse_args()
    
    tx = BuildTransaction()
    
    if args.command == "build":
        try:
            with tx:
                tx.run_build(args.type)
        except BuildError as e:
            print(f"Build failed and reverted: {e}")
            sys.exit(1)
    
    elif args.command == "list":
        snapshots = tx.list_snapshots()
        if not snapshots:
            print("No snapshots found")
        else:
            print(f"Found {len(snapshots)} snapshots:")
            for s in snapshots:
                data = tx.load_snapshot(s)
                print(f"  {s.name}: {data.timestamp} (v{data.version})")
    
    elif args.command == "revert":
        if not args.snapshot:
            print("Error: --snapshot required for revert")
            sys.exit(1)
        # TODO: implement full reversion from snapshot file
        print(f"Would revert to {args.snapshot}")


if __name__ == "__main__":
    main()

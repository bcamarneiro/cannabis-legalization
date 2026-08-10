#!/usr/bin/env python3
"""
Persistence Layer Operations for ICAD Statistics.

Provides write operations (create, update, delete, save) for validated
ICAD data structures using JSON-based storage.

Usage:
    from persistence_operations import RawICADRepository, ICADStatsRepository
    
    # Raw ICAD operations
    raw_repo = RawICADRepository("data/raw_icad_stats.json")
    record = RawICADRecord.from_dict(data)
    raw_repo.create(record)
    raw_repo.save()
    
    # ICAD Stats operations
    stats_repo = ICADStatsRepository("data/icad_stats.json")
    pattern = ConsumptionPattern(...)
    stats_repo.add_pattern(pattern)
    stats_repo.save()
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Dict, Any, Union

from data.raw_icad_schema import (
    RawICADCollection,
    RawICADRecord,
    DataQualityFlags,
)
from data.icad_stats_schema import (
    ICADStats,
    ConsumptionPattern,
    DemographicGroup,
    ConsumptionMetric,
    RiskAssessment,
)


class BaseRepository:
    """Base repository with common persistence operations."""
    
    def __init__(self, storage_path: str):
        """Initialize repository with storage path."""
        self.storage_path = Path(storage_path)
        self._data: Optional[Union[RawICADCollection, ICADStats]] = None
        self._backup_path: Optional[Path] = None
    
    def exists(self) -> bool:
        """Check if storage file exists."""
        return self.storage_path.exists()
    
    def _create_backup(self) -> None:
        """Create timestamped backup before modifications."""
        if self.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self._backup_path = self.storage_path.with_suffix(
                f".{self.storage_path.suffix}.backup_{timestamp}"
            )
            os.rename(self.storage_path, self._backup_path)
    
    def _rollback(self) -> None:
        """Rollback to backup if exists."""
        if self._backup_path and self._backup_path.exists():
            if self.storage_path.exists():
                os.remove(self.storage_path)
            os.rename(self._backup_path, self.storage_path)
            self._backup_path = None


class RawICADRepository(BaseRepository):
    """Repository for Raw ICAD Records with write operations."""
    
    def __init__(self, storage_path: str = "data/raw_icad_stats.json"):
        """Initialize Raw ICAD repository."""
        super().__init__(storage_path)
        self._collection: Optional[RawICADCollection] = None
    
    @property
    def collection(self) -> RawICADCollection:
        """Get or load the collection."""
        if self._collection is None:
            self.load()
        return self._collection
    
    def load(self) -> RawICADCollection:
        """Load collection from storage."""
        if not self.exists() or self.storage_path.stat().st_size == 0:
            self._collection = RawICADCollection()
        else:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._collection = RawICADCollection.from_dict(data)
        return self._collection
    
    def create(self, record: RawICADRecord) -> str:
        """
        Create a new record (insert operation).
        
        Args:
            record: RawICADRecord to insert
            
        Returns:
            record_id of the created record
            
        Raises:
            ValueError: If record_id already exists
        """
        # Check for duplicate
        for existing in self.collection.records:
            if existing.record_id == record.record_id:
                raise ValueError(f"Record {record.record_id} already exists")
        
        # Validate before inserting
        errors = record.validate()
        if errors:
            raise ValueError(f"Invalid record: {'; '.join(errors)}")
        
        self.collection.add_record(record)
        return record.record_id
    
    def update(self, record_id: str, updates: Dict[str, Any]) -> bool:
        """
        Update an existing record.
        
        Args:
            record_id: ID of record to update
            updates: Dictionary of field updates
            
        Returns:
            True if updated, False if not found
        """
        for record in self.collection.records:
            if record.record_id == record_id:
                # Apply updates
                for field, value in updates.items():
                    if hasattr(record, field):
                        setattr(record, field, value)
                    elif hasattr(record.quality_flags, field):
                        setattr(record.quality_flags, field, value)
                
                # Re-validate after update
                errors = record.validate()
                if errors:
                    raise ValueError(f"Invalid record after update: {'; '.join(errors)}")
                
                return True
        return False
    
    def delete(self, record_id: str) -> bool:
        """
        Delete a record by ID.
        
        Args:
            record_id: ID of record to delete
            
        Returns:
            True if deleted, False if not found
        """
        for i, record in enumerate(self.collection.records):
            if record.record_id == record_id:
                del self.collection.records[i]
                return True
        return False
    
    def delete_many(self, predicate) -> int:
        """
        Delete multiple records matching a predicate.
        
        Args:
            predicate: Function that takes RawICADRecord and returns bool
            
        Returns:
            Count of deleted records
        """
        original_count = len(self.collection.records)
        self.collection.records = [
            r for r in self.collection.records if not predicate(r)
        ]
        return original_count - len(self.collection.records)
    
    def upsert(self, record: RawICADRecord) -> str:
        """
        Update if exists, insert otherwise.
        
        Args:
            record: RawICADRecord to upsert
            
        Returns:
            record_id
        """
        for existing in self.collection.records:
            if existing.record_id == record.record_id:
                # Update existing
                for field, value in record.to_dict().items():
                    if hasattr(existing, field):
                        setattr(existing, field, value)
                return record.record_id
        
        # Insert new
        self.collection.add_record(record)
        return record.record_id
    
    def save(self, indent: int = 2) -> None:
        """
        Persist collection to storage with backup.
        
        Args:
            indent: JSON indentation level
        """
        self._create_backup()
        
        try:
            self.collection.last_updated = datetime.now().isoformat()
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.storage_path, "w", encoding="utf-8") as f:
                f.write(self.collection.to_json(indent=indent))
            
            # Clean up backup on success
            if self._backup_path and self._backup_path.exists():
                os.remove(self._backup_path)
                self._backup_path = None
                
        except Exception as e:
            self._rollback()
            raise e
    
    def count(self) -> int:
        """Return total record count."""
        return len(self.collection.records)
    
    def find_by_source(self, citation_key: str) -> List[RawICADRecord]:
        """Find all records from a source."""
        return [
            r for r in self.collection.records
            if r.source_citation_key == citation_key
        ]
    
    def find_by_population(self, population_type: str) -> List[RawICADRecord]:
        """Find all records for a population type."""
        return [
            r for r in self.collection.records
            if r.population_type == population_type
        ]


class ICADStatsRepository(BaseRepository):
    """Repository for ICAD Statistics with write operations."""
    
    def __init__(self, storage_path: str = "data/icad_stats.json"):
        """Initialize ICAD Stats repository."""
        super().__init__(storage_path)
        self._stats: Optional[ICADStats] = None
    
    @property
    def stats(self) -> ICADStats:
        """Get or load the stats."""
        if self._stats is None:
            self.load()
        return self._stats
    
    def load(self) -> ICADStats:
        """Load stats from storage."""
        if not self.exists() or self.storage_path.stat().st_size == 0:
            self._stats = ICADStats()
        else:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._stats = ICADStats.from_dict(data)
        return self._stats
    
    def add_pattern(self, pattern: ConsumptionPattern) -> None:
        """Add a consumption pattern."""
        self.stats.add_pattern(pattern)
    
    def create_pattern(self, demographic: DemographicGroup,
                      metrics: List[ConsumptionMetric],
                      source: str,
                      notes: Optional[str] = None,
                      risk_assessments: Optional[List[RiskAssessment]] = None) -> ConsumptionPattern:
        """
        Create and add a new consumption pattern.
        
        Args:
            demographic: DemographicGroup for the pattern
            metrics: List of ConsumptionMetric
            source: Citation key
            notes: Optional notes
            risk_assessments: Optional risk assessments
            
        Returns:
            The created ConsumptionPattern
        """
        pattern = ConsumptionPattern(
            demographic=demographic,
            metrics=metrics,
            source=source,
            notes=notes,
            risk_assessments=risk_assessments or [],
        )
        self.stats.add_pattern(pattern)
        return pattern
    
    def update_pattern(self, index: int, updates: Dict[str, Any]) -> bool:
        """
        Update a pattern at given index.
        
        Args:
            index: Index of pattern to update
            updates: Dictionary of updates
            
        Returns:
            True if updated, False if index out of range
        """
        if index < 0 or index >= len(self.stats.patterns):
            return False
        
        pattern = self.stats.patterns[index]
        for field, value in updates.items():
            if hasattr(pattern, field):
                setattr(pattern, field, value)
        
        return True
    
    def delete_pattern(self, index: int) -> bool:
        """
        Delete pattern at given index.
        
        Args:
            index: Index of pattern to delete
            
        Returns:
            True if deleted, False if index out of range
        """
        if index < 0 or index >= len(self.stats.patterns):
            return False
        
        del self.stats.patterns[index]
        return True
    
    def delete_patterns_by_source(self, source: str) -> int:
        """
        Delete all patterns from a source.
        
        Args:
            source: Citation key to match
            
        Returns:
            Count of deleted patterns
        """
        original_count = len(self.stats.patterns)
        self.stats.patterns = [
            p for p in self.stats.patterns if p.source != source
        ]
        return original_count - len(self.stats.patterns)
    
    def save(self, indent: int = 2) -> None:
        """
        Persist stats to storage with backup.
        
        Args:
            indent: JSON indentation level
        """
        self._create_backup()
        
        try:
            self.stats.last_updated = datetime.now().isoformat()
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.storage_path, "w", encoding="utf-8") as f:
                f.write(self.stats.to_json(indent=indent))
            
            # Clean up backup on success
            if self._backup_path and self._backup_path.exists():
                os.remove(self._backup_path)
                self._backup_path = None
                
        except Exception as e:
            self._rollback()
            raise e
    
    def count(self) -> int:
        """Return total pattern count."""
        return len(self.stats.patterns)
    
    def find_by_population(self, population_type: str) -> List[ConsumptionPattern]:
        """Find all patterns for a population type."""
        return [
            p for p in self.stats.patterns
            if p.demographic.population_type == population_type
        ]
    
    def find_by_gender(self, gender: str) -> List[ConsumptionPattern]:
        """Find all patterns for a gender."""
        return [
            p for p in self.stats.patterns
            if p.demographic.gender == gender
        ]


def initialize_from_migration(migration_script: str, output_path: str) -> None:
    """
    Initialize a repository by running a migration script.
    
    Args:
        migration_script: Path to migration script (e.g., "scripts/migrate_raw_icad_stats.py")
        output_path: Path where migration writes its output
    """
    import subprocess
    import sys
    
    project_root = Path(__file__).parent.parent
    script_path = project_root / migration_script
    
    if not script_path.exists():
        raise FileNotFoundError(f"Migration script not found: {script_path}")
    
    # Run migration
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(project_root),
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        raise RuntimeError(f"Migration failed: {result.stderr}")
    
    print(f"✓ Initialized from migration: {migration_script}")
    print(f"✓ Output: {output_path}")

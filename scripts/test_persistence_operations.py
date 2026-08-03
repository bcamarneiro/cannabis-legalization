#!/usr/bin/env python3
"""
Tests for Persistence Layer Operations.

Run with: python scripts/test_persistence_operations.py
"""

import sys
import os
import json
import tempfile
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from data.raw_icad_schema import (
    RawICADRecord,
    RawICADCollection,
    DataQualityFlags,
    ICADSourceType,
    DataCollectionMethod,
)
from data.icad_stats_schema import (
    ICADStats,
    ConsumptionPattern,
    DemographicGroup,
    ConsumptionMetric,
    RiskAssessment,
)
from data.persistence_operations import (
    RawICADRepository,
    ICADStatsRepository,
)


def test_raw_repository_create():
    """Test creating records in RawICADRepository."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        record = RawICADRecord(
            record_id="TEST-001",
            source_type=ICADSourceType.SURVEY,
            collection_method=DataCollectionMethod.ONLINE_SURVEY,
            source_name="Test Survey",
            source_citation_key="test2024",
            population_type="general",
            metric_name="lifetime_prevalence",
            metric_value=5.0,
            metric_unit="percentage",
            data_year=2024,
        )
        
        record_id = repo.create(record)
        assert record_id == "TEST-001", f"Expected TEST-001, got {record_id}"
        assert repo.count() == 1, f"Expected 1 record, got {repo.count()}"
        print("✓ test_raw_repository_create passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_raw_repository_duplicate():
    """Test that duplicate record_id raises error."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        record = RawICADRecord(
            record_id="TEST-002",
            source_type=ICADSourceType.SURVEY,
            collection_method=DataCollectionMethod.ONLINE_SURVEY,
            source_name="Test Survey",
            source_citation_key="test2024",
            population_type="general",
            metric_name="lifetime_prevalence",
            metric_value=5.0,
            metric_unit="percentage",
            data_year=2024,
        )
        
        repo.create(record)
        
        # Try to create duplicate
        try:
            repo.create(record)
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "already exists" in str(e)
        
        print("✓ test_raw_repository_duplicate passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_raw_repository_update():
    """Test updating a record."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        record = RawICADRecord(
            record_id="TEST-003",
            source_type=ICADSourceType.SURVEY,
            collection_method=DataCollectionMethod.ONLINE_SURVEY,
            source_name="Test Survey",
            source_citation_key="test2024",
            population_type="general",
            metric_name="lifetime_prevalence",
            metric_value=5.0,
            metric_unit="percentage",
            data_year=2024,
        )
        
        repo.create(record)
        repo.save()
        
        # Update
        success = repo.update("TEST-003", {"metric_value": 7.5})
        assert success, "Update should succeed"
        
        # Verify
        updated = [r for r in repo.collection.records if r.record_id == "TEST-003"][0]
        assert updated.metric_value == 7.5, f"Expected 7.5, got {updated.metric_value}"
        
        # Update non-existent
        success = repo.update("NONEXISTENT", {"metric_value": 10.0})
        assert not success, "Update should fail for non-existent record"
        
        print("✓ test_raw_repository_update passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_raw_repository_delete():
    """Test deleting records."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        
        for i in range(3):
            record = RawICADRecord(
                record_id=f"TEST-00{i}",
                source_type=ICADSourceType.SURVEY,
                collection_method=DataCollectionMethod.ONLINE_SURVEY,
                source_name="Test Survey",
                source_citation_key="test2024",
                population_type="general",
                metric_name="lifetime_prevalence",
                metric_value=5.0,
                metric_unit="percentage",
                data_year=2024,
            )
            repo.create(record)
        
        assert repo.count() == 3
        
        # Delete single
        success = repo.delete("TEST-000")
        assert success
        assert repo.count() == 2
        
        # Delete non-existent
        success = repo.delete("NONEXISTENT")
        assert not success
        
        # Delete many
        deleted = repo.delete_many(lambda r: r.record_id.startswith("TEST-00"))
        assert deleted == 2
        assert repo.count() == 0
        
        print("✓ test_raw_repository_delete passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_raw_repository_upsert():
    """Test upsert operation."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        record = RawICADRecord(
            record_id="TEST-004",
            source_type=ICADSourceType.SURVEY,
            collection_method=DataCollectionMethod.ONLINE_SURVEY,
            source_name="Test Survey",
            source_citation_key="test2024",
            population_type="general",
            metric_name="lifetime_prevalence",
            metric_value=5.0,
            metric_unit="percentage",
            data_year=2024,
        )
        
        # Insert
        record_id = repo.upsert(record)
        assert record_id == "TEST-004"
        assert repo.count() == 1
        
        # Update via upsert
        record.metric_value = 10.0
        record_id = repo.upsert(record)
        assert record_id == "TEST-004"
        assert repo.count() == 1  # Still 1, not 2
        
        updated = repo.collection.records[0]
        assert updated.metric_value == 10.0
        
        print("✓ test_raw_repository_upsert passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_raw_repository_save_load():
    """Test persistence to disk."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        record = RawICADRecord(
            record_id="TEST-005",
            source_type=ICADSourceType.SURVEY,
            collection_method=DataCollectionMethod.ONLINE_SURVEY,
            source_name="Test Survey",
            source_citation_key="test2024",
            population_type="general",
            metric_name="lifetime_prevalence",
            metric_value=5.0,
            metric_unit="percentage",
            data_year=2024,
        )
        
        repo.create(record)
        repo.save()
        
        # Load in new repo instance
        repo2 = RawICADRepository(test_path)
        repo2.load()
        assert repo2.count() == 1
        assert repo2.collection.records[0].record_id == "TEST-005"
        
        print("✓ test_raw_repository_save_load passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_raw_repository_finders():
    """Test finder methods."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        
        for i, source in enumerate(["sicad2022", "icad2024", "sicad2022"]):
            record = RawICADRecord(
                record_id=f"TEST-FINDER-{i}",
                source_type=ICADSourceType.SURVEY,
                collection_method=DataCollectionMethod.ONLINE_SURVEY,
                source_name="Test Survey",
                source_citation_key=source,
                population_type="general" if source == "sicad2022" else "prison",
                metric_name="lifetime_prevalence",
                metric_value=5.0,
                metric_unit="percentage",
                data_year=2024,
            )
            repo.create(record)
        
        # Find by source
        results = repo.find_by_source("sicad2022")
        assert len(results) == 2
        
        # Find by population
        results = repo.find_by_population("prison")
        assert len(results) == 1
        
        print("✓ test_raw_repository_finders passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_stats_repository_add_pattern():
    """Test adding patterns to ICADStatsRepository."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = ICADStatsRepository(test_path)
        
        pattern = ConsumptionPattern(
            demographic=DemographicGroup(
                age_min=15,
                age_max=64,
                gender="all",
                population_type="general",
            ),
            metrics=[
                ConsumptionMetric(
                    metric_type="lifetime_prevalence",
                    value=10.5,
                    year=2024,
                )
            ],
            source="test2024",
            notes="Test pattern",
        )
        
        repo.add_pattern(pattern)
        assert repo.count() == 1
        
        print("✓ test_stats_repository_add_pattern passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_stats_repository_create_pattern():
    """Test create_pattern helper method."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = ICADStatsRepository(test_path)
        
        pattern = repo.create_pattern(
            demographic=DemographicGroup(age_min=15, age_max=24),
            metrics=[
                ConsumptionMetric(metric_type="high_risk_prevalence", value=1.3),
            ],
            source="test2024",
            notes="High risk youth",
        )
        
        assert repo.count() == 1
        assert pattern.notes == "High risk youth"
        
        print("✓ test_stats_repository_create_pattern passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_stats_repository_update_delete():
    """Test update and delete operations."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = ICADStatsRepository(test_path)
        
        for i in range(3):
            repo.create_pattern(
                demographic=DemographicGroup(age_min=15 + i, age_max=24 + i),
                metrics=[ConsumptionMetric(metric_type="test", value=float(i))],
                source=f"source{i}",
            )
        
        assert repo.count() == 3
        
        # Update
        success = repo.update_pattern(0, {"notes": "Updated"})
        assert success
        assert repo.stats.patterns[0].notes == "Updated"
        
        # Update invalid index
        success = repo.update_pattern(999, {"notes": "Fail"})
        assert not success
        
        # Delete
        success = repo.delete_pattern(0)
        assert success
        assert repo.count() == 2
        
        # Delete by source
        deleted = repo.delete_patterns_by_source("source1")
        assert deleted == 1
        assert repo.count() == 1
        
        print("✓ test_stats_repository_update_delete passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_stats_repository_finders():
    """Test finder methods for stats repository."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = ICADStatsRepository(test_path)
        
        repo.create_pattern(
            demographic=DemographicGroup(age_min=15, gender="male", population_type="general"),
            metrics=[ConsumptionMetric(metric_type="test", value=1.0)],
            source="test",
        )
        repo.create_pattern(
            demographic=DemographicGroup(age_min=15, gender="female", population_type="prison"),
            metrics=[ConsumptionMetric(metric_type="test", value=2.0)],
            source="test",
        )
        
        # Find by population
        results = repo.find_by_population("prison")
        assert len(results) == 1
        assert results[0].demographic.gender == "female"
        
        # Find by gender
        results = repo.find_by_gender("male")
        assert len(results) == 1
        
        print("✓ test_stats_repository_finders passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_stats_repository_save_load():
    """Test persistence for stats repository."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = ICADStatsRepository(test_path)
        
        repo.create_pattern(
            demographic=DemographicGroup(age_min=15, age_max=64),
            metrics=[ConsumptionMetric(metric_type="lifetime_prevalence", value=10.5)],
            source="test2024",
        )
        repo.save()
        
        # Load in new instance
        repo2 = ICADStatsRepository(test_path)
        repo2.load()
        assert repo2.count() == 1
        assert repo2.stats.patterns[0].metrics[0].value == 10.5
        
        print("✓ test_stats_repository_save_load passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def test_validation_on_create():
    """Test that validation is enforced on create."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        test_path = f.name
    
    try:
        repo = RawICADRepository(test_path)
        
        # Invalid: percentage out of range
        record = RawICADRecord(
            record_id="TEST-INVALID",
            source_type=ICADSourceType.SURVEY,
            collection_method=DataCollectionMethod.ONLINE_SURVEY,
            source_name="Test Survey",
            source_citation_key="test2024",
            population_type="general",
            metric_name="lifetime_prevalence",
            metric_value=150.0,  # Invalid: > 100
            metric_unit="percentage",
            data_year=2024,
        )
        
        try:
            repo.create(record)
            assert False, "Should have raised ValueError for invalid record"
        except ValueError as e:
            assert "out of range" in str(e)
        
        print("✓ test_validation_on_create passed")
    finally:
        if os.path.exists(test_path):
            os.unlink(test_path)


def main():
    """Run all tests."""
    print("Running persistence operations tests...")
    print("-" * 60)
    
    tests = [
        test_raw_repository_create,
        test_raw_repository_duplicate,
        test_raw_repository_update,
        test_raw_repository_delete,
        test_raw_repository_upsert,
        test_raw_repository_save_load,
        test_raw_repository_finders,
        test_stats_repository_add_pattern,
        test_stats_repository_create_pattern,
        test_stats_repository_update_delete,
        test_stats_repository_finders,
        test_stats_repository_save_load,
        test_validation_on_create,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"✗ {test.__name__} FAILED: {e}")
    
    print("-" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    
    if failed > 0:
        sys.exit(1)
    else:
        print("All tests passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()

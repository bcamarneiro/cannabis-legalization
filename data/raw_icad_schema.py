#!/usr/bin/env python3
"""
Raw ICAD Statistics Database Schema.

Defines the schema for storing raw inbound ICAD (Instituto das Dependências e 
Comportamentos Aditivos) data records before any processing or aggregation.

Usage:
    from raw_icad_schema import RawICADRecord, ICADSource, DataQualityFlags
    
    # Validate raw record
    record = RawICADRecord.from_dict(data)
    record.validate()
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List, Optional, Dict, Any
from enum import Enum
import json


class ICADSourceType(str, Enum):
    """Source type for ICAD data."""
    SURVEY = "survey"
    INSTITUTIONAL_REPORT = "institutional_report"
    ACADEMIC_STUDY = "academic_study"
    GOVERNMENT_STATISTICS = "government_statistics"
    INTERNATIONAL_DATABASE = "international_database"


class DataCollectionMethod(str, Enum):
    """Method used to collect the data."""
    ONLINE_SURVEY = "online_survey"
    PHONE_INTERVIEW = "phone_interview"
    IN_PERSON_INTERVIEW = "in_person_interview"
    PAPER_QUESTIONNAIRE = "paper_questionnaire"
    ADMINISTRATIVE_RECORDS = "administrative_records"
    CLINICAL_ASSESSMENT = "clinical_assessment"
    OBSERVATIONAL_STUDY = "observational_study"


@dataclass
class DataQualityFlags:
    """Quality indicators for raw data record."""
    completeness_score: Optional[float] = None  # 0-1
    validated: bool = False
    validation_date: Optional[str] = None
    validation_method: Optional[str] = None  # "manual", "automated", "hybrid"
    issues: List[str] = field(default_factory=list)
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "completeness_score": self.completeness_score,
            "validated": self.validated,
            "validation_date": self.validation_date,
            "validation_method": self.validation_method,
            "issues": self.issues,
            "notes": self.notes,
        }


@dataclass
class RawICADRecord:
    """Single raw inbound ICAD data record."""
    record_id: str  # Unique identifier (e.g., "ICAD-2024-00123")
    source_type: ICADSourceType
    collection_method: DataCollectionMethod
    source_name: str  # e.g., "V Inquérito Nacional", "ICAD Relatório 2024"
    source_citation_key: str  # BibTeX key (e.g., "sicad2022", "icad2024consumo")
    population_type: str  # "general", "prison", "youth_center", "student"
    metric_name: str  # e.g., "lifetime_prevalence", "daily_use", "cast_score_mean"
    metric_value: float
    metric_unit: str  # "percentage", "count", "mean_score", "ratio"
    data_year: int  # Year the data represents
    
    # Demographic scope (optional)
    age_min: Optional[int] = None
    age_max: Optional[int] = None
    gender: Optional[str] = None  # "male", "female", "all"
    region: Optional[str] = None  # e.g., "Norte", "Lisboa", "Nacional"
    
    # Contextual data (optional)
    sample_size: Optional[int] = None
    confidence_interval: Optional[str] = None  # e.g., "95% CI: 2.5-3.1"
    standard_error: Optional[float] = None
    p_value: Optional[float] = None
    
    # Temporal data (optional)
    collection_start_date: Optional[str] = None  # ISO format
    collection_end_date: Optional[str] = None
    publication_date: Optional[str] = None
    
    # Quality and metadata (optional)
    raw_notes: Optional[str] = None  # Original notes from source
    quality_flags: DataQualityFlags = field(default_factory=DataQualityFlags)
    ingestion_timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    ingested_by: str = "migration_script"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "record_id": self.record_id,
            "source_type": self.source_type.value,
            "collection_method": self.collection_method.value,
            "source_name": self.source_name,
            "source_citation_key": self.source_citation_key,
            "population_type": self.population_type,
            "age_min": self.age_min,
            "age_max": self.age_max,
            "gender": self.gender,
            "region": self.region,
            "metric_name": self.metric_name,
            "metric_value": self.metric_value,
            "metric_unit": self.metric_unit,
            "sample_size": self.sample_size,
            "confidence_interval": self.confidence_interval,
            "standard_error": self.standard_error,
            "p_value": self.p_value,
            "data_year": self.data_year,
            "collection_start_date": self.collection_start_date,
            "collection_end_date": self.collection_end_date,
            "publication_date": self.publication_date,
            "quality_flags": self.quality_flags.to_dict(),
            "raw_notes": self.raw_notes,
            "ingestion_timestamp": self.ingestion_timestamp,
            "ingested_by": self.ingested_by,
        }
    
    def validate(self) -> List[str]:
        """Validate record and return list of errors."""
        errors = []
        
        if not self.record_id:
            errors.append("Missing record_id")
        
        if not 0 <= self.metric_value <= 100 and self.metric_unit == "percentage":
            errors.append(f"metric_value {self.metric_value} out of range [0, 100] for percentage")
        
        if self.sample_size is not None and self.sample_size <= 0:
            errors.append(f"sample_size {self.sample_size} must be positive")
        
        if self.age_min is not None and self.age_max is not None:
            if self.age_min > self.age_max:
                errors.append(f"age_min {self.age_min} > age_max {self.age_max}")
        
        if self.data_year < 1900 or self.data_year > date.today().year:
            errors.append(f"data_year {self.data_year} out of valid range")
        
        return errors
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RawICADRecord":
        """Deserialize from dictionary."""
        quality_data = data.get("quality_flags", {})
        quality = DataQualityFlags(
            completeness_score=quality_data.get("completeness_score"),
            validated=quality_data.get("validated", False),
            validation_date=quality_data.get("validation_date"),
            validation_method=quality_data.get("validation_method"),
            issues=quality_data.get("issues", []),
            notes=quality_data.get("notes"),
        )
        
        return cls(
            record_id=data["record_id"],
            source_type=ICADSourceType(data["source_type"]),
            collection_method=DataCollectionMethod(data["collection_method"]),
            source_name=data["source_name"],
            source_citation_key=data["source_citation_key"],
            population_type=data["population_type"],
            age_min=data.get("age_min"),
            age_max=data.get("age_max"),
            gender=data.get("gender"),
            region=data.get("region"),
            metric_name=data["metric_name"],
            metric_value=data["metric_value"],
            metric_unit=data["metric_unit"],
            sample_size=data.get("sample_size"),
            confidence_interval=data.get("confidence_interval"),
            standard_error=data.get("standard_error"),
            p_value=data.get("p_value"),
            data_year=data["data_year"],
            collection_start_date=data.get("collection_start_date"),
            collection_end_date=data.get("collection_end_date"),
            publication_date=data.get("publication_date"),
            quality_flags=quality,
            raw_notes=data.get("raw_notes"),
            ingestion_timestamp=data.get("ingestion_timestamp", datetime.now().isoformat()),
            ingested_by=data.get("ingested_by", "migration_script"),
        )
    
    @classmethod
    def from_json(cls, json_str: str) -> "RawICADRecord":
        """Deserialize from JSON string."""
        return cls.from_dict(json.loads(json_str))


@dataclass
class RawICADCollection:
    """Collection of raw ICAD records."""
    version: str = "1.0.0"
    last_updated: str = field(default_factory=lambda: date.today().isoformat())
    records: List[RawICADRecord] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_record(self, record: RawICADRecord) -> None:
        self.records.append(record)
    
    def validate_all(self) -> Dict[str, List[str]]:
        """Validate all records. Returns dict of record_id -> errors."""
        errors = {}
        for record in self.records:
            record_errors = record.validate()
            if record_errors:
                errors[record.record_id] = record_errors
        return errors
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "last_updated": self.last_updated,
            "metadata": self.metadata,
            "records": [r.to_dict() for r in self.records],
        }
    
    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RawICADCollection":
        """Deserialize from dictionary."""
        collection = cls(
            version=data.get("version", "1.0.0"),
            last_updated=data.get("last_updated", date.today().isoformat()),
            metadata=data.get("metadata", {}),
        )
        for r_data in data.get("records", []):
            collection.add_record(RawICADRecord.from_dict(r_data))
        return collection
    
    @classmethod
    def from_json(cls, json_str: str) -> "RawICADCollection":
        """Deserialize from JSON string."""
        return cls.from_dict(json.loads(json_str))

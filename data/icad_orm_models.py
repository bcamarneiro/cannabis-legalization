#!/usr/bin/env python3
"""
ICAD Statistics ORM Models.

SQLAlchemy ORM models for ICAD (Instituto das Dependências e Comportamentos Aditivos)
statistics database tables. Maps application-layer models to raw and processed tables
for consistency checks and data validation.

Usage:
    from icad_orm_models import Base, ICADStatsRecord, PrevalenceData
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    
    engine = create_engine("sqlite:///icad_stats.db")
    Base.metadata.create_all(engine)
    
    with Session(engine) as session:
        record = ICADStatsRecord(...)
        session.add(record)
        session.commit()
"""

try:
    from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey, Date, DateTime, Enum as SQLEnum
    from sqlalchemy.orm import relationship, declarative_base
    from sqlalchemy.sql import func
    SQLALCHEMY_AVAILABLE = True
except ImportError:
    SQLALCHEMY_AVAILABLE = False
    # Stub for when SQLAlchemy is not installed
    class Column:
        def __init__(self, *args, **kwargs): pass
    class Integer: pass
    class Float: pass
    class String: pass
    class Text: pass
    class ForeignKey:
        def __init__(self, *args, **kwargs): pass
    class Date: pass
    class DateTime: pass
    class SQLEnum: pass
    def relationship(*args, **kwargs): pass
    def declarative_base(): return type('Base', (), {})
    class func:
        class now: pass

Base = declarative_base() if SQLALCHEMY_AVAILABLE else type('Base', (), {'__abstract__': True})


class ICADSourceType:
    """Source type constants for ICAD data."""
    SURVEY = "survey"
    INSTITUTIONAL_REPORT = "institutional_report"
    ACADEMIC_STUDY = "academic_study"
    GOVERNMENT_STATISTICS = "government_statistics"
    INTERNATIONAL_DATABASE = "international_database"


class DataCollectionMethod:
    """Data collection method constants."""
    ONLINE_SURVEY = "online_survey"
    PHONE_INTERVIEW = "phone_interview"
    IN_PERSON_INTERVIEW = "in_person_interview"
    PAPER_QUESTIONNAIRE = "paper_questionnaire"
    ADMINISTRATIVE_RECORDS = "administrative_records"
    CLINICAL_ASSESSMENT = "clinical_assessment"
    OBSERVATIONAL_STUDY = "observational_study"


class RawICADRecord(Base):
    """
    ORM model for raw inbound ICAD data records.
    
    Corresponds to the RawICADRecord dataclass in raw_icad_schema.py.
    Stores unprocessed data directly from sources before validation/aggregation.
    """
    __tablename__ = "raw_icad_records"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    record_id = Column(String(64), unique=True, nullable=False, index=True)  # e.g., "ICAD-2024-00123"
    
    # Source metadata
    source_type = Column(String(32), nullable=False)  # ICADSourceType values
    collection_method = Column(String(32), nullable=False)  # DataCollectionMethod values
    source_name = Column(String(256), nullable=False)  # e.g., "V Inquérito Nacional"
    source_citation_key = Column(String(64), nullable=False, index=True)  # BibTeX key
    
    # Demographic scope
    population_type = Column(String(32), nullable=False, index=True)  # "general", "prison", etc.
    age_min = Column(Integer, nullable=True)
    age_max = Column(Integer, nullable=True)
    gender = Column(String(16), nullable=True, index=True)  # "male", "female", "all"
    region = Column(String(128), nullable=True)  # e.g., "Norte", "Nacional"
    
    # Metric data
    metric_name = Column(String(64), nullable=False, index=True)  # e.g., "lifetime_prevalence"
    metric_value = Column(Float, nullable=False)
    metric_unit = Column(String(32), nullable=False)  # "percentage", "count", "mean_score"
    data_year = Column(Integer, nullable=False, index=True)
    
    # Statistical context (optional)
    sample_size = Column(Integer, nullable=True)
    confidence_interval = Column(String(64), nullable=True)
    standard_error = Column(Float, nullable=True)
    p_value = Column(Float, nullable=True)
    
    # Temporal data
    collection_start_date = Column(Date, nullable=True)
    collection_end_date = Column(Date, nullable=True)
    publication_date = Column(Date, nullable=True)
    
    # Quality and audit
    raw_notes = Column(Text, nullable=True)
    completeness_score = Column(Float, nullable=True)  # 0-1
    validated = Column(Integer, default=0)  # Boolean as Integer for SQLite compatibility
    validation_date = Column(Date, nullable=True)
    validation_method = Column(String(32), nullable=True)  # "manual", "automated", "hybrid"
    quality_issues = Column(Text, nullable=True)  # JSON array of issues
    
    ingestion_timestamp = Column(DateTime, server_default=func.now())
    ingested_by = Column(String(64), default="migration_script")
    
    def __repr__(self):
        return f"<RawICADRecord(record_id='{self.record_id}', metric='{self.metric_name}', value={self.metric_value})>"
    
    def to_dict(self):
        """Serialize to dictionary (compatible with dataclass pattern)."""
        return {
            "id": self.id,
            "record_id": self.record_id,
            "source_type": self.source_type,
            "collection_method": self.collection_method,
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
            "data_year": self.data_year,
            "sample_size": self.sample_size,
            "confidence_interval": self.confidence_interval,
            "standard_error": self.standard_error,
            "p_value": self.p_value,
            "collection_start_date": self.collection_start_date.isoformat() if self.collection_start_date else None,
            "collection_end_date": self.collection_end_date.isoformat() if self.collection_end_date else None,
            "publication_date": self.publication_date.isoformat() if self.publication_date else None,
            "raw_notes": self.raw_notes,
            "completeness_score": self.completeness_score,
            "validated": bool(self.validated),
            "validation_date": self.validation_date.isoformat() if self.validation_date else None,
            "validation_method": self.validation_method,
            "quality_issues": self.quality_issues,
            "ingestion_timestamp": self.ingestion_timestamp.isoformat() if self.ingestion_timestamp else None,
            "ingested_by": self.ingested_by,
        }


class ProcessedICADRecord(Base):
    """
    ORM model for processed/aggregated ICAD statistics.
    
    Corresponds to the ConsumptionPattern dataclass in icad_stats_schema.py.
    Stores validated, aggregated data ready for analysis and reporting.
    """
    __tablename__ = "processed_icad_records"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Demographic scope (required)
    age_min = Column(Integer, nullable=True)
    age_max = Column(Integer, nullable=True)
    gender = Column(String(16), nullable=True, index=True)  # "male", "female", "all"
    population_type = Column(String(32), nullable=False, index=True)
    
    # Consumption metrics
    metric_type = Column(String(64), nullable=False, index=True)  # "lifetime_prevalence", "last_year", etc.
    metric_value = Column(Float, nullable=False)
    metric_year = Column(Integer, nullable=False, index=True)
    
    # Statistical context
    sample_size = Column(Integer, nullable=True)
    confidence_interval = Column(String(64), nullable=True)
    notes = Column(Text, nullable=True)
    
    # Source citation
    source = Column(String(64), nullable=False, index=True)  # BibTeX key
    
    # Risk assessments (separate table for one-to-many)
    risk_level = Column(String(32), nullable=True)  # "low", "moderate", "high", "very_high"
    risk_tool = Column(String(64), nullable=True)  # "CAST", "CUDIT", etc.
    risk_percentage = Column(Float, nullable=True)
    risk_description = Column(Text, nullable=True)
    
    # Audit
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<ProcessedICADRecord(metric='{self.metric_type}', value={self.metric_value}, year={self.metric_year})>"
    
    def to_dict(self):
        """Serialize to dictionary."""
        return {
            "id": self.id,
            "age_min": self.age_min,
            "age_max": self.age_max,
            "gender": self.gender,
            "population_type": self.population_type,
            "metric_type": self.metric_type,
            "metric_value": self.metric_value,
            "metric_year": self.metric_year,
            "sample_size": self.sample_size,
            "confidence_interval": self.confidence_interval,
            "notes": self.notes,
            "source": self.source,
            "risk_level": self.risk_level,
            "risk_tool": self.risk_tool,
            "risk_percentage": self.risk_percentage,
            "risk_description": self.risk_description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class DataQualityCheck(Base):
    """
    ORM model for data quality validation results.
    
    Tracks consistency checks between raw and processed tables.
    """
    __tablename__ = "data_quality_checks"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Reference to source record
    raw_record_id = Column(String(64), ForeignKey("raw_icad_records.record_id"), index=True)
    processed_record_id = Column(Integer, ForeignKey("processed_icad_records.id"), index=True)
    
    # Check metadata
    check_type = Column(String(64), nullable=False)  # "completeness", "consistency", "accuracy"
    check_name = Column(String(128), nullable=False)  # e.g., "value_range_check"
    check_timestamp = Column(DateTime, server_default=func.now())
    
    # Result
    passed = Column(Integer, nullable=False)  # Boolean as Integer
    severity = Column(String(16), default="warning")  # "info", "warning", "error", "critical"
    message = Column(Text, nullable=True)
    details = Column(Text, nullable=True)  # JSON with detailed findings
    
    # Resolution
    resolved = Column(Integer, default=0)
    resolved_at = Column(DateTime, nullable=True)
    resolved_by = Column(String(64), nullable=True)
    
    def __repr__(self):
        return f"<DataQualityCheck(check='{self.check_name}', passed={bool(self.passed)})>"


class ICADDataSource(Base):
    """
    ORM model for ICAD data source registry.
    
    Tracks all data sources referenced in raw and processed tables.
    """
    __tablename__ = "icad_data_sources"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    citation_key = Column(String(64), unique=True, nullable=False, index=True)  # BibTeX key
    
    # Source metadata
    source_type = Column(String(32), nullable=False)
    official_name = Column(String(256), nullable=False)
    publisher = Column(String(256), nullable=True)
    publication_date = Column(Date, nullable=True)
    url = Column(String(512), nullable=True)
    
    # Coverage
    population_coverage = Column(String(128), nullable=True)  # e.g., "general, 15-74 years"
    geographic_coverage = Column(String(128), nullable=True)  # e.g., "Nacional", "Norte"
    temporal_coverage_start = Column(Integer, nullable=True)  # Year
    temporal_coverage_end = Column(Integer, nullable=True)  # Year
    
    # Quality indicators
    reliability_score = Column(Float, nullable=True)  # 0-1
    sample_size_total = Column(Integer, nullable=True)
    methodology_notes = Column(Text, nullable=True)
    
    # Usage tracking
    record_count = Column(Integer, default=0)  # Number of records using this source
    last_used = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<ICADDataSource(key='{self.citation_key}', name='{self.official_name}')>"


# Table relationship helpers (for when SQLAlchemy is available)
if SQLALCHEMY_AVAILABLE:
    # Define relationships
    RawICADRecord.quality_checks = relationship(
        "DataQualityCheck",
        back_populates="raw_record",
        cascade="all, delete-orphan"
    )
    
    ProcessedICADRecord.quality_checks = relationship(
        "DataQualityCheck",
        back_populates="processed_record",
        cascade="all, delete-orphan"
    )
    
    # Add back references
    DataQualityCheck.raw_record = relationship("RawICADRecord", back_populates="quality_checks")
    DataQualityCheck.processed_record = relationship("ProcessedICADRecord", back_populates="quality_checks")


def create_tables(engine):
    """
    Create all ICAD tables in the database.
    
    Args:
        engine: SQLAlchemy Engine instance
    
    Usage:
        from sqlalchemy import create_engine
        engine = create_engine("sqlite:///icad_stats.db")
        create_tables(engine)
    """
    if not SQLALCHEMY_AVAILABLE:
        raise ImportError("SQLAlchemy is required to create tables")
    
    Base.metadata.create_all(engine)


def drop_tables(engine):
    """
    Drop all ICAD tables from the database.
    
    Args:
        engine: SQLAlchemy Engine instance
    """
    if not SQLALCHEMY_AVAILABLE:
        raise ImportError("SQLAlchemy is required to drop tables")
    
    Base.metadata.drop_all(engine)

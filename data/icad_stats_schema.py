#!/usr/bin/env python3
"""
ICAD Statistics Database Schema and Data Models.

Defines the schema for storing ICAD (Instituto das Dependências e Comportamentos Aditivos)
statistics referenced in the cannabis legalization policy document.

Usage:
    from icad_stats_schema import ICADStats, PrevalenceData, ConsumptionPattern
    
    # Validate stats data
    stats = ICADStats.from_dict(data)
    stats.validate()
"""

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional, Dict, Any
import json


@dataclass
class DemographicGroup:
    """Demographic group identifier (age range, gender, population type)."""
    age_min: Optional[int] = None
    age_max: Optional[int] = None
    gender: Optional[str] = None  # "male", "female", "all"
    population_type: str = "general"  # "general", "prison", "youth_center", "student"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "age_min": self.age_min,
            "age_max": self.age_max,
            "gender": self.gender,
            "population_type": self.population_type,
        }


@dataclass
class ConsumptionMetric:
    """Single consumption metric (prevalence, frequency, risk level)."""
    metric_type: str  # "lifetime_prevalence", "last_year", "last_month", "daily", "problematic"
    value: float  # percentage (0-100)
    sample_size: Optional[int] = None
    confidence_interval: Optional[str] = None  # e.g., "95% CI: 2.5-3.1"
    year: int = field(default_factory=lambda: date.today().year)
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "metric_type": self.metric_type,
            "value": self.value,
            "sample_size": self.sample_size,
            "confidence_interval": self.confidence_interval,
            "year": self.year,
            "notes": self.notes,
        }


@dataclass
class RiskAssessment:
    """Risk level assessment (CAST score, CUD risk, etc.)."""
    tool_name: str  # "CAST", "CUDIT", "DAST", "custom"
    risk_level: str  # "low", "moderate", "high", "very_high"
    percentage: float
    description: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "tool_name": self.tool_name,
            "risk_level": self.risk_level,
            "percentage": self.percentage,
            "description": self.description,
        }


@dataclass
class ConsumptionPattern:
    """Consumption pattern for a specific demographic group."""
    demographic: DemographicGroup
    metrics: List[ConsumptionMetric] = field(default_factory=list)
    risk_assessments: List[RiskAssessment] = field(default_factory=list)
    notes: Optional[str] = None
    source: str = ""  # Citation key (e.g., "sicad2022", "icad2024consumo")
    
    def add_metric(self, metric: ConsumptionMetric) -> None:
        self.metrics.append(metric)
    
    def add_risk_assessment(self, risk: RiskAssessment) -> None:
        self.risk_assessments.append(risk)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "demographic": self.demographic.to_dict(),
            "metrics": [m.to_dict() for m in self.metrics],
            "risk_assessments": [r.to_dict() for r in self.risk_assessments],
            "notes": self.notes,
            "source": self.source,
        }


@dataclass
class ICADStats:
    """Complete ICAD statistics dataset."""
    version: str = "1.0.0"
    last_updated: str = field(default_factory=lambda: date.today().isoformat())
    patterns: List[ConsumptionPattern] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_pattern(self, pattern: ConsumptionPattern) -> None:
        self.patterns.append(pattern)
    
    def validate(self) -> List[str]:
        """Validate all patterns and return list of errors."""
        errors = []
        for i, pattern in enumerate(self.patterns):
            if not pattern.source:
                errors.append(f"Pattern {i}: missing source citation")
            for metric in pattern.metrics:
                if not 0 <= metric.value <= 100:
                    errors.append(f"Pattern {i}: metric value {metric.value} out of range [0, 100]")
        return errors
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "last_updated": self.last_updated,
            "metadata": self.metadata,
            "patterns": [p.to_dict() for p in self.patterns],
        }
    
    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ICADStats":
        """Deserialize from dictionary."""
        stats = cls(
            version=data.get("version", "1.0.0"),
            last_updated=data.get("last_updated", date.today().isoformat()),
            metadata=data.get("metadata", {}),
        )
        for p_data in data.get("patterns", []):
            demo = DemographicGroup(**p_data["demographic"])
            pattern = ConsumptionPattern(
                demographic=demo,
                notes=p_data.get("notes"),
                source=p_data.get("source", ""),
            )
            for m_data in p_data.get("metrics", []):
                pattern.add_metric(ConsumptionMetric(**m_data))
            for r_data in p_data.get("risk_assessments", []):
                pattern.add_risk_assessment(RiskAssessment(**r_data))
            stats.add_pattern(pattern)
        return stats
    
    @classmethod
    def from_json(cls, json_str: str) -> "ICADStats":
        """Deserialize from JSON string."""
        return cls.from_dict(json.loads(json_str))

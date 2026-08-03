#!/usr/bin/env python3
"""
Processed ICAD Statistics Database Schema.

Defines the schema for storing derived/aggregated ICAD statistics records
for the Processed ICAD Statistics tab in the policy document dashboard.

Unlike the raw icad_stats_schema.py which stores individual consumption patterns,
this schema stores pre-computed aggregations, trends, and derived metrics.

Usage:
    from processed_icad_schema import ProcessedICADStats, AggregatedMetric, TrendAnalysis
    
    # Create processed stats
    processed = ProcessedICADStats()
    processed.add_aggregation(AggregatedMetric(...))
"""

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional, Dict, Any
import json


@dataclass
class TimeRange:
    """Time range for aggregated statistics."""
    start_year: int
    end_year: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "start_year": self.start_year,
            "end_year": self.end_year,
        }
    
    @property
    def span_years(self) -> int:
        return self.end_year - self.start_year + 1


@dataclass
class DemographicFilter:
    """Demographic filter for aggregated statistics."""
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
    
    def matches(self, other: "DemographicFilter") -> bool:
        """Check if this filter matches another (for grouping)."""
        return (
            self.population_type == other.population_type and
            self.gender == other.gender
        )


@dataclass
class AggregatedMetric:
    """
    Aggregated metric computed from raw ICAD statistics.
    
    Examples:
    - Average consumption rate across multiple years
    - Total affected population estimate
    - EU comparison ratio
    """
    metric_name: str  # e.g., "avg_last_year_prevalence", "eu_comparison_ratio"
    metric_category: str  # "prevalence", "frequency", "risk", "comparison", "trend"
    value: float
    unit: str = "percent"  # "percent", "ratio", "count", "index"
    time_range: Optional[TimeRange] = None
    demographic: Optional[DemographicFilter] = None
    source_metrics: List[str] = field(default_factory=list)  # Names of source metrics used
    computation_method: Optional[str] = None  # e.g., "mean", "weighted_mean", "sum"
    confidence_interval: Optional[str] = None  # e.g., "95% CI: 2.5-3.1"
    notes: Optional[str] = None
    computed_at: str = field(default_factory=lambda: date.today().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "metric_name": self.metric_name,
            "metric_category": self.metric_category,
            "value": self.value,
            "unit": self.unit,
            "time_range": self.time_range.to_dict() if self.time_range else None,
            "demographic": self.demographic.to_dict() if self.demographic else None,
            "source_metrics": self.source_metrics,
            "computation_method": self.computation_method,
            "confidence_interval": self.confidence_interval,
            "notes": self.notes,
            "computed_at": self.computed_at,
        }


@dataclass
class TrendAnalysis:
    """
    Trend analysis for a metric over time.
    
    Examples:
    - Year-over-year change in youth consumption
    - 5-year trend in high-risk prevalence
    """
    trend_name: str
    metric_type: str  # Base metric being analyzed
    demographic: DemographicFilter
    start_year: int
    end_year: int
    direction: str  # "increasing", "decreasing", "stable", "volatile"
    change_percent: float  # Overall percent change over period
    annual_rate: Optional[float] = None  # Average annual rate of change
    significance: Optional[str] = None  # "statistically_significant", "notable", "marginal"
    data_points: int = 0  # Number of data points in trend
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "trend_name": self.trend_name,
            "metric_type": self.metric_type,
            "demographic": self.demographic.to_dict(),
            "start_year": self.start_year,
            "end_year": self.end_year,
            "direction": self.direction,
            "change_percent": self.change_percent,
            "annual_rate": self.annual_rate,
            "significance": self.significance,
            "data_points": self.data_points,
            "notes": self.notes,
        }


@dataclass
class ComparativeAnalysis:
    """
    Comparative analysis between groups or against benchmarks.
    
    Examples:
    - Gender comparison (male vs female consumption)
    - Portugal vs EU average
    - Prison population vs general population
    """
    comparison_name: str
    group_a: str  # e.g., "portugal_male", "prison_population"
    group_b: str  # e.g., "portugal_female", "general_population", "eu_average"
    metric_type: str
    value_a: float
    value_b: float
    ratio: float  # a / b
    difference_percent: float  # (a - b) / b * 100
    interpretation: Optional[str] = None  # e.g., "50% higher than EU average"
    year: int = field(default_factory=lambda: date.today().year)
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "comparison_name": self.comparison_name,
            "group_a": self.group_a,
            "group_b": self.group_b,
            "metric_type": self.metric_type,
            "value_a": self.value_a,
            "value_b": self.value_b,
            "ratio": self.ratio,
            "difference_percent": self.difference_percent,
            "interpretation": self.interpretation,
            "year": self.year,
            "notes": self.notes,
        }


@dataclass
class SummaryStatistic:
    """
    High-level summary statistic for dashboard display.
    
    Examples:
    - "X Portuguese show lifetime cannabis use"
    - "Y% of users display problematic patterns"
    """
    title: str
    value: float
    unit: str  # "percent", "count", "ratio"
    category: str  # "key_finding", "alert", "benchmark"
    demographic_context: Optional[str] = None  # e.g., "ages 15-64, 2022"
    source: Optional[str] = None  # Citation key
    priority: int = 0  # Display priority (higher = more prominent)
    icon: Optional[str] = None  # Suggested icon: "alert", "info", "trend_up", "trend_down"
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "value": self.value,
            "unit": self.unit,
            "category": self.category,
            "demographic_context": self.demographic_context,
            "source": self.source,
            "priority": self.priority,
            "icon": self.icon,
            "notes": self.notes,
        }


@dataclass
class ProcessedICADStats:
    """
    Complete processed ICAD statistics dataset.
    
    Contains pre-computed aggregations, trends, comparisons, and summaries
    derived from raw ICAD statistics for dashboard display.
    """
    version: str = "1.0.0"
    last_updated: str = field(default_factory=lambda: date.today().isoformat())
    aggregations: List[AggregatedMetric] = field(default_factory=list)
    trends: List[TrendAnalysis] = field(default_factory=list)
    comparisons: List[ComparativeAnalysis] = field(default_factory=list)
    summaries: List[SummaryStatistic] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_aggregation(self, agg: AggregatedMetric) -> None:
        self.aggregations.append(agg)
    
    def add_trend(self, trend: TrendAnalysis) -> None:
        self.trends.append(trend)
    
    def add_comparison(self, comp: ComparativeAnalysis) -> None:
        self.comparisons.append(comp)
    
    def add_summary(self, summary: SummaryStatistic) -> None:
        self.summaries.append(summary)
    
    def validate(self) -> List[str]:
        """Validate all records and return list of errors."""
        errors = []
        
        for i, agg in enumerate(self.aggregations):
            if not agg.metric_name:
                errors.append(f"Aggregation {i}: missing metric_name")
            if agg.value < 0:
                errors.append(f"Aggregation {i}: negative value {agg.value}")
        
        for i, trend in enumerate(self.trends):
            if not trend.trend_name:
                errors.append(f"Trend {i}: missing trend_name")
            if trend.start_year > trend.end_year:
                errors.append(f"Trend {i}: start_year > end_year")
        
        for i, comp in enumerate(self.comparisons):
            if not comp.comparison_name:
                errors.append(f"Comparison {i}: missing comparison_name")
            if comp.group_a == comp.group_b:
                errors.append(f"Comparison {i}: group_a and group_b are identical")
        
        for i, summary in enumerate(self.summaries):
            if not summary.title:
                errors.append(f"Summary {i}: missing title")
        
        return errors
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "last_updated": self.last_updated,
            "metadata": self.metadata,
            "aggregations": [a.to_dict() for a in self.aggregations],
            "trends": [t.to_dict() for t in self.trends],
            "comparisons": [c.to_dict() for c in self.comparisons],
            "summaries": [s.to_dict() for s in self.summaries],
        }
    
    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProcessedICADStats":
        """Deserialize from dictionary."""
        stats = cls(
            version=data.get("version", "1.0.0"),
            last_updated=data.get("last_updated", date.today().isoformat()),
            metadata=data.get("metadata", {}),
        )
        
        for a_data in data.get("aggregations", []):
            time_range = None
            if a_data.get("time_range"):
                tr = a_data["time_range"]
                time_range = TimeRange(start_year=tr["start_year"], end_year=tr["end_year"])
            
            demographic = None
            if a_data.get("demographic"):
                d = a_data["demographic"]
                demographic = DemographicFilter(
                    age_min=d.get("age_min"),
                    age_max=d.get("age_max"),
                    gender=d.get("gender"),
                    population_type=d.get("population_type", "general"),
                )
            
            agg = AggregatedMetric(
                metric_name=a_data["metric_name"],
                metric_category=a_data["metric_category"],
                value=a_data["value"],
                unit=a_data.get("unit", "percent"),
                time_range=time_range,
                demographic=demographic,
                source_metrics=a_data.get("source_metrics", []),
                computation_method=a_data.get("computation_method"),
                confidence_interval=a_data.get("confidence_interval"),
                notes=a_data.get("notes"),
                computed_at=a_data.get("computed_at", date.today().isoformat()),
            )
            stats.add_aggregation(agg)
        
        for t_data in data.get("trends", []):
            demo = DemographicFilter(
                age_min=t_data["demographic"].get("age_min"),
                age_max=t_data["demographic"].get("age_max"),
                gender=t_data["demographic"].get("gender"),
                population_type=t_data["demographic"].get("population_type", "general"),
            )
            trend = TrendAnalysis(
                trend_name=t_data["trend_name"],
                metric_type=t_data["metric_type"],
                demographic=demo,
                start_year=t_data["start_year"],
                end_year=t_data["end_year"],
                direction=t_data["direction"],
                change_percent=t_data["change_percent"],
                annual_rate=t_data.get("annual_rate"),
                significance=t_data.get("significance"),
                data_points=t_data.get("data_points", 0),
                notes=t_data.get("notes"),
            )
            stats.add_trend(trend)
        
        for c_data in data.get("comparisons", []):
            comp = ComparativeAnalysis(
                comparison_name=c_data["comparison_name"],
                group_a=c_data["group_a"],
                group_b=c_data["group_b"],
                metric_type=c_data["metric_type"],
                value_a=c_data["value_a"],
                value_b=c_data["value_b"],
                ratio=c_data["ratio"],
                difference_percent=c_data["difference_percent"],
                interpretation=c_data.get("interpretation"),
                year=c_data.get("year", date.today().year),
                notes=c_data.get("notes"),
            )
            stats.add_comparison(comp)
        
        for s_data in data.get("summaries", []):
            summary = SummaryStatistic(
                title=s_data["title"],
                value=s_data["value"],
                unit=s_data["unit"],
                category=s_data["category"],
                demographic_context=s_data.get("demographic_context"),
                source=s_data.get("source"),
                priority=s_data.get("priority", 0),
                icon=s_data.get("icon"),
                notes=s_data.get("notes"),
            )
            stats.add_summary(summary)
        
        return stats
    
    @classmethod
    def from_json(cls, json_str: str) -> "ProcessedICADStats":
        """Deserialize from JSON string."""
        return cls.from_dict(json.loads(json_str))

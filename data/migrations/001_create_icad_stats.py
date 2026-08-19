#!/usr/bin/env python3
"""
Migration 001 — Create ICAD statistics initial data.

Populates data/icad_stats_initial.json with 10 consumption patterns
sourced from SICAD 2022, ICAD 2024 (Carapinha study), and EUDA 2024.

This is the schema-versioned equivalent of scripts/migrate_icad_stats.py —
the output file path and shape are unchanged so existing consumers
(loading scripts, persistence layer) keep working.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from data.icad_stats_schema import (  # noqa: E402
    ICADStats,
    ConsumptionPattern,
    DemographicGroup,
    ConsumptionMetric,
    RiskAssessment,
)


# Migration metadata (consumed by data.migrations.runner).
VERSION = "001"
NAME = "create_icad_stats"
DESCRIPTION = "Create initial ICAD statistics dataset (10 consumption patterns)"

# Relative paths the migration creates — used by the runner for status,
# and by operators to see what a migration owns at a glance.
TARGETS = ["data/icad_stats_initial.json"]

OUTPUT_PATH = REPO_ROOT / "data" / "icad_stats_initial.json"


def _build_stats() -> ICADStats:
    """Build the initial ICAD statistics from the document data."""
    stats = ICADStats(
        version="1.0.0",
        last_updated="2026-02-26",
        metadata={
            "description": "Initial ICAD statistics migration from cannabis legalization policy document",
            "sources": [
                "sicad2022 - V Inquérito Nacional (2022)",
                "icad2024consumo - ICAD December 2024 report (Carapinha study)",
                "carapinha2024icad - Institutional populations study",
                "euda2024cannabis - EMCDDA European averages",
            ],
            "document_branch": "main",
            "migration_script": "data/migrations/001_create_icad_stats.py",
        },
    )

    # Pattern 1: General population (15-64 years) - SICAD 2022
    general_pop = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=15, age_max=64, gender="all", population_type="general"
        ),
        source="sicad2022",
        notes="Portugal below European average",
    )
    general_pop.add_metric(ConsumptionMetric(
        metric_type="lifetime_prevalence", value=10.5, year=2022
    ))
    general_pop.add_metric(ConsumptionMetric(
        metric_type="last_year", value=2.8, year=2022, notes="EU average: 8.4%"
    ))
    stats.add_pattern(general_pop)

    # Pattern 2: Youth (15-24 years) - High-risk consumption increase
    youth_risk = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=15, age_max=24, gender="all", population_type="general"
        ),
        source="sicad2022",
        notes="Concerning increase in high-risk consumption",
    )
    youth_risk.add_metric(ConsumptionMetric(
        metric_type="high_risk_prevalence", value=0.2, year=2012,
        notes="Baseline CAST high-risk"
    ))
    youth_risk.add_metric(ConsumptionMetric(
        metric_type="high_risk_prevalence", value=1.3, year=2022,
        notes="6.5x increase over decade"
    ))
    stats.add_pattern(youth_risk)

    # Pattern 3: General population (15-74 years) - ICAD 2024
    icad_2024_general = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=15, age_max=74, gender="all", population_type="general"
        ),
        source="icad2024consumo",
        notes="~2% last year use, 25-35% show problematic patterns",
    )
    icad_2024_general.add_metric(ConsumptionMetric(
        metric_type="last_year", value=2.0, year=2024
    ))
    icad_2024_general.add_metric(ConsumptionMetric(
        metric_type="problematic_consumption", value=30.0, year=2024,
        notes="Range: 25-35% of users"
    ))
    stats.add_pattern(icad_2024_general)

    # Pattern 4: Men (15-74 years) - ICAD 2024 gender breakdown
    men_general = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=15, age_max=74, gender="male", population_type="general"
        ),
        source="icad2024consumo",
        notes="Men show 5-10x higher frequent use than women",
    )
    men_general.add_metric(ConsumptionMetric(
        metric_type="frequent_use", value=1.1, year=2024, notes="Range: 1-1.2%"
    ))
    men_general.add_metric(ConsumptionMetric(
        metric_type="problematic_consumption", value=32.0, year=2024,
        notes="Among male users"
    ))
    stats.add_pattern(men_general)

    # Pattern 5: Women (15-74 years) - ICAD 2024 gender breakdown
    women_general = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=15, age_max=74, gender="female", population_type="general"
        ),
        source="icad2024consumo",
        notes="Women show much lower frequent use but significant problematic patterns",
    )
    women_general.add_metric(ConsumptionMetric(
        metric_type="frequent_use", value=0.15, year=2024,
        notes="Range: 0.1-0.2%, 5-10x lower than men"
    ))
    women_general.add_metric(ConsumptionMetric(
        metric_type="problematic_consumption", value=19.0, year=2024,
        notes="Among female users"
    ))
    stats.add_pattern(women_general)

    # Pattern 6: Prison population - Gender inversion
    prison_women = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=18, age_max=None, gender="female", population_type="prison"
        ),
        source="carapinha2024icad",
        notes="CRITICAL: Gender pattern inverts in prison - 63% daily use",
    )
    prison_women.add_metric(ConsumptionMetric(
        metric_type="daily_use", value=63.0, year=2024,
        notes="vs 46% for men - dramatic inversion"
    ))
    stats.add_pattern(prison_women)

    prison_men = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=18, age_max=None, gender="male", population_type="prison"
        ),
        source="carapinha2024icad",
        notes="Men in prison: 46% daily use",
    )
    prison_men.add_metric(ConsumptionMetric(
        metric_type="daily_use", value=46.0, year=2024
    ))
    stats.add_pattern(prison_men)

    # Pattern 7: Youth centers (institutionalized) - Girls crisis
    youth_center_girls = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=12, age_max=18, gender="female", population_type="youth_center"
        ),
        source="carapinha2024icad",
        notes="CRITICAL: 100% of girls in youth centers show high-risk consumption",
    )
    youth_center_girls.add_metric(ConsumptionMetric(
        metric_type="high_risk_prevalence", value=100.0, year=2024,
        notes="All girls in institutional care"
    ))
    youth_center_girls.add_metric(ConsumptionMetric(
        metric_type="daily_use", value=62.0, year=2024,
        notes="Daily or near-daily use"
    ))
    youth_center_girls.add_risk_assessment(RiskAssessment(
        tool_name="CAST", risk_level="very_high", percentage=100.0,
        description="All girls show moderate-to-high risk consumption"
    ))
    stats.add_pattern(youth_center_girls)

    youth_center_boys = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=12, age_max=18, gender="male", population_type="youth_center"
        ),
        source="carapinha2024icad",
        notes="Boys in youth centers: 49% high-risk",
    )
    youth_center_boys.add_metric(ConsumptionMetric(
        metric_type="high_risk_prevalence", value=49.0, year=2024
    ))
    youth_center_boys.add_metric(ConsumptionMetric(
        metric_type="daily_use", value=62.0, year=2024,
        notes="Daily or near-daily use (same as girls)"
    ))
    stats.add_pattern(youth_center_boys)

    # Pattern 8: Students (13-18 years) - ICAD December 2024
    students = ConsumptionPattern(
        demographic=DemographicGroup(
            age_min=13, age_max=18, gender="all", population_type="student"
        ),
        source="icad2024consumo",
        notes="11,083 students, 329 schools - cannabis most consumed illicit substance",
    )
    students.add_metric(ConsumptionMetric(
        metric_type="lifetime_prevalence", value=6.6, year=2024,
        notes="Experimentation rate"
    ))
    students.add_metric(ConsumptionMetric(
        metric_type="recent_use", value=2.0, year=2024, notes="Last 30 days"
    ))
    students.add_metric(ConsumptionMetric(
        metric_type="daily_use", value=1.0, year=2024,
        notes="Under 1% daily in this age group"
    ))
    stats.add_pattern(students)

    return stats


def up() -> None:
    """Apply the migration: validate and write data/icad_stats_initial.json."""
    stats = _build_stats()
    errors = stats.validate()
    if errors:
        raise RuntimeError(
            f"ICAD stats validation failed: {errors}"
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(stats.to_json(indent=2), encoding="utf-8")


def down() -> None:
    """Rollback the migration: remove the generated JSON file."""
    if OUTPUT_PATH.exists():
        OUTPUT_PATH.unlink()


if __name__ == "__main__":
    # Allow `python -m data.migrations.001_create_icad_stats` style execution
    # for debugging. The runner is the canonical entry point.
    up()
    print(f"Applied {VERSION}_{NAME} → {OUTPUT_PATH}")

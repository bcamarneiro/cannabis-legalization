#!/usr/bin/env python3
"""
Migration 002 — Create raw ICAD statistics initial data.

Populates data/raw_icad_stats_initial.json with 19 raw inbound records
from the same source studies as migration 001: SICAD 2022, ICAD 2024
(Carapinha study), and EUDA 2024.

This is the schema-versioned equivalent of scripts/migrate_raw_icad_stats.py —
the output file path and shape are unchanged so existing consumers
keep working.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from data.raw_icad_schema import (  # noqa: E402
    RawICADCollection,
    RawICADRecord,
    DataQualityFlags,
    ICADSourceType,
    DataCollectionMethod,
)


# Migration metadata (consumed by data.migrations.runner).
VERSION = "002"
NAME = "create_raw_icad_stats"
DESCRIPTION = "Create initial raw ICAD records dataset (19 records)"

# Relative paths the migration creates.
TARGETS = ["data/raw_icad_stats_initial.json"]

OUTPUT_PATH = REPO_ROOT / "data" / "raw_icad_stats_initial.json"


def _build_collection() -> RawICADCollection:
    """Build the initial raw ICAD collection from the document data."""
    collection = RawICADCollection(
        version="1.0.0",
        last_updated="2026-02-26",
        metadata={
            "description": "Initial raw ICAD statistics migration from cannabis legalization policy document",
            "sources": [
                "sicad2022 - V Inquérito Nacional (2022)",
                "icad2024consumo - ICAD December 2024 report (Carapinha study)",
                "carapinha2024icad - Institutional populations study",
                "euda2024cannabis - EMCDDA European averages",
            ],
            "document_branch": "main",
            "migration_script": "data/migrations/002_create_raw_icad_stats.py",
            "note": "Raw inbound records - unprocessed, direct from sources",
        },
    )

    def _record(**kwargs) -> RawICADRecord:
        return RawICADRecord(**kwargs)

    # SICAD 2022 — General population (15-64 years)
    collection.add_record(_record(
        record_id="ICAD-2022-001",
        source_type=ICADSourceType.SURVEY,
        collection_method=DataCollectionMethod.IN_PERSON_INTERVIEW,
        source_name="V Inquérito Nacional 2022",
        source_citation_key="sicad2022",
        population_type="general",
        age_min=15, age_max=64, gender="all",
        region="Nacional",
        metric_name="lifetime_prevalence",
        metric_value=10.5, metric_unit="percentage",
        data_year=2022, publication_date="2022-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.95, validated=True,
            validation_date="2026-01-15", validation_method="automated",
        ),
        raw_notes="Portugal below European average (8.4%)",
    ))
    collection.add_record(_record(
        record_id="ICAD-2022-002",
        source_type=ICADSourceType.SURVEY,
        collection_method=DataCollectionMethod.IN_PERSON_INTERVIEW,
        source_name="V Inquérito Nacional 2022",
        source_citation_key="sicad2022",
        population_type="general",
        age_min=15, age_max=64, gender="all",
        region="Nacional",
        metric_name="last_year_prevalence",
        metric_value=2.8, metric_unit="percentage",
        data_year=2022, publication_date="2022-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.95, validated=True,
            validation_date="2026-01-15", validation_method="automated",
        ),
        raw_notes="EU average: 8.4%",
    ))

    # SICAD 2022 — Youth high-risk consumption (15-24 years)
    collection.add_record(_record(
        record_id="ICAD-2022-003",
        source_type=ICADSourceType.SURVEY,
        collection_method=DataCollectionMethod.IN_PERSON_INTERVIEW,
        source_name="V Inquérito Nacional 2022",
        source_citation_key="sicad2022",
        population_type="general",
        age_min=15, age_max=24, gender="all",
        region="Nacional",
        metric_name="high_risk_prevalence",
        metric_value=0.2, metric_unit="percentage",
        data_year=2012, publication_date="2022-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.90, validated=True,
            validation_date="2026-01-15", validation_method="automated",
        ),
        raw_notes="Baseline CAST high-risk 2012",
    ))
    collection.add_record(_record(
        record_id="ICAD-2022-004",
        source_type=ICADSourceType.SURVEY,
        collection_method=DataCollectionMethod.IN_PERSON_INTERVIEW,
        source_name="V Inquérito Nacional 2022",
        source_citation_key="sicad2022",
        population_type="general",
        age_min=15, age_max=24, gender="all",
        region="Nacional",
        metric_name="high_risk_prevalence",
        metric_value=1.3, metric_unit="percentage",
        data_year=2022, publication_date="2022-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.90, validated=True,
            validation_date="2026-01-15", validation_method="automated",
        ),
        raw_notes="6.5x increase over decade (2012-2022)",
    ))

    # ICAD 2024 — General population (15-74 years)
    collection.add_record(_record(
        record_id="ICAD-2024-001",
        source_type=ICADSourceType.INSTITUTIONAL_REPORT,
        collection_method=DataCollectionMethod.PHONE_INTERVIEW,
        source_name="ICAD Relatório Dezembro 2024",
        source_citation_key="icad2024consumo",
        population_type="general",
        age_min=15, age_max=74, gender="all",
        region="Nacional",
        metric_name="last_year_prevalence",
        metric_value=2.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.92, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="~2% last year use",
    ))
    collection.add_record(_record(
        record_id="ICAD-2024-002",
        source_type=ICADSourceType.INSTITUTIONAL_REPORT,
        collection_method=DataCollectionMethod.PHONE_INTERVIEW,
        source_name="ICAD Relatório Dezembro 2024",
        source_citation_key="icad2024consumo",
        population_type="general",
        age_min=15, age_max=74, gender="all",
        region="Nacional",
        metric_name="problematic_consumption",
        metric_value=30.0, metric_unit="percentage",
        confidence_interval="25-35%",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.88, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="25-35% of users show problematic patterns",
    ))

    # ICAD 2024 — Gender breakdown: Men (15-74 years)
    collection.add_record(_record(
        record_id="ICAD-2024-003M",
        source_type=ICADSourceType.INSTITUTIONAL_REPORT,
        collection_method=DataCollectionMethod.PHONE_INTERVIEW,
        source_name="ICAD Relatório Dezembro 2024",
        source_citation_key="icad2024consumo",
        population_type="general",
        age_min=15, age_max=74, gender="male",
        region="Nacional",
        metric_name="frequent_use",
        metric_value=1.1, metric_unit="percentage",
        confidence_interval="1-1.2%",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.90, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="Men show 5-10x higher frequent use than women",
    ))
    collection.add_record(_record(
        record_id="ICAD-2024-004M",
        source_type=ICADSourceType.INSTITUTIONAL_REPORT,
        collection_method=DataCollectionMethod.PHONE_INTERVIEW,
        source_name="ICAD Relatório Dezembro 2024",
        source_citation_key="icad2024consumo",
        population_type="general",
        age_min=15, age_max=74, gender="male",
        region="Nacional",
        metric_name="problematic_consumption",
        metric_value=32.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.90, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="Among male users",
    ))

    # ICAD 2024 — Gender breakdown: Women (15-74 years)
    collection.add_record(_record(
        record_id="ICAD-2024-003F",
        source_type=ICADSourceType.INSTITUTIONAL_REPORT,
        collection_method=DataCollectionMethod.PHONE_INTERVIEW,
        source_name="ICAD Relatório Dezembro 2024",
        source_citation_key="icad2024consumo",
        population_type="general",
        age_min=15, age_max=74, gender="female",
        region="Nacional",
        metric_name="frequent_use",
        metric_value=0.15, metric_unit="percentage",
        confidence_interval="0.1-0.2%",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.90, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="Women show 5-10x lower frequent use than men",
    ))
    collection.add_record(_record(
        record_id="ICAD-2024-004F",
        source_type=ICADSourceType.INSTITUTIONAL_REPORT,
        collection_method=DataCollectionMethod.PHONE_INTERVIEW,
        source_name="ICAD Relatório Dezembro 2024",
        source_citation_key="icad2024consumo",
        population_type="general",
        age_min=15, age_max=74, gender="female",
        region="Nacional",
        metric_name="problematic_consumption",
        metric_value=19.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.90, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="Among female users",
    ))

    # ICAD 2024 — Prison population: Women
    collection.add_record(_record(
        record_id="ICAD-2024-PRISON-F",
        source_type=ICADSourceType.ACADEMIC_STUDY,
        collection_method=DataCollectionMethod.CLINICAL_ASSESSMENT,
        source_name="ICAD Populações Institucionais 2024",
        source_citation_key="carapinha2024icad",
        population_type="prison",
        age_min=18, age_max=None, gender="female",
        region="Nacional",
        metric_name="daily_use",
        metric_value=63.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.85, validated=True,
            validation_date="2026-01-20", validation_method="manual",
            issues=["Small sample size in prison population"],
        ),
        raw_notes="CRITICAL: Gender pattern inverts in prison - 63% daily use vs 46% for men",
    ))

    # ICAD 2024 — Prison population: Men
    collection.add_record(_record(
        record_id="ICAD-2024-PRISON-M",
        source_type=ICADSourceType.ACADEMIC_STUDY,
        collection_method=DataCollectionMethod.CLINICAL_ASSESSMENT,
        source_name="ICAD Populações Institucionais 2024",
        source_citation_key="carapinha2024icad",
        population_type="prison",
        age_min=18, age_max=None, gender="male",
        region="Nacional",
        metric_name="daily_use",
        metric_value=46.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.85, validated=True,
            validation_date="2026-01-20", validation_method="manual",
            issues=["Small sample size in prison population"],
        ),
        raw_notes="Men in prison: 46% daily use",
    ))

    # ICAD 2024 — Youth centers: Girls (12-18 years)
    collection.add_record(_record(
        record_id="ICAD-2024-YC-F",
        source_type=ICADSourceType.ACADEMIC_STUDY,
        collection_method=DataCollectionMethod.CLINICAL_ASSESSMENT,
        source_name="ICAD Populações Institucionais 2024",
        source_citation_key="carapinha2024icad",
        population_type="youth_center",
        age_min=12, age_max=18, gender="female",
        region="Nacional",
        metric_name="high_risk_prevalence",
        metric_value=100.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.88, validated=True,
            validation_date="2026-01-20", validation_method="manual",
            issues=["Very small sample size", "Institutionalized population - not generalizable"],
        ),
        raw_notes="CRITICAL: 100% of girls in youth centers show high-risk consumption (CAST)",
    ))
    collection.add_record(_record(
        record_id="ICAD-2024-YC-F-DAILY",
        source_type=ICADSourceType.ACADEMIC_STUDY,
        collection_method=DataCollectionMethod.CLINICAL_ASSESSMENT,
        source_name="ICAD Populações Institucionais 2024",
        source_citation_key="carapinha2024icad",
        population_type="youth_center",
        age_min=12, age_max=18, gender="female",
        region="Nacional",
        metric_name="daily_use",
        metric_value=62.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.88, validated=True,
            validation_date="2026-01-20", validation_method="manual",
            issues=["Very small sample size", "Institutionalized population - not generalizable"],
        ),
        raw_notes="Daily or near-daily use",
    ))

    # ICAD 2024 — Youth centers: Boys (12-18 years)
    collection.add_record(_record(
        record_id="ICAD-2024-YC-M",
        source_type=ICADSourceType.ACADEMIC_STUDY,
        collection_method=DataCollectionMethod.CLINICAL_ASSESSMENT,
        source_name="ICAD Populações Institucionais 2024",
        source_citation_key="carapinha2024icad",
        population_type="youth_center",
        age_min=12, age_max=18, gender="male",
        region="Nacional",
        metric_name="high_risk_prevalence",
        metric_value=49.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.88, validated=True,
            validation_date="2026-01-20", validation_method="manual",
            issues=["Very small sample size", "Institutionalized population - not generalizable"],
        ),
        raw_notes="Boys in youth centers: 49% high-risk",
    ))
    collection.add_record(_record(
        record_id="ICAD-2024-YC-M-DAILY",
        source_type=ICADSourceType.ACADEMIC_STUDY,
        collection_method=DataCollectionMethod.CLINICAL_ASSESSMENT,
        source_name="ICAD Populações Institucionais 2024",
        source_citation_key="carapinha2024icad",
        population_type="youth_center",
        age_min=12, age_max=18, gender="male",
        region="Nacional",
        metric_name="daily_use",
        metric_value=62.0, metric_unit="percentage",
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.88, validated=True,
            validation_date="2026-01-20", validation_method="manual",
            issues=["Very small sample size", "Institutionalized population - not generalizable"],
        ),
        raw_notes="Daily or near-daily use (same as girls)",
    ))

    # ICAD 2024 — Students (13-18 years)
    collection.add_record(_record(
        record_id="ICAD-2024-STU-LT",
        source_type=ICADSourceType.SURVEY,
        collection_method=DataCollectionMethod.PAPER_QUESTIONNAIRE,
        source_name="ICAD Estudo Estudantes 2024",
        source_citation_key="icad2024consumo",
        population_type="student",
        age_min=13, age_max=18, gender="all",
        region="Nacional",
        metric_name="lifetime_prevalence",
        metric_value=6.6, metric_unit="percentage",
        sample_size=11083,
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.95, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="11,083 students, 329 schools - cannabis most consumed illicit substance",
    ))
    collection.add_record(_record(
        record_id="ICAD-2024-STU-30D",
        source_type=ICADSourceType.SURVEY,
        collection_method=DataCollectionMethod.PAPER_QUESTIONNAIRE,
        source_name="ICAD Estudo Estudantes 2024",
        source_citation_key="icad2024consumo",
        population_type="student",
        age_min=13, age_max=18, gender="all",
        region="Nacional",
        metric_name="recent_use",
        metric_value=2.0, metric_unit="percentage",
        sample_size=11083,
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.95, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="Last 30 days",
    ))
    collection.add_record(_record(
        record_id="ICAD-2024-STU-DAILY",
        source_type=ICADSourceType.SURVEY,
        collection_method=DataCollectionMethod.PAPER_QUESTIONNAIRE,
        source_name="ICAD Estudo Estudantes 2024",
        source_citation_key="icad2024consumo",
        population_type="student",
        age_min=13, age_max=18, gender="all",
        region="Nacional",
        metric_name="daily_use",
        metric_value=1.0, metric_unit="percentage",
        sample_size=11083,
        data_year=2024, publication_date="2024-12-01",
        quality_flags=DataQualityFlags(
            completeness_score=0.95, validated=True,
            validation_date="2026-01-20", validation_method="automated",
        ),
        raw_notes="Under 1% daily in this age group",
    ))

    return collection


def up() -> None:
    """Apply the migration: validate and write data/raw_icad_stats_initial.json."""
    collection = _build_collection()
    errors = collection.validate_all()
    if errors:
        # Surface all per-record errors so operators can fix data, not code.
        formatted = {
            rid: errs for rid, errs in errors.items()
        }
        raise RuntimeError(f"Raw ICAD collection validation failed: {formatted}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(collection.to_json(indent=2), encoding="utf-8")


def down() -> None:
    """Rollback the migration: remove the generated JSON file."""
    if OUTPUT_PATH.exists():
        OUTPUT_PATH.unlink()


if __name__ == "__main__":
    up()
    print(f"Applied {VERSION}_{NAME} → {OUTPUT_PATH}")

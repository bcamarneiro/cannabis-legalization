#!/usr/bin/env python3
"""
Initial Migration — Populate Roles and Permissions Database.

Migrates role definitions and permission mappings from the policy document
into structured data format. Data sourced from:
- KCanG §23 (Oficial de Prevenção requirements)
- Regulatory framework for cannabis clubs
- SICAD oversight structure

Usage:
    python scripts/migrate_roles.py
    
Output:
    Writes data/roles_initial.json with validated roles and permissions.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from data.roles_schema import (
    PermissionMapping,
    Role,
    Permission,
    PermissionCategory,
    PermissionScope,
)


def create_initial_mapping() -> PermissionMapping:
    """Create initial roles and permissions from document data."""
    mapping = PermissionMapping(
        version="1.0.0",
        last_updated="2026-02-26",
        metadata={
            "description": "Initial roles and permissions migration from cannabis legalization policy document",
            "sources": [
                "KCanG §23 - Oficial de Prevenção requirements",
                "Policy document chapters on club governance",
                "SICAD regulatory framework",
            ],
            "document_branch": "main",
            "migration_script": "scripts/migrate_roles.py",
        },
    )
    
    # =========================================================================
    # Permissions - Membership Category
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="MEMBER_ADD",
        name="Add Club Member",
        description="Register new members to the club",
        category=PermissionCategory.MEMBERSHIP,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="MEMBER_REMOVE",
        name="Remove Club Member",
        description="Remove members from the club (with cause)",
        category=PermissionCategory.MEMBERSHIP,
        scope=PermissionScope.CLUB,
        requires_dual_authorization=True,
    ))
    
    mapping.add_permission(Permission(
        permission_id="MEMBER_VERIFY",
        name="Verify Member Eligibility",
        description="Verify member meets eligibility requirements (age, residency, etc.)",
        category=PermissionCategory.MEMBERSHIP,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="MEMBERSHIP_LIST",
        name="View Membership List",
        description="Access full membership roster",
        category=PermissionCategory.MEMBERSHIP,
        scope=PermissionScope.CLUB,
    ))
    
    # =========================================================================
    # Permissions - Cultivation Category
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="CULTIVATION_PLAN",
        name="Create Cultivation Plan",
        description="Plan growing cycles, strains, quantities",
        category=PermissionCategory.CULTIVATION,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="HARVEST_APPROVE",
        name="Approve Harvest",
        description="Authorize harvest operations",
        category=PermissionCategory.CULTIVATION,
        scope=PermissionScope.CLUB,
        requires_dual_authorization=True,
    ))
    
    mapping.add_permission(Permission(
        permission_id="SEED_CERTIFY",
        name="Certify Seeds",
        description="Certify seeds meet regulatory requirements",
        category=PermissionCategory.CULTIVATION,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="INVENTORY_MANAGE",
        name="Manage Inventory",
        description="Track cannabis inventory from seed to distribution",
        category=PermissionCategory.CULTIVATION,
        scope=PermissionScope.CLUB,
    ))
    
    # =========================================================================
    # Permissions - Distribution Category
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="DISTRIBUTE_PRODUCT",
        name="Distribute Product",
        description="Distribute cannabis products to members",
        category=PermissionCategory.DISTRIBUTION,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="SET_PRICE",
        name="Set Product Pricing",
        description="Set cost-recovery pricing for products",
        category=PermissionCategory.DISTRIBUTION,
        scope=PermissionScope.CLUB,
        requires_dual_authorization=True,
    ))
    
    mapping.add_permission(Permission(
        permission_id="LIMIT_ENFORCE",
        name="Enforce Purchase Limits",
        description="Enforce monthly/weekly purchase limits per member",
        category=PermissionCategory.DISTRIBUTION,
        scope=PermissionScope.CLUB,
    ))
    
    # =========================================================================
    # Permissions - Financial Category
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="FINANCE_VIEW",
        name="View Financial Records",
        description="Access club financial statements and records",
        category=PermissionCategory.FINANCIAL,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="FINANCE_APPROVE",
        name="Approve Expenses",
        description="Approve club expenses and payments",
        category=PermissionCategory.FINANCIAL,
        scope=PermissionScope.CLUB,
        requires_dual_authorization=True,
    ))
    
    mapping.add_permission(Permission(
        permission_id="MEMBERSHIP_FEE",
        name="Set Membership Fees",
        description="Set monthly/annual membership fees",
        category=PermissionCategory.FINANCIAL,
        scope=PermissionScope.CLUB,
    ))
    
    # =========================================================================
    # Permissions - Compliance Category
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="COMPLIANCE_CHECK",
        name="Run Compliance Check",
        description="Verify club operations comply with regulations",
        category=PermissionCategory.COMPLIANCE,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="THC_TEST",
        name="Request THC Testing",
        description="Request laboratory THC potency testing",
        category=PermissionCategory.COMPLIANCE,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="AGE_VERIFY",
        name="Verify Age Compliance",
        description="Verify members meet minimum age requirements",
        category=PermissionCategory.COMPLIANCE,
        scope=PermissionScope.CLUB,
    ))
    
    # =========================================================================
    # Permissions - Reporting Category
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="REPORT_SICAD",
        name="Submit SICAD Report",
        description="Submit quarterly reports to SICAD",
        category=PermissionCategory.REPORTING,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="REPORT_CONSUMPTION",
        name="Report Consumption Data",
        description="Report member consumption patterns to national database",
        category=PermissionCategory.REPORTING,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="REPORT_INCIDENT",
        name="File Incident Report",
        description="File incident reports (adverse events, violations)",
        category=PermissionCategory.REPORTING,
        scope=PermissionScope.CLUB,
    ))
    
    # =========================================================================
    # Permissions - Administration Category
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="ADMIN_CLUB_CONFIG",
        name="Configure Club Settings",
        description="Configure club operational parameters",
        category=PermissionCategory.ADMINISTRATION,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="ADMIN_SCHEDULE",
        name="Manage Schedules",
        description="Manage staff and facility schedules",
        category=PermissionCategory.ADMINISTRATION,
        scope=PermissionScope.CLUB,
    ))
    
    mapping.add_permission(Permission(
        permission_id="ADMIN_ACCESS",
        name="Manage Access Control",
        description="Manage physical and system access permissions",
        category=PermissionCategory.ADMINISTRATION,
        scope=PermissionScope.CLUB,
    ))
    
    # =========================================================================
    # Permissions - Audit Category (Regional/National scope)
    # =========================================================================
    mapping.add_permission(Permission(
        permission_id="AUDIT_CLUB",
        name="Audit Club Operations",
        description="Conduct compliance audits of club operations",
        category=PermissionCategory.AUDIT,
        scope=PermissionScope.REGIONAL,
    ))
    
    mapping.add_permission(Permission(
        permission_id="AUDIT_FINANCIAL",
        name="Audit Financial Records",
        description="Audit club financial records and transactions",
        category=PermissionCategory.AUDIT,
        scope=PermissionScope.REGIONAL,
    ))
    
    mapping.add_permission(Permission(
        permission_id="AUDIT_SUSPEND",
        name="Suspend Club License",
        description="Suspend club license pending investigation",
        category=PermissionCategory.AUDIT,
        scope=PermissionScope.NATIONAL,
        requires_dual_authorization=True,
    ))
    
    # =========================================================================
    # Role: Assembleia de Membros (Member Assembly) - Supreme authority
    # =========================================================================
    assembleia = Role(
        role_id="ASSEMBLEIA",
        name="Assembleia de Membros",
        description="General assembly of all club members - supreme decision-making body",
        scope=PermissionScope.CLUB,
        required_qualifications=["Active club member in good standing"],
    )
    assembleia.add_permission("MEMBERSHIP_LIST")
    assembleia.add_permission("FINANCE_VIEW")
    assembleia.add_permission("MEMBERSHIP_FEE")
    mapping.add_role(assembleia)
    
    # =========================================================================
    # Role: Direção do Clube (Club Board/Admin)
    # =========================================================================
    direcao = Role(
        role_id="DIRECAO",
        name="Direção do Clube",
        description="Club board responsible for overall management and operations",
        scope=PermissionScope.CLUB,
        max_holders_per_club=3,  # Typically 3 board members
        required_qualifications=["Club member", "Good standing", "No criminal record"],
    )
    direcao.add_permission("MEMBER_ADD")
    direcao.add_permission("MEMBER_REMOVE")
    direcao.add_permission("MEMBER_VERIFY")
    direcao.add_permission("MEMBERSHIP_LIST")
    direcao.add_permission("CULTIVATION_PLAN")
    direcao.add_permission("HARVEST_APPROVE")
    direcao.add_permission("SEED_CERTIFY")
    direcao.add_permission("INVENTORY_MANAGE")
    direcao.add_permission("DISTRIBUTE_PRODUCT")
    direcao.add_permission("SET_PRICE")
    direcao.add_permission("LIMIT_ENFORCE")
    direcao.add_permission("FINANCE_VIEW")
    direcao.add_permission("FINANCE_APPROVE")
    direcao.add_permission("MEMBERSHIP_FEE")
    direcao.add_permission("COMPLIANCE_CHECK")
    direcao.add_permission("THC_TEST")
    direcao.add_permission("AGE_VERIFY")
    direcao.add_permission("REPORT_SICAD")
    direcao.add_permission("REPORT_CONSUMPTION")
    direcao.add_permission("ADMIN_CLUB_CONFIG")
    direcao.add_permission("ADMIN_SCHEDULE")
    direcao.add_permission("ADMIN_ACCESS")
    mapping.add_role(direcao)
    
    # =========================================================================
    # Role: Oficial de Prevenção (Prevention Officer) - KCanG §23
    # =========================================================================
    oficial_prevencao = Role(
        role_id="OFICIAL_PREVENCAO",
        name="Oficial de Prevenção",
        description="Prevention officer responsible for member education, monitoring, and SNS referrals",
        scope=PermissionScope.CLUB,
        max_holders_per_club=2,  # KCanG §23: 2 officers per club for shift coverage
        required_qualifications=[
            "Licenciatura (Bachelor's degree)",
            "40h specialization in addiction studies",
            "1 year experience in addiction/clinical work",
        ],
        salary_range_min=35000,  # Adjusted from €28-35k to €35-45k per ECON 3 analysis
        salary_range_max=45000,
        reports_to="DIRECAO",
    )
    oficial_prevencao.add_permission("MEMBER_VERIFY")
    oficial_prevencao.add_permission("MEMBERSHIP_LIST")
    oficial_prevencao.add_permission("COMPLIANCE_CHECK")
    oficial_prevencao.add_permission("AGE_VERIFY")
    oficial_prevencao.add_permission("REPORT_CONSUMPTION")
    oficial_prevencao.add_permission("REPORT_INCIDENT")
    mapping.add_role(oficial_prevencao)
    
    # =========================================================================
    # Role: Tesoureiro (Treasurer)
    # =========================================================================
    tesoureiro = Role(
        role_id="TESOUREIRO",
        name="Tesoureiro",
        description="Treasurer responsible for financial management",
        scope=PermissionScope.CLUB,
        max_holders_per_club=1,
        required_qualifications=["Club member", "Financial literacy"],
        reports_to="DIRECAO",
    )
    tesoureiro.add_permission("FINANCE_VIEW")
    tesoureiro.add_permission("FINANCE_APPROVE")
    tesoureiro.add_permission("MEMBERSHIP_FEE")
    mapping.add_role(tesoureiro)
    
    # =========================================================================
    # Role: Responsável de Cultura (Cultivation Manager)
    # =========================================================================
    cultura = Role(
        role_id="CULTURA_RESPONSAVEL",
        name="Responsável de Cultura",
        description="Cultivation manager responsible for growing operations",
        scope=PermissionScope.CLUB,
        max_holders_per_club=2,
        required_qualifications=[
            "Agricultural training or experience",
            "Knowledge of cannabis cultivation",
        ],
        reports_to="DIRECAO",
    )
    cultura.add_permission("CULTIVATION_PLAN")
    cultura.add_permission("HARVEST_APPROVE")
    cultura.add_permission("SEED_CERTIFY")
    cultura.add_permission("INVENTORY_MANAGE")
    cultura.add_permission("THC_TEST")
    mapping.add_role(cultura)
    
    # =========================================================================
    # Role: SICAD Auditor (Regional)
    # =========================================================================
    sicad_regional = Role(
        role_id="SICAD_AUDITOR_REGIONAL",
        name="SICAD Auditor (Regional)",
        description="SICAD regional auditor with oversight over multiple clubs",
        scope=PermissionScope.REGIONAL,
        required_qualifications=[
            "Government auditor certification",
            "Knowledge of cannabis regulations",
        ],
    )
    sicad_regional.add_permission("AUDIT_CLUB")
    sicad_regional.add_permission("AUDIT_FINANCIAL")
    sicad_regional.add_permission("MEMBERSHIP_LIST")
    sicad_regional.add_permission("FINANCE_VIEW")
    sicad_regional.add_permission("COMPLIANCE_CHECK")
    sicad_regional.add_permission("REPORT_INCIDENT")
    mapping.add_role(sicad_regional)
    
    # =========================================================================
    # Role: SICAD Director (National)
    # =========================================================================
    sicad_nacional = Role(
        role_id="SICAD_DIRETOR",
        name="SICAD Director (National)",
        description="SICAD national director with authority to suspend licenses",
        scope=PermissionScope.NATIONAL,
        required_qualifications=[
            "Senior government official",
            "Legal/regulatory expertise",
        ],
    )
    sicad_nacional.add_permission("AUDIT_CLUB")
    sicad_nacional.add_permission("AUDIT_FINANCIAL")
    sicad_nacional.add_permission("AUDIT_SUSPEND")
    sicad_nacional.add_permission("MEMBERSHIP_LIST")
    sicad_nacional.add_permission("FINANCE_VIEW")
    sicad_nacional.add_permission("REPORT_INCIDENT")
    mapping.add_role(sicad_nacional)
    
    return mapping


def run_migration():
    """Run migration and write output."""
    print("Running roles and permissions initial migration...")
    
    mapping = create_initial_mapping()
    
    # Validate
    errors = mapping.validate()
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    
    # Write output
    output_path = Path(__file__).parent.parent / "data" / "roles_initial.json"
    output_path.write_text(mapping.to_json(indent=2))
    
    print(f"✅ Migration complete: {len(mapping.roles)} roles, {len(mapping.permissions)} permissions")
    print(f"   Output: {output_path}")


if __name__ == "__main__":
    run_migration()

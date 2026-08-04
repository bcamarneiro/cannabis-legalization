#!/usr/bin/env python3
"""
Roles and Permissions Database Schema.

Defines the schema for storing role definitions and permission mappings
for the cannabis club regulatory framework.

Usage:
    from roles_schema import Role, Permission, PermissionMapping
    
    # Validate role data
    role = Role.from_dict(data)
    role.validate()
"""

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional, Dict, Any, Set
from enum import Enum
import json


class PermissionScope(str, Enum):
    """Scope levels for permissions."""
    CLUB = "club"  # Single club scope
    REGIONAL = "regional"  # Multiple clubs in a region
    NATIONAL = "national"  # SICAD/national authority scope
    SYSTEM = "system"  # System-wide administrative permissions


class PermissionCategory(str, Enum):
    """Categories of permissions for grouping."""
    MEMBERSHIP = "membership"  # Member management
    CULTIVATION = "cultivation"  # Growing/harvest operations
    DISTRIBUTION = "distribution"  # Product distribution
    FINANCIAL = "financial"  # Financial operations
    COMPLIANCE = "compliance"  # Regulatory compliance
    REPORTING = "reporting"  # Data reporting to SICAD
    ADMINISTRATION = "administration"  # General admin
    AUDIT = "audit"  # Audit and oversight


@dataclass
class Permission:
    """Single permission definition."""
    permission_id: str  # Unique identifier (e.g., "MEMBER_ADD", "HARVEST_APPROVE")
    name: str  # Human-readable name
    description: str  # What this permission allows
    category: PermissionCategory
    scope: PermissionScope = PermissionScope.CLUB
    requires_dual_authorization: bool = False  # Requires 2+ roles for sensitive ops
    audit_logged: bool = True  # Whether actions are logged
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "permission_id": self.permission_id,
            "name": self.name,
            "description": self.description,
            "category": self.category.value,
            "scope": self.scope.value,
            "requires_dual_authorization": self.requires_dual_authorization,
            "audit_logged": self.audit_logged,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Permission":
        return cls(
            permission_id=data["permission_id"],
            name=data["name"],
            description=data["description"],
            category=PermissionCategory(data["category"]),
            scope=PermissionScope(data.get("scope", "club")),
            requires_dual_authorization=data.get("requires_dual_authorization", False),
            audit_logged=data.get("audit_logged", True),
        )


@dataclass
class Role:
    """Role definition with associated permissions."""
    role_id: str  # Unique identifier (e.g., "CLUB_ADMIN", "OFICIAL_PREVENCAO")
    name: str  # Human-readable name
    description: str  # Role purpose
    permissions: List[str] = field(default_factory=list)  # List of permission_ids
    scope: PermissionScope = PermissionScope.CLUB
    max_holders_per_club: Optional[int] = None  # e.g., 2 for Oficial Prevenção (shifts)
    required_qualifications: List[str] = field(default_factory=list)
    reports_to: Optional[str] = None  # role_id of supervising role
    salary_range_min: Optional[int] = None  # Annual salary in EUR
    salary_range_max: Optional[int] = None
    
    def add_permission(self, permission_id: str) -> None:
        if permission_id not in self.permissions:
            self.permissions.append(permission_id)
    
    def has_permission(self, permission_id: str) -> bool:
        return permission_id in self.permissions
    
    def validate(self) -> List[str]:
        """Validate role and return list of errors."""
        errors = []
        if not self.permissions:
            errors.append(f"Role {self.role_id}: no permissions assigned")
        if self.salary_range_min and self.salary_range_max:
            if self.salary_range_min > self.salary_range_max:
                errors.append(f"Role {self.role_id}: salary min > max")
        return errors
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "role_id": self.role_id,
            "name": self.name,
            "description": self.description,
            "permissions": self.permissions,
            "scope": self.scope.value,
            "max_holders_per_club": self.max_holders_per_club,
            "required_qualifications": self.required_qualifications,
            "reports_to": self.reports_to,
            "salary_range_min": self.salary_range_min,
            "salary_range_max": self.salary_range_max,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Role":
        return cls(
            role_id=data["role_id"],
            name=data["name"],
            description=data["description"],
            permissions=data.get("permissions", []),
            scope=PermissionScope(data.get("scope", "club")),
            max_holders_per_club=data.get("max_holders_per_club"),
            required_qualifications=data.get("required_qualifications", []),
            reports_to=data.get("reports_to"),
            salary_range_min=data.get("salary_range_min"),
            salary_range_max=data.get("salary_range_max"),
        )


@dataclass
class PermissionMapping:
    """Mapping of roles to permissions with metadata."""
    version: str = "1.0.0"
    last_updated: str = field(default_factory=lambda: date.today().isoformat())
    roles: List[Role] = field(default_factory=list)
    permissions: List[Permission] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_role(self, role: Role) -> None:
        self.roles.append(role)
    
    def add_permission(self, permission: Permission) -> None:
        self.permissions.append(permission)
    
    def get_role(self, role_id: str) -> Optional[Role]:
        for role in self.roles:
            if role.role_id == role_id:
                return role
        return None
    
    def get_permission(self, permission_id: str) -> Optional[Permission]:
        for perm in self.permissions:
            if perm.permission_id == permission_id:
                return perm
        return None
    
    def validate(self) -> List[str]:
        """Validate all roles and permissions, return errors."""
        errors = []
        
        # Check for duplicate role_ids
        role_ids = [r.role_id for r in self.roles]
        duplicates = set([x for x in role_ids if role_ids.count(x) > 1])
        if duplicates:
            errors.append(f"Duplicate role_ids: {duplicates}")
        
        # Check for duplicate permission_ids
        perm_ids = [p.permission_id for p in self.permissions]
        duplicates = set([x for x in perm_ids if perm_ids.count(x) > 1])
        if duplicates:
            errors.append(f"Duplicate permission_ids: {duplicates}")
        
        # Validate each role
        for role in self.roles:
            errors.extend(role.validate())
            
            # Check all permissions exist
            perm_ids = {p.permission_id for p in self.permissions}
            for perm_id in role.permissions:
                if perm_id not in perm_ids:
                    errors.append(f"Role {role.role_id}: references unknown permission {perm_id}")
        
        return errors
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version,
            "last_updated": self.last_updated,
            "metadata": self.metadata,
            "roles": [r.to_dict() for r in self.roles],
            "permissions": [p.to_dict() for p in self.permissions],
        }
    
    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PermissionMapping":
        """Deserialize from dictionary."""
        mapping = cls(
            version=data.get("version", "1.0.0"),
            last_updated=data.get("last_updated", date.today().isoformat()),
            metadata=data.get("metadata", {}),
        )
        for p_data in data.get("permissions", []):
            mapping.add_permission(Permission.from_dict(p_data))
        for r_data in data.get("roles", []):
            mapping.add_role(Role.from_dict(r_data))
        return mapping
    
    @classmethod
    def from_json(cls, json_str: str) -> "PermissionMapping":
        """Deserialize from JSON string."""
        return cls.from_dict(json.loads(json_str))

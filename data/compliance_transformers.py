#!/usr/bin/env python3
"""
Regulatory Compliance Transformers for Cannabis Legalization.

Enforces age limits and geographic restrictions specific to cannabis legalization
policy. Used to validate and transform consumer/club data against regulatory requirements.

Usage:
    from compliance_transformers import AgeComplianceTransformer, GeographicComplianceTransformer
    
    # Age validation
    age_transformer = AgeComplianceTransformer(min_age=21)
    result = age_transformer.validate_consumer(consumer_data)
    
    # Geographic validation
    geo_transformer = GeographicComplianceTransformer(allowed_regions=["PT-11", "PT-14"])
    result = geo_transformer.validate_location(location_data)
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List, Optional, Dict, Any, Set
from enum import Enum
import json


class ComplianceStatus(str, Enum):
    """Compliance check result status."""
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    UNKNOWN = "unknown"
    EXEMPT = "exempt"


class RestrictionType(str, Enum):
    """Type of geographic restriction."""
    ALLOW_LIST = "allow_list"
    DENY_LIST = "deny_list"
    DISTANCE_BASED = "distance_based"
    ZONING = "zoning"


@dataclass
class ComplianceViolation:
    """Single compliance violation with details."""
    rule_name: str
    violation_type: str
    severity: str  # "critical", "high", "medium", "low"
    description: str
    actual_value: Any
    required_value: Any
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "rule_name": self.rule_name,
            "violation_type": self.violation_type,
            "severity": self.severity,
            "description": self.description,
            "actual_value": self.actual_value,
            "required_value": self.required_value,
            "timestamp": self.timestamp,
        }


@dataclass
class ComplianceResult:
    """Result of a compliance check."""
    status: ComplianceStatus
    violations: List[ComplianceViolation] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def is_compliant(self) -> bool:
        return self.status == ComplianceStatus.COMPLIANT
    
    def add_violation(self, violation: ComplianceViolation) -> None:
        self.violations.append(violation)
        if self.status == ComplianceStatus.COMPLIANT:
            self.status = ComplianceStatus.NON_COMPLIANT
    
    def add_warning(self, warning: str) -> None:
        self.warnings.append(warning)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status.value,
            "violations": [v.to_dict() for v in self.violations],
            "warnings": self.warnings,
            "metadata": self.metadata,
        }


@dataclass
class AgeComplianceTransformer:
    """
    Enforces minimum age requirements for cannabis access.
    
    Per policy: minimum age is 21 (not 18) based on international best practices
    for minimizing youth access and neurological development concerns.
    """
    min_age: int = 21
    max_age: Optional[int] = None
    require_proof: bool = True
    accepted_id_types: List[str] = field(default_factory=lambda: [
        "citizen_card", "passport", "drivers_license", "residence_permit"
    ])
    
    def validate_age(self, age: int, birth_date: Optional[str] = None) -> ComplianceResult:
        """
        Validate age against minimum (and optional maximum) age requirements.
        
        Args:
            age: Current age in years
            birth_date: Optional ISO format birth date for verification
            
        Returns:
            ComplianceResult with status and any violations
        """
        result = ComplianceResult(
            status=ComplianceStatus.COMPLIANT,
            metadata={"min_age": self.min_age, "max_age": self.max_age}
        )
        
        # Check minimum age
        if age < self.min_age:
            result.add_violation(ComplianceViolation(
                rule_name="minimum_age_requirement",
                violation_type="age_below_minimum",
                severity="critical",
                description=f"Age {age} is below minimum required age of {self.min_age}",
                actual_value=age,
                required_value=self.min_age,
            ))
        
        # Check maximum age (if configured)
        if self.max_age is not None and age > self.max_age:
            result.add_violation(ComplianceViolation(
                rule_name="maximum_age_requirement",
                violation_type="age_above_maximum",
                severity="high",
                description=f"Age {age} exceeds maximum allowed age of {self.max_age}",
                actual_value=age,
                required_value=self.max_age,
            ))
        
        # Verify birth date consistency if provided
        if birth_date:
            try:
                birth = datetime.fromisoformat(birth_date).date()
                calculated_age = (date.today() - birth).days // 365
                if abs(calculated_age - age) > 1:
                    result.add_warning(
                        f"Age mismatch: provided {age}, calculated from birth_date {calculated_age}"
                    )
            except ValueError:
                result.add_warning(f"Invalid birth_date format: {birth_date}")
        
        result.metadata["validated_age"] = age
        result.metadata["validated_at"] = datetime.now().isoformat()
        
        return result
    
    def validate_consumer(self, consumer_data: Dict[str, Any]) -> ComplianceResult:
        """
        Validate consumer data for age compliance.
        
        Args:
            consumer_data: Dict containing 'age' and optionally 'birth_date', 'id_type'
            
        Returns:
            ComplianceResult with full validation details
        """
        result = ComplianceResult(
            status=ComplianceStatus.COMPLIANT,
            metadata={"transformer": "AgeComplianceTransformer"}
        )
        
        # Extract age
        age = consumer_data.get("age")
        birth_date = consumer_data.get("birth_date")
        
        if age is None and birth_date is None:
            result.status = ComplianceStatus.UNKNOWN
            result.add_warning("Cannot validate: missing both age and birth_date")
            return result
        
        # Calculate age from birth_date if age not provided
        if age is None and birth_date:
            try:
                birth = datetime.fromisoformat(birth_date).date()
                age = (date.today() - birth).days // 365
                result.metadata["calculated_age"] = age
            except ValueError:
                result.status = ComplianceStatus.UNKNOWN
                result.add_warning(f"Invalid birth_date format: {birth_date}")
                return result
        
        # Age should now be defined; if still None, cannot validate
        if age is None:
            result.status = ComplianceStatus.UNKNOWN
            result.add_warning("Cannot validate: age is None")
            return result
        
        # Validate ID type if proof required
        if self.require_proof:
            id_type = consumer_data.get("id_type")
            if id_type is None:
                result.add_warning("ID verification required but no id_type provided")
            elif id_type not in self.accepted_id_types:
                result.add_violation(ComplianceViolation(
                    rule_name="id_verification_requirement",
                    violation_type="unaccepted_id_type",
                    severity="high",
                    description=f"ID type '{id_type}' not in accepted types",
                    actual_value=id_type,
                    required_value=self.accepted_id_types,
                ))
        
        # Run age validation
        age_result = self.validate_age(age, birth_date)
        for violation in age_result.violations:
            result.add_violation(violation)
        result.warnings.extend(age_result.warnings)
        
        return result
    
    def transform(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform consumer data by adding compliance metadata.
        
        Args:
            data: Consumer data dict
            
        Returns:
            Original data with compliance metadata added
        """
        result = self.validate_consumer(data)
        transformed = data.copy()
        transformed["compliance"] = {
            "age_check": result.to_dict(),
            "checked_at": datetime.now().isoformat(),
            "transformer_version": "1.0.0",
        }
        return transformed


@dataclass
class GeographicRestriction:
    """Geographic restriction rule."""
    restriction_type: RestrictionType
    regions: Set[str] = field(default_factory=set)  # ISO 3166-2 codes (e.g., "PT-11")
    distance_km: Optional[float] = None  # For distance-based restrictions
    reference_point: Optional[Dict[str, float]] = None  # {"lat": ..., "lon": ...}
    zoning_rules: Optional[Dict[str, Any]] = field(default=None)  # Custom zoning config
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "restriction_type": self.restriction_type.value,
            "regions": list(self.regions),
            "distance_km": self.distance_km,
            "reference_point": self.reference_point,
            "zoning_rules": self.zoning_rules,
        }


@dataclass
class GeographicComplianceTransformer:
    """
    Enforces geographic restrictions for cannabis access and club locations.
    
    Per policy: clubs restricted to specific zones, distance requirements from
    schools/youth centers, and regional authorization requirements.
    """
    restrictions: List[GeographicRestriction] = field(default_factory=list)
    allowed_regions: Set[str] = field(default_factory=set)
    denied_regions: Set[str] = field(default_factory=set)
    
    def add_restriction(self, restriction: GeographicRestriction) -> None:
        """Add a geographic restriction rule."""
        self.restrictions.append(restriction)
    
    def validate_region(self, region_code: str) -> ComplianceResult:
        """
        Validate a region code against allow/deny lists.
        
        Args:
            region_code: ISO 3166-2 region code (e.g., "PT-11" for Lisboa)
            
        Returns:
            ComplianceResult with validation status
        """
        result = ComplianceResult(
            status=ComplianceStatus.COMPLIANT,
            metadata={"region_code": region_code}
        )
        
        # Check deny list first (takes precedence)
        if region_code in self.denied_regions:
            result.add_violation(ComplianceViolation(
                rule_name="regional_denial",
                violation_type="region_not_allowed",
                severity="critical",
                description=f"Region {region_code} is explicitly denied",
                actual_value=region_code,
                required_value=f"not in {self.denied_regions}",
            ))
            return result
        
        # Check allow list (if configured)
        if self.allowed_regions and region_code not in self.allowed_regions:
            result.add_violation(ComplianceViolation(
                rule_name="regional_allow_list",
                violation_type="region_not_allowed",
                severity="critical",
                description=f"Region {region_code} not in allowed regions",
                actual_value=region_code,
                required_value=list(self.allowed_regions),
            ))
        
        return result
    
    def validate_location(
        self,
        latitude: float,
        longitude: float,
        region_code: Optional[str] = None
    ) -> ComplianceResult:
        """
        Validate a geographic location against all restrictions.
        
        Args:
            latitude: Location latitude
            longitude: Location longitude
            region_code: Optional ISO region code for additional validation
            
        Returns:
            ComplianceResult with all applicable violations
        """
        result = ComplianceResult(
            status=ComplianceStatus.COMPLIANT,
            metadata={"latitude": latitude, "longitude": longitude}
        )
        
        # Validate region if provided
        if region_code:
            region_result = self.validate_region(region_code)
            if not region_result.is_compliant():
                result.status = ComplianceStatus.NON_COMPLIANT
                result.violations.extend(region_result.violations)
        
        # Check each restriction
        for restriction in self.restrictions:
            if restriction.restriction_type == RestrictionType.DISTANCE_BASED:
                if restriction.reference_point and restriction.distance_km:
                    # Haversine distance calculation
                    from math import radians, sin, cos, sqrt, atan2
                    
                    lat1, lon1 = radians(latitude), radians(longitude)
                    lat2, lon2 = (
                        radians(restriction.reference_point["lat"]),
                        radians(restriction.reference_point["lon"])
                    )
                    
                    dlat = lat2 - lat1
                    dlon = lon2 - lon1
                    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                    c = 2 * atan2(sqrt(a), sqrt(1-a))
                    distance_km = 6371 * c  # Earth radius
                    
                    if distance_km < restriction.distance_km:
                        result.add_violation(ComplianceViolation(
                            rule_name="distance_restriction",
                            violation_type="too_close_to_protected_zone",
                            severity="high",
                            description=f"Location is {distance_km:.2f}km from protected point "
                                       f"(minimum: {restriction.distance_km}km)",
                            actual_value=round(distance_km, 2),
                            required_value=restriction.distance_km,
                        ))
        
        result.metadata["validated_at"] = datetime.now().isoformat()
        return result
    
    def validate_club_location(
        self,
        location_data: Dict[str, Any]
    ) -> ComplianceResult:
        """
        Validate a cannabis social club location against all geographic rules.
        
        Args:
            location_data: Dict with latitude, longitude, region_code, address
            
        Returns:
            ComplianceResult with full validation details
        """
        result = ComplianceResult(
            status=ComplianceStatus.COMPLIANT,
            metadata={"transformer": "GeographicComplianceTransformer"}
        )
        
        lat = location_data.get("latitude")
        lon = location_data.get("longitude")
        region = location_data.get("region_code")
        
        if lat is None or lon is None:
            result.status = ComplianceStatus.UNKNOWN
            result.add_warning("Cannot validate: missing latitude or longitude")
            return result
        
        # Run location validation
        location_result = self.validate_location(lat, lon, region)
        if not location_result.is_compliant():
            result.status = ComplianceStatus.NON_COMPLIANT
            result.violations.extend(location_result.violations)
        result.warnings.extend(location_result.warnings)
        
        return result
    
    def transform(self, location_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform location data by adding compliance metadata.
        
        Args:
            location_data: Location data dict
            
        Returns:
            Original data with compliance metadata added
        """
        result = self.validate_club_location(location_data)
        transformed = location_data.copy()
        transformed["compliance"] = {
            "geographic_check": result.to_dict(),
            "checked_at": datetime.now().isoformat(),
            "transformer_version": "1.0.0",
        }
        return transformed


@dataclass
class RegulatoryCompliancePipeline:
    """
    Combined compliance pipeline for full regulatory validation.
    
    Chains age and geographic compliance checks for comprehensive validation
    of consumers, club members, and club locations.
    """
    age_transformer: Optional[AgeComplianceTransformer] = None
    geo_transformer: Optional[GeographicComplianceTransformer] = None
    
    def validate_consumer_full(
        self,
        consumer_data: Dict[str, Any]
    ) -> ComplianceResult:
        """
        Run full consumer compliance validation (age + geography if provided).
        
        Args:
            consumer_data: Consumer data with age, birth_date, and optionally location
            
        Returns:
            Combined ComplianceResult
        """
        result = ComplianceResult(
            status=ComplianceStatus.COMPLIANT,
            metadata={"pipeline": "RegulatoryCompliancePipeline"}
        )
        
        # Age check
        if self.age_transformer:
            age_result = self.age_transformer.validate_consumer(consumer_data)
            if not age_result.is_compliant():
                result.status = ComplianceStatus.NON_COMPLIANT
                result.violations.extend(age_result.violations)
            result.warnings.extend(age_result.warnings)
        
        # Geographic check (if location data provided)
        if self.geo_transformer:
            lat = consumer_data.get("latitude")
            lon = consumer_data.get("longitude")
            region = consumer_data.get("region_code")
            
            if lat is not None and lon is not None:
                geo_result = self.geo_transformer.validate_location(lat, lon, region)
                if not geo_result.is_compliant():
                    result.status = ComplianceStatus.NON_COMPLIANT
                    result.violations.extend(geo_result.violations)
                result.warnings.extend(geo_result.warnings)
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize pipeline configuration."""
        return {
            "age_transformer": {
                "min_age": self.age_transformer.min_age,
                "max_age": self.age_transformer.max_age,
                "require_proof": self.age_transformer.require_proof,
                "accepted_id_types": self.age_transformer.accepted_id_types,
            } if self.age_transformer else None,
            "geo_transformer": {
                "allowed_regions": list(self.geo_transformer.allowed_regions),
                "denied_regions": list(self.geo_transformer.denied_regions),
                "restrictions": [r.to_dict() for r in self.geo_transformer.restrictions],
            } if self.geo_transformer else None,
        }


def create_default_pipeline() -> RegulatoryCompliancePipeline:
    """
    Create a default compliance pipeline with policy-mandated restrictions.
    
    Returns:
        RegulatoryCompliancePipeline with age=21 and standard geographic rules
    """
    age_transformer = AgeComplianceTransformer(
        min_age=21,
        require_proof=True,
    )
    
    geo_transformer = GeographicComplianceTransformer(
        allowed_regions=set(),  # Empty = all regions allowed by default
        denied_regions=set(),   # Configure per policy requirements
    )
    
    # Add standard distance restriction (e.g., 500m from schools)
    # geo_transformer.add_restriction(GeographicRestriction(
    #     restriction_type=RestrictionType.DISTANCE_BASED,
    #     distance_km=0.5,
    #     reference_point={"lat": 38.7223, "lon": -9.1393},  # Example: school location
    # ))
    
    return RegulatoryCompliancePipeline(
        age_transformer=age_transformer,
        geo_transformer=geo_transformer,
    )


if __name__ == "__main__":
    # Demo/test usage
    print("Regulatory Compliance Transformers - Demo")
    print("=" * 60)
    
    # Test age compliance
    age_transformer = AgeComplianceTransformer(min_age=21)
    
    test_consumer_young = {"age": 18, "id_type": "citizen_card"}
    result_young = age_transformer.validate_consumer(test_consumer_young)
    print(f"\nConsumer (age 18): {result_young.status.value}")
    if result_young.violations:
        for v in result_young.violations:
            print(f"  ✗ {v.description}")
    
    test_consumer_ok = {"age": 25, "id_type": "citizen_card"}
    result_ok = age_transformer.validate_consumer(test_consumer_ok)
    print(f"\nConsumer (age 25): {result_ok.status.value}")
    
    # Test geographic compliance
    geo_transformer = GeographicComplianceTransformer(
        allowed_regions={"PT-11", "PT-14", "PT-13"}  # Lisboa, Porto, Algarve
    )
    
    test_location_ok = {"latitude": 38.7223, "longitude": -9.1393, "region_code": "PT-11"}
    result_geo_ok = geo_transformer.validate_club_location(test_location_ok)
    print(f"\nLocation (Lisboa): {result_geo_ok.status.value}")
    
    test_location_denied = {"latitude": 38.7223, "longitude": -9.1393, "region_code": "PT-06"}
    result_geo_denied = geo_transformer.validate_club_location(test_location_denied)
    print(f"\nLocation (Évora - not in allow list): {result_geo_denied.status.value}")
    if result_geo_denied.violations:
        for v in result_geo_denied.violations:
            print(f"  ✗ {v.description}")
    
    print("\n" + "=" * 60)
    print("Demo complete!")

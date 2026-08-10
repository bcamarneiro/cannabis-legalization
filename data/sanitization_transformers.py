#!/usr/bin/env python3
"""
Sanitization Transformers for Cannabis Legalization.

Provides transformers for trimming, casing, and basic type coercion for text/numbers
across payloads. Used to clean and normalize input data before validation and processing.

Usage:
    from sanitization_transformers import TextSanitizer, NumberSanitizer, PayloadSanitizer
    
    # Text sanitization
    text_sanitizer = TextSanitizer(trim=True, lowercase=False)
    cleaned = text_sanitizer.sanitize("  Hello World  ")
    
    # Number sanitization
    num_sanitizer = NumberSanitizer(coerce=True, default=0)
    value = num_sanitizer.sanitize("42")
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any, Union
from enum import Enum
import re


class SanitizationStatus(str, Enum):
    """Result of sanitization operation."""
    CLEAN = "clean"
    SANITIZED = "sanitized"
    INVALID = "invalid"
    UNKNOWN = "unknown"


class CasingStyle(str, Enum):
    """Text casing transformation styles."""
    LOWER = "lower"
    UPPER = "upper"
    TITLE = "title"
    SENTENCE = "sentence"
    NONE = "none"


@dataclass
class SanitizationResult:
    """Result of a sanitization operation with metadata."""
    status: SanitizationStatus
    original_value: Any
    sanitized_value: Any
    transformations_applied: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def is_valid(self) -> bool:
        return self.status != SanitizationStatus.INVALID
    
    def was_sanitized(self) -> bool:
        return self.status == SanitizationStatus.SANITIZED
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status.value,
            "original_value": self.original_value,
            "sanitized_value": self.sanitized_value,
            "transformations_applied": self.transformations_applied,
            "warnings": self.warnings,
            "errors": self.errors,
            "metadata": self.metadata,
        }


@dataclass
class TextSanitizer:
    """
    Sanitizes text values with trimming, casing, and normalization.
    
    Supports:
    - Whitespace trimming (leading/trailing)
    - Internal whitespace normalization
    - Casing transformations (lower, upper, title, sentence)
    - Removal of special characters
    - Empty string handling
    """
    trim: bool = True
    normalize_whitespace: bool = True
    casing: CasingStyle = CasingStyle.NONE
    remove_special_chars: bool = False
    allow_empty: bool = False
    strip_chars: Optional[str] = None
    
    def sanitize(self, value: Any) -> SanitizationResult:
        """
        Sanitize a text value.
        
        Args:
            value: Input value (will be converted to string)
            
        Returns:
            SanitizationResult with cleaned value and metadata
        """
        transformations = []
        warnings = []
        errors = []
        
        # Handle None
        if value is None:
            if self.allow_empty:
                return SanitizationResult(
                    status=SanitizationStatus.CLEAN,
                    original_value=None,
                    sanitized_value="",
                    transformations_applied=["none_to_empty"],
                    metadata={"handled_none": True},
                )
            else:
                return SanitizationResult(
                    status=SanitizationStatus.INVALID,
                    original_value=None,
                    sanitized_value=None,
                    errors=["Null value not allowed"],
                    metadata={"handled_none": True},
                )
        
        # Convert to string
        original = str(value)
        result = original
        
        # Handle empty string
        if result == "":
            if self.allow_empty:
                return SanitizationResult(
                    status=SanitizationStatus.CLEAN,
                    original_value=original,
                    sanitized_value="",
                    transformations_applied=[],
                    metadata={"was_empty": True},
                )
            else:
                return SanitizationResult(
                    status=SanitizationStatus.INVALID,
                    original_value=original,
                    sanitized_value=None,
                    errors=["Empty string not allowed"],
                    metadata={"was_empty": True},
                )
        
        # Strip specific characters if configured
        if self.strip_chars:
            old_result = result
            result = result.strip(self.strip_chars)
            if result != old_result:
                transformations.append(f"strip_chars({repr(self.strip_chars)})")
        
        # Trim whitespace
        if self.trim:
            old_result = result
            result = result.strip()
            if result != old_result:
                transformations.append("trim_whitespace")
        
        # Normalize internal whitespace
        if self.normalize_whitespace:
            old_result = result
            result = re.sub(r'\s+', ' ', result)
            if result != old_result:
                transformations.append("normalize_whitespace")
        
        # Apply casing transformation
        if self.casing != CasingStyle.NONE:
            old_result = result
            if self.casing == CasingStyle.LOWER:
                result = result.lower()
                transformations.append("lowercase")
            elif self.casing == CasingStyle.UPPER:
                result = result.upper()
                transformations.append("uppercase")
            elif self.casing == CasingStyle.TITLE:
                result = result.title()
                transformations.append("title_case")
            elif self.casing == CasingStyle.SENTENCE:
                # Sentence case: first char upper, rest lower
                if result:
                    result = result[0].upper() + result[1:].lower()
                    transformations.append("sentence_case")
        
        # Remove special characters (keep alphanumeric, spaces, basic punctuation)
        if self.remove_special_chars:
            old_result = result
            result = re.sub(r'[^a-zA-Z0-9\s\.\,\-\_\']', '', result)
            if result != old_result:
                transformations.append("remove_special_chars")
        
        # Final empty check after transformations
        if result == "" and not self.allow_empty:
            return SanitizationResult(
                status=SanitizationStatus.INVALID,
                original_value=original,
                sanitized_value=None,
                transformations_applied=transformations,
                errors=["Result is empty after sanitization"],
            )
        
        # Determine status
        if result != original:
            status = SanitizationStatus.SANITIZED
        else:
            status = SanitizationStatus.CLEAN
        
        return SanitizationResult(
            status=status,
            original_value=original,
            sanitized_value=result,
            transformations_applied=transformations,
            warnings=warnings,
            errors=errors,
            metadata={
                "original_length": len(original),
                "sanitized_length": len(result),
                "sanitized_at": datetime.now().isoformat(),
            },
        )
    
    def sanitize_field(
        self,
        data: Dict[str, Any],
        field_name: str,
        required: bool = True
    ) -> Dict[str, Any]:
        """
        Sanitize a specific field in a data dict.
        
        Args:
            data: Input data dictionary
            field_name: Name of field to sanitize
            required: If True, missing field is an error
            
        Returns:
            Updated data dict with sanitized field
        """
        result = data.copy()
        
        if field_name not in data:
            if required:
                result.setdefault("_sanitization_errors", []).append(
                    f"Missing required field: {field_name}"
                )
            return result
        
        sanitization_result = self.sanitize(data[field_name])
        result[field_name] = sanitization_result.sanitized_value
        
        if not sanitization_result.is_valid():
            result.setdefault("_sanitization_errors", []).append(
                f"Field '{field_name}': {', '.join(sanitization_result.errors)}"
            )
        
        if sanitization_result.was_sanitized():
            result.setdefault("_sanitization_metadata", {})[field_name] = \
                sanitization_result.to_dict()
        
        return result


@dataclass
class NumberSanitizer:
    """
    Sanitizes numeric values with type coercion and range validation.
    
    Supports:
    - String to number coercion
    - Integer vs float conversion
    - Range validation (min/max)
    - Default value for invalid/missing
    - Rounding
    """
    coerce: bool = True
    number_type: str = "float"  # "int" or "float"
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    default: Optional[float] = None
    allow_null: bool = False
    round_decimals: Optional[int] = None
    
    def sanitize(self, value: Any) -> SanitizationResult:
        """
        Sanitize a numeric value.
        
        Args:
            value: Input value (string, int, float, etc.)
            
        Returns:
            SanitizationResult with cleaned value and metadata
        """
        transformations = []
        warnings = []
        errors = []
        
        # Handle None
        if value is None:
            if self.allow_null:
                return SanitizationResult(
                    status=SanitizationStatus.CLEAN,
                    original_value=None,
                    sanitized_value=None,
                    transformations_applied=[],
                    metadata={"handled_null": True},
                )
            elif self.default is not None:
                return SanitizationResult(
                    status=SanitizationStatus.SANITIZED,
                    original_value=None,
                    sanitized_value=self.default,
                    transformations_applied=["use_default"],
                    metadata={"handled_null": True, "default_used": self.default},
                )
            else:
                return SanitizationResult(
                    status=SanitizationStatus.INVALID,
                    original_value=None,
                    sanitized_value=None,
                    errors=["Null value not allowed"],
                )
        
        # Already a number
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            result = float(value)
            if self.number_type == "int":
                old_result = result
                result = int(result)
                if old_result != result:
                    transformations.append("convert_to_int")
            original = value
        else:
            # Try to coerce
            original = value
            if not self.coerce:
                return SanitizationResult(
                    status=SanitizationStatus.INVALID,
                    original_value=original,
                    sanitized_value=None,
                    errors=[f"Expected number, got {type(value).__name__}"],
                )
            
            # String coercion
            if isinstance(value, str):
                value = value.strip()
                if value == "":
                    if self.default is not None:
                        transformations.append("empty_to_default")
                        result = self.default
                    elif self.allow_null:
                        transformations.append("empty_to_null")
                        return SanitizationResult(
                            status=SanitizationStatus.SANITIZED,
                            original_value=original,
                            sanitized_value=None,
                            transformations_applied=transformations,
                        )
                    else:
                        return SanitizationResult(
                            status=SanitizationStatus.INVALID,
                            original_value=original,
                            sanitized_value=None,
                            errors=["Empty string not allowed"],
                        )
                try:
                    if self.number_type == "int" and '.' not in value:
                        result = int(value)
                    else:
                        result = float(value)
                    transformations.append("string_to_number")
                except ValueError:
                    if self.default is not None:
                        transformations.append("parse_failed_use_default")
                        warnings.append(f"Could not parse '{value}' as number")
                        result = self.default
                    else:
                        return SanitizationResult(
                            status=SanitizationStatus.INVALID,
                            original_value=original,
                            sanitized_value=None,
                            errors=[f"Could not parse '{value}' as number"],
                        )
            else:
                return SanitizationResult(
                    status=SanitizationStatus.INVALID,
                    original_value=original,
                    sanitized_value=None,
                    errors=[f"Cannot coerce {type(value).__name__} to number"],
                )
        
        # Apply rounding
        if self.round_decimals is not None and isinstance(result, float):
            old_result = result
            result = round(result, self.round_decimals)
            if old_result != result:
                transformations.append(f"round({self.round_decimals})")
        
        # Range validation
        if self.min_value is not None and result < self.min_value:
            if self.default is not None:
                transformations.append("below_min_use_default")
                warnings.append(f"Value {result} below minimum {self.min_value}")
                result = self.default
            else:
                return SanitizationResult(
                    status=SanitizationStatus.INVALID,
                    original_value=original,
                    sanitized_value=None,
                    transformations_applied=transformations,
                    errors=[f"Value {result} below minimum {self.min_value}"],
                )
        
        if self.max_value is not None and result > self.max_value:
            if self.default is not None:
                transformations.append("above_max_use_default")
                warnings.append(f"Value {result} above maximum {self.max_value}")
                result = self.default
            else:
                return SanitizationResult(
                    status=SanitizationStatus.INVALID,
                    original_value=original,
                    sanitized_value=None,
                    transformations_applied=transformations,
                    errors=[f"Value {result} above maximum {self.max_value}"],
                )
        
        # Determine status
        if result != original:
            status = SanitizationStatus.SANITIZED
        else:
            status = SanitizationStatus.CLEAN
        
        return SanitizationResult(
            status=status,
            original_value=original,
            sanitized_value=result,
            transformations_applied=transformations,
            warnings=warnings,
            errors=errors,
            metadata={
                "number_type": self.number_type,
                "min_value": self.min_value,
                "max_value": self.max_value,
                "sanitized_at": datetime.now().isoformat(),
            },
        )
    
    def sanitize_field(
        self,
        data: Dict[str, Any],
        field_name: str,
        required: bool = True
    ) -> Dict[str, Any]:
        """
        Sanitize a numeric field in a data dict.
        
        Args:
            data: Input data dictionary
            field_name: Name of field to sanitize
            required: If True, missing field is an error
            
        Returns:
            Updated data dict with sanitized field
        """
        result = data.copy()
        
        if field_name not in data:
            if required:
                if self.default is not None:
                    result[field_name] = self.default
                    result.setdefault("_sanitization_metadata", {})[field_name] = {
                        "status": "sanitized",
                        "transformations_applied": ["missing_use_default"],
                    }
                else:
                    result.setdefault("_sanitization_errors", []).append(
                        f"Missing required field: {field_name}"
                    )
            return result
        
        sanitization_result = self.sanitize(data[field_name])
        result[field_name] = sanitization_result.sanitized_value
        
        if not sanitization_result.is_valid():
            result.setdefault("_sanitization_errors", []).append(
                f"Field '{field_name}': {', '.join(sanitization_result.errors)}"
            )
        
        if sanitization_result.was_sanitized():
            result.setdefault("_sanitization_metadata", {})[field_name] = \
                sanitization_result.to_dict()
        
        return result


@dataclass
class PayloadSanitizer:
    """
    Combined sanitization pipeline for full payload validation.
    
    Chains text and number sanitizers for comprehensive payload cleaning.
    """
    text_sanitizer: Optional[TextSanitizer] = None
    number_sanitizer: Optional[NumberSanitizer] = None
    field_rules: Dict[str, Union[TextSanitizer, NumberSanitizer]] = field(
        default_factory=dict
    )
    
    def add_rule(self, field_name: str, sanitizer: Union[TextSanitizer, NumberSanitizer]) -> None:
        """Add a sanitization rule for a specific field."""
        self.field_rules[field_name] = sanitizer
    
    def sanitize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sanitize an entire payload according to field rules.
        
        Args:
            payload: Input data dictionary
            
        Returns:
            Sanitized payload with metadata
        """
        result = payload.copy()
        all_errors = []
        all_metadata = {}
        
        # Apply field-specific rules
        for field_name, sanitizer in self.field_rules.items():
            if isinstance(sanitizer, TextSanitizer):
                sanitization_result = sanitizer.sanitize(payload.get(field_name))
            elif isinstance(sanitizer, NumberSanitizer):
                sanitization_result = sanitizer.sanitize(payload.get(field_name))
            else:
                continue
            
            result[field_name] = sanitization_result.sanitized_value
            
            if not sanitization_result.is_valid():
                all_errors.extend([
                    f"Field '{field_name}': {err}" for err in sanitization_result.errors
                ])
            
            if sanitization_result.was_sanitized():
                all_metadata[field_name] = sanitization_result.to_dict()
        
        # Add sanitization summary
        if all_errors:
            result["_sanitization_errors"] = all_errors
        if all_metadata:
            result["_sanitization_metadata"] = all_metadata
        result["_sanitized_at"] = datetime.now().isoformat()
        
        return result


def create_default_sanitizers() -> Dict[str, Union[TextSanitizer, NumberSanitizer]]:
    """
    Create default sanitizers for common use cases.
    
    Returns:
        Dict of configured sanitizers
    """
    return {
        "text_trim": TextSanitizer(
            trim=True,
            normalize_whitespace=True,
            casing=CasingStyle.NONE,
        ),
        "text_lowercase": TextSanitizer(
            trim=True,
            normalize_whitespace=True,
            casing=CasingStyle.LOWER,
        ),
        "text_title": TextSanitizer(
            trim=True,
            normalize_whitespace=True,
            casing=CasingStyle.TITLE,
        ),
        "number_coerce": NumberSanitizer(
            coerce=True,
            number_type="float",
            allow_null=False,
        ),
        "number_int": NumberSanitizer(
            coerce=True,
            number_type="int",
            allow_null=False,
        ),
        "number_percentage": NumberSanitizer(
            coerce=True,
            number_type="float",
            min_value=0,
            max_value=100,
            round_decimals=2,
        ),
    }


if __name__ == "__main__":
    # Demo/test usage
    print("Sanitization Transformers - Demo")
    print("=" * 60)
    
    # Test text sanitization
    text_sanitizer = TextSanitizer(
        trim=True,
        normalize_whitespace=True,
        casing=CasingStyle.TITLE,
    )
    
    test_cases = [
        "  hello   world  ",
        "UPPERCASE TEXT",
        "  mixed   CASE  text ",
        None,
        "",
    ]
    
    print("\nText Sanitization Tests:")
    for test in test_cases:
        result = text_sanitizer.sanitize(test)
        print(f"  Input: {repr(test)}")
        print(f"  Output: {repr(result.sanitized_value)} [{result.status.value}]")
        if result.transformations_applied:
            print(f"  Transformations: {result.transformations_applied}")
        if result.errors:
            print(f"  Errors: {result.errors}")
        print()
    
    # Test number sanitization
    number_sanitizer = NumberSanitizer(
        coerce=True,
        number_type="float",
        min_value=0,
        max_value=100,
        round_decimals=2,
        default=0,
    )
    
    number_tests = [
        "42",
        "  3.14159  ",
        "invalid",
        150,
        -5,
        None,
        "  ",
    ]
    
    print("\nNumber Sanitization Tests:")
    for test in number_tests:
        result = number_sanitizer.sanitize(test)
        print(f"  Input: {repr(test)}")
        print(f"  Output: {repr(result.sanitized_value)} [{result.status.value}]")
        if result.transformations_applied:
            print(f"  Transformations: {result.transformations_applied}")
        if result.warnings:
            print(f"  Warnings: {result.warnings}")
        if result.errors:
            print(f"  Errors: {result.errors}")
        print()
    
    # Test payload sanitization
    print("\nPayload Sanitization Test:")
    pipeline = PayloadSanitizer()
    pipeline.add_rule("name", TextSanitizer(trim=True, casing=CasingStyle.TITLE))
    pipeline.add_rule("email", TextSanitizer(trim=True, casing=CasingStyle.LOWER))
    pipeline.add_rule("age", NumberSanitizer(coerce=True, number_type="int", min_value=0))
    pipeline.add_rule("score", NumberSanitizer(coerce=True, min_value=0, max_value=100))
    
    test_payload = {
        "name": "  john   DOE  ",
        "email": "  JOHN@EXAMPLE.COM  ",
        "age": "25",
        "score": "85.5",
    }
    
    result = pipeline.sanitize(test_payload)
    print(f"  Input: {test_payload}")
    print(f"  Output: {result}")
    
    print("\n" + "=" * 60)
    print("Demo complete!")

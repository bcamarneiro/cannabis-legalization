#!/usr/bin/env python3
"""
Response-to-Domain Mapper - Transform HTTP responses into typed domain objects.

Provides utility functions and classes for transforming raw HTTP responses
into typed domain objects based on status codes and payloads.

Usage:
    from response_mapper import ResponseMapper, DomainResponse, MappingError
    from fetch_client import FetchClient, FetchResponse
    
    # Basic usage
    mapper = ResponseMapper()
    
    # Register a handler for specific status codes
    @mapper.handle(200)
    def handle_success(response: FetchResponse) -> DomainResponse:
        return DomainResponse(
            success=True,
            data=response.json(),
            status_code=response.status_code,
        )
    
    # Register a handler for error status codes
    @mapper.handle(404)
    def handle_not_found(response: FetchResponse) -> DomainResponse:
        return DomainResponse(
            success=False,
            error="Resource not found",
            status_code=response.status_code,
        )
    
    # Map a response
    client = FetchClient()
    fetch_response = client.get("https://api.example.com/resource")
    domain_response = mapper.map(fetch_response)
    
    # Or use the convenience method
    domain_response = mapper.map_response(fetch_response)
"""

import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, Callable, TypeVar, Generic, Union, List
from enum import Enum


class MappingError(Exception):
    """Base exception for response mapping operations."""
    pass


class NoHandlerError(MappingError):
    """No handler registered for the given status code."""
    pass


class MappingValidationError(MappingError):
    """Response mapping validation failed."""
    pass


@dataclass
class DomainResponse:
    """
    Generic domain response wrapper.
    
    Attributes:
        success: Whether the operation was successful
        data: The response data (parsed JSON, text, or raw bytes)
        error: Error message if operation failed
        status_code: Original HTTP status code
        metadata: Additional metadata (headers, timing, etc.)
    """
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    status_code: Optional[int] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def raise_if_error(self) -> None:
        """Raise MappingError if the response indicates failure."""
        if not self.success:
            raise MappingError(self.error or f"Request failed with status {self.status_code}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "success": self.success,
            "data": self.data,
            "error": self.error,
            "status_code": self.status_code,
            "metadata": self.metadata,
        }


T = TypeVar("T")


@dataclass
class TypedResponse(Generic[T]):
    """
    Type-safe domain response wrapper.
    
    Attributes:
        success: Whether the operation was successful
        data: The typed response data
        error: Error message if operation failed
        status_code: Original HTTP status code
    """
    success: bool
    data: T
    error: Optional[str] = None
    status_code: Optional[int] = None
    
    def raise_if_error(self) -> None:
        """Raise MappingError if the response indicates failure."""
        if not self.success:
            raise MappingError(self.error or f"Request failed with status {self.status_code}")


@dataclass
class ApiError:
    """
    Structured API error representation.
    
    Attributes:
        code: Error code (string or integer)
        message: Human-readable error message
        details: Additional error details
        status_code: HTTP status code
    """
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None
    status_code: Optional[int] = None
    
    @classmethod
    def from_response(cls, response: Any, status_code: int) -> "ApiError":
        """
        Create ApiError from response payload.
        
        Args:
            response: Parsed response body (dict or string)
            status_code: HTTP status code
            
        Returns:
            ApiError instance
        """
        if isinstance(response, dict):
            return cls(
                code=str(response.get("code", response.get("error", "unknown"))),
                message=response.get("message", response.get("error", "Unknown error")),
                details=response.get("details"),
                status_code=status_code,
            )
        elif isinstance(response, str):
            return cls(
                code="unknown",
                message=response,
                status_code=status_code,
            )
        else:
            return cls(
                code="unknown",
                message=str(response),
                status_code=status_code,
            )


HandlerFunc = Callable[[Any], DomainResponse]


class ResponseMapper:
    """
    Maps HTTP responses to domain objects based on status codes and payloads.
    
    Features:
    - Register handlers for specific status codes
    - Default handlers for success/error ranges
    - Payload-based routing
    - Type-safe response wrappers
    
    Usage:
        mapper = ResponseMapper()
        
        @mapper.handle(200)
        def handle_ok(response):
            return DomainResponse(success=True, data=response.json())
        
        @mapper.handle(404)
        def handle_not_found(response):
            return DomainResponse(success=False, error="Not found")
        
        @mapper.handle_range(500, 599)
        def handle_server_error(response):
            return DomainResponse(success=False, error="Server error")
        
        result = mapper.map(fetch_response)
    """
    
    def __init__(self):
        """Initialize the response mapper."""
        self._handlers: Dict[int, HandlerFunc] = {}
        self._range_handlers: List[tuple] = []  # [(start, end, handler), ...]
        self._default_handler: Optional[HandlerFunc] = None
        self._setup_default_handlers()
    
    def _setup_default_handlers(self) -> None:
        """Set up default handlers for common status code ranges."""
        # Default success handler for 2xx
        @self.handle_range(200, 299)
        def default_success(response: Any) -> DomainResponse:
            if hasattr(response, "status_code"):
                status_code = response.status_code
            else:
                status_code = 200
            
            data = None
            if hasattr(response, "json"):
                try:
                    data = response.json()
                except (json.JSONDecodeError, AttributeError):
                    pass
            elif isinstance(response, dict):
                data = response
            
            return DomainResponse(
                success=True,
                data=data,
                status_code=status_code,
            )
        
        # Default error handler for 4xx
        @self.handle_range(400, 499)
        def default_client_error(response: Any) -> DomainResponse:
            status_code = getattr(response, "status_code", 400)
            error_data = None
            
            if hasattr(response, "json"):
                try:
                    error_data = response.json()
                except (json.JSONDecodeError, AttributeError):
                    pass
            
            if isinstance(error_data, dict):
                error_msg = error_data.get("message", error_data.get("error", "Client error"))
            elif hasattr(response, "text"):
                error_msg = response.text()
            else:
                error_msg = "Client error"
            
            return DomainResponse(
                success=False,
                error=error_msg,
                status_code=status_code,
                metadata={"error_data": error_data},
            )
        
        # Default error handler for 5xx
        @self.handle_range(500, 599)
        def default_server_error(response: Any) -> DomainResponse:
            status_code = getattr(response, "status_code", 500)
            
            error_msg = "Internal server error"
            if hasattr(response, "text"):
                error_msg = response.text()
            
            return DomainResponse(
                success=False,
                error=error_msg,
                status_code=status_code,
            )
    
    def handle(self, status_code: int) -> Callable[[HandlerFunc], HandlerFunc]:
        """
        Decorator to register a handler for a specific status code.
        
        Args:
            status_code: HTTP status code to handle
            
        Returns:
            Decorator function
            
        Usage:
            @mapper.handle(200)
            def handle_ok(response):
                return DomainResponse(success=True, data=response.json())
        """
        def decorator(func: HandlerFunc) -> HandlerFunc:
            self._handlers[status_code] = func
            return func
        return decorator
    
    def handle_range(self, start: int, end: int) -> Callable[[HandlerFunc], HandlerFunc]:
        """
        Decorator to register a handler for a range of status codes.
        
        Args:
            start: Start of status code range (inclusive)
            end: End of status code range (inclusive)
            
        Returns:
            Decorator function
            
        Usage:
            @mapper.handle_range(500, 599)
            def handle_server_error(response):
                return DomainResponse(success=False, error="Server error")
        """
        def decorator(func: HandlerFunc) -> HandlerFunc:
            self._range_handlers.append((start, end, func))
            return func
        return decorator
    
    def set_default_handler(self, func: HandlerFunc) -> None:
        """
        Set a default handler for unregistered status codes.
        
        Args:
            func: Handler function
        """
        self._default_handler = func
    
    def _find_handler(self, status_code: int) -> Optional[HandlerFunc]:
        """
        Find the appropriate handler for a status code.
        
        Args:
            status_code: HTTP status code
            
        Returns:
            Handler function or None
        """
        # Check exact match first
        if status_code in self._handlers:
            return self._handlers[status_code]
        
        # Check range handlers
        for start, end, handler in self._range_handlers:
            if start <= status_code <= end:
                return handler
        
        # Fall back to default
        return self._default_handler
    
    def map(self, response: Any) -> DomainResponse:
        """
        Map an HTTP response to a domain object.
        
        Args:
            response: HTTP response object (e.g., FetchResponse)
            
        Returns:
            DomainResponse object
            
        Raises:
            NoHandlerError: If no handler is registered for the status code
            MappingError: If the handler raises an exception
        """
        status_code = getattr(response, "status_code", 200)
        
        handler = self._find_handler(status_code)
        if handler is None:
            raise NoHandlerError(f"No handler registered for status code {status_code}")
        
        try:
            return handler(response)
        except Exception as e:
            raise MappingError(f"Failed to map response: {e}") from e
    
    def map_response(self, response: Any) -> DomainResponse:
        """
        Alias for map() method.
        
        Args:
            response: HTTP response object
            
        Returns:
            DomainResponse object
        """
        return self.map(response)
    
    def map_to_type(self, response: Any, response_type: type[T]) -> TypedResponse[T]:
        """
        Map a response to a specific type.
        
        Args:
            response: HTTP response object
            response_type: Expected data type
            
        Returns:
            TypedResponse object
        """
        domain_response = self.map(response)
        
        if not domain_response.success:
            return TypedResponse[T](
                success=False,
                data=None,  # type: ignore[arg-type]
                error=domain_response.error,
                status_code=domain_response.status_code,
            )
        
        return TypedResponse[T](
            success=True,
            data=domain_response.data,  # type: ignore[arg-type]
            status_code=domain_response.status_code,
        )
    
    def validate_response(self, response: Any, schema: Dict[str, Any]) -> DomainResponse:
        """
        Map and validate a response against a schema.
        
        Args:
            response: HTTP response object
            schema: Expected schema dict with 'required' and 'types' keys
            
        Returns:
            DomainResponse object
            
        Raises:
            MappingValidationError: If validation fails
        """
        domain_response = self.map(response)
        
        if not domain_response.success:
            return domain_response
        
        data = domain_response.data
        if not isinstance(data, dict):
            raise MappingValidationError("Response data is not a dictionary")
        
        # Check required fields
        required = schema.get("required", [])
        for field_name in required:
            if field_name not in data:
                raise MappingValidationError(f"Missing required field: {field_name}")
        
        # Check types
        types = schema.get("types", {})
        for field_name, expected_type in types.items():
            if field_name in data:
                if not isinstance(data[field_name], expected_type):
                    raise MappingValidationError(
                        f"Field '{field_name}' has wrong type: expected {expected_type.__name__}, "
                        f"got {type(data[field_name]).__name__}"
                    )
        
        return domain_response


def create_success_response(
    data: Any,
    status_code: int = 200,
    metadata: Optional[Dict[str, Any]] = None,
) -> DomainResponse:
    """
    Create a success domain response.
    
    Args:
        data: Response data
        status_code: HTTP status code
        metadata: Additional metadata
        
    Returns:
        DomainResponse with success=True
    """
    return DomainResponse(
        success=True,
        data=data,
        status_code=status_code,
        metadata=metadata or {},
    )


def create_error_response(
    error: str,
    status_code: int = 400,
    error_data: Optional[Dict[str, Any]] = None,
) -> DomainResponse:
    """
    Create an error domain response.
    
    Args:
        error: Error message
        status_code: HTTP status code
        error_data: Additional error data
        
    Returns:
        DomainResponse with success=False
    """
    return DomainResponse(
        success=False,
        error=error,
        status_code=status_code,
        metadata={"error_data": error_data} if error_data else {},
    )


def main():
    """CLI demo and test."""
    print("Response Mapper - Demo")
    print("=" * 50)
    
    # Create mapper with custom handlers
    mapper = ResponseMapper()
    
    @mapper.handle(201)
    def handle_created(response: Any) -> DomainResponse:
        status_code = getattr(response, "status_code", 201)
        data = None
        if hasattr(response, "json"):
            try:
                data = response.json()
            except (json.JSONDecodeError, AttributeError):
                pass
        return DomainResponse(
            success=True,
            data=data,
            status_code=status_code,
            metadata={"message": "Resource created successfully"},
        )
    
    # Demo: Create mock responses
    class MockResponse:
        def __init__(self, status_code: int, body: Any):
            self.status_code = status_code
            self._body = body
        
        def json(self):
            return self._body
        
        def text(self):
            return str(self._body)
    
    # Test 200 OK
    print("\n1. Testing 200 OK:")
    mock_200 = MockResponse(200, {"id": 1, "name": "Test"})
    result = mapper.map(mock_200)
    print(f"   Success: {result.success}, Data: {result.data}")
    
    # Test 201 Created
    print("\n2. Testing 201 Created:")
    mock_201 = MockResponse(201, {"id": 2, "name": "Created"})
    result = mapper.map(mock_201)
    print(f"   Success: {result.success}, Data: {result.data}")
    print(f"   Metadata: {result.metadata}")
    
    # Test 404 Not Found
    print("\n3. Testing 404 Not Found:")
    mock_404 = MockResponse(404, {"error": "Not found"})
    result = mapper.map(mock_404)
    print(f"   Success: {result.success}, Error: {result.error}")
    
    # Test 500 Internal Server Error
    print("\n4. Testing 500 Internal Server Error:")
    mock_500 = MockResponse(500, "Server crashed")
    result = mapper.map(mock_500)
    print(f"   Success: {result.success}, Error: {result.error}")
    
    # Test convenience functions
    print("\n5. Testing convenience functions:")
    success = create_success_response({"key": "value"}, 200, {"timing": "0.1s"})
    print(f"   Success response: {success.to_dict()}")
    
    error = create_error_response("Something went wrong", 400, {"code": "INVALID_INPUT"})
    print(f"   Error response: {error.to_dict()}")
    
    print("\n" + "=" * 50)
    print("Demo complete!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Tests for Response-to-Domain Mapper.

Run: python3 tests/test_response_mapper.py
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from response_mapper import (
    ResponseMapper,
    DomainResponse,
    TypedResponse,
    ApiError,
    MappingError,
    NoHandlerError,
    MappingValidationError,
    create_success_response,
    create_error_response,
)


class MockResponse:
    """Mock HTTP response for testing."""
    
    def __init__(self, status_code: int, body: any, headers: dict = None):
        self.status_code = status_code
        self._body = body
        self.headers = headers or {}
    
    def json(self):
        """Return body as JSON."""
        return self._body
    
    def text(self, encoding: str = "utf-8") -> str:
        """Return body as text."""
        if isinstance(self._body, str):
            return self._body
        return str(self._body)


def test_domain_response_creation():
    """Test DomainResponse creation and methods."""
    print("Test: DomainResponse creation...")
    
    # Success response
    success = DomainResponse(
        success=True,
        data={"id": 1, "name": "Test"},
        status_code=200,
    )
    assert success.success is True
    assert success.data == {"id": 1, "name": "Test"}
    assert success.error is None
    
    # Error response
    error = DomainResponse(
        success=False,
        error="Not found",
        status_code=404,
    )
    assert error.success is False
    assert error.error == "Not found"
    assert error.data is None
    
    # to_dict method
    result = success.to_dict()
    assert result["success"] is True
    assert result["data"] == {"id": 1, "name": "Test"}
    assert result["status_code"] == 200
    
    # raise_if_error on success (should not raise)
    success.raise_if_error()
    
    # raise_if_error on error (should raise)
    try:
        error.raise_if_error()
        assert False, "Should have raised MappingError"
    except MappingError as e:
        assert "Not found" in str(e)
    
    print("  ✓ DomainResponse creation passed")


def test_mapper_handle_decorator():
    """Test handler registration via decorator."""
    print("Test: handle decorator...")
    
    mapper = ResponseMapper()
    
    @mapper.handle(201)
    def handle_created(response):
        return DomainResponse(
            success=True,
            data=response.json(),
            status_code=response.status_code,
            metadata={"message": "Created"},
        )
    
    mock_response = MockResponse(201, {"id": 123})
    result = mapper.map(mock_response)
    
    assert result.success is True
    assert result.data == {"id": 123}
    assert result.metadata["message"] == "Created"
    
    print("  ✓ handle decorator passed")


def test_mapper_handle_range():
    """Test handler registration for status code ranges."""
    print("Test: handle_range decorator...")
    
    mapper = ResponseMapper()
    
    # Clear default range handlers to test custom one
    mapper._range_handlers = []
    
    @mapper.handle_range(500, 599)
    def handle_server_error(response):
        return DomainResponse(
            success=False,
            error=f"Server error: {response.status_code}",
            status_code=response.status_code,
        )
    
    # Test 500
    mock_500 = MockResponse(500, "Error")
    result = mapper.map(mock_500)
    assert result.success is False
    assert "500" in result.error
    
    # Test 503
    mock_503 = MockResponse(503, "Unavailable")
    result = mapper.map(mock_503)
    assert result.success is False
    assert "503" in result.error
    
    print("  ✓ handle_range decorator passed")


def test_default_handlers():
    """Test default handlers for common status codes."""
    print("Test: default handlers...")
    
    mapper = ResponseMapper()
    
    # Test 200 OK (default success handler)
    mock_200 = MockResponse(200, {"data": "value"})
    result = mapper.map(mock_200)
    assert result.success is True
    assert result.data == {"data": "value"}
    assert result.status_code == 200
    
    # Test 404 Not Found (default client error handler)
    mock_404 = MockResponse(404, {"error": "Not found"})
    result = mapper.map(mock_404)
    assert result.success is False
    assert result.status_code == 404
    
    # Test 500 Internal Server Error (default server error handler)
    mock_500 = MockResponse(500, "Crash")
    result = mapper.map(mock_500)
    assert result.success is False
    assert result.status_code == 500
    
    print("  ✓ default handlers passed")


def test_no_handler_error():
    """Test NoHandlerError when no handler is registered."""
    print("Test: no handler error...")
    
    mapper = ResponseMapper()
    
    # Remove all range handlers to test no handler scenario
    mapper._range_handlers = []
    mapper._handlers = {}
    mapper._default_handler = None
    
    mock_response = MockResponse(200, {})
    
    try:
        mapper.map(mock_response)
        assert False, "Should have raised NoHandlerError"
    except NoHandlerError as e:
        assert "200" in str(e)
    
    print("  ✓ no handler error passed")


def test_mapping_error_on_handler_failure():
    """Test MappingError when handler raises exception."""
    print("Test: mapping error on handler failure...")
    
    mapper = ResponseMapper()
    
    @mapper.handle(200)
    def broken_handler(response):
        raise ValueError("Handler broken")
    
    mock_response = MockResponse(200, {})
    
    try:
        mapper.map(mock_response)
        assert False, "Should have raised MappingError"
    except MappingError as e:
        assert "Handler broken" in str(e)
    
    print("  ✓ mapping error on handler failure passed")


def test_api_error_from_response():
    """Test ApiError creation from response."""
    print("Test: ApiError from response...")
    
    # From dict
    error_dict = {"code": "INVALID", "message": "Invalid input", "details": {"field": "email"}}
    api_error = ApiError.from_response(error_dict, 400)
    assert api_error.code == "INVALID"
    assert api_error.message == "Invalid input"
    assert api_error.details == {"field": "email"}
    assert api_error.status_code == 400
    
    # From string
    api_error = ApiError.from_response("Something went wrong", 500)
    assert api_error.code == "unknown"
    assert api_error.message == "Something went wrong"
    assert api_error.status_code == 500
    
    print("  ✓ ApiError from response passed")


def test_typed_response():
    """Test TypedResponse generic wrapper."""
    print("Test: TypedResponse...")
    
    # Success
    typed = TypedResponse[str](
        success=True,
        data="hello",
        status_code=200,
    )
    assert typed.success is True
    assert typed.data == "hello"
    
    # Error
    typed_error = TypedResponse[dict](
        success=False,
        data=None,
        error="Failed",
        status_code=400,
    )
    assert typed_error.success is False
    assert typed_error.error == "Failed"
    
    # raise_if_error
    try:
        typed_error.raise_if_error()
        assert False, "Should have raised"
    except MappingError:
        pass  # Expected
    
    print("  ✓ TypedResponse passed")


def test_map_to_type():
    """Test map_to_type method."""
    print("Test: map_to_type...")
    
    mapper = ResponseMapper()
    
    mock_response = MockResponse(200, {"key": "value"})
    result = mapper.map_to_type(mock_response, dict)
    
    assert result.success is True
    assert result.data == {"key": "value"}
    assert result.status_code == 200
    
    print("  ✓ map_to_type passed")


def test_validate_response():
    """Test response validation against schema."""
    print("Test: validate_response...")
    
    mapper = ResponseMapper()
    
    schema = {
        "required": ["id", "name"],
        "types": {
            "id": int,
            "name": str,
        },
    }
    
    # Valid response
    mock_valid = MockResponse(200, {"id": 1, "name": "Test"})
    result = mapper.validate_response(mock_valid, schema)
    assert result.success is True
    
    # Missing required field
    mock_missing = MockResponse(200, {"id": 1})
    try:
        mapper.validate_response(mock_missing, schema)
        assert False, "Should have raised MappingValidationError"
    except MappingValidationError as e:
        assert "name" in str(e)
    
    # Wrong type
    mock_wrong_type = MockResponse(200, {"id": "one", "name": "Test"})
    try:
        mapper.validate_response(mock_wrong_type, schema)
        assert False, "Should have raised MappingValidationError"
    except MappingValidationError as e:
        assert "id" in str(e)
    
    print("  ✓ validate_response passed")


def test_create_success_response():
    """Test create_success_response convenience function."""
    print("Test: create_success_response...")
    
    result = create_success_response(
        {"data": "value"},
        201,
        {"timing": "0.1s"},
    )
    
    assert result.success is True
    assert result.data == {"data": "value"}
    assert result.status_code == 201
    assert result.metadata["timing"] == "0.1s"
    
    print("  ✓ create_success_response passed")


def test_create_error_response():
    """Test create_error_response convenience function."""
    print("Test: create_error_response...")
    
    result = create_error_response(
        "Something went wrong",
        400,
        {"code": "INVALID"},
    )
    
    assert result.success is False
    assert result.error == "Something went wrong"
    assert result.status_code == 400
    assert result.metadata["error_data"]["code"] == "INVALID"
    
    print("  ✓ create_error_response passed")


def test_mapper_map_response_alias():
    """Test map_response is alias for map."""
    print("Test: map_response alias...")
    
    mapper = ResponseMapper()
    mock_response = MockResponse(200, {"test": "data"})
    
    result1 = mapper.map(mock_response)
    result2 = mapper.map_response(mock_response)
    
    assert result1.success == result2.success
    assert result1.data == result2.data
    
    print("  ✓ map_response alias passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 50)
    print("Response-to-Domain Mapper - Test Suite")
    print("=" * 50 + "\n")
    
    tests = [
        test_domain_response_creation,
        test_mapper_handle_decorator,
        test_mapper_handle_range,
        test_default_handlers,
        test_no_handler_error,
        test_mapping_error_on_handler_failure,
        test_api_error_from_response,
        test_typed_response,
        test_map_to_type,
        test_validate_response,
        test_create_success_response,
        test_create_error_response,
        test_mapper_map_response_alias,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 50 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

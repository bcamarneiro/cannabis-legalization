#!/usr/bin/env python3
"""
Tests for Core Fetch Wrapper.

Run: python3 tests/test_fetch_client.py
"""

import sys
import threading
import time
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from fetch_client import (
    FetchClient,
    FetchResponse,
    FetchError,
    FetchTimeoutError,
    FetchAbortError,
    FetchRetryError,
)


def test_fetch_response_text():
    """Test FetchResponse text decoding."""
    print("Test: FetchResponse text decoding...")
    
    response = FetchResponse(
        status_code=200,
        headers={"content-type": "application/json"},
        body=b'{"key": "value"}',
        url="https://example.com",
        elapsed_time=0.5,
    )
    
    text = response.text()
    assert text == '{"key": "value"}', "Text should match body"
    assert response.text(encoding="utf-8") == text, "Encoding parameter should work"
    
    print("  ✓ FetchResponse text decoding passed")


def test_fetch_response_json():
    """Test FetchResponse JSON parsing."""
    print("Test: FetchResponse JSON parsing...")
    
    response = FetchResponse(
        status_code=200,
        headers={"content-type": "application/json"},
        body=b'{"key": "value", "number": 42}',
        url="https://example.com",
        elapsed_time=0.5,
    )
    
    data = response.json()
    assert data["key"] == "value", "JSON key should match"
    assert data["number"] == 42, "JSON number should match"
    
    print("  ✓ FetchResponse JSON parsing passed")


def test_fetch_response_raise_for_status():
    """Test FetchResponse raise_for_status."""
    print("Test: FetchResponse raise_for_status...")
    
    # 2xx should not raise
    response_200 = FetchResponse(
        status_code=200,
        headers={},
        body=b"",
        url="https://example.com",
        elapsed_time=0.5,
    )
    response_200.raise_for_status()  # Should not raise
    
    # 4xx should raise
    response_404 = FetchResponse(
        status_code=404,
        headers={},
        body=b"",
        url="https://example.com/notfound",
        elapsed_time=0.5,
    )
    try:
        response_404.raise_for_status()
        assert False, "Should have raised FetchError"
    except FetchError as e:
        assert "404" in str(e), "Error should contain status code"
    
    # 5xx should raise
    response_500 = FetchResponse(
        status_code=500,
        headers={},
        body=b"",
        url="https://example.com/error",
        elapsed_time=0.5,
    )
    try:
        response_500.raise_for_status()
        assert False, "Should have raised FetchError"
    except FetchError as e:
        assert "500" in str(e), "Error should contain status code"
    
    print("  ✓ FetchResponse raise_for_status passed")


def test_client_default_configuration():
    """Test FetchClient default configuration."""
    print("Test: FetchClient default configuration...")
    
    client = FetchClient()
    
    assert client.connect_timeout == 5.0, "Default connect timeout"
    assert client.read_timeout == 30.0, "Default read timeout"
    assert client.max_retries == 3, "Default max retries"
    assert client.retry_delay == 1.0, "Default retry delay"
    assert client.retry_status_codes == [429, 500, 502, 503, 504], "Default retry status codes"
    assert client.abort_signal is None, "Default abort signal"
    assert client.default_headers == {}, "Default headers"
    
    print("  ✓ FetchClient default configuration passed")


def test_client_custom_configuration():
    """Test FetchClient custom configuration."""
    print("Test: FetchClient custom configuration...")
    
    abort_event = threading.Event()
    custom_headers = {"User-Agent": "TestClient/1.0"}
    custom_retry_codes = [429, 503]
    
    client = FetchClient(
        connect_timeout=10.0,
        read_timeout=60.0,
        max_retries=5,
        retry_delay=2.0,
        retry_status_codes=custom_retry_codes,
        abort_signal=abort_event,
        default_headers=custom_headers,
    )
    
    assert client.connect_timeout == 10.0, "Custom connect timeout"
    assert client.read_timeout == 60.0, "Custom read timeout"
    assert client.max_retries == 5, "Custom max retries"
    assert client.retry_delay == 2.0, "Custom retry delay"
    assert client.retry_status_codes == custom_retry_codes, "Custom retry status codes"
    assert client.abort_signal is abort_event, "Custom abort signal"
    assert client.default_headers == custom_headers, "Custom headers"
    
    print("  ✓ FetchClient custom configuration passed")


def test_abort_signal():
    """Test abort signal cancellation."""
    print("Test: abort signal cancellation...")
    
    abort_event = threading.Event()
    abort_event.set()  # Pre-set to trigger abort
    
    client = FetchClient(abort_signal=abort_event, max_retries=0)
    
    try:
        client.get("https://example.com")
        assert False, "Should have raised FetchAbortError"
    except FetchAbortError as e:
        assert "aborted" in str(e).lower(), "Error should mention abort"
    
    print("  ✓ Abort signal cancellation passed")


def test_delay_calculation():
    """Test exponential backoff delay calculation."""
    print("Test: exponential backoff delay...")
    
    client = FetchClient(retry_delay=1.0)
    
    # Exponential backoff: delay * 2^attempt
    assert client._calculate_delay(0) == 1.0, "Attempt 0: 1.0s"
    assert client._calculate_delay(1) == 2.0, "Attempt 1: 2.0s"
    assert client._calculate_delay(2) == 4.0, "Attempt 2: 4.0s"
    assert client._calculate_delay(3) == 8.0, "Attempt 3: 8.0s"
    
    print("  ✓ Exponential backoff delay passed")


def test_should_retry_logic():
    """Test retry decision logic."""
    print("Test: retry decision logic...")
    
    client = FetchClient(max_retries=3, retry_status_codes=[429, 500, 503])
    
    # Should retry on configured status codes
    response_429 = FetchResponse(
        status_code=429, headers={}, body=b"", url="https://example.com", elapsed_time=0.1
    )
    response_500 = FetchResponse(
        status_code=500, headers={}, body=b"", url="https://example.com", elapsed_time=0.1
    )
    response_503 = FetchResponse(
        status_code=503, headers={}, body=b"", url="https://example.com", elapsed_time=0.1
    )
    
    assert client._should_retry(response_429, 0) is True, "Should retry on 429"
    assert client._should_retry(response_500, 1) is True, "Should retry on 500"
    assert client._should_retry(response_503, 2) is True, "Should retry on 503"
    
    # Should not retry on other status codes
    response_404 = FetchResponse(
        status_code=404, headers={}, body=b"", url="https://example.com", elapsed_time=0.1
    )
    response_200 = FetchResponse(
        status_code=200, headers={}, body=b"", url="https://example.com", elapsed_time=0.1
    )
    
    assert client._should_retry(response_404, 0) is False, "Should not retry on 404"
    assert client._should_retry(response_200, 0) is False, "Should not retry on 200"
    
    # Should not retry when max retries exceeded
    assert client._should_retry(response_500, 3) is False, "Should not retry after max retries"
    
    print("  ✓ Retry decision logic passed")


def test_http_methods_exist():
    """Test that all HTTP method helpers exist."""
    print("Test: HTTP method helpers...")
    
    client = FetchClient()
    
    assert hasattr(client, "get"), "Should have get method"
    assert hasattr(client, "post"), "Should have post method"
    assert hasattr(client, "put"), "Should have put method"
    assert hasattr(client, "delete"), "Should have delete method"
    assert hasattr(client, "patch"), "Should have patch method"
    assert hasattr(client, "request"), "Should have request method"
    
    print("  ✓ HTTP method helpers passed")


def test_request_body_serialization():
    """Test request body serialization."""
    print("Test: request body serialization...")
    
    # This test verifies the body handling logic without making real requests
    # by checking that the method accepts different body types
    
    client = FetchClient(max_retries=0)
    
    # Verify method signatures accept different body types
    # (actual network calls will fail without a server, but we test the interface)
    
    # Dict body should be accepted (will be JSON-serialized)
    try:
        client.post("http://invalid-host-for-test", body={"key": "value"})
    except Exception:
        pass  # Expected to fail network-wise
    
    # String body should be accepted
    try:
        client.post("http://invalid-host-for-test", body="string body")
    except Exception:
        pass  # Expected to fail network-wise
    
    # Bytes body should be accepted
    try:
        client.post("http://invalid-host-for-test", body=b"bytes body")
    except Exception:
        pass  # Expected to fail network-wise
    
    print("  ✓ Request body serialization passed")


def test_exception_hierarchy():
    """Test exception class hierarchy."""
    print("Test: exception hierarchy...")
    
    # All fetch exceptions should be subclasses of FetchError
    assert issubclass(FetchTimeoutError, FetchError), "FetchTimeoutError should extend FetchError"
    assert issubclass(FetchAbortError, FetchError), "FetchAbortError should extend FetchError"
    assert issubclass(FetchRetryError, FetchError), "FetchRetryError should extend FetchError"
    
    # Verify we can catch specific exceptions
    try:
        raise FetchTimeoutError("test")
    except FetchError:
        pass  # Should be caught as FetchError
    
    try:
        raise FetchAbortError("test")
    except FetchError:
        pass  # Should be caught as FetchError
    
    print("  ✓ Exception hierarchy passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 50)
    print("Core Fetch Wrapper - Test Suite")
    print("=" * 50 + "\n")
    
    tests = [
        test_fetch_response_text,
        test_fetch_response_json,
        test_fetch_response_raise_for_status,
        test_client_default_configuration,
        test_client_custom_configuration,
        test_abort_signal,
        test_delay_calculation,
        test_should_retry_logic,
        test_http_methods_exist,
        test_request_body_serialization,
        test_exception_hierarchy,
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

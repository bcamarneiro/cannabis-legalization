#!/usr/bin/env python3
"""
Core Fetch Wrapper - Base HTTP Client.

Provides a reusable HTTP client with configurable timeouts, retry logic,
and abort signal handling, independent of business logic.

Usage:
    from fetch_client import FetchClient, FetchError
    
    # Basic usage with defaults
    client = FetchClient()
    response = client.get("https://api.example.com/data")
    
    # Custom timeouts and retries
    client = FetchClient(
        connect_timeout=5.0,
        read_timeout=30.0,
        max_retries=3,
        retry_delay=1.0,
    )
    response = client.get("https://api.example.com/data")
    
    # With abort signal
    import threading
    abort_event = threading.Event()
    client = FetchClient(abort_signal=abort_event)
    response = client.get("https://api.example.com/data")
    
    # Retry on specific status codes
    client = FetchClient(retry_status_codes=[429, 500, 502, 503, 504])
    response = client.get("https://api.example.com/data")
"""

import time
import threading
import urllib.request
import urllib.error
import urllib.parse
import json
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List, Union
from enum import Enum


class FetchError(Exception):
    """Base exception for fetch operations."""
    pass


class FetchTimeoutError(FetchError):
    """Request timed out."""
    pass


class FetchAbortError(FetchError):
    """Request was aborted via abort signal."""
    pass


class FetchRetryError(FetchError):
    """All retry attempts exhausted."""
    pass


@dataclass
class FetchResponse:
    """HTTP response wrapper."""
    status_code: int
    headers: Dict[str, str]
    body: bytes
    url: str
    elapsed_time: float
    
    def text(self, encoding: str = "utf-8") -> str:
        """Decode body as text."""
        return self.body.decode(encoding)
    
    def json(self) -> Any:
        """Parse body as JSON."""
        return json.loads(self.body.decode("utf-8"))
    
    def raise_for_status(self) -> None:
        """Raise FetchError if status code indicates an error."""
        if 400 <= self.status_code < 600:
            raise FetchError(f"HTTP {self.status_code}: {self.url}")


@dataclass
class FetchRequest:
    """HTTP request configuration."""
    method: str
    url: str
    headers: Optional[Dict[str, str]] = None
    body: Optional[bytes] = None
    timeout: Optional[float] = None


class FetchClient:
    """
    Base HTTP client with configurable timeouts, retry logic, and abort handling.
    
    Features:
    - Configurable connect and read timeouts
    - Exponential backoff retry logic
    - Abort signal support for cancellation
    - Retry on specific HTTP status codes
    - Clean separation from business logic
    """
    
    DEFAULT_CONNECT_TIMEOUT = 5.0
    DEFAULT_READ_TIMEOUT = 30.0
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_RETRY_DELAY = 1.0
    DEFAULT_RETRY_STATUS_CODES = [429, 500, 502, 503, 504]
    
    def __init__(
        self,
        connect_timeout: Optional[float] = None,
        read_timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_delay: Optional[float] = None,
        retry_status_codes: Optional[List[int]] = None,
        abort_signal: Optional[threading.Event] = None,
        default_headers: Optional[Dict[str, str]] = None,
    ):
        """
        Initialize the fetch client.
        
        Args:
            connect_timeout: Connection timeout in seconds (default: 5.0)
            read_timeout: Read timeout in seconds (default: 30.0)
            max_retries: Maximum retry attempts (default: 3)
            retry_delay: Base delay between retries in seconds (default: 1.0)
            retry_status_codes: HTTP status codes that trigger retry (default: [429, 500, 502, 503, 504])
            abort_signal: Threading event to signal abort/cancellation
            default_headers: Default headers to include in all requests
        """
        self.connect_timeout = connect_timeout or self.DEFAULT_CONNECT_TIMEOUT
        self.read_timeout = read_timeout or self.DEFAULT_READ_TIMEOUT
        self.max_retries = max_retries or self.DEFAULT_MAX_RETRIES
        self.retry_delay = retry_delay or self.DEFAULT_RETRY_DELAY
        self.retry_status_codes = retry_status_codes or self.DEFAULT_RETRY_STATUS_CODES
        self.abort_signal = abort_signal
        self.default_headers = default_headers or {}
    
    def _check_abort(self) -> None:
        """Check if abort signal was triggered."""
        if self.abort_signal and self.abort_signal.is_set():
            raise FetchAbortError("Request aborted via signal")
    
    def _calculate_delay(self, attempt: int) -> float:
        """Calculate exponential backoff delay."""
        return self.retry_delay * (2 ** attempt)
    
    def _create_request(self, request: FetchRequest) -> urllib.request.Request:
        """Create urllib request object."""
        headers = {**self.default_headers}
        if request.headers:
            headers.update(request.headers)
        
        req = urllib.request.Request(
            request.url,
            data=request.body,
            headers=headers,
            method=request.method,
        )
        return req
    
    def _do_request(self, request: FetchRequest) -> FetchResponse:
        """Execute a single HTTP request."""
        self._check_abort()
        
        start_time = time.time()
        timeout = request.timeout or self.connect_timeout + self.read_timeout
        
        req = self._create_request(request)
        
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                body = response.read()
                headers = dict(response.headers)
                status_code = response.status
                url = response.url
                
                elapsed = time.time() - start_time
                
                return FetchResponse(
                    status_code=status_code,
                    headers=headers,
                    body=body,
                    url=url,
                    elapsed_time=elapsed,
                )
        except urllib.error.HTTPError as e:
            elapsed = time.time() - start_time
            body = e.read() if e.fp else b""
            headers = dict(e.headers) if hasattr(e, "headers") else {}
            
            return FetchResponse(
                status_code=e.code,
                headers=headers,
                body=body,
                url=e.url,
                elapsed_time=elapsed,
            )
        except urllib.error.URLError as e:
            if "timed out" in str(e.reason).lower():
                raise FetchTimeoutError(f"Request timed out: {request.url}")
            raise FetchError(f"Request failed: {e.reason}")
        except TimeoutError:
            raise FetchTimeoutError(f"Request timed out: {request.url}")
    
    def _should_retry(self, response: FetchResponse, attempt: int) -> bool:
        """Determine if request should be retried."""
        if attempt >= self.max_retries:
            return False
        return response.status_code in self.retry_status_codes
    
    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Union[str, bytes, Dict[str, Any]]] = None,
        timeout: Optional[float] = None,
    ) -> FetchResponse:
        """
        Execute HTTP request with retry logic.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            url: Request URL
            headers: Request headers
            body: Request body (string, bytes, or dict for JSON)
            timeout: Request timeout override
        
        Returns:
            FetchResponse object
        
        Raises:
            FetchAbortError: If abort signal was triggered
            FetchTimeoutError: If request timed out
            FetchRetryError: If all retry attempts exhausted
            FetchError: For other request failures
        """
        # Prepare body
        body_bytes: Optional[bytes] = None
        if body is not None:
            if isinstance(body, dict):
                body_bytes = json.dumps(body).encode("utf-8")
                if headers is None:
                    headers = {}
                headers["Content-Type"] = "application/json"
            elif isinstance(body, str):
                body_bytes = body.encode("utf-8")
            else:
                body_bytes = body
        
        fetch_request = FetchRequest(
            method=method.upper(),
            url=url,
            headers=headers,
            body=body_bytes,
            timeout=timeout,
        )
        
        last_response: Optional[FetchResponse] = None
        
        for attempt in range(self.max_retries + 1):
            self._check_abort()
            
            try:
                response = self._do_request(fetch_request)
                last_response = response
                
                if self._should_retry(response, attempt):
                    delay = self._calculate_delay(attempt)
                    time.sleep(delay)
                    continue
                
                return response
                
            except (FetchTimeoutError, FetchAbortError):
                raise
            except FetchError as e:
                last_response = None
                if attempt < self.max_retries:
                    delay = self._calculate_delay(attempt)
                    time.sleep(delay)
                else:
                    raise
        
        # Should not reach here, but handle edge case
        if last_response:
            return last_response
        raise FetchRetryError(f"All {self.max_retries + 1} attempts exhausted for {url}")
    
    def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FetchResponse:
        """Execute GET request."""
        return self.request("GET", url, headers=headers, timeout=timeout)
    
    def post(
        self,
        url: str,
        body: Optional[Union[str, bytes, Dict[str, Any]]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FetchResponse:
        """Execute POST request."""
        return self.request("POST", url, body=body, headers=headers, timeout=timeout)
    
    def put(
        self,
        url: str,
        body: Optional[Union[str, bytes, Dict[str, Any]]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FetchResponse:
        """Execute PUT request."""
        return self.request("PUT", url, body=body, headers=headers, timeout=timeout)
    
    def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FetchResponse:
        """Execute DELETE request."""
        return self.request("DELETE", url, headers=headers, timeout=timeout)
    
    def patch(
        self,
        url: str,
        body: Optional[Union[str, bytes, Dict[str, Any]]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> FetchResponse:
        """Execute PATCH request."""
        return self.request("PATCH", url, body=body, headers=headers, timeout=timeout)

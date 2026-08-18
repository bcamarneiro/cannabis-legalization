"""
Test suite for backend.server — stdlib unittest (no pytest).

Usage:
    python3 -m unittest backend.tests.test_server
"""

from __future__ import annotations

import json
import threading
import unittest
from http.server import HTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from backend.server import HOST, PORT, SubmissionHandler


def _find_free_port() -> int:
    """Return an unused port number for test isolation."""
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


class TestServer(unittest.TestCase):
    """Integration tests for the HTTP API server."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.port = _find_free_port()
        cls.server = HTTPServer((HOST, cls.port), SubmissionHandler)
        cls._thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls._thread.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls._thread.join(timeout=5)

    @property
    def base_url(self) -> str:
        return f"http://{HOST}:{self.port}"

    # -----------------------------------------------------------------------
    # GET /health
    # -----------------------------------------------------------------------

    def test_health_returns_200(self) -> None:
        with urlopen(f"{self.base_url}/health") as resp:
            self.assertEqual(resp.status, 200)
            data = json.loads(resp.read())
            self.assertEqual(data, {"status": "ok"})

    # -----------------------------------------------------------------------
    # GET unknown route → 404
    # -----------------------------------------------------------------------

    def test_get_unknown_returns_404(self) -> None:
        with self.assertRaises(HTTPError) as ctx:
            urlopen(f"{self.base_url}/nonexistent")
        self.assertEqual(ctx.exception.code, 404)

    # -----------------------------------------------------------------------
    # OPTIONS preflight returns CORS headers
    # -----------------------------------------------------------------------

    def test_options_returns_cors_headers(self) -> None:
        req = Request(f"{self.base_url}/api/submissions", method="OPTIONS")
        with urlopen(req) as resp:
            self.assertEqual(resp.status, 204)
            self.assertEqual(
                resp.getheader("Access-Control-Allow-Origin"), "*"
            )
            self.assertIn("GET", resp.getheader("Access-Control-Allow-Methods", ""))
            self.assertIn("POST", resp.getheader("Access-Control-Allow-Methods", ""))
            self.assertIn("OPTIONS", resp.getheader("Access-Control-Allow-Methods", ""))

    # -----------------------------------------------------------------------
    # POST /api/submissions — success (201)
    # -----------------------------------------------------------------------

    def test_post_valid_submission_returns_201(self) -> None:
        body = json.dumps({
            "chapter_number": 1,
            "title": "Test Chapter",
            "content": "This is a test submission.",
        }).encode("utf-8")
        req = Request(
            f"{self.base_url}/api/submissions",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        with urlopen(req) as resp:
            self.assertEqual(resp.status, 201)
            data = json.loads(resp.read())
            self.assertEqual(data["chapter_number"], 1)
            self.assertEqual(data["title"], "Test Chapter")
            self.assertIn("# Test Chapter", data["markdown"])
            self.assertIn("This is a test submission.", data["markdown"])

    # -----------------------------------------------------------------------
    # POST /api/submissions — validation error (422)
    # -----------------------------------------------------------------------

    def test_post_invalid_submission_returns_422(self) -> None:
        body = json.dumps({
            "chapter_number": "not-a-number",
        }).encode("utf-8")
        req = Request(
            f"{self.base_url}/api/submissions",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        with self.assertRaises(HTTPError) as ctx:
            urlopen(req)
        self.assertEqual(ctx.exception.code, 422)

    # -----------------------------------------------------------------------
    # POST /api/submissions — bad JSON (400)
    # -----------------------------------------------------------------------

    def test_post_bad_json_returns_400(self) -> None:
        body = b"not json at all"
        req = Request(
            f"{self.base_url}/api/submissions",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        with self.assertRaises(HTTPError) as ctx:
            urlopen(req)
        self.assertEqual(ctx.exception.code, 400)

    # -----------------------------------------------------------------------
    # POST unknown route → 404
    # -----------------------------------------------------------------------

    def test_post_unknown_route_returns_404(self) -> None:
        body = b"{}"
        req = Request(
            f"{self.base_url}/unknown",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        with self.assertRaises(HTTPError) as ctx:
            urlopen(req)
        self.assertEqual(ctx.exception.code, 404)

    # -----------------------------------------------------------------------
    # CORS header on error responses
    # -----------------------------------------------------------------------

    def test_error_response_includes_cors_header(self) -> None:
        body = b"bad"
        req = Request(
            f"{self.base_url}/api/submissions",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        try:
            urlopen(req)
        except HTTPError as exc:
            self.assertEqual(
                exc.headers.get("Access-Control-Allow-Origin"), "*"
            )

    # -----------------------------------------------------------------------
    # /health also includes CORS header
    # -----------------------------------------------------------------------

    def test_health_includes_cors_header(self) -> None:
        with urlopen(f"{self.base_url}/health") as resp:
            self.assertEqual(
                resp.getheader("Access-Control-Allow-Origin"), "*"
            )


if __name__ == "__main__":
    unittest.main()

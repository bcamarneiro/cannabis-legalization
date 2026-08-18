#!/usr/bin/env python3
"""
HTTP API server — Backend processor & Markdown generator for
cannabis-legalization submissions.

Usage:
    python3 backend/server.py [--host HOST] [--port PORT]

Endpoints:
    GET  /health          — Health check
    POST /api/submissions — Validate, sanitize, and transform a submission

Pure stdlib — no external dependencies.
"""

from __future__ import annotations

import json
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Any

# Handle both `python3 -m backend.server` (relative import) and
# `python3 backend/server.py` (absolute import) gracefully.
try:
    from .processor import (
        ValidationError,
        process_submission,
    )
except ImportError:
    # Running as `python3 backend/server.py` — add project root to path
    _project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, _project_root)
    from backend.processor import (
        ValidationError,
        process_submission,
    )

HOST = "127.0.0.1"
PORT = 8080


class SubmissionHandler(BaseHTTPRequestHandler):
    """HTTP request handler with CORS support for the submissions API."""

    def _send_json(self, data: Any, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False, indent=2)
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def _read_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        raw = self.rfile.read(length)
        return json.loads(raw)

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send_json({"status": "ok"})
        else:
            self._send_json({"error": "Not found"}, status=404)

    def do_POST(self) -> None:
        if self.path != "/api/submissions":
            self._send_json({"error": "Not found"}, status=404)
            return

        try:
            body = self._read_body()
        except json.JSONDecodeError:
            self._send_json(
                {"error": "Invalid JSON body"}, status=400
            )
            return

        try:
            result = process_submission(body)
        except ValidationError as exc:
            self._send_json({"error": str(exc)}, status=422)
            return

        self._send_json(result, status=201)

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
        """Suppress default stderr logging; write to stdout."""
        print(f"[api] {args[0]}", flush=True)


def main() -> None:
    host = HOST
    port = PORT
    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "--host" and i + 1 < len(args):
            host = args[i + 1]
            i += 2
        elif args[i] == "--port" and i + 1 < len(args):
            port = int(args[i + 1])
            i += 2
        else:
            i += 1

    server = HTTPServer((host, port), SubmissionHandler)
    print(f"Backend processor listening on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()

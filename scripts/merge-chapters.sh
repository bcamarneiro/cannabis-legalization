#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cat "$PROJECT_DIR"/chapters/*.md > "$PROJECT_DIR/documento.md"
echo "✅ documento.md regenerated from chapters/"

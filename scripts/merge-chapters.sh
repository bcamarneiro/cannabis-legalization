#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

{
  echo "<!-- FICHEIRO AUTO-GERADO — NÃO EDITAR DIRECTAMENTE -->"
  echo "<!-- Fonte de verdade: chapters/*.md -->"
  echo "<!-- Regenerar com: bash scripts/merge-chapters.sh -->"
  echo ""
  cat "$PROJECT_DIR"/chapters/*.md
} > "$PROJECT_DIR/documento.md"
echo "✅ documento.md regenerated from chapters/"

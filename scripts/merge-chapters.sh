#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "$SCRIPT_DIR/common.sh"

gather_sources

# Create build directory if it doesn't exist
mkdir -p "$PROJECT_DIR/build"

{
  echo "<!-- FICHEIRO AUTO-GERADO — NÃO EDITAR DIRECTAMENTE -->"
  echo "<!-- Fonte de verdade: chapters/*.md -->"
  echo "<!-- Regenerar com: bash scripts/merge-chapters.sh -->"
  echo ""
  concat_chapters
} > "$PROJECT_DIR/build/documento.md"
echo "✅ build/documento.md regenerated from chapters/"

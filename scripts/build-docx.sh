#!/usr/bin/env bash
set -euo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

OUTPUT_DOCX="$OUTPUT_DIR/$OUTPUT_BASENAME.docx"

mkdir -p "$OUTPUT_DIR"
gather_sources
require_pandoc 2

if [[ ! -f "$CSL_FILE" ]]; then
    echo "❌ CSL style not found: $CSL_FILE" >&2
    exit 1
fi

echo "📄 Convertendo Markdown → DOCX..."
echo "   Fonte: chapters/ (${#SOURCE_FILES[@]} ficheiros)"
echo "   Destino: $OUTPUT_DOCX"
echo ""

make_temp_md
concat_chapters | sed 's/#heading=/#/' > "$TEMP_MD"

pandoc "$TEMP_MD" \
    --from="$PANDOC_FROM" \
    --to=docx \
    --output="$OUTPUT_DOCX" \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --variable lang=pt-PT \
    --variable toc-title="Índice" \
    --citeproc \
    --bibliography="$BIB_FILE" \
    --csl="$CSL_FILE" \
    --resource-path=".:assets/diagrams" \
    --standalone

echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_DOCX"

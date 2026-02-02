#!/usr/bin/env bash
set -euo pipefail

# Configuração
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CHAPTERS_DIR="$PROJECT_DIR/chapters"
OUTPUT_DOCX="$PROJECT_DIR/output/Documento_Cannabis.docx"
CSL_STYLE="$PROJECT_DIR/ieee.csl"

# Criar pasta output
mkdir -p "$PROJECT_DIR/output"

# Recolher ficheiros fonte (chapters/ se existir, senão documento.md)
if [[ -d "$CHAPTERS_DIR" ]]; then
    SOURCE_FILES=("$CHAPTERS_DIR"/[0-9]*.md)
    SOURCE_LABEL="chapters/"
else
    SOURCE_FILES=("$PROJECT_DIR/documento.md")
    SOURCE_LABEL="documento.md"
fi

echo "📄 Convertendo Markdown → DOCX..."
echo "   Fonte: $SOURCE_LABEL (${#SOURCE_FILES[@]} ficheiros)"
echo "   Destino: $OUTPUT_DOCX"
echo ""

# Verificar que CSL existe
if [[ ! -f "$CSL_STYLE" ]]; then
    echo "❌ CSL style not found: $CSL_STYLE"
    exit 1
fi

# Preprocessar Markdown
TEMP_MD="/tmp/doc-clean-temp.md"
cat "${SOURCE_FILES[@]}" | sed 's/#heading=/#/' > "$TEMP_MD"

# Conversão com Pandoc
pandoc "$TEMP_MD" \
    --from=markdown+footnotes+pipe_tables+autolink_bare_uris \
    --to=docx \
    --output="$OUTPUT_DOCX" \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --variable lang=pt-PT \
    --variable toc-title="Índice" \
    --citeproc \
    --bibliography="$PROJECT_DIR/references.bib" \
    --csl="$CSL_STYLE" \
    --resource-path=".:assets/diagrams" \
    --standalone

# Limpar ficheiros temporários
rm -f "$TEMP_MD"

echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_DOCX"
echo ""
echo "ℹ️  Gerado com Pandoc (formatação básica)"
echo "ℹ️  TOC automático com links"
echo "ℹ️  Secções numeradas automaticamente"
echo "ℹ️  Citações BibTeX processadas"

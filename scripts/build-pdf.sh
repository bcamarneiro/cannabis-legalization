#!/usr/bin/env bash
set -euo pipefail

export PATH="/Library/TeX/texbin:$PATH"

source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

TEMPLATE_TEX="$PROJECT_DIR/assets/templates/template.tex"
OUTPUT_PDF="$OUTPUT_DIR/$OUTPUT_BASENAME.pdf"
OUTPUT_TEX="$OUTPUT_DIR/$OUTPUT_BASENAME.tex"

mkdir -p "$OUTPUT_DIR"
gather_sources
require_pandoc 2

echo "📄 Convertendo Markdown → LaTeX → PDF..."
echo "   Fonte: chapters/ (${#SOURCE_FILES[@]} ficheiros)"
echo "   Template: $TEMPLATE_TEX"
echo "   Destino: $OUTPUT_PDF"
echo ""

# Remove emojis e CO₂ (a fonte do PDF não os tem), normaliza espaço antes de citações
make_temp_md
concat_chapters | \
sed 's/#heading=/#/' | \
sed 's/⚠️//g' | \
sed 's/✅//g' | \
sed 's/❌//g' | \
sed 's/CO₂/CO2/g' | \
sed 's/ {-}$//' | \
sed 's/\[@/ \[@/g' | \
sed 's/  \[@/ \[@/g' > "$TEMP_MD"

echo "📝 Passo 1/2: Convertendo Markdown → LaTeX..."
pandoc "$TEMP_MD" \
    --from="$PANDOC_FROM" \
    --to=latex \
    --output="$OUTPUT_TEX" \
    --template="$TEMPLATE_TEX" \
    --variable lang=pt-PT \
    --resource-path=".:assets/diagrams" \
    --number-sections \
    --toc \
    --toc-depth=3 \
    --standalone \
    --citeproc \
    --csl="$CSL_FILE" \
    --metadata link-citations=true \
    --bibliography="$BIB_FILE"

echo "✅ LaTeX gerado: $OUTPUT_TEX"

echo "📝 Passo 2/2: Compilando LaTeX → PDF..."
cd "$OUTPUT_DIR"

if command -v xelatex &> /dev/null; then
    LATEX_CMD="xelatex"
else
    LATEX_CMD="pdflatex"
fi
echo "   Usando: $LATEX_CMD"

for pass in 1 2 3; do
    $LATEX_CMD -interaction=nonstopmode "$OUTPUT_BASENAME.tex" 2>&1 | tail -20 || true
    echo "   Compilação $pass/3 completa"
done

if [[ ! -f "$OUTPUT_BASENAME.pdf" ]]; then
    echo "❌ ERRO: PDF não foi gerado!"
    grep -A5 "^!" "$OUTPUT_BASENAME.log" 2>/dev/null || echo "   (sem log disponível)"
    exit 1
fi

rm -f *.aux *.log *.out *.toc

FILE_SIZE=$(ls -lh "$OUTPUT_PDF" | awk '{print $5}')
echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_PDF"
echo "   Tamanho: $FILE_SIZE"

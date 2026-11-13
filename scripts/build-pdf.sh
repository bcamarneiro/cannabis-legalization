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

# Limite por passagem: um xelatex parado falha em minutos, com o log, em vez de horas.
LIMITE=()
if command -v timeout &> /dev/null; then
    LIMITE=(timeout 300)
fi

for pass in 1 2 3; do
    ${LIMITE[@]+"${LIMITE[@]}"} $LATEX_CMD -interaction=nonstopmode "$OUTPUT_BASENAME.tex" < /dev/null 2>&1 | tail -20 || true
    echo "   Compilação $pass/3 completa"
done

# Um PDF que existe mas está vazio ou truncado também é falha: entre Fevereiro e
# Novembro de 2026 as releases saíram com um PDF de 431 bytes sem o CI dar por isso.
PDF_BYTES=0
if [[ -f "$OUTPUT_BASENAME.pdf" ]]; then
    PDF_BYTES=$(wc -c < "$OUTPUT_BASENAME.pdf" | tr -d ' ')
fi
if (( PDF_BYTES < 200000 )) || ! grep -q "^Output written on " "$OUTPUT_BASENAME.log" 2>/dev/null; then
    echo "❌ ERRO: PDF não foi gerado, ou saiu incompleto ($PDF_BYTES bytes)!"
    grep -A5 "^!" "$OUTPUT_BASENAME.log" 2>/dev/null || echo "   (sem erros «!» no log)"
    echo "   Últimas linhas do log:"
    tail -40 "$OUTPUT_BASENAME.log" 2>/dev/null || echo "   (sem log disponível)"
    exit 1
fi

rm -f *.aux *.log *.out *.toc

FILE_SIZE=$(ls -lh "$OUTPUT_PDF" | awk '{print $5}')
echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_PDF"
echo "   Tamanho: $FILE_SIZE"

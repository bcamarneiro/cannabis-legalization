#!/usr/bin/env bash
set -euo pipefail

# Adicionar MacTeX ao PATH
export PATH="/Library/TeX/texbin:$PATH"

# Configuração
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
CHAPTERS_DIR="$PROJECT_DIR/chapters"
TEMPLATE_TEX="$PROJECT_DIR/assets/templates/template.tex"
OUTPUT_PDF="$PROJECT_DIR/output/Documento_Cannabis.pdf"
OUTPUT_TEX="$PROJECT_DIR/output/Documento_Cannabis.tex"

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

echo "📄 Convertendo Markdown → LaTeX → PDF..."
echo "   Fonte: $SOURCE_LABEL (${#SOURCE_FILES[@]} ficheiros)"
echo "   Template: $TEMPLATE_TEX"
echo "   Destino: $OUTPUT_PDF"
echo ""

# Preprocessar Markdown (remover emojis e limpar links)
TEMP_MD="/tmp/doc-clean-temp.md"
cat "${SOURCE_FILES[@]}" | \
sed 's/#heading=/#/' | \
sed 's/⚠️//g' | \
sed 's/✅//g' | \
sed 's/❌//g' | \
sed 's/CO₂/CO2/g' > "$TEMP_MD"

# Passo 1: Markdown → LaTeX
echo "📝 Passo 1/2: Convertendo Markdown → LaTeX..."
pandoc "$TEMP_MD" \
    --from=markdown+footnotes+pipe_tables+autolink_bare_uris \
    --to=latex \
    --output="$OUTPUT_TEX" \
    --template="$TEMPLATE_TEX" \
    --variable lang=pt-PT \
    --resource-path=".:assets/diagrams" \
    --number-sections \
    --standalone \
    --citeproc \
    --csl="$PROJECT_DIR/ieee.csl" \
    --metadata link-citations=true \
    --bibliography="$PROJECT_DIR/references.bib"

echo "✅ LaTeX gerado: $OUTPUT_TEX"

# Passo 2: LaTeX → PDF
echo "📝 Passo 2/2: Compilando LaTeX → PDF..."
cd "$PROJECT_DIR/output"
pdflatex -interaction=nonstopmode Documento_Cannabis.tex > /dev/null 2>&1 || true
echo "   Compilação 1/2 completa"
pdflatex -interaction=nonstopmode Documento_Cannabis.tex > /dev/null 2>&1 || true
echo "   Compilação 2/2 completa"

# Limpar ficheiros temporários
rm -f *.aux *.log *.out *.toc "$TEMP_MD"

# Resultado
FILE_SIZE=$(ls -lh "$OUTPUT_PDF" | awk '{print $5}')
echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_PDF"
echo "   Tamanho: $FILE_SIZE"

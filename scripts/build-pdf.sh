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
    SOURCE_FILES=("$PROJECT_DIR/build/documento.md")
    SOURCE_LABEL="build/documento.md"
fi

echo "📄 Convertendo Markdown → LaTeX → PDF..."
echo "   Fonte: $SOURCE_LABEL (${#SOURCE_FILES[@]} ficheiros)"
echo "   Template: $TEMPLATE_TEX"
echo "   Destino: $OUTPUT_PDF"
echo ""

# Preprocessar Markdown (remover emojis, limpar links, normalizar espaços antes de citações)
TEMP_MD="/tmp/doc-clean-temp.md"
cat "${SOURCE_FILES[@]}" | \
sed 's/#heading=/#/' | \
sed 's/⚠️//g' | \
sed 's/✅//g' | \
sed 's/❌//g' | \
sed 's/CO₂/CO2/g' | \
sed 's/ {-}$//' | \
sed 's/\[@/ \[@/g' | \
sed 's/  \[@/ \[@/g' > "$TEMP_MD"

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
    --toc \
    --toc-depth=3 \
    --standalone \
    --citeproc \
    --csl="$PROJECT_DIR/ieee.csl" \
    --metadata link-citations=true \
    --bibliography="$PROJECT_DIR/references.bib"

echo "✅ LaTeX gerado: $OUTPUT_TEX"

# Debug: mostrar primeiros headers
echo "📋 DEBUG - Primeiras secções no .tex:"
grep -m5 "\\\\section" "$OUTPUT_TEX" || echo "   (nenhuma \\section encontrada)"

# Passo 2: LaTeX → PDF
echo "📝 Passo 2/2: Compilando LaTeX → PDF..."
cd "$PROJECT_DIR/output"

# Usar xelatex se disponível (melhor suporte Unicode), senão pdflatex
if command -v xelatex &> /dev/null; then
    LATEX_CMD="xelatex"
else
    LATEX_CMD="pdflatex"
fi

echo "   Usando: $LATEX_CMD"
$LATEX_CMD -interaction=nonstopmode Documento_Cannabis.tex 2>&1 | tail -20 || true
echo "   Compilação 1/3 completa"
echo "📋 DEBUG - Ficheiros após 1ª compilação:"
ls -la *.toc *.aux 2>/dev/null || echo "   (nenhum .toc/.aux)"
echo "📋 DEBUG - Conteúdo do .toc (se existir):"
head -20 Documento_Cannabis.toc 2>/dev/null || echo "   (sem .toc)"
$LATEX_CMD -interaction=nonstopmode Documento_Cannabis.tex 2>&1 | tail -20 || true
echo "   Compilação 2/3 completa"
$LATEX_CMD -interaction=nonstopmode Documento_Cannabis.tex 2>&1 | tail -20 || true
echo "   Compilação 3/3 completa"

# Verificar se PDF foi gerado
if [[ ! -f "Documento_Cannabis.pdf" ]]; then
    echo "❌ ERRO: PDF não foi gerado!"
    echo "   Log de erros:"
    cat Documento_Cannabis.log 2>/dev/null | grep -A5 "^!" || echo "   (sem log disponível)"
    exit 1
fi

# Limpar ficheiros temporários
rm -f *.aux *.log *.out *.toc "$TEMP_MD"

# Resultado
FILE_SIZE=$(ls -lh "$OUTPUT_PDF" | awk '{print $5}')
echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_PDF"
echo "   Tamanho: $FILE_SIZE"

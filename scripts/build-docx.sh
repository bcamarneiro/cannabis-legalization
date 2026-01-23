#!/usr/bin/env bash
set -euo pipefail

# Configuração
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SOURCE_MD="$PROJECT_DIR/documento.md"
OUTPUT_DOCX="$PROJECT_DIR/output/Documento_Cannabis.docx"
CSL_STYLE="$PROJECT_DIR/assets/templates/csl/apa.csl"

# Criar pasta output
mkdir -p "$PROJECT_DIR/output"

echo "📄 Convertendo Markdown → DOCX..."
echo "   Fonte: $SOURCE_MD"
echo "   Destino: $OUTPUT_DOCX"
echo ""

# Download CSL se não existir (estilo APA)
if [[ ! -f "$CSL_STYLE" ]]; then
    echo "📥 Downloading APA citation style..."
    mkdir -p "$PROJECT_DIR/assets/templates/csl"
    curl -sL https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl -o "$CSL_STYLE"
fi

# Preprocessar Markdown
TEMP_MD="/tmp/doc-clean-temp.md"
sed 's/#heading=/#/' "$SOURCE_MD" > "$TEMP_MD"

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

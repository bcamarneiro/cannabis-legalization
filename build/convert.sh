#!/usr/bin/env bash
set -euo pipefail

# Configuração
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
SOURCE_MD="$PROJECT_DIR/Documento_Posicao_Cannabis_LIVRE-REV-CTS.md"
BIBFILE="$SCRIPT_DIR/references.bib"
OUTPUT_DOCX="$PROJECT_DIR/output/Documento_Cannabis.docx"
CSL_STYLE="$SCRIPT_DIR/csl/apa.csl"

# Criar pasta output
mkdir -p "$PROJECT_DIR/output"

echo "📄 Convertendo Markdown → DOCX..."
echo "   Fonte: $SOURCE_MD"
echo "   Destino: $OUTPUT_DOCX"
echo ""

# Verificar se ficheiros existem
if [[ ! -f "$SOURCE_MD" ]]; then
    echo "❌ Ficheiro fonte não encontrado: $SOURCE_MD"
    exit 1
fi

if [[ ! -f "$BIBFILE" ]]; then
    echo "⚠️  Ficheiro de referências não encontrado: $BIBFILE"
    echo "   As citações [@key] não serão resolvidas."
    echo "   Executa: python3 build/migrate-references.py"
fi

# Download CSL se não existir (estilo APA)
if [[ ! -f "$CSL_STYLE" ]]; then
    echo "📥 Downloading APA citation style..."
    mkdir -p csl
    curl -sL https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl -o "$CSL_STYLE"
fi

# Limpar links vazios #heading= que causam erro no Pandoc
TEMP_MD="/tmp/doc-clean-temp.md"
sed 's/#heading=/#/' "$SOURCE_MD" > "$TEMP_MD"

# Conversão com Pandoc
cd "$PROJECT_DIR"
pandoc "$TEMP_MD" \
    --from=markdown+footnotes+pipe_tables+autolink_bare_uris \
    --to=docx \
    --output="$OUTPUT_DOCX" \
    --toc \
    --toc-depth=3 \
    --number-sections \
    ${BIBFILE:+--bibliography="$BIBFILE"} \
    ${CSL_STYLE:+--csl="$CSL_STYLE"} \
    --resource-path=".:assets/diagrams" \
    --standalone
cd "$SCRIPT_DIR"

# Limpar ficheiro temporário se existir
if [[ -f "/tmp/doc-clean-temp.md" ]]; then
    rm "/tmp/doc-clean-temp.md"
fi

echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_DOCX"
echo ""
echo "ℹ️  Índice: Gerado automaticamente com --toc"
echo "ℹ️  Numeração: Secções numeradas automaticamente"
echo "ℹ️  Referências: ${BIBFILE:+Geradas de $BIBFILE}"

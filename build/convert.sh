#!/usr/bin/env bash
set -euo pipefail

# Configuração
SOURCE_MD="../Documento_Posicao_Cannabis_LIVRE-REV-CTS.md"
BIBFILE="references.bib"
OUTPUT_DOCX="../output/Documento_Cannabis.docx"
CSL_STYLE="csl/apa.csl"  # Estilo de citação (APA, Chicago, etc.)

# Criar pasta output
mkdir -p ../output

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

# Conversão com Pandoc
pandoc "$SOURCE_MD" \
    --from=markdown+footnotes+pipe_tables+autolink_bare_uris \
    --to=docx \
    --output="$OUTPUT_DOCX" \
    --toc \
    --toc-depth=3 \
    --number-sections \
    ${BIBFILE:+--bibliography="$BIBFILE"} \
    ${CSL_STYLE:+--csl="$CSL_STYLE"} \
    --reference-doc="${TEMPLATE_DOCX:-}" \
    --resource-path="..:../assets/diagrams" \
    --standalone

echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_DOCX"
echo ""
echo "ℹ️  Índice: Gerado automaticamente com --toc"
echo "ℹ️  Numeração: Secções numeradas automaticamente"
echo "ℹ️  Referências: ${BIBFILE:+Geradas de $BIBFILE}"

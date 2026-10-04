#!/usr/bin/env bash
set -euo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

SITE_DIR="$OUTPUT_DIR/site"
SITE_SRC="$PROJECT_DIR/site"
REPO="${GITHUB_REPOSITORY:-bcamarneiro/cannabis-legalization}"

gather_sources
require_pandoc 3

echo "🌐 Construindo o site em $SITE_DIR ..."

mkdir -p "$OUTPUT_DIR"
rm -rf "$SITE_DIR"
mkdir -p "$SITE_DIR"

make_temp_md
concat_chapters | sed 's/#heading=/#/' > "$TEMP_MD"

META_JSON="$OUTPUT_DIR/site-meta.json"
python3 "$COMMON_SCRIPT_DIR/heading_ids.py" meta --repo "$REPO" --out "$META_JSON"

ZIP="$OUTPUT_DIR/site.zip"
rm -f "$ZIP"
pandoc "$TEMP_MD" \
    --from="$PANDOC_FROM" \
    --to=chunkedhtml \
    --split-level=1 \
    --chunk-template="%i.html" \
    --output="$ZIP" \
    --template="$SITE_SRC/template.html" \
    --lua-filter="$SITE_SRC/section-actions.lua" \
    --metadata-file="$META_JSON" \
    --variable lang=pt-PT \
    --variable version="$(tr -d '[:space:]' < "$PROJECT_DIR/VERSION")" \
    --variable builddate="$(date +%Y-%m-%d)" \
    --resource-path=".:assets/diagrams" \
    --number-sections \
    --toc \
    --toc-depth=3 \
    --standalone \
    --citeproc \
    --csl="$CSL_FILE" \
    --metadata link-citations=true \
    --bibliography="$BIB_FILE"

# Python em vez de unzip: o unzip do macOS estraga nomes de ficheiro com acentos (UTF-8).
python3 -c 'import sys, zipfile; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])' "$ZIP" "$SITE_DIR"
rm -f "$ZIP"
cp "$SITE_SRC/site.css" "$SITE_DIR/site.css"

if [[ -d "$PROJECT_DIR/assets/diagrams" ]]; then
    mkdir -p "$SITE_DIR/assets/diagrams"
    cp "$PROJECT_DIR"/assets/diagrams/*.png "$SITE_DIR/assets/diagrams/" 2>/dev/null || true
fi

if [[ "${SKIP_PAGEFIND:-0}" != "1" ]]; then
    npx -y pagefind@1 --site "$SITE_DIR"
fi

echo "✅ Site gerado: $SITE_DIR ($(find "$SITE_DIR" -maxdepth 1 -name '*.html' | wc -l | tr -d ' ') páginas)"

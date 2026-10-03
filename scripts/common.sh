#!/usr/bin/env bash
# Funções e variáveis partilhadas pelos scripts de build. Usar com `source`.

COMMON_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$COMMON_SCRIPT_DIR")"
CHAPTERS_DIR="$PROJECT_DIR/chapters"
OUTPUT_DIR="$PROJECT_DIR/output"
BIB_FILE="$PROJECT_DIR/references.bib"
CSL_FILE="$PROJECT_DIR/ieee.csl"
OUTPUT_BASENAME="Regulacao_Cannabis_Portugal"
PANDOC_FROM="markdown+footnotes+pipe_tables+autolink_bare_uris"

gather_sources() {
    shopt -s nullglob
    SOURCE_FILES=("$CHAPTERS_DIR"/[0-9]*.md)
    shopt -u nullglob
    if [[ ${#SOURCE_FILES[@]} -eq 0 ]]; then
        echo "❌ Nenhum capítulo encontrado em $CHAPTERS_DIR" >&2
        return 1
    fi
}

require_pandoc() {
    local min_major="$1" version
    if ! command -v pandoc >/dev/null 2>&1; then
        echo "❌ pandoc não encontrado" >&2
        return 1
    fi
    version="$(pandoc --version | head -1 | awk '{print $2}')"
    if [[ "${version%%.*}" -lt "$min_major" ]]; then
        echo "❌ pandoc $version encontrado; é preciso ${min_major}.x ou superior" >&2
        return 1
    fi
}

make_temp_md() {
    TEMP_MD="$(mktemp "${TMPDIR:-/tmp}/cannabis-doc.XXXXXX")"
    trap 'rm -f "$TEMP_MD"' EXIT
}

# Imprime cada capítulo seguido de uma linha em branco, para que o primeiro
# cabeçalho do capítulo seguinte nunca fique colado ao último parágrafo.
concat_chapters() {
    local f
    for f in "${SOURCE_FILES[@]}"; do
        cat "$f"
        printf '\n'
    done
}

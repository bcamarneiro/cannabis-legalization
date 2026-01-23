#!/usr/bin/env bash
set -euo pipefail

# Configuração
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse argumentos
BUILD_PDF=false
BUILD_DOCX=false

if [[ $# -eq 0 ]]; then
    # Sem argumentos: build ambos
    BUILD_PDF=true
    BUILD_DOCX=true
else
    # Com argumentos: build apenas o especificado
    for arg in "$@"; do
        case "$arg" in
            pdf)
                BUILD_PDF=true
                ;;
            docx)
                BUILD_DOCX=true
                ;;
            *)
                echo "Uso: $0 [pdf] [docx]"
                echo ""
                echo "Exemplos:"
                echo "  $0           # Build PDF e DOCX"
                echo "  $0 pdf       # Build apenas PDF"
                echo "  $0 docx      # Build apenas DOCX"
                echo "  $0 pdf docx  # Build ambos"
                exit 1
                ;;
        esac
    done
fi

echo "========================================="
echo "Build Documento Cannabis - LIVRE"
echo "========================================="
echo ""

# Build PDF
if [[ "$BUILD_PDF" == true ]]; then
    echo "🔨 Building PDF..."
    bash "$SCRIPT_DIR/build-pdf.sh"
    echo ""
fi

# Build DOCX
if [[ "$BUILD_DOCX" == true ]]; then
    echo "🔨 Building DOCX..."
    bash "$SCRIPT_DIR/build-docx.sh"
    echo ""
fi

echo "========================================="
echo "✅ Build completo!"
echo "========================================="

#!/usr/bin/env bash
set -euo pipefail

# Configuração
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# Check if reversion-enabled build is requested
USE_REVERSION=false
if [[ "${1:-}" == "--with-reversion" ]]; then
    USE_REVERSION=true
    shift
fi

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
                echo "Uso: $0 [--with-reversion] [pdf] [docx]"
                echo ""
                echo "Exemplos:"
                echo "  $0           # Build PDF e DOCX"
                echo "  $0 pdf       # Build apenas PDF"
                echo "  $0 docx      # Build apenas DOCX"
                echo "  $0 pdf docx  # Build ambos"
                echo "  $0 --with-reversion pdf  # Build PDF with automatic rollback on failure"
                exit 1
                ;;
        esac
    done
fi

echo "========================================="
echo "Build Documento Cannabis - LIVRE"
echo "========================================="
echo ""

# Build with reversion logic
if [[ "$USE_REVERSION" == true ]]; then
    echo "🔄 Reversion logic enabled - automatic rollback on failure"
    echo ""
    
    # Determine build type argument
    BUILD_TYPE="both"
    if [[ "$BUILD_PDF" == true && "$BUILD_DOCX" == false ]]; then
        BUILD_TYPE="pdf"
    elif [[ "$BUILD_DOCX" == true && "$BUILD_PDF" == false ]]; then
        BUILD_TYPE="docx"
    fi
    
    # Run build with transactional reversion
    python3 "$SCRIPT_DIR/build_state.py" build --type "$BUILD_TYPE"
else
    # Traditional build (no reversion)
    
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
fi

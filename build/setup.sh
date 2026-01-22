#!/usr/bin/env bash
set -euo pipefail

echo "🔧 Instalando dependências para build do documento..."

# Verificar se Homebrew está instalado
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew não encontrado. Instala primeiro: https://brew.sh"
    exit 1
fi

# Instalar Pandoc
if ! command -v pandoc &> /dev/null; then
    echo "📦 Instalando Pandoc..."
    brew install pandoc
else
    echo "✅ Pandoc já instalado ($(pandoc --version | head -1))"
fi

# Instalar pandoc-crossref (para referências cruzadas)
if ! command -v pandoc-crossref &> /dev/null; then
    echo "📦 Instalando pandoc-crossref..."
    brew install pandoc-crossref
else
    echo "✅ pandoc-crossref já instalado"
fi

# Opcional: Mermaid CLI
if ! command -v mmdc &> /dev/null; then
    echo "📦 Instalando mermaid-cli..."
    brew install mermaid-cli
else
    echo "✅ mermaid-cli já instalado"
fi

# Verificar Python (para script de migração)
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Python3 não encontrado. Instala para usar migrate-references.py"
else
    echo "✅ Python3 disponível ($(python3 --version))"
fi

echo ""
echo "✨ Setup completo!"
echo ""
echo "Próximos passos:"
echo "1. Migrar referências atuais: python3 build/migrate-references.py"
echo "2. Editar documento com citações dinâmicas: [@key]"
echo "3. Build: ./build/convert.sh"

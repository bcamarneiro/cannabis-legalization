#!/bin/bash
set -e

# Install dependencies (Vercel runs as root, no sudo needed)
apt-get update
apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-latex-extra

# Run build (generates PDF and DOCX in output/)
bash scripts/build.sh

# Create a simple index.html for Vercel to serve
mkdir -p public
cat > public/index.html << 'EOF'
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Regulação da Cannabis em Portugal - LIVRE</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; }
        h1 { color: #1a1a1a; }
        a { color: #0066cc; }
        .download { background: #0066cc; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; display: inline-block; margin: 10px 10px 10px 0; }
        .download:hover { background: #0055aa; }
    </style>
</head>
<body>
    <h1>Proposta de Regulação da Cannabis em Portugal</h1>
    <p>Documento de posição do LIVRE sobre regulação da cannabis em Portugal, abrangendo uso medicinal, recreativo e industrial.</p>
    <h2>Downloads</h2>
    <a href="../output/Regulacao_Cannabis_Portugal.pdf" class="download">📄 PDF</a>
    <a href="../output/Regulacao_Cannabis_Portugal.docx" class="download">📝 DOCX</a>
    <h2>Contribuir</h2>
    <p>Este documento é desenvolvido de forma aberta e colaborativa.</p>
    <ul>
        <li><a href="https://github.com/bcamarneiro/cannabis-legalization">Repositório GitHub</a></li>
        <li><a href="https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md">Como Contribuir</a></li>
    </ul>
</body>
</html>
EOF

echo "Build complete - static site created in public/"

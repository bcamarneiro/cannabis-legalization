#!/bin/bash
set -e

# Lightweight Vercel build: deploy a static landing page that links to the
# latest PDF/DOCX releases on GitHub. The full LaTeX build runs in GitHub
# Actions (auto-release.yml) and is too heavy for Vercel's build environment.

mkdir -p public

cat > public/index.html << 'EOF'
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Regulação da Cannabis em Portugal - LIVRE</title>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6; color: #1a1a1a; }
        h1 { color: #1a1a1a; margin-bottom: 8px; }
        .subtitle { color: #555; font-size: 1.1em; margin-top: 0; }
        a { color: #0066cc; }
        .download { background: #0066cc; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; display: inline-block; margin: 10px 10px 10px 0; }
        .download:hover { background: #0055aa; }
        .releases { background: #f5f5f5; padding: 16px; border-radius: 6px; margin-top: 24px; }
    </style>
</head>
<body>
    <h1>Proposta de Regulação da Cannabis em Portugal</h1>
    <p class="subtitle">Documento de posição do LIVRE sobre regulação da cannabis em Portugal, abrangendo uso medicinal, recreativo e industrial.</p>

    <h2>Downloads</h2>
    <p>O PDF e DOCX são gerados automaticamente a cada alteração. Descarregue a versão mais recente:</p>
    <a href="https://github.com/bcamarneiro/cannabis-legalization/releases/latest" class="download">📦 Ver últimos releases</a>

    <div class="releases">
        <h3>Como é construído</h3>
        <p>Este documento é escrito em <a href="https://github.com/bcamarneiro/cannabis-legalization/blob/main/chapters/">Markdown</a> e compilado para PDF/DOCX com <a href="https://pandoc.org/">Pandoc</a> + <a href="https://xetex.sourceforge.net/">XeLaTeX</a>. O build automático corre em GitHub Actions sempre que há alterações aos capítulos.</p>
    </div>

    <h2>Contribuir</h2>
    <p>Este documento é desenvolvido de forma aberta e colaborativa.</p>
    <ul>
        <li><a href="https://github.com/bcamarneiro/cannabis-legalization">Repositório GitHub</a></li>
        <li><a href="https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md">Como Contribuir</a></li>
    </ul>
</body>
</html>
EOF

echo "Build complete - static landing page created in public/"

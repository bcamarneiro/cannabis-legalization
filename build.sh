#!/bin/bash
set -e
mkdir -p output
cat > output/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Cannabis Legalization Project</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Cannabis Legalization Proposal</h1>
    <p>This repository contains research and documentation about cannabis legalization in Brazil.</p>
</body>
</html>
EOF
echo "Build complete"

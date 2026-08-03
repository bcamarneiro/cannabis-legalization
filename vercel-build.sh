#!/bin/bash
set -e

# Install dependencies (Vercel runs as root, no sudo needed)
apt-get update
apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-latex-extra

# Run build
bash scripts/build.sh

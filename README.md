# Documento de Posição: Regulação da Cannabis em Portugal

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Discussions](https://img.shields.io/github/discussions/bcamarneiro/cannabis-legalization)](https://github.com/bcamarneiro/cannabis-legalization/discussions)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Posição oficial do LIVRE** sobre enquadramento legal e regulatório da cannabis em Portugal, abrangendo uso medicinal, recreativo e industrial.

## 📖 Sobre Este Documento

**Desenvolvido pelo LIVRE de forma aberta e colaborativa.**

### Contribuições Externas
- ✅ **Bem-vindas de todos** — outros partidos, associações, profissionais, cidadãos
- ✅ **Avaliadas pelo mérito** — evidência científica e rigor técnico, não ideologia
- ✅ **Creditadas explicitamente** — todos os contribuidores aparecem nos commits
- ⚖️ **LIVRE mantém decisão final** sobre conteúdo da posição oficial

### Uso por Outros Partidos/Grupos
- 📋 **Licença CC BY-SA 4.0** — reutilização livre com atribuição
- 🔄 **Fork e adaptação permitidos** — outros podem criar suas versões
- 🤝 **Se múltiplos partidos adoptarem** → potencial proposta cross-party

**Transparência total:** Todo o processo é público ([GitHub](https://github.com/bcamarneiro/cannabis-legalization)), todas as decisões rastreáveis.

---

## 🤝 Como Contribuir

**Advogado? Médico? Economista? Activista? Qualquer cidadão?** Precisamos de ti!

- ⚖️ **Não-técnicos** (não sabes Git): Ver [CONTRIBUTING.md - Secção Não-Técnicos](CONTRIBUTING.md#-para-contribuidores-não-técnicos)
- 💻 **Técnicos** (sabes Git/GitHub): Ver [CONTRIBUTING.md - Secção Técnicos](CONTRIBUTING.md#-workflow-de-contribuição-técnico)

**Issues abertas**: [Vulnerabilidades identificadas em TASKS.md](docs/TASKS.md)

---

## 🚀 Build Rápido

```bash
# Build PDF + DOCX
bash scripts/build.sh

# Ou apenas um formato:
bash scripts/build.sh pdf
bash scripts/build.sh docx
```

**Output**: `output/Documento_Cannabis.pdf` e `output/Documento_Cannabis.docx`

## 📋 Requisitos

- **Pandoc** 2.19+ ([instalação](https://pandoc.org/installing.html))
- **pdflatex** (MacTeX, TeX Live, ou MiKTeX)
- **Bash** (macOS/Linux/WSL)

## 📂 Estrutura do Projeto

```
.
├── documento.md                    ← Source of truth (Markdown + Pandoc citations)
├── references.bib                  ← Base de dados bibliográfica (BibTeX)
├── scripts/
│   ├── build.sh                    ← Wrapper principal (PDF + DOCX)
│   ├── build-pdf.sh                ← Build PDF via LaTeX
│   └── build-docx.sh               ← Build DOCX direto
├── assets/
│   ├── templates/
│   │   ├── template.tex            ← Template LaTeX customizado
│   │   └── csl/apa.csl             ← Estilo citações APA (auto-download)
│   └── diagrams/                   ← Diagramas Mermaid (PNG)
└── output/                         ← Outputs gerados (gitignored)
```

## 📝 Workflow de Edição

### 1. Editar o Documento

Ficheiro principal: [`documento.md`](documento.md)

- **Markdown padrão** com extensões Pandoc
- **Citações**: formato `[@key]` → resolvidas via `references.bib`
- **Tabelas**: Markdown pipe tables
- **Diagramas**: Mermaid (pre-renderizados em `assets/diagrams/`)

### 2. Adicionar Referências

Editar [`references.bib`](references.bib) com entries BibTeX:

```bibtex
@article{exemplo2024,
  author = {Autor, Nome},
  title = {Título do Artigo},
  journal = {Nome da Revista},
  year = {2024},
  url = {https://...}
}
```

Depois usar no documento como `[@exemplo2024]`.

### 3. Navegar Citações

**Realidade**: Nenhuma extensão VSCode funciona de forma fiável para navegar de `[@key]` em Markdown para `references.bib`.

**Workaround**:
1. Seleciona a key dentro de `[@infarmed2024]` → só `infarmed2024`
2. **Cmd+Shift+F** (macOS) ou **Ctrl+Shift+F** (Windows) → search global
3. Clica no resultado em `references.bib`

Ou usa `grep`:
```bash
grep "@.*{infarmed2024" references.bib
```

### 4. Build

```bash
bash scripts/build.sh
```

O que acontece:
- **PDF**: `documento.md` → LaTeX → PDF (2 passes pdflatex)
- **DOCX**: `documento.md` → DOCX direto (Pandoc)
- **Citações**: Resolvidas automaticamente via `--citeproc` (estilo APA)
- **TOC**: Gerado automaticamente com links
- **Numeração**: Secções numeradas automaticamente

## 🔧 Troubleshooting

### Build falha com "pandoc: command not found"

```bash
# macOS (Homebrew)
brew install pandoc

# Ubuntu/Debian
sudo apt install pandoc

# Windows (Chocolatey)
choco install pandoc
```

### Build PDF falha com "pdflatex: command not found"

```bash
# macOS
brew install --cask mactex

# Ubuntu/Debian
sudo apt install texlive-full

# Windows
# Instalar MiKTeX: https://miktex.org/download
```

### Citações não aparecem no output

1. Verifica que a key existe em `references.bib`:
   ```bash
   grep "@.*{sua_key" references.bib
   ```

2. Verifica sintaxe no documento: `[@key]` com **espaço antes** da citação:
   - ✅ `texto [@key]`
   - ❌ `texto[@key]`

### LaTeX compilation errors

- Verifica `output/Documento_Cannabis.log` para detalhes
- Problema comum: Caracteres Unicode não suportados → remover ou escapar

## 📚 Referências Técnicas

- **Pandoc Manual**: https://pandoc.org/MANUAL.html
- **Pandoc Citations**: https://pandoc.org/MANUAL.html#citations
- **BibTeX Format**: http://www.bibtex.org/Format/
- **CSL Styles**: https://citationstyles.org/

## ✅ Validação

Para garantir qualidade do output:

```bash
# Build completo
bash scripts/build.sh

# Verifica outputs gerados
ls -lh output/

# Abre PDFs para verificação visual
open output/Documento_Cannabis.pdf  # macOS
xdg-open output/Documento_Cannabis.pdf  # Linux
```

## 🤝 Contribuir

1. Edita [`documento.md`](documento.md) para mudanças de conteúdo
2. Edita [`references.bib`](references.bib) para novas referências
3. Testa build: `bash scripts/build.sh`
4. Commit apenas ficheiros fonte (não outputs em `output/`)

---

**Gerado por**: Pandoc + Bash
**Última atualização**: Janeiro 2026

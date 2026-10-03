# Fonte única para PDF, DOCX e site: plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Gerar PDF, DOCX e um site pesquisável a partir de `chapters/*.md` e `references.bib`, com IDs de secção estáveis e botões para contribuir.

**Architecture:** Três scripts de build partilham `scripts/common.sh`. O site é uma única execução do Pandoc em modo `chunkedhtml` com template próprio e um filtro Lua que acrescenta as ligações "Levantar questão" e "Sugerir alteração" a cada secção. Pagefind indexa o HTML. `scripts/heading_ids.py` gera e verifica os IDs, e o CI corre-o em PRs.

**Tech Stack:** Bash, Pandoc 3.x (`chunkedhtml`, Lua filters, citeproc), xelatex, Python 3 (só biblioteca standard, testes com `unittest`), Pagefind (via `npx` em CI), GitHub Actions e GitHub Pages.

**Spec:** `docs/adr/0001-fonte-unica-pdf-e-site.md`

## Global Constraints

- `chapters/` mantém o nome; a única fonte de conteúdo é `chapters/[0-9]*.md` mais `references.bib`.
- Mesmos argumentos do Pandoc de hoje no PDF e no DOCX: `--citeproc`, `--csl ieee.csl`, `--number-sections`, `--toc`, `--variable lang=pt-PT`, `--resource-path=".:assets/diagrams"`.
- A limpeza específica do PDF (emojis, CO₂, espaço antes de citações) fica só em `build-pdf.sh`.
- `scripts/build.sh` continua a aceitar `pdf` e `docx`; sem argumentos constrói só PDF e DOCX (o `build_state.py` depende disto). O site constrói-se com o argumento `site`.
- Site: Pandoc 3.0 ou superior. PDF e DOCX continuam a funcionar com o Pandoc que já têm.
- Python só com a biblioteca standard. Sem dependências novas de runtime; Pagefind só é invocado no build do site.
- Todo o texto visível em pt-PT.
- Identidade, licença e governação (passo 6 do ADR) e a fase 2 (formulário com backend) estão **fora deste plano**; as perguntas em aberto do ADR continuam abertas. O subtítulo "Documento de Posição — LIVRE" em `chapters/00-metadata.md` não se altera aqui.
- Os diagramas só são redesenhados se o Bruno o pedir; fora de âmbito.
- Commits locais com o trailer `Co-Authored-By: Claude Code <noreply@anthropic.com>`. Nada de `git push`, PR, nem alterações às definições do repo no GitHub sem o Bruno pedir.

## Review Focus

1. Títulos com acentos, travessões, números à frente ou formatação (`*...*`) geram o mesmo ID que o Pandoc gera sozinho, para que os links e o `.tex` não mudem. Teste em Task 4.
2. Dois títulos iguais (em capítulos diferentes) recebem IDs distintos (`riscos`, `riscos-1`) e estáveis. Teste em Task 4.
3. Ligações internas `](#id)` que apontam para IDs inexistentes são detectadas e listadas, não ignoradas. Hoje existem links assim. Teste em Task 4.
4. Reconstruir o site com uma pasta `output/site/` antiga não deixa páginas obsoletas. Teste em Task 5.
5. IDs com acentos ou pontos (`5.5-estratégia-de-negociação-em-3-níveis`) saem correctamente codificados nos URLs de Issue e de edição. Teste em Task 6.

---

## File Structure

| Ficheiro | Responsabilidade |
|---|---|
| `scripts/common.sh` (novo) | Caminhos, recolha de capítulos, ficheiro temporário seguro, verificação da versão do Pandoc |
| `scripts/build-pdf.sh`, `scripts/build-docx.sh` (alterados) | Só o que é específico de cada formato |
| `scripts/build-site.sh` (novo) | Site HTML mais pesquisa |
| `scripts/build.sh` (alterado) | Aceita `site` |
| `scripts/heading_ids.py` (novo) | Gerar, verificar, bloquear e exportar IDs de secção |
| `site/template.html`, `site/site.css`, `site/section-actions.lua` (novos) | Aspecto do site e botões por secção |
| `docs/heading-ids.lock` (novo) | IDs já publicados que não podem desaparecer |
| `tests/test_heading_ids.py`, `tests/test_site_actions.py`, `tests/test_site_build.py` (novos) | Testes `unittest` |
| `.github/ISSUE_TEMPLATE/*.yml` (novos) | Três formulários de Issue |
| `.github/workflows/ci.yml` (novo), `site.yml` (novo), `auto-release.yml`, `manual-release.yml` (alterados) | CI em PRs, publicação do site, releases |

---

### Task 1: Ramo, ADR no git e linha de base

**Files:**
- Commit: `docs/adr/0001-fonte-unica-pdf-e-site.md`, este plano
- Criar fora do repo: `/tmp/baseline/pdf.tex`, `/tmp/baseline/docx.sha`

**Interfaces:**
- Produces: `/tmp/baseline/pdf.tex` e `/tmp/baseline/docx.sha`, comparados nas Tasks 2, 3 e 4.

- [ ] **Step 1: Criar o ramo e commitar ADR e plano**

```bash
cd /Users/bruno/Projects/cannabis-legalization
git checkout -b feat/fonte-unica-pdf-site
git add docs/adr/0001-fonte-unica-pdf-e-site.md docs/superpowers/plans/2026-10-03-fonte-unica-pdf-e-site.md
git commit -m "docs: ADR 0001 (fonte única para PDF, DOCX e site) e plano de implementação" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

Expected: commit criado; `git status --short` vazio.

- [ ] **Step 2: Instalar o Pandoc e confirmar a versão**

```bash
brew install pandoc
pandoc --version | head -1
```

Expected: `pandoc 3.x`. Se for 2.x, parar e avisar o Bruno (o site exige 3.0 ou superior). O `xelatex` não está instalado nesta máquina (`/Library/TeX/texbin/xelatex` não existe), por isso o PDF só se compila em CI; localmente verifica-se o `.tex`.

- [ ] **Step 3: Capturar a linha de base com os scripts actuais**

```bash
mkdir -p /tmp/baseline
bash scripts/build-pdf.sh || true
cp output/Regulacao_Cannabis_Portugal.tex /tmp/baseline/pdf.tex
bash scripts/build-docx.sh
unzip -p output/Regulacao_Cannabis_Portugal.docx word/document.xml | shasum -a 256 > /tmp/baseline/docx.sha
ls -l /tmp/baseline
```

Expected: `build-pdf.sh` termina com "PDF não foi gerado" (sem xelatex), o que é esperado, mas o `.tex` foi copiado. `pdf.tex` e `docx.sha` existem e não estão vazios.

---

### Task 2: Remover código sem uso e ficheiros obsoletos

**Files:**
- Apagar: `data/`, `scripts/fetch_client.py`, `scripts/response_mapper.py`, `scripts/mermaid_svg.py`, `scripts/migrate_icad_stats.py`, `scripts/migrate_raw_icad_stats.py`, `scripts/migrate_roles.py`, `tests/test_fetch_client.py`, `tests/test_response_mapper.py`, `tests/test_mermaid_svg.py`, `assets/formatted_doc.pdf`, `assets/templates/csl/apa.csl`
- Modificar: `.gitignore`, `chapters/17-referencias.md`, `assets/templates/template.tex` (3 comentários)
- Untrack: `.claude/settings.local.json`

**Interfaces:**
- Consumes: linha de base da Task 1.
- Produces: repo sem código morto. `build_state.py` e `tests/test_build_state.py` ficam (pergunta em aberto no ADR).

- [ ] **Step 1: Confirmar que os números do ICAD já estão nos capítulos**

```bash
python3 - <<'EOF'
import json, pathlib
text = " ".join(p.read_text(encoding="utf-8") for p in sorted(pathlib.Path("chapters").glob("*.md")))
nums = set()
def walk(o):
    if isinstance(o, dict): [walk(v) for v in o.values()]
    elif isinstance(o, list): [walk(v) for v in o]
    elif isinstance(o, (int, float)) and not isinstance(o, bool) and o >= 100: nums.add(o)
for f in ["icad_stats_initial.json", "raw_icad_stats_initial.json", "roles_initial.json"]:
    walk(json.load(open("data/" + f, encoding="utf-8")))
def forms(n):
    s = str(int(n)) if float(n).is_integer() else str(n)
    return {s, f"{int(n):,}".replace(",", ".") if float(n).is_integer() else s, f"{int(n):,}".replace(",", " ") if float(n).is_integer() else s}
missing = [n for n in sorted(nums) if not any(f in text for f in forms(n))]
print("números >= 100:", len(nums), "| sem correspondência nos capítulos:", missing)
EOF
```

Expected: lista de números sem correspondência. **Se a lista contiver estatísticas reais (não IDs ou identificadores), parar e mostrá-la ao Bruno**: a decisão de apagar assumia que os dados já estão no documento. Se a lista estiver vazia ou só tiver identificadores, continuar.

- [ ] **Step 2: Confirmar que nada mais importa o código a apagar**

```bash
grep -rn -E "fetch_client|response_mapper|mermaid_svg|migrate_|icad_stats_schema|raw_icad_schema|roles_schema" --exclude-dir=.git --exclude-dir=docs . | grep -v -E "^./(scripts/(fetch_client|response_mapper|mermaid_svg|migrate_[a-z_]+)\.py|tests/test_(fetch_client|response_mapper|mermaid_svg)\.py|data/)"
```

Expected: sem saída. Se aparecer alguma linha (por exemplo no README), anotá-la; é tratada na Task 8.

- [ ] **Step 3: Apagar**

```bash
git rm -r data
git rm scripts/fetch_client.py scripts/response_mapper.py scripts/mermaid_svg.py scripts/migrate_icad_stats.py scripts/migrate_raw_icad_stats.py scripts/migrate_roles.py
git rm tests/test_fetch_client.py tests/test_response_mapper.py tests/test_mermaid_svg.py
git rm assets/formatted_doc.pdf assets/templates/csl/apa.csl
git rm --cached .claude/settings.local.json
```

- [ ] **Step 4: Ignorar as definições locais do Claude**

Acrescentar ao fim de `.gitignore`:

```
# Definições locais do Claude Code
.claude/settings.local.json
```

- [ ] **Step 5: Limpar o stub das referências**

Substituir o conteúdo de `chapters/17-referencias.md` por (o título é onde o citeproc coloca a bibliografia):

```markdown
# Referências
```

- [ ] **Step 6: Tirar a referência ao PDF apagado nos comentários do template**

Em `assets/templates/template.tex`, alterar as três linhas:

- `% Colors (matching formatted_doc.pdf exactly)` para `% Colors`
- `% Headers and footers (gray #666666 matching formatted_doc.docx)` para `% Headers and footers (gray #666666)`
- `% Title page (matching formatted_doc.pdf layout exactly)` para `% Title page`

- [ ] **Step 7: Verificar que o output não mudou**

```bash
bash scripts/build-pdf.sh || true
diff /tmp/baseline/pdf.tex output/Regulacao_Cannabis_Portugal.tex && echo "TEX IGUAL"
bash scripts/build-docx.sh
unzip -p output/Regulacao_Cannabis_Portugal.docx word/document.xml | shasum -a 256 | diff - /tmp/baseline/docx.sha && echo "DOCX IGUAL"
```

Expected: `TEX IGUAL` e `DOCX IGUAL`. Qualquer diferença é um bug desta task.

- [ ] **Step 8: Commit**

```bash
git add -A
git status --short
git commit -m "chore: remove código e ficheiros sem uso; deixa de versionar settings locais" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

Expected: `git status --short` antes do commit mostra apenas apagamentos, o `.gitignore`, `17-referencias.md`, `template.tex` e o untrack de `.claude/settings.local.json`.

---

### Task 3: `common.sh` e deduplicação dos scripts

**Files:**
- Criar: `scripts/common.sh`
- Modificar: `scripts/build-pdf.sh`, `scripts/build-docx.sh`

**Interfaces:**
- Produces (para a Task 5): variáveis `PROJECT_DIR`, `CHAPTERS_DIR`, `OUTPUT_DIR`, `BIB_FILE`, `CSL_FILE`, `OUTPUT_BASENAME`, `PANDOC_FROM`; funções `gather_sources` (preenche `SOURCE_FILES`), `require_pandoc <major>`, `make_temp_md` (define `TEMP_MD`, apaga-o ao sair).

- [ ] **Step 1: Criar `scripts/common.sh`**

```bash
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
```

(`mktemp` no macOS exige que os `X` fiquem no fim do modelo, por isso o ficheiro não tem extensão; o Pandoc recebe `--from` explícito.)

- [ ] **Step 2: Reescrever `scripts/build-docx.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

OUTPUT_DOCX="$OUTPUT_DIR/$OUTPUT_BASENAME.docx"

mkdir -p "$OUTPUT_DIR"
gather_sources
require_pandoc 2

if [[ ! -f "$CSL_FILE" ]]; then
    echo "❌ CSL style not found: $CSL_FILE" >&2
    exit 1
fi

echo "📄 Convertendo Markdown → DOCX..."
echo "   Fonte: chapters/ (${#SOURCE_FILES[@]} ficheiros)"
echo "   Destino: $OUTPUT_DOCX"
echo ""

make_temp_md
cat "${SOURCE_FILES[@]}" | sed 's/#heading=/#/' > "$TEMP_MD"

pandoc "$TEMP_MD" \
    --from="$PANDOC_FROM" \
    --to=docx \
    --output="$OUTPUT_DOCX" \
    --toc \
    --toc-depth=3 \
    --number-sections \
    --variable lang=pt-PT \
    --variable toc-title="Índice" \
    --citeproc \
    --bibliography="$BIB_FILE" \
    --csl="$CSL_FILE" \
    --resource-path=".:assets/diagrams" \
    --standalone

echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_DOCX"
```

- [ ] **Step 3: Reescrever `scripts/build-pdf.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail

export PATH="/Library/TeX/texbin:$PATH"

source "$(dirname "${BASH_SOURCE[0]}")/common.sh"

TEMPLATE_TEX="$PROJECT_DIR/assets/templates/template.tex"
OUTPUT_PDF="$OUTPUT_DIR/$OUTPUT_BASENAME.pdf"
OUTPUT_TEX="$OUTPUT_DIR/$OUTPUT_BASENAME.tex"

mkdir -p "$OUTPUT_DIR"
gather_sources
require_pandoc 2

echo "📄 Convertendo Markdown → LaTeX → PDF..."
echo "   Fonte: chapters/ (${#SOURCE_FILES[@]} ficheiros)"
echo "   Template: $TEMPLATE_TEX"
echo "   Destino: $OUTPUT_PDF"
echo ""

# Remove emojis e CO₂ (a fonte do PDF não os tem), normaliza espaço antes de citações
make_temp_md
cat "${SOURCE_FILES[@]}" | \
sed 's/#heading=/#/' | \
sed 's/⚠️//g' | \
sed 's/✅//g' | \
sed 's/❌//g' | \
sed 's/CO₂/CO2/g' | \
sed 's/ {-}$//' | \
sed 's/\[@/ \[@/g' | \
sed 's/  \[@/ \[@/g' > "$TEMP_MD"

echo "📝 Passo 1/2: Convertendo Markdown → LaTeX..."
pandoc "$TEMP_MD" \
    --from="$PANDOC_FROM" \
    --to=latex \
    --output="$OUTPUT_TEX" \
    --template="$TEMPLATE_TEX" \
    --variable lang=pt-PT \
    --resource-path=".:assets/diagrams" \
    --number-sections \
    --toc \
    --toc-depth=3 \
    --standalone \
    --citeproc \
    --csl="$CSL_FILE" \
    --metadata link-citations=true \
    --bibliography="$BIB_FILE"

echo "✅ LaTeX gerado: $OUTPUT_TEX"

echo "📝 Passo 2/2: Compilando LaTeX → PDF..."
cd "$OUTPUT_DIR"

if command -v xelatex &> /dev/null; then
    LATEX_CMD="xelatex"
else
    LATEX_CMD="pdflatex"
fi
echo "   Usando: $LATEX_CMD"

for pass in 1 2 3; do
    $LATEX_CMD -interaction=nonstopmode "$OUTPUT_BASENAME.tex" 2>&1 | tail -20 || true
    echo "   Compilação $pass/3 completa"
done

if [[ ! -f "$OUTPUT_BASENAME.pdf" ]]; then
    echo "❌ ERRO: PDF não foi gerado!"
    grep -A5 "^!" "$OUTPUT_BASENAME.log" 2>/dev/null || echo "   (sem log disponível)"
    exit 1
fi

rm -f *.aux *.log *.out *.toc

FILE_SIZE=$(ls -lh "$OUTPUT_PDF" | awk '{print $5}')
echo ""
echo "✅ Conversão completa!"
echo "   Ficheiro: $OUTPUT_PDF"
echo "   Tamanho: $FILE_SIZE"
```

- [ ] **Step 4: Verificar paridade com a linha de base**

```bash
bash scripts/build-pdf.sh || true
diff /tmp/baseline/pdf.tex output/Regulacao_Cannabis_Portugal.tex && echo "TEX IGUAL"
bash scripts/build-docx.sh
unzip -p output/Regulacao_Cannabis_Portugal.docx word/document.xml | shasum -a 256 | diff - /tmp/baseline/docx.sha && echo "DOCX IGUAL"
ls /tmp/doc-clean-temp.md 2>&1 | head -1
```

Expected: `TEX IGUAL`, `DOCX IGUAL`, e o último comando diz que `/tmp/doc-clean-temp.md` não existe (já não é usado). Confirmar também que não ficou nenhum `cannabis-doc.*` em `${TMPDIR:-/tmp}`: `ls "${TMPDIR:-/tmp}"/cannabis-doc.* 2>&1 | head -1` deve dizer "No such file".

- [ ] **Step 5: Commit**

```bash
git add scripts/common.sh scripts/build-pdf.sh scripts/build-docx.sh
git commit -m "refactor: scripts de build partilham common.sh e usam ficheiro temporário seguro" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

---

### Task 4: IDs estáveis nas secções (ferramenta, testes e aplicação)

**Files:**
- Criar: `scripts/heading_ids.py`, `tests/test_heading_ids.py`, `docs/heading-ids.lock`
- Modificar: `chapters/*.md` (IDs acrescentados; ligações quebradas corrigidas)

**Interfaces:**
- Produces (para as Tasks 6 e 7): CLI `python3 scripts/heading_ids.py {check,fix,lock,meta}`; `meta` escreve JSON `{"repo": str, "sectionmap": {id: "chapters/NN-x.md"}}`; funções `slugify(text) -> str`, `scan(chapters_dir)`, `assign_missing(headings, anchors)`, `check(chapters_dir, lock_file) -> list[str]`.

- [ ] **Step 1: Escrever os testes que falham** — `tests/test_heading_ids.py`

```python
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import heading_ids as hi  # noqa: E402


def make_chapters(files):
    root = Path(tempfile.mkdtemp())
    (root / "chapters").mkdir()
    for name, text in files.items():
        (root / "chapters" / name).write_text(text, encoding="utf-8")
    return root


class SlugifyTest(unittest.TestCase):
    def test_cases(self):
        cases = {
            "Impacto no consumo juvenil": "impacto-no-consumo-juvenil",
            "3.5 Impacto": "impacto",
            "Tailândia (2022–2026): o chicote político": "tailândia-20222026-o-chicote-político",
            "Idade 21 vs. Desenvolvimento — Transparência": "idade-21-vs.-desenvolvimento--transparência",
            "Autocultivo regulado *(proposta de compromisso)*": "autocultivo-regulado-proposta-de-compromisso",
            "[link](http://x.pt) texto": "link-texto",
            "2025": "section",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(hi.slugify(text), expected)


class ScanAndAssignTest(unittest.TestCase):
    def test_fenced_code_is_ignored(self):
        root = make_chapters({"01-a.md": "# A\n\n```bash\n# comentário\n```\n"})
        headings, _, _ = hi.scan(root / "chapters")
        self.assertEqual([h.text for h in headings], ["A"])

    def test_attribute_block_without_id_is_rejected(self):
        root = make_chapters({"01-a.md": "# A {.unnumbered}\n"})
        with self.assertRaises(ValueError):
            hi.scan(root / "chapters")

    def test_duplicate_titles_get_distinct_stable_ids(self):
        root = make_chapters({"01-a.md": "# Riscos\n", "02-b.md": "# Riscos\n\n## Riscos\n"})
        headings, anchors, _ = hi.scan(root / "chapters")
        new = hi.assign_missing(headings, anchors)
        self.assertEqual([new[i] for i in sorted(new)], ["riscos", "riscos-1", "riscos-2"])

    def test_explicit_ids_are_kept_and_reserved(self):
        root = make_chapters({"01-a.md": "# Um {#riscos}\n\n## Riscos\n"})
        headings, anchors, _ = hi.scan(root / "chapters")
        new = hi.assign_missing(headings, anchors)
        self.assertEqual(list(new.values()), ["riscos-1"])

    def test_fix_is_idempotent(self):
        root = make_chapters({"01-a.md": "# A\n\n## B\n\ntexto\n"})
        hi.fix(root / "chapters")
        first = (root / "chapters" / "01-a.md").read_text(encoding="utf-8")
        self.assertEqual(first, "# A {#a}\n\n## B {#b}\n\ntexto\n")
        hi.fix(root / "chapters")
        self.assertEqual((root / "chapters" / "01-a.md").read_text(encoding="utf-8"), first)


class CheckTest(unittest.TestCase):
    def test_reports_missing_ids(self):
        root = make_chapters({"01-a.md": "# A\n"})
        problems = hi.check(root / "chapters", root / "no.lock")
        self.assertTrue(any("sem ID" in p for p in problems))

    def test_reports_duplicate_ids(self):
        root = make_chapters({"01-a.md": "# A {#x}\n\n## B {#x}\n"})
        problems = hi.check(root / "chapters", root / "no.lock")
        self.assertTrue(any("duplicado" in p for p in problems))

    def test_reports_broken_internal_links(self):
        root = make_chapters({"01-a.md": "# A {#a}\n\nVer [isto](#nao-existe) e [aquilo](#a).\n"})
        problems = hi.check(root / "chapters", root / "no.lock")
        self.assertEqual(len([p for p in problems if "quebrada" in p]), 1)
        self.assertTrue(any("#nao-existe" in p for p in problems))

    def test_link_to_level4_auto_id_is_valid(self):
        root = make_chapters({"01-a.md": "# A {#a}\n\n#### Detalhe fino\n\nVer [x](#detalhe-fino).\n"})
        self.assertEqual(hi.check(root / "chapters", root / "no.lock"), [])

    def test_locked_id_must_survive(self):
        root = make_chapters({"01-a.md": "# A {#novo}\n"})
        lock = root / "lock"
        lock.write_text("antigo\nnovo\n", encoding="utf-8")
        problems = hi.check(root / "chapters", lock)
        self.assertEqual(len([p for p in problems if "desapareceu" in p]), 1)

    def test_anchor_span_keeps_locked_id_alive(self):
        root = make_chapters({"01-a.md": '# A {#novo}\n<span id="antigo"></span>\n'})
        lock = root / "lock"
        lock.write_text("antigo\nnovo\n", encoding="utf-8")
        self.assertEqual(hi.check(root / "chapters", lock), [])


class MetaTest(unittest.TestCase):
    def test_sectionmap_points_to_chapter_files(self):
        root = make_chapters({"01-a.md": "# A {#a}\n", "02-b.md": "# B {#b}\n"})
        meta = hi.meta(root / "chapters", "dono/repo")
        self.assertEqual(meta["repo"], "dono/repo")
        self.assertEqual(meta["sectionmap"], {"a": "chapters/01-a.md", "b": "chapters/02-b.md"})


@unittest.skipUnless(shutil.which("pandoc"), "pandoc não instalado")
class PandocParityTest(unittest.TestCase):
    def test_slugs_match_pandoc_auto_identifiers(self):
        titles = [
            "Impacto no consumo juvenil",
            "Tailândia (2022–2026): o chicote político",
            "Idade 21 vs. Desenvolvimento — Transparência",
            "Autocultivo regulado *(proposta de compromisso)*",
            "3.5 Estratégia de Negociação em 3 Níveis",
        ]
        md = "\n\n".join(f"## {t}" for t in titles) + "\n"
        html = subprocess.run(
            ["pandoc", "--from", "markdown", "--to", "html"],
            input=md, capture_output=True, text=True, check=True,
        ).stdout
        pandoc_ids = re.findall(r'<h2 id="([^"]+)"', html)
        self.assertEqual(pandoc_ids, [hi.slugify(t) for t in titles])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Correr e ver falhar**

Run: `python3 -m unittest discover -s tests -p 'test_heading_ids.py' -v`
Expected: erro de importação (`ModuleNotFoundError: No module named 'heading_ids'`).

- [ ] **Step 3: Implementar `scripts/heading_ids.py`**

```python
#!/usr/bin/env python3
"""IDs estáveis de secção: gerar, verificar, bloquear e exportar."""
import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = PROJECT_DIR / "chapters"
LOCK_FILE = PROJECT_DIR / "docs" / "heading-ids.lock"
REQUIRED_MAX_LEVEL = 3

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ATTR_RE = re.compile(r"\s*\{([^}]*)\}\s*$")
ID_IN_ATTR_RE = re.compile(r"(?:^|\s)#([^\s}]+)")
ANCHOR_RE = re.compile(r'<(?:span|a)\s[^>]*\bid="([^"]+)"')
LINK_RE = re.compile(r"\]\(#([^)\s]+)\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


@dataclass
class Heading:
    file: Path
    line: int
    level: int
    text: str
    id: "str | None"


def slugify(text):
    """Mesmo algoritmo que o Pandoc usa para identificadores automáticos."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[\^[^\]]*\]", "", text)
    text = re.sub(r"[*`~]", "", text)
    text = re.sub(r"\s+", " ", text.strip()).lower()
    text = re.sub(r"[^\w.\- ]", "", text).replace(" ", "-")
    first_letter = re.search(r"[^\W\d_]", text)
    return text[first_letter.start():] if first_letter else "section"


def chapter_files(chapters_dir):
    return sorted(Path(chapters_dir).glob("[0-9]*.md"))


def scan(chapters_dir):
    headings, anchors, links = [], set(), []
    for path in chapter_files(chapters_dir):
        in_fence = False
        for i, raw in enumerate(path.read_text(encoding="utf-8").split("\n")):
            if FENCE_RE.match(raw):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            anchors.update(ANCHOR_RE.findall(raw))
            links.extend((path, i, target) for target in LINK_RE.findall(raw))
            match = HEADING_RE.match(raw)
            if not match:
                continue
            level, body, hid = len(match.group(1)), match.group(2), None
            attrs = ATTR_RE.search(body)
            if attrs:
                id_match = ID_IN_ATTR_RE.search(attrs.group(1))
                if not id_match:
                    raise ValueError(f"{path.name}:{i + 1}: bloco de atributos sem ID não suportado: {raw}")
                hid = id_match.group(1)
                body = body[: attrs.start()]
            headings.append(Heading(path, i, level, body.strip(), hid))
    return headings, anchors, links


def assign_missing(headings, anchors):
    """Devolve {índice do título: novo ID} só para títulos de nível <= 3 sem ID."""
    used = {h.id for h in headings if h.id} | set(anchors)
    new = {}
    for idx, h in enumerate(headings):
        if h.id:
            continue
        base = slugify(h.text)
        candidate, n = base, 0
        while candidate in used:
            n += 1
            candidate = f"{base}-{n}"
        used.add(candidate)
        if h.level <= REQUIRED_MAX_LEVEL:
            new[idx] = candidate
    return new


def present_ids(headings, anchors):
    ids = {h.id for h in headings if h.id} | set(anchors)
    ids |= {slugify(h.text) for h in headings if not h.id}
    return ids


def fix(chapters_dir):
    headings, anchors, _ = scan(chapters_dir)
    new = assign_missing(headings, anchors)
    by_file = {}
    for idx, hid in new.items():
        by_file.setdefault(headings[idx].file, {})[headings[idx].line] = hid
    for path, edits in by_file.items():
        lines = path.read_text(encoding="utf-8").split("\n")
        for line_no, hid in edits.items():
            lines[line_no] = f"{lines[line_no].rstrip()} {{#{hid}}}"
        path.write_text("\n".join(lines), encoding="utf-8")
    return len(new)


def check(chapters_dir, lock_file):
    headings, anchors, links = scan(chapters_dir)
    problems = []
    seen = set()
    for h in headings:
        if h.level <= REQUIRED_MAX_LEVEL and not h.id:
            problems.append(f"{h.file.name}:{h.line + 1}: título sem ID: {h.text}")
        if h.id:
            if h.id in seen:
                problems.append(f"{h.file.name}:{h.line + 1}: ID duplicado: {h.id}")
            seen.add(h.id)
    present = present_ids(headings, anchors)
    for path, i, target in links:
        if target not in present:
            problems.append(f"{path.name}:{i + 1}: ligação interna quebrada: #{target}")
    lock_file = Path(lock_file)
    if lock_file.exists():
        for locked in lock_file.read_text(encoding="utf-8").split():
            if locked not in present:
                problems.append(
                    f'ID publicado desapareceu: {locked} (mantém <span id="{locked}"></span> junto do novo título)'
                )
    return problems


def lock(chapters_dir, lock_file):
    headings, anchors, _ = scan(chapters_dir)
    ids = sorted({h.id for h in headings if h.id} | set(anchors))
    Path(lock_file).write_text("\n".join(ids) + "\n", encoding="utf-8")
    return len(ids)


def meta(chapters_dir, repo):
    headings, _, _ = scan(chapters_dir)
    root = Path(chapters_dir).parent
    sectionmap = {
        h.id: h.file.relative_to(root).as_posix()
        for h in headings
        if h.id and h.level <= REQUIRED_MAX_LEVEL
    }
    return {"repo": repo, "sectionmap": sectionmap}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("fix")
    sub.add_parser("lock")
    meta_parser = sub.add_parser("meta")
    meta_parser.add_argument("--repo", default="bcamarneiro/cannabis-legalization")
    meta_parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)

    if args.cmd == "check":
        problems = check(CHAPTERS_DIR, LOCK_FILE)
        for p in problems:
            print(p)
        print(f"{len(problems)} problema(s)")
        return 1 if problems else 0
    if args.cmd == "fix":
        print(f"{fix(CHAPTERS_DIR)} ID(s) acrescentados")
    elif args.cmd == "lock":
        print(f"{lock(CHAPTERS_DIR, LOCK_FILE)} ID(s) bloqueados em {LOCK_FILE}")
    elif args.cmd == "meta":
        Path(args.out).write_text(
            json.dumps(meta(CHAPTERS_DIR, args.repo), ensure_ascii=False, indent=1), encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Correr os testes e ver passar**

Run: `python3 -m unittest discover -s tests -p 'test_heading_ids.py' -v`
Expected: todos passam (o teste de paridade com o Pandoc corre porque o Pandoc foi instalado na Task 1). Se `PandocParityTest` falhar, corrigir `slugify` até coincidir com o Pandoc; não relaxar o teste.

- [ ] **Step 5: Ver o estado real dos capítulos**

Run: `python3 scripts/heading_ids.py check | tail -30`
Expected: falha, com cerca de 224 "título sem ID" e algumas "ligação interna quebrada" (por exemplo `#3.5-impacto-no-consumo-juvenil` não é gerado pelo Pandoc, mas pode existir como ID explícito; `#financiamento`, `#gap-mercado` e `#sensitivity-roi` precisam de ser verificados).

- [ ] **Step 6: Acrescentar os IDs**

```bash
python3 scripts/heading_ids.py fix
git diff --stat | tail -3
```

Expected: `~224 ID(s) acrescentados`; o diff só acrescenta ` {#...}` ao fim de linhas de título.

- [ ] **Step 7: Verificar que o documento não mudou**

```bash
bash scripts/build-pdf.sh || true
diff /tmp/baseline/pdf.tex output/Regulacao_Cannabis_Portugal.tex && echo "TEX IGUAL"
```

Expected: `TEX IGUAL`. Como os IDs gerados seguem o algoritmo do Pandoc, o `.tex` não pode mudar. Se houver diferenças, cada uma tem de ser explicada: só são aceitáveis em títulos cujo ID automático colidia com um ID explícito posterior (o Pandoc geraria um ID duplicado, a ferramenta evita-o). Qualquer outra é um bug de `slugify`.

- [ ] **Step 8: Corrigir as ligações internas quebradas**

Run: `python3 scripts/heading_ids.py check`
Expected: só linhas "ligação interna quebrada: #...". Para cada uma, abrir o ficheiro na linha indicada, encontrar o título que o autor queria apontar (`grep -n` pelo tema) e trocar o `#alvo` pelo ID real dele. Se não existir nenhum título adequado, **não inventar**: listar as ligações e perguntar ao Bruno. Voltar a correr `check` até dar `0 problema(s)`.

- [ ] **Step 9: Bloquear os IDs e confirmar**

```bash
python3 scripts/heading_ids.py lock
python3 scripts/heading_ids.py check
```

Expected: `N ID(s) bloqueados em .../docs/heading-ids.lock`, e depois `0 problema(s)`.

- [ ] **Step 10: Commit**

```bash
git add scripts/heading_ids.py tests/test_heading_ids.py docs/heading-ids.lock chapters
git commit -m "feat: IDs estáveis em todas as secções, com verificação e bloqueio dos já publicados" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

---

### Task 5: Site com Pandoc `chunkedhtml` e pesquisa

**Files:**
- Criar: `scripts/build-site.sh`, `site/template.html`, `site/site.css`, `tests/test_site_build.py`
- Modificar: `scripts/build.sh`

**Interfaces:**
- Consumes: `common.sh` (Task 3); `heading_ids.py meta` (Task 4).
- Produces: `output/site/` plano (um `.html` por capítulo mais `index.html`), `site.css` na raiz; variável `SKIP_PAGEFIND=1` salta a indexação; `build.sh site`.

- [ ] **Step 1: Spike de 10 minutos (descartável) para confirmar o `chunkedhtml`**

```bash
cd /Users/bruno/Projects/cannabis-legalization
cat chapters/[0-9]*.md > /tmp/spike.md
pandoc /tmp/spike.md --from=markdown+footnotes+pipe_tables+autolink_bare_uris --to=chunkedhtml \
  --split-level=1 --chunk-template="%i.html" --citeproc --csl=ieee.csl --bibliography=references.bib \
  --number-sections --toc --standalone -V lang=pt-PT -o /tmp/spike.zip
unzip -l /tmp/spike.zip | head -30
pandoc -D chunkedhtml > /tmp/default-chunked-template.html
grep -n -E '\$body\$|\$navigation\$|\$prev|\$next|\$up|</head>' /tmp/default-chunked-template.html
```

Expected, para cada ponto, e anotar o resultado nas notas da task:
1. O output é um zip plano (sem subpastas) com `index.html` e uma página por capítulo, com nome igual ao ID do título (`--chunk-template="%i.html"`).
2. As citações `[@...]` aparecem resolvidas e a bibliografia aparece na página das referências.
3. O template por omissão contém `$body$` e as variáveis de navegação.

Se algum destes falhar (por exemplo, se o zip tiver subpastas), parar e ajustar as Steps seguintes (caminhos relativos em `site.css`, `pagefind`) antes de continuar; se não houver `chunkedhtml` utilizável, parar e avisar o Bruno, porque a decisão do ADR depende disto. Apagar `/tmp/spike*` no fim.

- [ ] **Step 2: Escrever o teste que falha** — `tests/test_site_build.py`

```python
import os
import re
import shutil
import subprocess
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SITE = PROJECT / "output" / "site"


def pandoc_major():
    if not shutil.which("pandoc"):
        return 0
    out = subprocess.run(["pandoc", "--version"], capture_output=True, text=True).stdout
    return int(re.search(r"pandoc (\d+)", out).group(1))


@unittest.skipUnless(pandoc_major() >= 3, "precisa de pandoc 3.x")
class SiteBuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        SITE.mkdir(parents=True, exist_ok=True)
        (SITE / "stale.html").write_text("obsoleto", encoding="utf-8")
        env = dict(os.environ, SKIP_PAGEFIND="1")
        subprocess.run(["bash", str(PROJECT / "scripts" / "build-site.sh")], check=True, env=env, cwd=PROJECT)
        cls.pages = sorted(SITE.glob("*.html"))

    def test_stale_pages_are_removed(self):
        self.assertFalse((SITE / "stale.html").exists())

    def test_one_page_per_chapter_plus_index(self):
        self.assertTrue((SITE / "index.html").exists())
        self.assertGreaterEqual(len(self.pages), 17)

    def test_citations_are_resolved(self):
        for page in self.pages:
            self.assertNotIn("[@", page.read_text(encoding="utf-8"), page.name)

    def test_every_page_is_searchable_and_styled(self):
        for page in self.pages:
            html = page.read_text(encoding="utf-8")
            self.assertIn("data-pagefind-body", html, page.name)
            self.assertIn('href="site.css"', html, page.name)
        self.assertTrue((SITE / "site.css").exists())

    def test_version_is_shown(self):
        version = (PROJECT / "VERSION").read_text().strip()
        self.assertIn(version, (SITE / "index.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Correr e ver falhar**

Run: `python3 -m unittest discover -s tests -p 'test_site_build.py' -v`
Expected: falha (`scripts/build-site.sh` não existe).

- [ ] **Step 4: Criar o template a partir do default do Pandoc**

```bash
mkdir -p site
pandoc -D chunkedhtml > site/template.html
```

Editar `site/template.html` com exactamente estas alterações, mantendo tudo o resto:

1. Antes de `</head>`, acrescentar:
   ```html
   <link rel="stylesheet" href="site.css">
   <link href="pagefind/pagefind-ui.css" rel="stylesheet">
   ```
2. Imediatamente depois da abertura de `<body>` (antes de qualquer conteúdo gerado), acrescentar:
   ```html
   <header class="site-header">
     <a class="site-title" href="index.html">Regulação da Cannabis em Portugal</a>
     <div id="search"></div>
   </header>
   ```
3. Envolver `$body$` (e só o corpo) em:
   ```html
   <main id="content" data-pagefind-body>
   $body$
   </main>
   ```
4. Antes de `</body>`, acrescentar:
   ```html
   <footer class="site-footer">
     <p>Versão $version$ · construída em $builddate$ ·
     <a href="https://github.com/bcamarneiro/cannabis-legalization">Código e histórico</a></p>
   </footer>
   <script src="pagefind/pagefind-ui.js"></script>
   <script>window.addEventListener("DOMContentLoaded", function () {
     if (window.PagefindUI) { new PagefindUI({ element: "#search", showSubResults: true }); }
   });</script>
   ```

- [ ] **Step 5: Criar `site/site.css`**

```css
:root { --texto: #1c1c1c; --fundo: #fff; --ligacao: #0b5cad; --suave: #666; }
* { box-sizing: border-box; }
body { margin: 0; font: 18px/1.65 Georgia, "Times New Roman", serif; color: var(--texto); background: var(--fundo); }
a { color: var(--ligacao); }
.site-header, .site-footer { padding: 0.75rem 1.25rem; border-bottom: 1px solid #ddd; }
.site-footer { border-top: 1px solid #ddd; border-bottom: 0; color: var(--suave); font-size: 0.85rem; }
.site-header { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; justify-content: space-between; }
.site-title { font-weight: bold; text-decoration: none; color: var(--texto); }
#content { max-width: 46rem; margin: 0 auto; padding: 1.5rem 1.25rem 3rem; }
#content table { display: block; overflow-x: auto; border-collapse: collapse; }
#content th, #content td { border: 1px solid #ccc; padding: 0.3rem 0.6rem; }
.section-actions { display: flex; gap: 0.9rem; flex-wrap: wrap; margin: -0.4rem 0 1rem; font: 0.8rem/1.2 system-ui, sans-serif; }
.section-actions a { color: var(--suave); }
nav#TOC ul { list-style: none; padding-left: 1rem; }
@media print { .site-header, .site-footer, .section-actions { display: none; } }
```

- [ ] **Step 6: Criar `scripts/build-site.sh`**

```bash
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
cat "${SOURCE_FILES[@]}" | sed 's/#heading=/#/' > "$TEMP_MD"

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

unzip -q "$ZIP" -d "$SITE_DIR"
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
```

(Se o spike do Step 1 mostrar que os caminhos das imagens no HTML são diferentes de `assets/diagrams/...`, ajustar só a cópia final das imagens. Enquanto os capítulos não embebem imagens, é inofensiva.)

- [ ] **Step 7: Criar um filtro Lua provisório para o teste correr**

O filtro real chega na Task 6; para esta task bastar um filtro vazio. Criar `site/section-actions.lua`:

```lua
return {}
```

- [ ] **Step 8: Acrescentar `site` ao `scripts/build.sh`**

Em `scripts/build.sh`: declarar `BUILD_SITE=false` junto de `BUILD_PDF`; acrescentar o caso `site) BUILD_SITE=true ;;` no `case`; no texto de uso acrescentar a linha `echo "  $0 site      # Build apenas o site"`; e a seguir ao bloco "Build DOCX" (no ramo sem reversão) acrescentar:

```bash
    if [[ "$BUILD_SITE" == true ]]; then
        echo "🔨 Building site..."
        bash "$SCRIPT_DIR/build-site.sh"
        echo ""
    fi
```

No ramo `--with-reversion`, antes de chamar `build_state.py`, acrescentar:

```bash
    if [[ "$BUILD_SITE" == true ]]; then
        echo "❌ 'site' não suporta --with-reversion" >&2
        exit 1
    fi
```

Sem argumentos continua a construir só PDF e DOCX.

- [ ] **Step 9: Correr o teste**

Run: `python3 -m unittest discover -s tests -p 'test_site_build.py' -v`
Expected: passa. Ver também a página no browser: `open output/site/index.html` (pesquisa só funciona depois do Pagefind).

- [ ] **Step 10: Testar a pesquisa com Pagefind**

```bash
bash scripts/build.sh site
ls output/site/pagefind | head -3
```

Expected: pasta `pagefind/` com `pagefind-ui.js`. Servir com `python3 -m http.server -d output/site 8000`, abrir `http://localhost:8000` e confirmar que a caixa de pesquisa devolve resultados para "autocultivo". Parar o servidor.

- [ ] **Step 11: Commit**

```bash
git add scripts/build-site.sh scripts/build.sh site tests/test_site_build.py
git commit -m "feat: site HTML a partir dos capítulos (Pandoc chunkedhtml) com pesquisa Pagefind" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

---

### Task 6: Botões por secção e formulários de Issue

**Files:**
- Substituir: `site/section-actions.lua`
- Criar: `tests/test_site_actions.py`, `.github/ISSUE_TEMPLATE/corrigir-erro-ou-fonte.yml`, `propor-alteracao.yml`, `contestar-argumento.yml`, `config.yml`
- Apagar: `.github/ISSUE_TEMPLATE/proposta-nao-tecnica.md`, `vulnerability-fix.md`

**Interfaces:**
- Consumes: metadados `repo` e `sectionmap` (Task 4, via `--metadata-file`).
- Produces: abaixo de cada título de nível 1 a 3 com ID, um bloco `<p class="section-actions">` com três ligações.

- [ ] **Step 1: Escrever o teste que falha** — `tests/test_site_actions.py`

```python
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

LUA = Path(__file__).resolve().parent.parent / "site" / "section-actions.lua"


@unittest.skipUnless(shutil.which("pandoc"), "pandoc não instalado")
class SectionActionsTest(unittest.TestCase):
    def render(self, md, sectionmap):
        meta = Path(tempfile.mkdtemp()) / "meta.json"
        meta.write_text(json.dumps({"repo": "dono/repo", "sectionmap": sectionmap}), encoding="utf-8")
        return subprocess.run(
            ["pandoc", "--from", "markdown", "--to", "html", "--lua-filter", str(LUA), "--metadata-file", str(meta)],
            input=md, capture_output=True, text=True, check=True,
        ).stdout

    def test_links_are_added_under_the_heading(self):
        html = self.render("## Riscos {#riscos}\n\ntexto\n", {"riscos": "chapters/02-ciencia.md"})
        self.assertIn('class="section-actions"', html)
        self.assertIn('href="#riscos"', html)
        self.assertIn("https://github.com/dono/repo/issues/new?template=propor-alteracao.yml&amp;section=riscos", html)
        self.assertIn("https://github.com/dono/repo/edit/main/chapters/02-ciencia.md", html)

    def test_ids_with_accents_and_dots_are_percent_encoded(self):
        html = self.render(
            "## Estratégia {#5.5-estratégia-de-negociação}\n",
            {"5.5-estratégia-de-negociação": "chapters/10-politica.md"},
        )
        self.assertIn("section=5.5-estrat%C3%A9gia-de-negocia%C3%A7%C3%A3o", html)
        self.assertNotIn("section=5.5-estratégia", html)

    def test_level4_and_headings_without_map_entry_get_no_edit_link(self):
        html = self.render("#### Detalhe {#detalhe}\n\n## Sem mapa {#sem-mapa}\n", {})
        self.assertNotIn("section-actions", html.split("Sem mapa")[0])
        self.assertIn("section=sem-mapa", html)
        self.assertNotIn("/edit/main/", html)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Correr e ver falhar**

Run: `python3 -m unittest discover -s tests -p 'test_site_actions.py' -v`
Expected: falha (o filtro está vazio).

- [ ] **Step 3: Implementar `site/section-actions.lua`**

```lua
local repo = ""
local map = {}

local function urlencode(s)
  return (s:gsub("[^%w%-%._~]", function(c)
    return string.format("%%%02X", string.byte(c))
  end))
end

local function read_meta(meta)
  repo = pandoc.utils.stringify(meta.repo or "")
  map = {}
  for id, file in pairs(meta.sectionmap or {}) do
    map[id] = pandoc.utils.stringify(file)
  end
end

local function add_actions(h)
  if h.level > 3 or h.identifier == "" then
    return nil
  end
  local id = h.identifier
  local links = {
    string.format('<a class="permalink" href="#%s">Ligação</a>', id),
    string.format(
      '<a href="https://github.com/%s/issues/new?template=propor-alteracao.yml&section=%s">Levantar questão</a>',
      repo, urlencode(id)),
  }
  if map[id] then
    table.insert(links, string.format(
      '<a href="https://github.com/%s/edit/main/%s">Sugerir alteração</a>', repo, map[id]))
  end
  local block = pandoc.RawBlock("html", '<p class="section-actions">' .. table.concat(links, "") .. "</p>")
  return { h, block }
end

return { { Meta = read_meta }, { Header = add_actions } }
```

(O `&` nos URLs dentro de `RawBlock` é escrito tal e qual; o Pandoc não o reescreve em HTML bruto. O teste espera `&amp;`; se o Pandoc o deixar como `&`, ajustar a asserção do teste e não o filtro, porque ambas as formas são HTML válido num atributo `href`.)

- [ ] **Step 4: Correr os testes**

Run: `python3 -m unittest discover -s tests -p 'test_site_*.py' -v`
Expected: passam, incluindo `test_site_build` (agora com o filtro real). Abrir `output/site/index.html` e uma página de capítulo e confirmar que cada secção mostra as três ligações.

- [ ] **Step 5: Criar os três formulários de Issue**

`.github/ISSUE_TEMPLATE/corrigir-erro-ou-fonte.yml`:

```yaml
name: Corrigir erro ou fonte
description: Encontraste um erro factual, um número errado ou uma fonte que não confirma o texto.
title: "[ERRO] "
labels: ["correcção", "triagem"]
body:
  - type: input
    id: section
    attributes:
      label: Secção
      description: ID da secção (o site preenche isto por ti). Exemplo, pilar-recreativo.
    validations:
      required: true
  - type: textarea
    id: texto_actual
    attributes:
      label: Texto actual
      description: Cola o trecho que está errado.
    validations:
      required: true
  - type: textarea
    id: correccao
    attributes:
      label: O que está errado e qual é a correcção
    validations:
      required: true
  - type: textarea
    id: fonte
    attributes:
      label: Fonte
      description: Ligação, DOI ou referência completa que sustenta a correcção.
    validations:
      required: true
  - type: markdown
    attributes:
      value: "Este pedido fica **público** no GitHub. Podes usar um pseudónimo."
```

`.github/ISSUE_TEMPLATE/propor-alteracao.yml`:

```yaml
name: Propor alteração
description: Sugerir uma melhoria, um acrescento ou uma mudança de proposta.
title: "[PROPOSTA] "
labels: ["proposta", "triagem"]
body:
  - type: input
    id: section
    attributes:
      label: Secção
      description: ID da secção (o site preenche isto por ti).
    validations:
      required: true
  - type: textarea
    id: proposta
    attributes:
      label: O que propões
    validations:
      required: true
  - type: textarea
    id: justificacao
    attributes:
      label: Porquê
      description: Argumentos e evidência. Toda a alteração factual precisa de fonte.
    validations:
      required: true
  - type: input
    id: expertise
    attributes:
      label: Área de especialidade (opcional)
      description: Direito, saúde, economia, activismo, etc.
  - type: markdown
    attributes:
      value: "Este pedido fica **público** no GitHub. Podes usar um pseudónimo."
```

`.github/ISSUE_TEMPLATE/contestar-argumento.yml`:

```yaml
name: Contestar um argumento
description: Discordas do raciocínio ou das conclusões de uma secção.
title: "[CONTESTAÇÃO] "
labels: ["contestação", "triagem"]
body:
  - type: input
    id: section
    attributes:
      label: Secção
      description: ID da secção (o site preenche isto por ti).
    validations:
      required: true
  - type: textarea
    id: argumento
    attributes:
      label: Que argumento contestas
    validations:
      required: true
  - type: textarea
    id: contra
    attributes:
      label: Contra-argumento e evidência
    validations:
      required: true
  - type: markdown
    attributes:
      value: "Este pedido fica **público** no GitHub. Podes usar um pseudónimo."
```

`.github/ISSUE_TEMPLATE/config.yml`:

```yaml
blank_issues_enabled: true
```

- [ ] **Step 6: Apagar os templates antigos e pedir autorização para criar as etiquetas**

```bash
git rm .github/ISSUE_TEMPLATE/proposta-nao-tecnica.md .github/ISSUE_TEMPLATE/vulnerability-fix.md
```

As etiquetas `correcção`, `proposta`, `contestação` e `triagem` têm de existir no GitHub para serem aplicadas. **Não as criar sem o Bruno autorizar** (é uma alteração ao repo remoto): propor-lhe `gh label create "triagem" --repo bcamarneiro/cannabis-legalization` e as restantes.

- [ ] **Step 7: Commit**

```bash
git add site/section-actions.lua tests/test_site_actions.py .github/ISSUE_TEMPLATE
git commit -m "feat: botões 'Levantar questão' e 'Sugerir alteração' por secção e formulários de Issue" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

---

### Task 7: CI em PRs, publicação do site e releases

**Files:**
- Criar: `.github/workflows/ci.yml`, `.github/workflows/site.yml`
- Modificar: `.github/workflows/auto-release.yml`, `.github/workflows/manual-release.yml`
- Untrack: `build/documento.md`

**Interfaces:**
- Consumes: `scripts/build.sh pdf docx site`, `scripts/heading_ids.py check|lock`, `scripts/merge-chapters.sh`.

- [ ] **Step 1: Confirmar que o projecto Vercel não lê `build/documento.md`**

```bash
git ls-files | grep -i -E "vercel|netlify" || echo "sem ficheiros de deploy no repo"
git ls-files | xargs grep -l "build/documento.md" 2>/dev/null
```

Expected: sem ficheiros Vercel no repo; as únicas referências a `build/documento.md` são os workflows e `merge-chapters.sh`. O repo não prova o que o Vercel faz: **pedir ao Bruno que confirme no painel do projecto `cannabis-legalization` que o comando de build e a raiz não dependem de `build/documento.md`** antes do Step 6. Se depender, parar e discutir.

- [ ] **Step 2: Criar `.github/workflows/ci.yml`**

```yaml
name: CI

on:
  pull_request:
    paths:
      - 'chapters/**'
      - 'references.bib'
      - 'scripts/**'
      - 'site/**'
      - 'assets/**'
      - 'tests/**'
      - 'ieee.csl'
      - '.github/workflows/**'

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Pandoc and LaTeX
        run: |
          sudo apt-get update
          sudo apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-latex-extra
          pandoc --version | head -1

      - name: Verify heading IDs and internal links
        run: python3 scripts/heading_ids.py check

      - name: Unit tests
        run: |
          python3 -m unittest discover -s tests -p 'test_heading_ids.py' -v
          python3 -m unittest discover -s tests -p 'test_site_actions.py' -v

      - name: Build PDF, DOCX and site
        run: bash scripts/build.sh pdf docx site

      - name: Site build test
        run: python3 -m unittest discover -s tests -p 'test_site_build.py' -v

      - name: Upload build for review
        uses: actions/upload-artifact@v4
        with:
          name: build
          path: |
            output/*.pdf
            output/*.docx
            output/site
```

- [ ] **Step 3: Criar `.github/workflows/site.yml`**

```yaml
name: Site

on:
  workflow_call:
    inputs:
      ref:
        type: string
        default: main
  workflow_dispatch:
  push:
    branches: [main]
    paths:
      - 'site/**'
      - 'scripts/build-site.sh'
      - 'scripts/common.sh'

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ inputs.ref || 'main' }}

      - name: Install Pandoc
        run: |
          sudo apt-get update
          sudo apt-get install -y pandoc
          pandoc --version | head -1

      - name: Build site
        run: bash scripts/build.sh site

      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: output/site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

Nota: o `ubuntu-latest` actual traz Pandoc 3.1.x; se alguma vez trouxer 2.x, `require_pandoc 3` falha com mensagem clara em vez de gerar um site partido.

- [ ] **Step 4: Alterar `auto-release.yml`**

1. Passo "Commit version bump": antes de `git add VERSION`, gerar o lock e incluí-lo:

```yaml
      - name: Commit version bump and heading lock
        run: |
          python3 scripts/heading_ids.py lock
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add VERSION docs/heading-ids.lock
          git commit -m "chore: Bump version to ${{ steps.version.outputs.version }} [skip ci]" || echo "No changes to commit"
          git push || echo "Nothing to push"
```

2. Substituir o passo "Regenerate documento.md from chapters" por (sem commit):

```yaml
      - name: Generate documento.md (release asset)
        run: bash scripts/merge-chapters.sh
```

3. No passo "Create Release", acrescentar `build/documento.md` à lista `files:` e trocar `[Ver documento fonte](../../blob/main/build/documento.md)` por `[Ver documento fonte](../../tree/main/chapters)`.

4. No fim do ficheiro, depois do job `auto-release`, acrescentar:

```yaml
  site:
    needs: auto-release
    permissions:
      contents: read
      pages: write
      id-token: write
    uses: ./.github/workflows/site.yml
    with:
      ref: main
```

- [ ] **Step 5: Alterar `manual-release.yml`**

Aplicar as alterações 2, 3 e 4 do Step 4 (gerar `documento.md` antes do passo "Create Release", acrescentá-lo aos `files:`, trocar a ligação, e acrescentar o job `site`). A alteração 1 também: gerar e commitar o lock junto do bump (`git add VERSION docs/heading-ids.lock`, mantendo a mensagem actual do commit). No job `site`, `needs: manual-release`.

- [ ] **Step 6: Deixar de versionar `build/documento.md`**

```bash
git rm --cached build/documento.md
git status --short
```

Expected: só `D  build/documento.md` (o ficheiro continua no disco, ignorado por `.gitignore`).

- [ ] **Step 7: Validar a sintaxe dos workflows**

```bash
python3 - <<'EOF'
import sys
try:
    import yaml
except ImportError:
    sys.exit("pyyaml não instalado: validar os YAML por inspecção e pelo primeiro run no GitHub")
for f in ["ci", "site", "auto-release", "manual-release"]:
    yaml.safe_load(open(f".github/workflows/{f}.yml", encoding="utf-8"))
    print(f, "ok")
EOF
```

Expected: `ok` para os quatro, ou a mensagem de que o `yaml` não está instalado (nesse caso, o primeiro run no GitHub é a validação; dizer isso ao Bruno em vez de afirmar que os workflows estão validados).

- [ ] **Step 8: Commit**

```bash
git add .github/workflows build/documento.md
git commit -m "ci: verificação em PRs, publicação do site no Pages, documento.md como anexo de release" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

---

### Task 8: Documentação e fecho

**Files:**
- Modificar: `README.md`, `CONTRIBUTING.md`, `docs/adr/0001-fonte-unica-pdf-e-site.md`

- [ ] **Step 1: Reescrever `README.md`**

Ler o README actual, preservar a descrição do projecto e as ligações que continuam válidas, e substituir as secções de estrutura e de build por (texto final em pt-PT):

```markdown
## Estrutura

    chapters/            ← fonte de verdade (um ficheiro por capítulo)
    references.bib       ← bibliografia (BibTeX), citada como [@chave]
    ieee.csl             ← estilo de citação
    assets/diagrams/     ← diagramas (.mmd e imagem)
    assets/templates/    ← template LaTeX do PDF
    site/                ← template, CSS e filtro do site
    scripts/             ← build (build.sh, build-pdf.sh, build-docx.sh, build-site.sh) e heading_ids.py
    docs/adr/            ← decisões de arquitectura
    docs/TASKS.md        ← tarefas e vulnerabilidades em aberto

## Compilar

Requer Pandoc 3.x; o PDF requer também xelatex.

    bash scripts/build.sh              # PDF e DOCX
    bash scripts/build.sh site         # site (output/site/)
    bash scripts/build.sh pdf docx site

Os resultados ficam em `output/` (PDF e DOCX com o nome `Regulacao_Cannabis_Portugal`).
O PDF, o DOCX e o site saem dos mesmos capítulos e da mesma bibliografia.

## Verificar

    python3 scripts/heading_ids.py check
    python3 -m unittest discover -s tests -p 'test_heading_ids.py'

Todos os títulos até ao nível 3 têm um ID explícito (`{#id}`). Não mudes um ID já publicado:
o `check` falha. Se renomeares um título, mantém o ID antigo com `<span id="id-antigo"></span>`.
```

Remover do README as referências ao `documento.md` na raiz, a `output/Documento_Cannabis.*`, a "2 passes pdflatex" e a `apa.csl`.

- [ ] **Step 2: Actualizar `CONTRIBUTING.md`**

Localizar as secções com `grep -n -i -E "estrutura|workflow|merge-chapters|documento.md" CONTRIBUTING.md`. Substituir o bloco da estrutura do repo pelo bloco "Estrutura" do README, e o fluxo técnico por:

```markdown
## Como contribuir

1. **Sem GitHub avançado:** no site, em cada secção, usa "Levantar questão" (abre um formulário já com a secção preenchida).
2. **Com GitHub:** usa "Sugerir alteração" no site (abre o editor do capítulo) ou faz um fork e edita `chapters/`.
3. Antes de abrir o PR: `python3 scripts/heading_ids.py check`.

## Critérios de aceitação

- Toda a alteração factual traz fonte, acrescentada a `references.bib` e citada como `[@chave]`.
- Não mudes IDs de secção já publicados (o CI falha).
- As propostas e contestações ficam públicas; podes usar pseudónimo.
```

Remover as instruções de `bash scripts/merge-chapters.sh` para compilar (já não faz parte do fluxo) e as referências aos templates de Issue apagados.

- [ ] **Step 3: Marcar o ADR como implementado e anotar os desvios**

Em `docs/adr/0001-fonte-unica-pdf-e-site.md` mudar `- Estado: **proposto** ...` para `- Estado: **aceite; implementado nos passos 1 a 5 (ver docs/superpowers/plans/2026-10-03-fonte-unica-pdf-e-site.md)**` e acrescentar, no fim, uma secção `## Notas de implementação` com: a versão do Pandoc confirmada, o resultado do spike do `chunkedhtml` (Task 5, Step 1), o resultado da verificação do Vercel (Task 7, Step 1), e quaisquer ligações internas que tenham sido corrigidas ou deixadas por decidir (Task 4, Step 8).

- [ ] **Step 4: Verificação final do ramo**

```bash
python3 scripts/heading_ids.py check
python3 -m unittest discover -s tests -p 'test_heading_ids.py' -v
python3 -m unittest discover -s tests -p 'test_site_actions.py' -v
bash scripts/build.sh site
python3 -m unittest discover -s tests -p 'test_site_build.py' -v
bash scripts/build-pdf.sh || true
git status --short
git log --oneline main..HEAD
```

Expected: `0 problema(s)`, todos os testes passam, o site constrói com pesquisa, o `.tex` gera-se (o PDF só em CI), e `git status` está limpo, com uma commit por task. Comparar `output/Regulacao_Cannabis_Portugal.tex` com `/tmp/baseline/pdf.tex` uma última vez: tem de ser igual.

- [ ] **Step 5: Commit**

```bash
git add README.md CONTRIBUTING.md docs/adr/0001-fonte-unica-pdf-e-site.md
git commit -m "docs: README e CONTRIBUTING no novo layout; ADR 0001 marcado como implementado" -m "Co-Authored-By: Claude Code <noreply@anthropic.com>"
```

- [ ] **Step 6: Passos manuais que dependem do Bruno (não executar sozinho)**

Listar ao Bruno, sem os fazer: (1) activar GitHub Pages em Settings → Pages → Source: "GitHub Actions"; (2) autorizar a criação das etiquetas `triagem`, `correcção`, `proposta`, `contestação`; (3) decidir quando fazer `git push` e abrir o PR; (4) o ADR no Obsidian (`Vault/10-pessoal/Projetos/`) ficou desactualizado face ao repo e pode ser copiado de novo; (5) as perguntas em aberto do ADR (governação, anonimato, licença, `build_state.py`, diagramas) e o passo 6 (identidade) ainda não foram feitos.

---

## Self-review (feita ao escrever)

- **Cobertura do ADR:** pipeline e `common.sh` (Task 3), site e Pagefind (Task 5), `documento.md` como anexo (Task 7), remoção do código morto (Task 2), IDs estáveis e CI de verificação (Tasks 4 e 7), botões e formulários da fase 1 (Task 6), CI em PRs e Pages (Task 7), versão e data no site (Task 5), critério de aceitação no CONTRIBUTING (Task 8). Fora por decisão explícita: identidade, licença, governação, fase 2, diagramas, e `build_state.py` (fica).
- **Verificações pendentes do ADR:** versão do Pandoc (Task 1 Step 2, `require_pandoc`), `chunkedhtml` com template (Task 5 Step 1), Vercel (Task 7 Step 1), números do ICAD (Task 2 Step 1), limpeza do PDF só no PDF (Task 3).
- **Consistência de nomes:** `slugify`, `scan`, `assign_missing`, `fix`, `check`, `lock`, `meta` definidos na Task 4 e usados com as mesmas assinaturas nas Tasks 5 a 7; `SKIP_PAGEFIND`, `TEMP_MD`, `SOURCE_FILES`, `COMMON_SCRIPT_DIR` definidos em `common.sh` e usados em `build-site.sh`.
- **Riscos assumidos:** o formato exacto do `chunkedhtml` (zip plano, nomes de ficheiro) só é confirmado no spike; os workflows só ficam validados no primeiro run no GitHub, porque localmente não há `act` nem `xelatex`.

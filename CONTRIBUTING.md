# Como Contribuir

Este é um projecto aberto a todos, independentemente de filiação partidária, ideologia ou background. É uma iniciativa independente de qualquer partido: partidos, associações, profissionais e cidadãos podem contribuir. Concordar com os princípios de política baseada em evidência, redução de danos e direitos humanos é o que importa; as contribuições são avaliadas pelo mérito.

Questões ainda por decidir (co-maintainers): ver as perguntas em aberto no [ADR 0001](docs/adr/0001-fonte-unica-pdf-e-site.md). Até serem decididas, não há regras formais sobre elas. A identidade está decidida: ver abaixo.

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

Os capítulos usam prefixo numérico (`00`, `01`, ...) para fixar a ordem. Edita sempre o capítulo apropriado em `chapters/`; PDF, DOCX e site são apenas saídas.

## Como contribuir

1. **Sem GitHub avançado:** no site, em cada secção, usa "Levantar questão" (abre um formulário já com a secção preenchida).
2. **Com GitHub:** usa "Sugerir alteração" no site (abre o editor do capítulo) ou faz um fork e edita `chapters/`.
3. Antes de abrir o PR: `python3 scripts/heading_ids.py check`.

Há três formulários de Issue: corrigir erro ou fonte, propor alteração, contestar um argumento. Perguntas gerais e ideias em aberto ficam melhor nas [Discussions](https://github.com/bcamarneiro/cannabis-legalization/discussions).

## Critérios de aceitação

- Toda a alteração factual traz fonte, acrescentada a `references.bib` e citada como `[@chave]`.
- Não mudes IDs de secção já publicados (o CI falha).
- **Quem integra:** por agora, o Bruno Camarneiro é o único maintainer. Quando existirem co-maintainers, cada PR precisa de uma segunda pessoa a rever. Alterações factuais sem fonte não são integradas. Quando houver contribuidores recorrentes, convidam-se co-maintainers, com prioridade para direito e economia.
- **Licença:** o conteúdo é CC BY-SA 4.0 (ver `LICENSE`).
- **Identidade:** o CI recusa PRs com commits sem `Signed-off-by`. Quem altera o texto (Pull Request) assina com o nome real, no autor do commit e com `Signed-off-by` (`git commit -s`), e aparece na lista de contribuidores. O histórico do git é público e permanente: só contribuis com nome se estiveres de acordo com isso.
- **Questões e sugestões (Issues):** ficam públicas e podem ser feitas com a conta GitHub, incluindo sob pseudónimo. Não contam como apoio ao documento.
- **Apoio público ao documento:** só conta com nome e cara.
- O nome real não é verificado; é uma regra de honestidade, não um controlo técnico.

## Escolher uma tarefa

Consulta [docs/TASKS.md](docs/TASKS.md). Por área de expertise:

- **Direito:** LEGAL 1-9, IMPLEMENT 7
- **Economia:** ECON 1-5, DEVIL 6
- **Medicina e saúde pública:** HEALTH 1-4, DEVIL 8
- **Política:** POLITIC 1-6, DEVIL 2-3
- **Análise de dados:** DEVIL 1, 4, 9

Prioridade máxima: TIER 1 (DEVIL 1-4).

## Fluxo técnico

    git clone https://github.com/bcamarneiro/cannabis-legalization.git
    cd cannabis-legalization
    git checkout -b fix/devil-2-germany-failure-rate

1. Edita o capítulo em `chapters/` (por exemplo, `chapters/08-pilar-recreativa.md`).
2. Se acrescentares uma fonte, junta a entrada a `references.bib` e cita-a como `[@chave]`.
3. Verifica os IDs: `python3 scripts/heading_ids.py check`.
4. Opcional, para ver o resultado: `bash scripts/build.sh site` (site em `output/site/`) ou `bash scripts/build.sh` (PDF e DOCX; o PDF requer xelatex). Requer Pandoc 3.x.
5. Faz commit de `chapters/` e `references.bib` (nunca de `output/`) e abre o PR. No CI são compilados PDF, DOCX e site e validados os IDs.

No PR, indica a vulnerabilidade ou questão a que responde, o que mudou, porque funciona e as fontes usadas.

### IDs de secção

Todos os títulos até ao nível 3 têm um ID explícito (`## Título {#id}`). Um título novo sem ID recebe um automaticamente com `python3 scripts/heading_ids.py fix`. Se renomeares um título, mantém o ID antigo com `<span id="id-antigo"></span>` junto ao título.

### Referências internas

Liga a secções com o ID: `[ver descriminalização](#desc-2001)`. As ligações só funcionam no documento compilado, não na pré-visualização do editor.

### Citações

    ✅ Portugal exportou 32.558 kg em 2024 [@infarmed2024]
    ❌ Portugal exportou muito [@infarmed2024]

Tipos de entrada em `references.bib`: `@online` (web), `@article` (artigos revistos por pares), `@legislation` (leis e decretos), `@report` (relatórios oficiais) e `@book`. Para encontrar uma chave: `grep "@.*{infarmed2024" references.bib`.

## Convenções de estilo

- **Títulos:** `#` reservado para capítulos; depois `##` e `###`.
- **Listas:** `-` para marcadores, `1.` para numeradas.
- **Tom:** profissional mas acessível, baseado em evidência; evita linguagem emotiva e superlativos.
- **Números:** formato português (€52-151M, 18.400 utilizadores).
- **Tabelas:** pipe tables do Markdown, com uma coluna de fonte quando fizer sentido.

## Checklist antes de submeter

- [ ] Editei o capítulo correcto em `chapters/`
- [ ] Toda a alteração factual tem fonte em `references.bib`, citada como `[@chave]`
- [ ] `python3 scripts/heading_ids.py check` passa
- [ ] O PR referencia a questão ou vulnerabilidade (ex: "Fixes DEVIL 2")

## Problemas comuns

- **"Citeproc: citation X not found":** falta a entrada em `references.bib`.
- **PDF não compila:** caracteres especiais LaTeX (`%`, `$`, `&`, `#`) ou tabelas mal formadas; revê a secção editada.
- **`heading_ids.py check` falha:** um ID publicado mudou ou desapareceu; repõe-no ou mantém-no com `<span id="...">`.

## Código de conduta

- Respeito mútuo em todas as interações.
- Feedback construtivo, baseado em evidência.
- Foco em melhorar o documento, não em atacar contribuições anteriores.
- Reconhecer o trabalho de outros contribuidores (`Co-Authored-By` nos commits).

## Contacto

- **Issues e Discussions no GitHub:** para tudo o que possa ser público.
- **Email:** <bruno@camarneiro.com>, para feedback confidencial antes de o tornar público.

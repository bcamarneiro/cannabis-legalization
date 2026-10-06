# Regulação da Cannabis em Portugal

[![Discussions](https://img.shields.io/github/discussions/bcamarneiro/cannabis-legalization)](https://github.com/bcamarneiro/cannabis-legalization/discussions)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

Proposta de enquadramento legal e regulatório da cannabis em Portugal, abrangendo uso medicinal, recreativo e industrial. É uma iniciativa independente de qualquer partido, desenvolvida de forma aberta e colaborativa; as posições oficiais dos partidos são registadas à parte (anexo E).

**Origem e independência.** O documento começou em Janeiro de 2026 como trabalho no contexto do LIVRE. Desde Outubro de 2026 é mantido de forma independente: nenhum partido tem controlo editorial, todos os partidos com representação parlamentar recebem as mesmas perguntas e são registados pelas mesmas regras (anexo E), e todas as correcções ficam públicas no histórico do repositório.

Licença: o ficheiro [LICENSE](LICENSE) indica CC BY-SA 4.0; a licença definitiva do conteúdo está por decidir (ver [ADR 0001](docs/adr/0001-fonte-unica-pdf-e-site.md), perguntas em aberto).

## Documento

- **Fonte:** [`chapters/`](chapters/), um ficheiro por capítulo.
- **Bibliografia:** [`references.bib`](references.bib).
- **PDF e DOCX:** em [Releases](../../releases), gerados automaticamente a partir dos capítulos. Cada release traz também `documento.md`, o texto completo num só ficheiro.

### Como funcionam as citações

No texto verás referências como `[@bundesministerium2024]`. Para encontrar a fonte completa, procura a chave (sem `@`) em [`references.bib`](references.bib):

    grep "@.*{infarmed2024" references.bib

Para acrescentar uma fonte, junta uma entrada BibTeX a `references.bib` e cita-a no capítulo como `[@chave]`.

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

O site inclui pesquisa (Pagefind); para o compilar sem ela, usa `SKIP_PAGEFIND=1`.

## Verificar

    python3 scripts/heading_ids.py check
    python3 -m unittest discover -s tests

Todos os títulos até ao nível 3 têm um ID explícito (`{#id}`). Não mudes um ID já publicado:
o `check` falha. Se renomeares um título, mantém o ID antigo com `<span id="id-antigo"></span>`.

## Contribuir

Vê [CONTRIBUTING.md](CONTRIBUTING.md). Em resumo: no site, cada secção tem "Levantar questão" e "Sugerir alteração"; toda a alteração factual traz fonte em `references.bib`. Vulnerabilidades e melhorias em aberto: [docs/TASKS.md](docs/TASKS.md).

As afirmações em que o argumento assenta, com o estado da prova de cada uma, estão em [docs/registo-afirmacoes.md](docs/registo-afirmacoes.md).

## Problemas frequentes

- **`pandoc: command not found`:** instala o Pandoc 3.x (`brew install pandoc`, `apt install pandoc`).
- **PDF não compila:** falta o `xelatex` (`brew install --cask mactex` ou `apt install texlive-xetex`). Sem ele, o `.tex` é gerado em `output/` mas o PDF não.
- **Citação não aparece:** confirma que a chave existe em `references.bib` e que há um espaço antes de `[@chave]`.

## Referências técnicas

- [Pandoc Manual](https://pandoc.org/MANUAL.html) e [Citations](https://pandoc.org/MANUAL.html#citations)
- [Formato BibTeX](http://www.bibtex.org/Format/)
- [Estilos CSL](https://citationstyles.org/)

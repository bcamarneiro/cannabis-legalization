# ADR 0001: Fonte única para PDF, DOCX e site; abertura a contribuições

- Estado: **aceite; implementado na fase 1 (passos 1 a 5 da ordem de implementação; ver docs/superpowers/plans/2026-10-03-fonte-unica-pdf-e-site.md). Identidade, licença e fase 2 por decidir/fazer**
- Data: 2026-10-03

## Contexto

O projecto começou como documento de posição do LIVRE e cresceu para propostas, soluções e esclarecimentos. O objectivo passa a ser uma iniciativa cívica independente, que não depende de o LIVRE a promover.

Público e prioridades, por ordem:

1. **Contribuir:** especialistas (direito, saúde, economia) e activistas corrigem e melhoram as propostas.
2. **Ler e citar:** jornalistas, deputados e investigadores usam o documento como referência fiável.

Restrição: `chapters/*.md` e `references.bib` são a única fonte. PDF, DOCX e site são apenas saídas.

Estado actual relevante: README e CONTRIBUTING descrevem um layout que já não existe; `build-pdf.sh` e `build-docx.sh` duplicam lógica e usam um ficheiro temporário fixo; `build/documento.md` é gerado mas forçado para o git pelo CI; existe código de agentes sem uso no documento (`fetch_client`, `response_mapper`, `mermaid_svg`, `migrate_*`, `data/`); os 4 diagramas em `assets/diagrams` contradizem os capítulos e nenhum é usado; o CI não tem verificação em PRs.

## Decisão

### 1. Pipeline: Pandoc para as três saídas

```
chapters/*.md + references.bib + assets/diagrams
        │
   scripts/common.sh   (junta capítulos, mktemp, limpeza partilhada)
        ├── build-pdf.sh   → output/Regulacao_Cannabis_Portugal.pdf
        ├── build-docx.sh  → output/Regulacao_Cannabis_Portugal.docx
        └── build-site.sh  → output/site/
```

- `chapters/` mantém o nome (os workflows disparam sobre `chapters/**`).
- Site: uma única execução do Pandoc em modo `chunkedhtml`, com template e CSS em `site/`, seguida de Pagefind para pesquisa. Mesmo `--citeproc`, `references.bib` e `ieee.csl` do PDF, por isso as saídas não divergem. Uma execução só garante que referências cruzadas e numeração resolvem entre capítulos.
- A limpeza específica do PDF (emojis, CO₂) fica só em `build-pdf.sh`.
- `build/documento.md` deixa de ser versionado; passa a anexo da release.
- Diagramas redesenhados a partir dos capítulos e embebidos neles (`.mmd` mais imagem pré-renderizada).
- Removidos: `fetch_client`, `response_mapper`, `mermaid_svg`, `migrate_*`, `data/` e os respectivos testes. `build_state.py` e o seu teste: decisão pendente.

### 2. Contribuição

- Todos os títulos até ao nível 3 têm ID explícito (`{#pilar-recreativo-clubes}`). Um passo de CI falha se faltar um ID ou se um ID da última release desaparecer sem alias.
- **Fase 1 (sem backend):** em cada secção, ligação permanente, "Levantar questão" (Issue pré-preenchido com o ID, três formulários: corrigir erro ou fonte, propor alteração, contestar argumento) e "Sugerir alteração" (editor web do GitHub no capítulo; abre o ficheiro, não a linha). O Issue é o caminho principal.
- **Fase 2:** formulário no site e função serverless (Vercel) que cria o Issue com um token restrito a Issues, com anti-spam (Turnstile). Aviso explícito de que o Issue é público.
- CI em PRs: compila PDF, DOCX e site e valida IDs. Critério de aceitação em `CONTRIBUTING.md`: toda a alteração factual traz fonte em `references.bib`.

### 3. CI, alojamento, versões e identidade

- Push para main (`chapters/**`, `references.bib`): bump de versão, build e release com PDF, DOCX e `documento.md`, mais publicação do site. Remove-se o `git add -f build/documento.md`.
- Alojamento na fase 1: GitHub Pages. O Vercel só entra na fase 2.
- O site mostra a versão mais recente, com número e data de build injectados a partir de `VERSION`. Versões antigas ficam citáveis pelo PDF da respectiva release. Sem snapshots do site por versão por agora.
- Identidade: iniciativa cívica independente, título neutro "Regulação da Cannabis em Portugal". O LIVRE aparece como origem ("nasceu como documento de posição do LIVRE"), não como dono nem autor. O capítulo 10 fica, com revisão de tom.

## Verificações pendentes antes de implementar

1. [resolvida] Pandoc: confirmado 3.12 localmente; o CI instala o do apt e imprime a versão. `require_pandoc` falha abaixo de 3.x.
2. [resolvida] `chunkedhtml` aceita o template e a navegação do site (ver Notas de implementação).
3. [**em aberto**] O que faz o projecto Vercel `cannabis-legalization`; verificar que não lê `build/documento.md`. O repo não mostra o que o projecto Vercel lê: tem de ser confirmado no painel do Vercel.
4. [resolvida, com ressalva] Números do ICAD: o valor 11083 (dimensão da amostra, em `data/raw_icad_stats_initial.json`) não existe nos capítulos; `data/` foi apagado por não ser alegação do documento e fica no histórico git (9c5834e).
5. [resolvida] A limpeza do PDF (emojis, CO₂) fica só em `build-pdf.sh`; o site e o DOCX não a sofrem.

## Perguntas em aberto (decisão do Bruno, não de código)

- ~~Quem decide as fusões?~~ Decidido: Bruno único maintainer, 2.ª revisão obrigatória; co-maintainers a recrutar (direito, economia).
- ~~Contribuições anónimas?~~ Decidido: ver notas de implementação.
- ~~Licença~~ Decidido: manter CC BY-SA 4.0.
- `build_state.py` e o seu teste ficam? (por agora ficam)
- ~~Redesenhar os diagramas~~ Feito: ver notas de implementação.

## Fora de âmbito

Explorador de modelos, simulador, assistente de contribuição e mapa de clubes (PRs fechados). Só voltam com caso de uso próprio e outro ADR.

## Consequências

- Site e PDF não divergem em citações nem numeração; um só CI.
- Interactividade futura obriga a JS à mão. Se for necessária UX rica, migrar para um gerador próprio é possível, porque fontes e IDs estáveis não mudam.
- IDs estáveis passam a ser uma regra editorial: renomear um título já não parte ligações.
- Limpeza de repo (README, CONTRIBUTING, `17-referencias.md`, `.claude/settings.local.json` versionado, `assets/formatted_doc.pdf`, `apa.csl`) acompanha a implementação.

## Ordem de implementação sugerida

1. Limpeza sem risco: tooling morto, docs desactualizadas, ficheiro de settings versionado.
2. `common.sh` e deduplicação dos scripts, com PDF e DOCX idênticos aos actuais.
3. IDs estáveis e verificação em CI.
4. `build-site.sh`, template e Pagefind.
5. CI em PRs e publicação no Pages; formulários de Issue; botões nas secções.
6. Identidade e licença, depois de respondidas as perguntas em aberto.
7. Fase 2 (formulário e função serverless).

## Notas de implementação

- **Pandoc:** 3.12 na máquina de desenvolvimento; o `chunkedhtml` exige 3.0 ou superior.
- **`chunkedhtml`:** funciona com template e CSS próprios (`site/`) e produz um zip plano, mas `unzip` no macOS corrompe nomes com acentos, por isso `build-site.sh` extrai com `zipfile` do Python. Resultado: 21 páginas, com Pagefind (`SKIP_PAGEFIND=1` salta a pesquisa).
- **Vercel:** projecto pausado pelo Bruno em Outubro de 2026. O site publicado é o do GitHub Pages.
- **Paridade das saídas:** o `.tex` e o DOCX diferem do original só por: remoção de comentários mortos, `# Referências` passar a ser secção (capítulos concatenados com linha em branco) e um nome de marcador interno no DOCX (ID `{#potencial-de-co2}`, escrito à mão porque o PDF reescreve CO₂).
- **IDs:** 224 títulos com ID explícito; `docs/heading-ids.lock` guarda 248 IDs publicados. O `slugify` segue o do Pandoc (separa por espaços, ignora vazios). Não se encontraram ligações internas partidas.
- **Por fazer:** recrutar co-maintainers; fase 2 (formulário e função serverless). O passo 6 (identidade e licença) está decidido (ver abaixo).
- **Fora do código (feito):** GitHub Pages activo (Source: GitHub Actions); etiquetas `triagem`, `correcção`, `proposta` e `contestação` criadas.
- **Diagramas (feito):** os 4 foram redesenhados a partir dos capítulos 01, 05, 08 e 11 e embebidos neles. `receitas-fiscais` passou a `balanco-fiscal` (desde a auditoria de Outubro de 2026: custo líquido na Fase 2; receitas só como Fase 3 especulativa); emojis removidos; `mermaid-config.json` e README novos. O PDF não foi compilado neste ambiente (falta `pdflatex`); DOCX e site foram verificados.
- **Identidade (decidido pelo Bruno):** PRs com nome real e `Signed-off-by`; Issues abertas com conta GitHub (pseudónimo aceite, sem valor de apoio); apoio público só com nome. Não verificável tecnicamente. Falta aplicar sign-off no CI, se se quiser impor.
- **Governação e licença (decididos):** Bruno único maintainer; 2.ª revisão obrigatória quando houver co-maintainers; CC BY-SA 4.0 mantida. O CI exige `Signed-off-by` em cada commit de PR (passo em `ci.yml`, só validado no primeiro PR).

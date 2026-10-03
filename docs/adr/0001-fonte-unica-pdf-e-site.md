# ADR 0001: Fonte única para PDF, DOCX e site; abertura a contribuições

- Estado: **proposto** (aguarda revisão; nada está implementado)
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

1. O Pandoc não está instalado nesta máquina. Confirmar a versão no CI e localmente: `chunkedhtml` exige 3.0 ou superior.
2. Teste descartável: o `chunkedhtml` aceita o template e a navegação de que o site precisa?
3. O que faz o projecto Vercel `cannabis-legalization`; verificar que não lê `build/documento.md`.
4. Antes de apagar `data/`: confirmar que os números do ICAD já existem nos capítulos.
5. Garantir que a limpeza do PDF não remove conteúdo que o site deva mostrar.

## Perguntas em aberto (decisão do Bruno, não de código)

- Quem decide as fusões além do Bruno (co-maintainers, critérios)?
- Aceitam-se contribuições anónimas ou com pseudónimo?
- Licença do conteúdo: CC BY-SA, CC BY ou outra?
- `build_state.py` e o seu teste ficam?
- Redesenhar os diagramas (cronograma, estrutura, modelo alemão; "poupanças vs custos" no lugar de receitas fiscais) como parte desta mudança ou depois?

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

# Diagramas

Fonte Mermaid (`.mmd`) mais PNG pré-renderizado, que é o que PDF, DOCX e site embebem. Cada diagrama está inserido no capítulo indicado.

| Ficheiro | Capítulo | O que mostra |
| :---- | :---- | :---- |
| `estrutura-proposta` | 01 Sumário executivo | Três pilares (o que) e três fases (quando); a Fase 3 é condicional |
| `cronograma-implementacao` | 11 Cronograma | Gantt do cenário base (realista) |
| `modelo-alemao-pillars` | 05 Modelos internacionais | CanG: Pillar 1 em vigor, Pillar 2 bloqueado; correspondência com as fases portuguesas |
| `balanco-fiscal` | 08 Pilar recreativo | Fase 2: poupança líquida de enforcement; Fase 3: receitas fiscais especulativas |

Terminologia: "Pilares" (Medicinal, Recreativo, Cânhamo) dizem *o que*; "Fases 1-3" dizem *quando*; "Pillar 1/2" são os pilares da lei alemã.

## Editar e regenerar

1. Edita o `.mmd`.
2. Regenera o PNG a partir desta pasta (mermaid-cli v12, sem `-w/-H`):
   ```bash
   echo '{"args":["--no-sandbox"]}' > /tmp/pp.json   # só necessário em contentores
   npx -y @mermaid-js/mermaid-cli -q -i X.mmd -o X.png -c mermaid-config.json -p /tmp/pp.json -b white -s 2
   ```
3. Faz commit do `.mmd` e do `.png`.

`mermaid-config.json` fixa o tema, o tipo de letra e as larguras para os quatro diagramas ficarem coerentes.

## Build

PDF, DOCX e site usam `--resource-path=".:assets/diagrams"`. `scripts/build-site.sh` copia `assets/diagrams/*.png` para `output/site/assets/diagrams/`.

## Convenções

- Azul: elementos da proposta; borda tracejada: condicional ou especulativo.
- Sem emojis; texto em português europeu.
- Os números vêm dos capítulos; se mudarem lá, actualizar aqui.

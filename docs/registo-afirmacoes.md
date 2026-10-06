# Registo de afirmações

Este registo reúne as **afirmações em que o argumento assenta** — não todas as citações do documento, mas as que sustentam as conclusões. Para cada uma indica-se o estado da prova, para que qualquer leitor veja de imediato o que é facto com fonte, o que é cálculo e o que é pressuposto por confirmar.

É deliberado publicar aqui as fraquezas. Um pressuposto assinalado é honesto; um pressuposto escondido é um risco. As afirmações marcadas **pressuposto** ou **pendente** são as prioridades de validação (ver [docs/TASKS.md](TASKS.md) e os pedidos de dados ao abrigo da Lei 26/2016).

## Legenda do estado

- **confirmado** — fonte primária aberta e verificada.
- **secundária** — só confirmado por fonte secundária (a primária está inacessível).
- **derivado** — resulta de um cálculo a partir de pressupostos; a aritmética está verificada, as entradas não.
- **pressuposto** — assunção dos autores, sem fonte; declarada como tal no texto.
- **pendente** — à espera de dados oficiais (pedido Lei 26/2016).
- **especulativo** — cenário condicional (Fase 3), apresentado como hipótese.

## Economia (capítulo 8 — a base do argumento financeiro)

| Afirmação | Valor | Estado | Fonte / nota |
| :---- | :---- | :---- | :---- |
| Base de custos de repressão | €40-80M/ano (central €60M) | **pressuposto + pendente** | Sem fonte. É o pressuposto mais frágil do documento. Pedidos a PSP, GNR, DGPJ, DGRSP e ICAD para o substituir por dados. |
| Consumidores no último ano | ~180.000 (2%, 15-74) | confirmado | [@carapinha2024icad] (ICAD/INPG 2022) |
| Captura de mercado por cenário | 5,3 / 13,8 / 25,9% | pressuposto | Cenários dos autores (taxa operacional × clubes × membros + autocultivo) |
| Poupança de repressão | €3,2 / 8,3 / 15,5M/ano | derivado | captura × €60M |
| Custos regulatórios | €15 / 17 / 20M/ano | pressuposto | Assunção dos autores |
| Balanço operacional (custo líquido) | −€4,5 a −€11,8M/ano | derivado | poupança − custos |
| Balanço a 10 anos | −€61M a −€119M | derivado | inclui investimento inicial €20-30M |
| Investimento inicial | €20-30M | pressuposto | Assunção dos autores |
| Preço do mercado ilegal | €5,33/g (2023) | confirmado | [@icad2024anexo] (Quadro 170; liamba, média) |
| Volume do mercado ilegal | 36-58 t/ano | secundária | [@ribeiro2024economic] (working paper, não revisto por pares) |
| Receita fiscal da Fase 3 | €37-60M/ano | especulativo | volume × €5,33 × captura 78% × taxa 25% |
| Custo por grama nos clubes | €2,40-4,80 (sem IVA) | derivado | modelo de custos do Anexo A; depende do consumo médio |

## Pilar medicinal e cânhamo (Fase 1)

| Afirmação | Valor | Estado | Fonte / nota |
| :---- | :---- | :---- | :---- |
| Exportação de cannabis medicinal | 32.558 kg (2024) | confirmado | [@eco2024] |
| Embalagens prescritas internamente | 1.157 (2023) | confirmado | [@infarmed2024] |
| "2.º maior exportador mundial" | — | secundária | Imprensa sectorial, sem ranking oficial [@eco2024; @cannareporter2024] |
| Rendimento de fibra de cânhamo | ~1,2 t/ha | pressuposto | Assunção dos autores; falta fonte (InterChanvre/FranceAgriMer) |

## Enquadramento legal

| Afirmação | Estado | Fonte / nota |
| :---- | :---- | :---- |
| Lei 30/2000: proposta 1-6-2000, VFG 6-7-2000, veto, Decreto 39/VIII | confirmado | [@parlamento2000ppl31] |
| Lei 55/2023: detenção para consumo é contra-ordenação; cultivo é crime | confirmado | [@tc2025acordao347] |
| Processos CDT só com cannabis: 83% (2018), 75% (2021) | confirmado | [@icad2024anexo] (Quadro 132) |
| Condenações por consumo: 475 em 2021 (definitivo) | confirmado | [@icad2024anexo] (Quadro 196) |
| KCanG: residência ≥6 meses (§16); amostragem obrigatória (§18(2)) | confirmado | gesetze-im-internet.de |
| Condução: 3,5 ng/ml soro (Alemanha, §24a StVG) | confirmado | [@stvg2024para24a]; o limiar proposto para PT é dos autores |

## Experiência internacional e saúde

| Afirmação | Estado | Fonte / nota |
| :---- | :---- | :---- |
| Alemanha: 337 licenças / 759 pedidos (Out 2025) | confirmado | [@bcav2025] (captura de arquivo) |
| Uruguai: 557 clubes; 46% dos consumidores registados | confirmado | [@ircca2025resumen] |
| Colorado: consumo juvenil 19,7% (2013) → 12,8% (2023) | secundária | CDPHE bloqueado; confirmado por imprensa |
| Avaliação alemã: ainda não deslocou o mercado negro | confirmado | [@ekocan2025]; resultado preliminar, final em 2028 |
| Dependência: ~9% de quem experimenta; 22% CUD / 13% | confirmado | Lopez-Quintero 2011; Leung 2020 |
| Consumo juvenil após regulação: evidência mista | confirmado | assente em todo o documento |

## Como manter este registo

- Quando uma afirmação muda de estado (por exemplo, um pedido de dados responde à base de repressão), actualiza-se a linha e cita-se a fonte nova no capítulo, por *pull request*.
- As respostas dos partidos (anexo E) e dos pedidos Lei 26/2016 são registadas com a data, como aqui.
- Serve também de resposta rápida: perante uma afirmação pública sobre o tema, confronta-se com a linha correspondente.

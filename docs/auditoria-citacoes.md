# Auditoria de citações

Revisão de todas as citações (`[@chave]`) contra as fontes, feita em 2026-10-04 por subagentes de pesquisa, com revisão humana ainda por fazer. Cada citação foi classificada como: **Apoiada** (a fonte diz isto), **Parcial** (diz algo próximo, com número, âmbito ou ressalva diferente), **Não apoiada** (a fonte não diz isto ou diz o contrário) e **Inacessível** (não foi possível abrir a fonte).

| Veredicto | Citações |
| :---- | ----: |
| Apoiada | 128 (21%) |
| Parcial | 254 (41%) |
| Não apoiada | 193 (31%) |
| Inacessível | 33 (5%) |
| Total | 608 |

## O que já foi corrigido

- 160 correcções de metadados em `references.bib` (autores, títulos, anos, DOIs, URLs, revistas) com evidência da própria fonte.
- 3 chaves duplicadas fundidas (`oasas2024synthetic`, `opcm2024`, `nabiximols2024`).
- 5 citações sem entrada na bibliografia retiradas do capítulo 04 (`casey2019`, `bbrfoundation2023`, `frontiers2025cannabis`, `utdallas2023`, `pmc2013adolescent`); as afirmações ficam sem fonte até se encontrar uma verificável (o artigo de Casey et al. 2019 proposto pelo auditor não foi confirmado).
- Capítulo 10 (posições partidárias) e citação de Goulão no capítulo 02, corrigidos antes desta auditoria.

## O que NÃO foi alterado

Nenhuma afirmação do texto foi reescrita automaticamente. Os problemas abaixo exigem decisão: corrigir o número, trocar a fonte, acrescentar a ressalva ou retirar a afirmação. As correcções de metadados que o auditor propôs sem evidência suficiente também ficaram de fora.

## Citações não apoiadas pela fonte (193)


### 01-sumario-executivo.md

- **L11** `[@infarmed2024]`: Infarmed PDF (versao actualizada nov 2024) Quadro 2: exportado 11973 kg em 2023 e 18521 kg ate 2024 3T; nao ha valor de 32.558 kg nem ranking mundial.
  - *Sugestão:* Citar [@eco2024] para 32.558 kg em 2024 e [@infarmed2024] para 11.973 kg em 2023 / 18.521 kg a 3T 2024.
- **L11** `[@euronews2024]`: Euronews (A. Elci, 19-21/04/2024) so diz 'second biggest producer of cannabis in the EU' (34 t declaradas para 2024); nao e ranking mundial de exportadores e, sendo de abril 2024, nao pode conter dados de 2025.
  - *Sugestão:* Remover 'ultrapassados nos primeiros 8 meses de 2025' ou citar fonte 2025 (nao encontrei fonte verificada para '8 meses de 2025'; pesquisa apenas devolveu 79.883 kg em todo 2025 segundo Infarmed via imprensa, nao verificado).
- **L11** `[@eco2024]`: O artigo ECO nao contem as 1.157 prescricoes de 2023 (trata exportacoes: 32.558 kg em 2024, +172%).
  - *Sugestão:* Citar [@infarmed2024] (Quadro 5: 1157 embalagens prescritas em 2023) ou [@cannareporter2024].
- **L11** `[@cannareporter2024]`: Artigo nao contem '17 kg' nem equivalencia entre 1.157 prescricoes e 17 kg; alem disso 1.157 sao embalagens prescritas, 17 kg e venda local (outra grandeza).
  - *Sugestão:* Cortar 'equivalendo a cerca de 17 kg' ou citar [@euronews2024] para os 17 kg sem a palavra 'equivalendo'.
- **L36** `[@drug2024]`: Pagina aberta: comunicado da Drug Policy Alliance (18/12/2025) sobre reescalonamento da marijuana nos EUA; nao menciona Portugal, EUR 150 nem comparticipacao.
  - *Sugestão:* Substituir por [@euronews2024]; 'EUR 150/mes' assume 1 caixa de 15 g por mes, que a fonte nao diz.
- **L42** `[@cannareporter2025medicinal]`: Artigo CannaReporter (L. Sousa, 12/06/2025) nao contem estatisticas sobre mercado negro nem 95%; so diz que os produtos sao caros e nao comparticipados.
  - *Sugestão:* Procurar fonte primaria (ex. inquerito ICAD/SICAD sobre fonte de obtencao) ou remover '95%'.
- **L101** `[@springer2021pt]`: Springer/PMC (Rego et al. 2021): Estrategia Nacional 1999; Lei 30/2000 aprovada em 29/11/2000; entrada em vigor julho 2001; 'These tendencies cannot be, however, linearly related with the decriminalization law per se'; prevalencia 'stayed reasonably low'; criticas: contradicoes, 'modest ambitions', acordao do STJ 2008 e aumento da punitividade; sem percentagens 8,2%/8,3%.
  - *Sugestão:* Remover '~18 meses' ou calcular explicitamente (lei->vigor ~8 meses; estrategia 1999->vigor >18 meses) e citar fonte da data da estrategia.
- **L101** `[@transform2016pt]`: Transform (pagina datada 13/05/2021): 'In 2001, Portugal decriminalised the personal possession of all drugs'; 'regularly held up as the leading example'; consumo 'keenly disputed and often misrepresented'; subida do consumo desde 2012 'particularly among those over 25' com dados 'relatively limited'. Sem cronologia 1999/2000/18 meses.
  - *Sugestão:* Retirar Transform desta frase.

### 02-panorama-portugues.md

- **L19** `[@cannareporter2025]`: Article (5 Jun 2025) is about new Infarmed import/export documentation requirements; contains no 2024 export figures (only "50 companies licensed to export and 49 to import"). Also "Eco" is not CannaReporter.
  - *Sugestão:* Trocar para [@eco2024] (chave existente no .bib) após verificar que contém 32.558 kg.
- **L21** `[@cmslaw2024]`: Guide (18 Jun 2024) does not mention 37 companies authorised for cultivation.
  - *Sugestão:* Procurar fonte Infarmed/Eco com o número 37; remover citação a cmslaw2024.
- **L21** `[@ec2024]`: EC hemp page has nothing on EU-GMP certified companies or Portugal.
  - *Sugestão:* Remover; citar Infarmed ou fonte do setor para as 20 empresas EU-GMP.
- **L23** `[@rtp2019]`: 2019 article cannot contain 2023 prescription data; it does not mention 1,157.
  - *Sugestão:* Trocar para [@prohibition2025] (460->1.157, 2021-2023).
- **L23** `[@prohibition2017]`: Article mentions only a EUR 106M recreational market estimate and EUR 40M Tilray revenue; no price per 15 g.
  - *Sugestão:* Usar [@euronews2024] (citado no cap. 07 para os 150 EUR) se confirmado.
- **L30** `[@sicad2022]`: The V INPG 2022 report is a population consumption survey; text search finds no GACP/EU-GMP/certification content.
  - *Sugestão:* Citar legislação (DL 8/2019) / Infarmed; não o INPG.
- **L31** `[@euda2025]`: Full EDR 2025 cannabis page read; no mention of Portugal authorisation times or "2-3 months"; it is about use, treatment, markets.
  - *Sugestão:* Remover ou citar Infarmed/imprensa com prazo verificado.
- **L32** `[@open2013]`: Article is about dissolution of the IDT and austerity threats to decriminalisation (2012); says nothing on medical cannabis prescriptions.
  - *Sugestão:* Trocar para [@prohibition2025].
- **L33** `[@jacobin2023]`: Article on decriminalisation and treatment funding (Oregon M110, Portugal); no CBD, Infarmed, DGAV or novel food.
  - *Sugestão:* Citar fonte regulatória (Infarmed/DGAV/EFSA novel food).
- **L33** `[@renascencalusa2025]`: Lusa text (26 Feb 2025): Goulão on ICAD funding, therapeutic communities, overdoses; no hemp, THC<0.3% or regulation.
  - *Sugestão:* Citar Reg. (UE) 2021/2115 / Lei 33/2025 etc. para o limite de THC.
- **L39** `[@euda2025a]`: Drug-induced deaths page: mortality data, polysubstance; nothing on medical cannabis or teaching.
  - *Sugestão:* Citar fonte sobre formação médica (ex.: rtp2019, parcial).
- **L40** `[@greenwald2009]`: Cato paper concerns decriminalisation outcomes (2009); nothing on doctors prescribing cannabis.
  - *Sugestão:* Remover ou citar fonte sobre prescritores.
- **L41** `[@drug2023]`: DPA PDF (read in full text) says "Medical or adult-use marijuana is also not available in Portugal"; no mention of 7 indications or failure of other options. It is a US advocacy brief on decriminalisation.
  - *Sugestão:* Citar Portaria 2018/Infarmed para indicações.
- **L42** `[@cannareporter2020]`: Article reports the AEFMUP debate on recreational regulation; says nothing on each prescription requiring failed conventional therapy.
  - *Sugestão:* Citar cmslaw2024 / Prohibition Partners.
- **L43** `[@drug2024]`: Pagina aberta: comunicado da Drug Policy Alliance (18/12/2025) sobre reescalonamento da marijuana nos EUA; nao menciona Portugal, EUR 150 nem comparticipacao.
  - *Sugestão:* [@euronews2024]
- **L44** `[@national2017]`: US NASEM report on health effects; nothing on Portuguese doctors refusing patients.
  - *Sugestão:* Citar fonte portuguesa (OPCM/rtp2019 parcial).
- **L49** `[@torresmoreno2023]`: Source is a nabiximols/MS meta-analysis; nothing on the Portuguese illegal market. Search snippets attribute 36-58 t to the ResearchGate paper (ribeiro2024 key), which could not be opened.
  - *Sugestão:* Trocar para [@ribeiro2024] e corrigir "estudo de 2024" (snippets indicam jun. 2022).
- **L58** `[@nugent2017]`: Systematic review of cannabis for chronic pain; no Portuguese prevalence. 10.5% lifetime is in sicad2022 (V INPG 2022: "canábis ... 10,5 %" lifetime) but for ages 15-74, not 15-64.
  - *Sugestão:* [@sicad2022]; corrigir faixa etária para 15-74.
- **L59** `[@marconi2016]`: O resumo de Marconi 2016 trata de nivel de consumo e risco de psicose (OR 3,90 IC 2,84-5,34 nos consumidores mais pesados vs nao consumidores); nao contem prevalencia de consumo em Portugal (2,8%) nem media UE (8,4%).
  - *Sugestão:* Retirar [@marconi2016; @di2019] desta linha; citar a fonte real das percentagens (inquerito nacional SICAD/ICAD ou EUDA European Drug Report), apos confirmar os valores 2,8% e 8,4% (nao verificados).
- **L59** `[@di2019]`: Estudo EU-GEI de caso-controlo sobre psicose (901 casos, 1237 controlos); nao contem prevalencia de consumo no ultimo ano em Portugal nem media UE.
  - *Sugestão:* Remover esta chave desta linha; usar fonte de prevalencia (SICAD/ICAD, EUDA).
- **L61** `[@leung2020]`: Leung 2020 e uma meta-analise internacional de CUD; nao tem dados de Portugal nem CAST 15-24 anos 2012-2022. O relatorio ICAD (Carapinha) mostra consumo de risco moderado/elevado (CAST) de 1,3% em 15-34 anos em 2012 e igualmente 1,3% em 2022 (estavel), e em 15-74 anos ligeira diminuicao; 0,2% e a prevalencia nas mulheres (1,2% homens vs 0,2% mulheres), nao um valor de 2012.
  - *Sugestão:* Remover a frase "aumentou de 0,2% para 1,3%". Alternativa verificavel: "O consumo de risco moderado/elevado (CAST) em 15-34 anos manteve-se em 1,3% entre 2012 e 2022 [@carapinha2024icad]".
- **L103** `[@transform2020]`: O guia nao menciona Portugal nem o CAST 0,2%->1,3% (pesquisa no texto completo do PDF sem ocorrencias de "Portugal" nem 1,3%).
  - *Sugestão:* Retirar a chave; ver correcao ICAD em leung2020.
- **L103** `[@tax2024]`: Pagina do Tax Policy Center trata de impostos estaduais/locais sobre cannabis nos EUA; nao trata de Portugal nem de financiamento de servicos de dependencias (EUR 76M->16M). Pagina nao aberta integralmente (403); conclusao baseada no ambito da pagina e em excertos.
  - *Sugestão:* Retirar a chave; fonte necessaria para o corte de financiamento (nao verificada).
- **L103** `[@nutt2010]`: Estudo sobre danos de 20 drogas no Reino Unido; nada sobre financiamento de servicos portugueses.
  - *Sugestão:* Retirar a chave.
- **L103** `[@rogeberg2019]`: Meta-analise do risco de acidente de condutores THC-positivos; nada sobre tempo de espera para tratamento em Portugal.
  - *Sugestão:* Retirar a chave; o dado "4 horas -> 1 ano" nao tem fonte verificada.
- **L103** `[@bundesministerium2024]`: A pagina do Ministerio alemao nao menciona Joao Goulao nem orcamento portugues pos-2012.
  - *Sugestão:* Retirar a chave; fonte necessaria (nao verificada).
- **L108** `[@bessergrowen2025]`: O artigo trata de testes rapidos de THC na estrada na Alemanha; nao menciona Portugal, overdoses nem 369/80.
  - *Sugestão:* Substituir por fonte que contenha 369->~80 mortes e 10 vs 22 por milhao (p.ex. relatorio EUDA/SICAD; nao verificado).
- **L109** `[@manthey2024]`: Artigo trata de procura de tratamento de cannabis na Alemanha; sem HIV nem Portugal.
  - *Sugestão:* Substituir por fonte que contenha a serie HIV 907 (2000) -> 18 (2017) (candidato a verificar: relatorios nacionais EMCDDA/EUDA sobre Portugal, ou Transform Drugs 'Drug decriminalisation in Portugal: setting the record straight'); nao verificado por mim.
- **L110** `[@businesscannabis2025a]`: Artigo sobre Alemanha; nao menciona populacao prisional portuguesa.
  - *Sugestão:* Usar fonte sobre prisoes em Portugal (candidato: Transform Drugs 'setting the record straight', snippet indica 15,7% em 2019 e >40% em 2001; o 44% de 1999 nao verificado) e confirmar 'media europeia 18%'.
- **L112** `[@marijuanamoment2025]`: Artigo sobre relatorio alemao; nao menciona Cato Institute.
  - *Sugestão:* Trocar para [@greenwald2009] (fonte da citacao Cato).
- **L120** `[@internationalcbc2025]`: Fonte e inquerito KonCanG na Alemanha; sem HIV nem Portugal.
  - *Sugestão:* Substituir por fonte que contenha a serie HIV 907 (2000) -> 18 (2017) (candidato a verificar: relatorios nacionais EMCDDA/EUDA sobre Portugal, ou Transform Drugs 'Drug decriminalisation in Portugal: setting the record straight'); nao verificado por mim.
- **L121** `[@businesscannabis2025b]`: Artigo sobre clubes na Baviera; sem Portugal nem overdoses.
  - *Sugestão:* Usar [@bessergrowen2025] ou fonte oficial sobre mortes por overdose.
- **L122** `[@mmjdaily2025]`: Artigo sobre clubes alemaes; sem mortalidade em Portugal.
  - *Sugestão:* Usar relatorio EUDA/SICAD para mortalidade.
- **L129** `[@cbcnews2025]`: Artigo sobre receita fiscal do Canada.
  - *Sugestão:* Ver businesscannabis2025a, fonte correcta para prisoes em Portugal.
- **L130** `[@insolvency2025]`: Artigo sobre producao de cannabis canadiana.
  - *Sugestão:* Usar fonte sobre tratamento de heroina em Portugal.
- **L131** `[@cdays2025]`: Artigo sobre Uruguai; sem Portugal/CDTs.
  - *Sugestão:* Usar fonte sobre CDTs portuguesas.
- **L135** `[@latinamerica2024]`: Artigo sobre farmacias uruguaias; nao trata de austeridade em Portugal.
  - *Sugestão:* Usar tni2018 / fonte portuguesa.
- **L135** `[@softsecrets2025]`: Artigo sobre Uruguai; sem Portugal.
  - *Sugestão:* Usar fonte portuguesa.
- **L135** `[@tni2018]`: A fonte é um briefing sobre clubes sociais em Espanha; nada sobre austeridade ou desinvestimento em Portugal.
  - *Sugestão:* Retirar @tni2018 desta frase; manter só as fontes sobre Portugal.
- **L137** `[@transform2018]`: Artigo sobre clubes em Espanha; sem referência a Portugal nem a cortes de €76M para €16M.
  - *Sugestão:* Citar fonte portuguesa/SICAD para o corte de financiamento (ex.: relatório do Tribunal de Contas ou SICAD); retirar @transform2018.
- **L138** `[@hightimes2024]`: Artigo sobre clubes em Barcelona; nada sobre equipas de rua portuguesas nem ONGs.
  - *Sugestão:* Citar fonte portuguesa sobre subcontratação de equipas de rua ou retirar.
- **L139** `[@cdphe2024]`: Inquérito a jovens do Colorado; nada sobre overdoses em Portugal (63 para 81 mortes).
  - *Sugestão:* Fonte errada; usar SICAD/EUDA para mortes por overdose em Portugal.
- **L140** `[@marijuanapolicy2025]`: Comunicado sobre consumo juvenil nos EUA; nada sobre investimento contínuo em Portugal.
  - *Sugestão:* Citar fonte sobre Portugal (ex.: Goulão/SICAD).
- **L146** `[@pan2021]`: Página PAN: proposta portuguesa de 2019; nada sobre 24 estados dos EUA nem apoio público de 32% (2006) para 88% (2022) (a página é de 2019, não poderia citar 2022).
  - *Sugestão:* Citar Gallup/Pew para o apoio público nos EUA; retirar @pan2021.
- **L146** `[@publico2023]`: Artigo não cita a Drug Policy Alliance nem a frase "a descriminalização não é suficiente".
  - *Sugestão:* Citar a fonte original da DPA ou retirar a citação entre aspas.

### 03-contexto-historico.md

- **L21** `[@jodope2024]`: Fonte fala de Colombo (1492) e Magalhães; não menciona caravelas portuguesas, Brasil nem 1500.
  - *Sugestão:* Retirar @jodope2024 desta frase.
- **L29** `[@releaf2023]`: Página diz o oposto/outra coisa: declínio do cultivo no séc. XVIII; nada sobre obrigatoriedade até 1961 no Estado Novo.
  - *Sugestão:* Citar fonte histórica (Real Feitoria do Linho Cânhamo; legislação do Estado Novo) ou retirar.
- **L114** `[@infarmed2024]`: Infarmed PDF (versao actualizada nov 2024) Quadro 2: exportado 11973 kg em 2023 e 18521 kg ate 2024 3T; nao ha valor de 32.558 kg nem ranking mundial.
  - *Sugestão:* [@eco2024; @cannareporter2024] para 32.558 kg e ranking; remover referencia a 2025 ou citar fonte com dados 2025.
- **L114** `[@euronews2024]`: Euronews (A. Elci, 19-21/04/2024) so diz 'second biggest producer of cannabis in the EU' (34 t declaradas para 2024); nao e ranking mundial de exportadores e, sendo de abril 2024, nao pode conter dados de 2025.
  - *Sugestão:* Citar [@cannareporter2024; @eco2024] para ranking; tirar o Euronews.
- **L115** `[@eco2024]`: ECO nao tem 1.157 prescricoes nem 17 kg; 0,05% nao aparece em nenhuma fonte e e incoerente com 99,85% (17 kg/11.973 kg = 0,14%).
  - *Sugestão:* 'Apenas 1.157 prescricoes (embalagens) em 2023 [@infarmed2024]; 17 kg vendidos no mercado interno [@euronews2024], ~0,15% das quantidades exportadas'.
- **L116** `[@cannareporter2025medicinal]`: Artigo CannaReporter (L. Sousa, 12/06/2025) nao contem estatisticas sobre mercado negro nem 95%; so diz que os produtos sao caros e nao comparticipados.
  - *Sugestão:* Manter [@sicad2022prevalence] so se tiver o numero; senao remover '95% via mercado negro'.
- **L116** `[@sicad2022prevalence]`: Sumário executivo 2022 não contém 540.000-900.000 nem 95% mercado negro; indica prevalência recente de qualquer droga 3% (15-74 anos). Relatório completo não foi obtido, por isso verificar antes de eliminar.
  - *Sugestão:* Reportar números do INPG 2022 (prevalência ao longo da vida, 12 meses) ou citar a fonte efectiva da estimativa.

### 04-ciencia.md

- **L5** `[@publico2018a]`: Artigo não menciona NASEM.
  - *Sugestão:* Citar NASEM 2017, The Health Effects of Cannabis and Cannabinoids (doi 10.17226/24625); a afirmação (mais de 10.000 resumos; evidência conclusiva ou substancial para dor crónica em adultos, náuseas da quimioterapia e espasticidade na EM) está correcta segundo pesquisa.
- **L7** `[@publico2018b]`: Artigo sobre votação parlamentar; sem evidência clínica sobre dor crónica.
  - *Sugestão:* Citar NASEM 2017 (substantial evidence for chronic pain in adults).
- **L8** `[@cannareporter2024b]`: Fact-check político; nada sobre epilepsia, NEJM, Epidiolex.
  - *Sugestão:* Citar Devinsky et al., NEJM 2017 (doi 10.1056/NEJMoa1611618, Dravet) e FDA/EMA; o valor 39% e datas não foram verificados aqui.
- **L9** `[@publico2022]`: Artigo sobre a JS; sem espasticidade, OR 2,41 nem Sativex.
  - *Sugestão:* Citar a meta-análise (OR 2,41) e a fonte da aprovação do Sativex; não verificado.
- **L10** `[@colorado2023]`: Estudo sobre uso de drogas após legalização; nada sobre náuseas oncológicas.
  - *Sugestão:* Citar NASEM 2017 (CINV).
- **L12** `[@kirby2019]`: O artigo trata de alcool como gateway drug em alunos do 12.º ano (MTF 2008); nada sobre dor neuropática.
  - *Sugestão:* Substituir por revisão sobre dor neuropática (candidato por verificar: Mücke et al., Cochrane 2018); ou usar Kirby apenas na secção gateway.
- **L142** `[@tax2024]`: Excertos da pagina: Colorado afecta a receita a construcao de escolas publicas; Washington gasta metade em programas de saude; 37% e a taxa de imposto especial de consumo do Washington (Colorado 15% + imposto por peso), nao uma quota de receita. "~37-50% destinado a educacao/saude" mistura taxa com afectacao. Caveat: pagina nao aberta integralmente.
  - *Sugestão:* "...receitas fiscais significativas; p.ex. no Colorado a receita e afecta a construcao de escolas e no Washington cerca de metade a saude [@tax2024]" (confirmar na pagina).
- **L206** `[@rogeberg2019]`: O abstract (texto integral Elsevier nao acedido) trata de vies interpretativo em estudos de culpabilidade; nao refere janela de deteccao do THC nem correlacao sangue-incapacidade.
  - *Sugestão:* Retirar [@rogeberg2019]; citar fonte farmacocinetica (nao verificada; BesserGrowen refere apenas dias/semanas de detectabilidade).

### 05-modelos-internacionais.md

- **L77** `[@marijuanamoment2025]`: Artigo nao contem 6,7% nem 6,1%; so diz que o consumo juvenil 'has continued to decline'. Pesquisa ao relatorio EKOCAN tambem nao confirmou os valores; relatorio refere tendencia descendente desde 2019, anterior a lei.
  - *Sugestão:* Consumo juvenil (12-17) continuou a descer apos a lei, tendencia ja visivel desde 2019 (EKOCAN); citar o relatorio EKOCAN para quaisquer percentagens.
- **L182** `[@transform2018]`: Ligações a crime organizado e exportação ilegal não são mencionadas no artigo (só preocupações com deriva comercial e turistas).
  - *Sugestão:* Retirar @transform2018 ou citar fonte sobre crime organizado/exportação (ex.: relatórios Europol/EUDA).
- **L222** `[@marijuanapolicy2025]`: Comunicado não fala de verificação de idade nem licenças retiradas (só "age-restricted access" numa frase).
  - *Sugestão:* Citar fonte específica sobre sanções a vendedores licenciados.

### 06-principios-orientadores.md

- **L19** `[@cannareporter2025medicinal]`: Artigo CannaReporter (L. Sousa, 12/06/2025) nao contem estatisticas sobre mercado negro nem 95%; so diz que os produtos sao caros e nao comparticipados.
  - *Sugestão:* Idem.
- **L29** `[@born2invest2024canada]`: Source has no 2018 data and says illegal share was 5% in 2024, not 3%. 96% (2018) and 3% (2024) are not in it.
  - *Sugestão:* Usar 5% em 2024 (Born2Invest) e 22% em 2022 (Hammond 2025); retirar 96% de 2018.
- **L30** `[@arcview2017colorado]`: Source says legal market was 27% of total spending in Colorado (2017); nothing about 40% or "after 10 years". A 2017 source cannot support a 10-year figure.
  - *Sugestão:* Reformular: "27% em 2017 (Colorado)"; retirar 40% e a referencia a 10 anos.
- **L51** `[@euda2024threat]`: Hungary 30-poisoning outbreak is in EDR 2025, not this 2024 highlights page. Source says "potent semi-synthetic cannabinoids", not "adulterated".
  - *Sugestão:* Trocar a chave para euda2025nps.
- **L65** `[@euda2024threat]`: Page mentions adulteration and poisoning risk but not rising hospitalisations.
- **L74** `[@nature2021cannabis]`: Claim of 50-70% reduction with 100% renewables not found in the abstract; study is US-only, so "Portuguese grid" is not supported.
  - *Sugestão:* Retirar ou citar fonte para a rede portuguesa.
- **L78** `[@nature2021cannabis]`: 22.7 kg CO2/kg is from New Frontier Data 2018 (electricity only), not this paper. Paper reports about 42% (greenhouse) and 96% (outdoor) reductions, not 99%.
  - *Sugestão:* Corrigir valores e fonte.
- **L79** `[@marijuanamoment2024outdoor]`: Source says up to 76% reduction; "75% outdoor -> 80% reduction" not in it.
  - *Sugestão:* Usar "ate 76%".
- **L80** `[@lampoon2024hemp]`: Source: 8-22 t CO2/ha/year (citing Hudson Carbon), heat tolerance to 35 C. No 8-12 t per harvest, no 15-20 t with two harvests, no Portugal.
  - *Sugestão:* Usar 8-22 t CO2/ha/ano.
- **L113** `[@euda2024threat]`: "Fewer emergency visits with tested products" is not in the source.
- **L119** `[@ribeiro2024economic]`: EUR 52-151M is projected tax revenue, not the market currently controlled by illegal networks.
  - *Sugestão:* Reformular como receita fiscal potencial, ou citar o 36-58 t para o mercado.
- **L127** `[@cannareporter2025medicinal]`: Artigo CannaReporter (L. Sousa, 12/06/2025) nao contem estatisticas sobre mercado negro nem 95%; so diz que os produtos sao caros e nao comparticipados.
  - *Sugestão:* Idem.
- **L138** `[@cannareporter2025medicinal]`: Artigo CannaReporter (L. Sousa, 12/06/2025) nao contem estatisticas sobre mercado negro nem 95%; so diz que os produtos sao caros e nao comparticipados.
  - *Sugestão:* Idem.
- **L139** `[@euda2025nps]`: "800x" is not in EUDA. It comes from OASAS and refers to synthetic cannabinoids generally.
  - *Sugestão:* Citar oasas2024synthetic para 2-800x e especificar que e sobre canabinoides sinteticos.
- **L143** `[@ribeiro2024economic]`: EUR 52-151M is projected tax revenue, not funds for non-profit clubs.
  - *Sugestão:* Remover a ligacao aos clubes sem fins lucrativos ou citar outra fonte.
- **L149** `[@Jackson2016]`: Two twin cohorts; no dose-response, no greater IQ decline versus abstinent co-twins, attributed to familial factors. Does not say risk is concentrated in heavy users.
  - *Sugestão:* Descrever como estudo de gemeos que nao encontrou efeito causal.

### 07-pilar-medicinal.md

- **L17** `[@eco2024]`: ECO: 32.558 kg em 2024 (+172%), nao 18 t / +54%. 18.521 kg e o valor de Infarmed a 2024 3T (so 9 meses) e 54% resulta de comparar 9 meses de 2024 com 12 meses de 2023 (11.973 kg).
  - *Sugestão:* Citar [@infarmed2024] e dizer 'ate ao 3.o trimestre de 2024, 18,5 t (vs 12,0 t em todo 2023)'; ou citar ECO para 32,6 t no ano e +172%.
- **L23** `[@cannareporter2021]`: Sativex 37% comparticipacao and EUR 300 cost not mentioned.
- **L26** `[@cannareporter2021]`: Stigma not discussed.
- **L32** `[@lancet2024germany]`: Paper (accepted 24 Apr 2024, published Jul 2024) cannot describe an Oct 2024 change; text discusses medical cannabis only as risk of misuse and says CanG will "ease prescription rules"; no mention of 16 specialties or insurer pre-approval.
  - *Sugestão:* Remover citação; procurar fonte primária (G-BA/BfArM/BMG) para a regra de Outubro 2024, ou eliminar a afirmação.
- **L70** `[@norml2024]`: "20-35% reductions" and "EUR 2,000-5,000 per patient" not in source; it reports about 5.9-6.4% lower opioid prescribing (JAMA Intern Med 2018). Advocacy source.
  - *Sugestão:* Usar o valor de cerca de 6%.
- **L124** `[@kuhathasan2022]`: DOI resolves to a CBD pilot RCT (n=30), not a meta-analysis, and not about THC or CBN. CBD similar to placebo for most outcomes.
  - *Sugestão:* Substituir por fonte correta.

### 08-pilar-recreativa.md

- **L117** `[@wootten2023ontario]`: Paper reports the opposite: 'we did not find evidence of increases in health service use or incident cases of psychotic disorders over the short-term (17 month) period following cannabis legalization'. Increasing trends in substance-induced psychotic disorders were seen over 2014-2020 (pre-existing), and a longer window is needed.
  - *Sugestão:* Reescrever: sem evidência de aumento a curto prazo (17 meses); tendência pré-existente de psicoses induzidas por substâncias; necessária observação mais longa.
- **L275** `[@kcang2024]`: Section 24 only requires fees in statutes; section 25 limited to propagation material cost reimbursement. Profit ban stems from the non-profit purpose, not these sections. cannabusinessplans2024cscs is not in this audit.
  - *Sugestão:* Reescrever sem atribuir a "no profit" aos sections 24-25.
- **L317** `[@acog2025cannabis]`: ACOG Clinical Consensus No. 10 says nothing about product labelling, pictograms or label size.
  - *Sugestão:* Citar outra fonte para rotulagem, ou remover a atribuição à ACOG.
- **L371** `[@sciety2025illicit]`: '7 of 27 illicit samples with heavy metals above limits' is not in the paper (50 illicit and 50 licensed samples). Paper says As, Cd, Pb, Hg more prevalent in illicit; Cr higher in licensed; several metals exceeded USP limits in one or both groups.
  - *Sugestão:* Substituir pelo que o preprint reporta.
- **L381** `[@canndelta2024germany]`: Page (Cloudflare-blocked; read once with browser UA) has nothing on mandatory lab testing for clubs. Also line 381 cites a broken key eurofins2024cannabis; bib key is eurofins2024.
  - *Sugestão:* Remover ou citar fonte adequada; corrigir chave para eurofins2024.
- **L421** `[@eurofins2024cannabis]`: Nothing about seeds or licensed seed suppliers; KCanG section 20 only regulates propagation material transfer by clubs.
  - *Sugestão:* Retirar.
- **L439** `[@ivv2025]`: DCP is an obligation of all economic operators who harvested grapes; only exemption is for cooperative-associated growers who delivered all grapes and kept the right to vinify under 10 hl for household use. Home production up to 1,000 L without declaration is not stated.
  - *Sugestão:* Corrigir ou citar o DL 213/2004 / norma vitivinícola.
- **L560** `[@cmslaw2024]`: No "37 licensed companies" in the guide.
  - *Sugestão:* Citar fonte que contenha o número (Infarmed).
- **L592** `[@springer2024zurican]`: The 21 points of sale were 10 pharmacies, 10 cannabis social clubs and the DIZ (municipal drug information centre); no producers operated POS.
  - *Sugestão:* Corrigir para farmácias, clubes e centro municipal de informação sobre drogas.
- **L709** `[@lancet2024germany]`: Paper has no mention of an information campaign, Bild, "Cannabis-Chaos" or BMG data publication; it is a critical commentary on risks of the German model.
  - *Sugestão:* Remover citação ou substituir por fonte do BMG/BIÖG e imprensa alemã.
- **L832** `[@colorado2022tax]`: $423M is calendar 2021; 2022 is $325M. Allocation percentages 37/26/12 are not on this page.
  - *Sugestão:* Corrigir ano/valor e citar fonte da alocação.
- **L993** `[@ribeiro2024economic]`: "Mercado total PT EUR 52-151M" mislabels tax revenue as market size.
  - *Sugestão:* Corrigir para receita fiscal projetada (52,7-70,8 M conservador; 151,3 M otimista).
- **L1111** `[@talkingdrugs2024]`: No 37% in the text. Radío estimated ~USD 25M diverted from narcotrafficking in 2024, roughly half of the Uruguayan cannabis market.
  - *Sugestão:* Remover ~37% ou citar fonte.
- **L1112** `[@businesscannabis2025b]`: Percentagem ~2% de elegiveis com acesso nao consta da fonte.
  - *Sugestão:* Citar fonte que contenha esse valor ou retirar.
- **L1117** `[@talkingdrugs2024]`: '~14% of registered' not in text: 14,000 registered home cultivators and 249 clubs as of 2022; no percentage.
  - *Sugestão:* Remover a percentagem ou calcular com fonte explícita.

### 09-pilar-canhamo.md

- **L9** `[@psmarketresearch2024]`: Page: 2024 global market USD 20.1B, Europe largest region, THC limit raised 0.2% to 0.3%. '31% of global market' / ~40% not found (31.01% for 2023 is from Fortune Business Insights).
  - *Sugestão:* Corrigir citação ou valor.
- **L27** `[@lampoon2024hemp]`: 8-12 t / 15-20 t values, two harvests and Portugal not in source.
  - *Sugestão:* Usar 8-22 t CO2/ha/ano.
- **L88** `[@lampoon2024hemp]`: Same unsupported per-harvest and Portugal claims.
  - *Sugestão:* Usar 8-22 t CO2/ha/ano.

### 10-posicoes-partidarias.md

- **L26** `[@publico2021js]`: Cited URL is an unrelated article. Correct source (Lusa, 21 Jun 2021) covers JS motion at PS congress; adoption outcome not stated, 'posicao nao foi adoptada' unverified.
  - *Sugestão:* Replace URL; for 'since at least 2019' add https://www.publico.pt/2019/01/18/politica/noticia/js-quer-colocar-legalizacao-canabis-programa-governo-ps-1858461
- **L26** `[@publico2023ps]`: Costa Matos and the 'maioria absoluta' appeal are not in this article.
  - *Sugestão:* Use https://www.publico.pt/2022/12/18/politica/noticia/lider-js-ps-aproveitar-maioria-absoluta-legalizar-cannabis-2031938 (Lusa, 18 Dec 2022).
- **L89** `[@government2023netherlands]`: government.nl page is about the toleration policy and 2013 resident criterion; no Maastricht pilot. Wietexperiment covers 10 municipalities, started Dec 2023 (Breda, Tilburg), full phase 7 Apr 2025, runs to 2029 with an evaluation due; national rollout not planned.
  - *Sugestão:* Rename 'Experimento Wietexperiment (10 municipios)'; replace 'planeia expansao nacional' with 'avaliacao final prevista'; cite a Wietexperiment source.

### 13-anexo-a-clubes.md

- **L39** `[@natgeo2024amsterdam]`: No 58% and no 3 million figure; no i-criterium or black-market failure. Halsema 'blight on the city...' is NatGeo's paraphrase; article only says the mayor proposed banning foreigners from coffeeshops.
  - *Sugestão:* Remove the figures or find a source; present Halsema as paraphrase.
- **L39** `[@schengen2024amsterdam]`: Confirms public smoking ban in the Red-Light District; does not support 58%, 3 million, the quote or i-criterium failing from black-market fears.
  - *Sugestão:* Cite only for the smoking ban.

### 16-anexo-d-argumentacao.md

- **L59** `[@transform2020]`: A fonte recomenda o contrario: "An age threshold at or near 18 would seem to be realistic starting point"; alerta que idade acima da do alcool pode "preference alcohol for the intervening age period" e que o 21 do Quebeque pode empurrar jovens adultos para o mercado nao regulado.
  - *Sugestão:* "Idade minima de 21 anos (opcao mais restritiva do que a sugerida pela Transform, que aponta para ~18)" ou retirar a citacao e justificar o 21 com outra fonte.
- **L69** `[@di2019]`: O estudo trata apenas de psicose; nao aborda dependencia nem impacto cognitivo.
  - *Sugestão:* Retirar [@di2019] de "dependencia, impacto cognitivo"; usar fontes proprias (p.ex. leung2020 para dependencia; fonte cognitiva a verificar).
- **L82** `[@nugent2017]`: No Portuguese prevalence in source; ~10% matches sicad2022 (10.5%).
  - *Sugestão:* [@sicad2022]
- **L89** `[@nugent2017]`: Wrong source for 10.5%.
  - *Sugestão:* [@sicad2022] (15-74 anos)
- **L98** `[@suraev2020insomnia]`: Review has 5 studies (2 RCTs, 3 non-randomised), 219 participants, all poor quality; no SMD 0.60; '6 trials, 1,077 patients' not in it.
  - *Sugestão:* Rename key bhagavan2020insomnia; remove numbers or find source.
- **L109** `[@suraev2020insomnia]`: same
- **L118** `[@drug2024]`: Pagina aberta: comunicado da Drug Policy Alliance (18/12/2025) sobre reescalonamento da marijuana nos EUA; nao menciona Portugal, EUR 150 nem comparticipacao.
  - *Sugestão:* [@euronews2024]
- **L128** `[@suraev2020insomnia]`: same
- **L133** `[@hauser2022bmc]`: 'Evidencia robusta THC' not supported: all other effects have low, very low or no grade.
  - *Sugestão:* Rename key bilbao2022bmc; soften.
- **L140** `[@rock2024opioids]`: Revisão narrativa sobre cannabis medicinal como terapêutica emergente para perturbação por uso de opióides (craving/abstinência); nada sobre substituir medicação 'mais cara' nem poupanças. Resumo (Europe PMC): potencial, mas 'a paucity of rigorous randomised controlled trials'.
  - *Sugestão:* Retirar o argumento de custo ou usar outra fonte; esta serve apenas para: pode reduzir craving/abstinência em OUD (evidência observacional).
- **L140** `[@publico2023consumidor]`: O artigo dá 71% para stress/relaxar (não 84%) e refere-se a consumidores de produtos CBD/baixo THC legais comprados em lojas (n=928), não a consumo ilegal de cannabis.
  - *Sugestão:* Usar apenas @cannareporter2022stress para o 84%; retirar esta citação.
- **L148** `[@ncbi2024opioids]`: Página bloqueada por reCAPTCHA (WebFetch, PubMed, Europe PMC sem resumo); conclusões obtidas por pesquisa web sobre o relatório CADTH: 'Evidence is inconsistent and of very low to moderate quality ... lack of consensus ... whether use of cannabis in OUD is beneficial or detrimental'; uma guideline canadiana 'strongly recommends against' canabinóides para OUD. Trata de OUD, não de dor crónica, e não sustenta 'evidência promissora'. Confiança média (fonte lida só via excerto).
  - *Sugestão:* Retirar @ncbi2024opioids como apoio de 'promissora', ou citá-lo como contra-evidência: evidência inconsistente e de qualidade muito baixa a moderada.
- **L154** `[@publico2023consumidor]`: 84% não consta; o artigo diz 71% (stress/relaxar) e o universo é outro (produtos CBD de lojas).
  - *Sugestão:* Retirar @publico2023consumidor desta linha.
- **L172** `[@portugal2025oe]`: O comunicado só dá valores per capita (€1.660,88 por utente) e metas; não contém o total de 17,3 mil milhões nem os 92%.
  - *Sugestão:* Manter apenas @publico2025oe2026 para os 17,3 mil milhões; retirar @portugal2025oe desta frase (ou usá-lo para o valor per capita).
- **L177** `[@norml2024opioids]`: A fonte não trata de comparticipação do SNS, de internamentos nem de custo; nada sustenta que 'há potencial de substituir medicação mais cara ou reduzir internamentos'.
  - *Sugestão:* Retirar a justificação de custos ou citar estudo farmacoeconómico; manter só a referência à substituição de opiáceos como hipótese.
- **L177** `[@rock2024opioids]`: A fonte não trata de comparticipação, custos nem internamentos.
  - *Sugestão:* Retirar esta citação desta frase.
- **L192** `[@ncbi2024opioids]`: Idem: o relatório conclui evidência inconsistente e sem consenso sobre benefício; não apoia 'substituir opiáceos'.
  - *Sugestão:* Idem; reformular como 'evidência inconclusiva'.
- **L204** `[@drug2024]`: Pagina aberta: comunicado da Drug Policy Alliance (18/12/2025) sobre reescalonamento da marijuana nos EUA; nao menciona Portugal, EUR 150 nem comparticipacao.
  - *Sugestão:* [@euronews2024]; reformular 'EUR 150/mes' para 'EUR 150 por caixa de 15 g'.
- **L213** `[@infarmed2024prescricoes]`: Document lists no indications (no epilepsia/espasticidade found).
  - *Sugestão:* Cite another source for indications.
- **L213** `[@lei332018]`: A Lei 33/2018 não contém lista de indicações terapêuticas ("não há lista específica"; remete para o Infarmed). As indicações estão na Deliberação 11/CD/2019. A lista do texto (4 de 7) é parcial e não refere as restantes. A outra fonte citada (@infarmed2024prescricoes) não estava neste lote.
  - *Sugestão:* Citar a Deliberação n.º 11/CD/2019 do Infarmed em vez (ou além) da Lei; indicar que são 4 das 7 indicações.
- **L215** `[@drug2024]`: Pagina aberta: comunicado da Drug Policy Alliance (18/12/2025) sobre reescalonamento da marijuana nos EUA; nao menciona Portugal, EUR 150 nem comparticipacao.
  - *Sugestão:* [@euronews2024]
- **L238** `[@drug2024]`: Pagina aberta: comunicado da Drug Policy Alliance (18/12/2025) sobre reescalonamento da marijuana nos EUA; nao menciona Portugal, EUR 150 nem comparticipacao.
  - *Sugestão:* [@euronews2024]; 'por mes' nao esta na fonte.
- **L258** `[@bundesministerium2024]`: A fonte diz o contrario ou nada: "Cannabis seeds may be imported from EU Member States for the purpose of private self-cultivation... purchasing of cannabis online or via distance sales... admissible"; associacoes de cultivo podem passar ate 7 sementes ou 5 estacas por mes a nao membros. Nao ha exigencia de fornecedor autorizado nem THC maximo certificado.
  - *Sugestão:* Propomos que as sementes so possam ser compradas a fornecedores autorizados (medida portuguesa, distinta da alema)
- **L268** `[@bundesministerium2024]`: A fonte diz o contrario ou nada: "Cannabis seeds may be imported from EU Member States for the purpose of private self-cultivation... purchasing of cannabis online or via distance sales... admissible"; associacoes de cultivo podem passar ate 7 sementes ou 5 estacas por mes a nao membros. Nao ha exigencia de fornecedor autorizado nem THC maximo certificado.
  - *Sugestão:* Proposta: sementes certificadas com THC maximo rotulado (sem equivalente na lei alema)
- **L279** `[@bundesministerium2024]`: A fonte diz o contrario ou nada: "Cannabis seeds may be imported from EU Member States for the purpose of private self-cultivation... purchasing of cannabis online or via distance sales... admissible"; associacoes de cultivo podem passar ate 7 sementes ou 5 estacas por mes a nao membros. Nao ha exigencia de fornecedor autorizado nem THC maximo certificado.
  - *Sugestão:* Apresentar como proposta portuguesa, nao como regra alema.
- **L283** `[@bundesministerium2024]`: A fonte diz o contrario ou nada: "Cannabis seeds may be imported from EU Member States for the purpose of private self-cultivation... purchasing of cannabis online or via distance sales... admissible"; associacoes de cultivo podem passar ate 7 sementes ou 5 estacas por mes a nao membros. Nao ha exigencia de fornecedor autorizado nem THC maximo certificado.
  - *Sugestão:* Apresentar como proposta portuguesa, nao como regra alema.
- **L291** `[@bundesministerium2024]`: A fonte diz o contrario ou nada: "Cannabis seeds may be imported from EU Member States for the purpose of private self-cultivation... purchasing of cannabis online or via distance sales... admissible"; associacoes de cultivo podem passar ate 7 sementes ou 5 estacas por mes a nao membros. Nao ha exigencia de fornecedor autorizado nem THC maximo certificado.
  - *Sugestão:* Alemanha: sementes importaveis da UE ou fornecidas por associacoes de cultivo (ate 7 sementes/5 estacas por mes a nao membros); sem certificacao oficial de THC maximo
- **L295** `[@nutt2010]`: O estudo nao fala de autocultivo de vinho nem de Portugal.
  - *Sugestão:* Retirar a chave.
- **L409** `[@marijuanamoment2025]`: 6,7%->6,1% nao esta na fonte.
  - *Sugestão:* Retirar numeros ou citar EKOCAN com valor verificado.
- **L410** `[@leung2020]`: Leung nao contem dados SICAD/Portugal; ICAD mostra 1,3% estavel 2012-2022 em 15-34 anos.
  - *Sugestão:* Retirar a linha ou substituir pelo valor ICAD verificado e chave carapinha2024icad.
- **L418** `[@bessergrowen2025]`: O artigo nao refere Portugal/overdoses.
  - *Sugestão:* Trocar a chave por fonte verificada sobre mortes por overdose em Portugal (ex.: EUDA country report ou greenwald2009 se contiver; nao verificado).
- **L418** `[@manthey2024]`: HIV -98% nao esta nesta fonte (trata de tratamento de cannabis na Alemanha).
  - *Sugestão:* Manter overdose [@bessergrowen2025]; atribuir HIV a fonte que o contenha. Substituir por fonte que contenha a serie HIV 907 (2000) -> 18 (2017) (candidato a verificar: relatorios nacionais EMCDDA/EUDA sobre Portugal, ou Transform Drugs 'Drug decriminalisation in Portugal: setting the record straight'); nao verificado por mim.
- **L424** `[@bessergrowen2025]`: Idem.
  - *Sugestão:* Trocar a chave por fonte verificada sobre mortes por overdose em Portugal (ex.: EUDA country report ou greenwald2009 se contiver; nao verificado).
- **L425** `[@manthey2024]`: Fonte nao contem HIV nem Portugal.
  - *Sugestão:* Substituir por fonte que contenha a serie HIV 907 (2000) -> 18 (2017) (candidato a verificar: relatorios nacionais EMCDDA/EUDA sobre Portugal, ou Transform Drugs 'Drug decriminalisation in Portugal: setting the record straight'); nao verificado por mim.
- **L434** `[@bessergrowen2025]`: Idem; tambem nao ha HIV -98%.
  - *Sugestão:* Trocar a chave por fonte verificada sobre mortes por overdose em Portugal (ex.: EUDA country report ou greenwald2009 se contiver; nao verificado).
- **L434** `[@manthey2024]`: HIV -98% nao esta na fonte.
  - *Sugestão:* Retirar [@manthey2024] deste ponto; Substituir por fonte que contenha a serie HIV 907 (2000) -> 18 (2017) (candidato a verificar: relatorios nacionais EMCDDA/EUDA sobre Portugal, ou Transform Drugs 'Drug decriminalisation in Portugal: setting the record straight'); nao verificado por mim.
- **L436** `[@springer2021pt]`: Os valores 8,2% vs 8,3% nao constam do artigo; 'refuta previsoes catastrofistas' excede a cautela causal do artigo.
  - *Sugestão:* Citar [@euda2024cannabis] para os valores; para Springer: 'prevalencia permaneceu relativamente baixa, sem relacao causal linear demonstravel'.
- **L443** `[@nugent2017]`: Wrong source; also Portugal decriminalised use (2001), so "A proibição não impediu" is imprecise for consumption.
  - *Sugestão:* [@sicad2022]; reformular "proibição da oferta/mercado".
- **L447** `[@nugent2017]`: Wrong source.
  - *Sugestão:* [@sicad2022]
- **L456** `[@marijuanamoment2025]`: 6,7%->6,1% nao esta na fonte; 'no primeiro ano' tambem nao.
  - *Sugestão:* Idem.
- **L462** `[@nugent2017]`: Wrong source.
  - *Sugestão:* [@sicad2022]
- **L465** `[@marijuanamoment2025]`: 6,7%->6,1% nao esta na fonte.
  - *Sugestão:* Idem.
- **L490** `[@businesscannabis2025a]`: Artigo cita o Ministerio do Interior: 'no evidence partial legalisation has curbed the illegal market'. Nao ha evidencia de reducao do mercado negro na Alemanha.
  - *Sugestão:* Retirar [@businesscannabis2025a] desta afirmacao; manter apenas [@healthcanada2024] se este a apoiar.
- **L490** `[@cdphe2024]`: Inquérito descritivo (13% em 2023, sem mudança vs 2021); não avalia efeito da legalização.
  - *Sugestão:* Citar estudos causais (ex.: revisões sobre legalização e consumo juvenil) ou suavizar para "não há evidência de aumento".
- **L507** `[@greenwald2009]`: Source from 2009 covers ~8 years, not 25 years of data.
  - *Sugestão:* Citar fonte recente (ex. relatório SICAD/ICAD 2025) para "25 anos".
- **L511** `[@greenwald2009]`: Same: 2009 paper cannot document 25 years.
  - *Sugestão:* Idem.
- **L521** `[@greenwald2009]`: Same: no 2001-2026 data in a 2009 paper.
  - *Sugestão:* Idem.
- **L521** `[@bessergrowen2025]`: Idem.
  - *Sugestão:* Trocar a chave por fonte verificada sobre mortes por overdose em Portugal (ex.: EUDA country report ou greenwald2009 se contiver; nao verificado).
- **L521** `[@manthey2024]`: Fonte sobre Alemanha nao apoia '25 anos de dados de descriminalizacao em Portugal'.
  - *Sugestão:* Retirar [@manthey2024].
- **L523** `[@cdphe2024]`: Página não menciona 24 estados nem dados multi-anos.
  - *Sugestão:* Citar fonte para nº de estados (NCSL/MPP).
- **L525** `[@torresmoreno2023]`: Same as 02:49: wrong key.
  - *Sugestão:* [@ribeiro2024] se confirmado.
- **L555** `[@leung2020]`: Idem.
  - *Sugestão:* Retirar a linha ou substituir pelo valor ICAD verificado; nao descrever como "sob proibicao" um aumento que a fonte nao mostra.
- **L565** `[@cdphe2024]`: Página tem só dados de 2023 (e comparação com 2021); "10+ anos do Colorado" não consta.
  - *Sugestão:* Citar série HKCS completa ou MPP.
- **L569** `[@bessergrowen2025]`: Idem; a queda de 78% e calculo (369->80) sem fonte no artigo.
  - *Sugestão:* Trocar a chave por fonte verificada sobre mortes por overdose em Portugal (ex.: EUDA country report ou greenwald2009 se contiver; nao verificado).
- **L569** `[@manthey2024]`: HIV -98% nao esta na fonte.
  - *Sugestão:* Retirar [@manthey2024]; Substituir por fonte que contenha a serie HIV 907 (2000) -> 18 (2017) (candidato a verificar: relatorios nacionais EMCDDA/EUDA sobre Portugal, ou Transform Drugs 'Drug decriminalisation in Portugal: setting the record straight'); nao verificado por mim.
- **L580** `[@infarmed2024]`: Infarmed PDF nao contem ranking de exportadores (so quantidades e destinos).
  - *Sugestão:* [@cannareporter2024; @eco2024] (ambos afirmam 2.o a nivel mundial, atras do Canada).
- **L580** `[@euronews2024]`: Euronews (A. Elci, 19-21/04/2024) so diz 'second biggest producer of cannabis in the EU' (34 t declaradas para 2024); nao e ranking mundial de exportadores e, sendo de abril 2024, nao pode conter dados de 2025.
  - *Sugestão:* Citar [@cannareporter2024; @eco2024].
- **L587** `[@cdphe2024]`: Nem 24 estados nem 10+ anos constam na página.
  - *Sugestão:* Citar fonte para estados e série temporal.
- **L590** `[@infarmed2024]`: Infarmed PDF nao contem ranking de exportadores.
  - *Sugestão:* [@cannareporter2024; @eco2024]
- **L590** `[@euronews2024]`: Euronews (A. Elci, 19-21/04/2024) so diz 'second biggest producer of cannabis in the EU' (34 t declaradas para 2024); nao e ranking mundial de exportadores e, sendo de abril 2024, nao pode conter dados de 2025.
  - *Sugestão:* Citar [@cannareporter2024; @eco2024].

### chapters/04-ciencia.md

- **L17** `[@unnews2020]`: Notícia da UN News sobre reclassificação na CND; não contém a meta-análise de Marconi nem OR 3,90.
  - *Sugestão:* Substituir por [@marconi2016].
- **L18** `[@dezeen2021]`: URL aponta para artigo sobre cânhamo que sequestra carbono; nada sobre EU-GEI, psicose ou potência.
  - *Sugestão:* Substituir por [@di2019] (Di Forti et al. 2019, Lancet Psychiatry 6:427-436: uso diário de cannabis de alta potência, OR 4,8).
- **L35** `[@hanway2022]`: Página é o lançamento de relatório de mercado (Recreational Europe); não trata de medidas de mitigação de riscos baseadas em modelos internacionais.
  - *Sugestão:* Citar fontes sobre modelos (p.ex. [@bundesministerium2024]) ou retirar.
- **L35** `[@cleirec2025]`: Entrada fabricada: o URL é o EU-GEI (Di Forti 2019), que não trata de "medidas baseadas em modelos internacionais".
  - *Sugestão:* Remover [@cleirec2025]; citar fontes sobre modelos regulatórios.
- **L128** `[@autor2024]`: Sem fonte identificável; a entrada é um placeholder.
  - *Sugestão:* Substituir por fonte real (p.ex. [@di2019] para uso diário + alta potência) ou suavizar a frase.
- **L144** `[@cdphe2024monitoring]`: Prevalência adulta no Colorado ~19% nos dados consultados, não 13-15%.
  - *Sugestão:* Corrigir intervalo e citar o valor com ano.
- **L144** `[@brfss2023cannabis]`: Fonte é a página inicial do BRFSS; sem os valores. Prevalência do Colorado ~19% noutros dados.
  - *Sugestão:* Citar tabela BRFSS específica.
- **L200** `[@colorado2023dui]`: Página CDOT não contém 5 ng/ml, "permissible inference", multa ou suspensão.
  - *Sugestão:* Citar C.R.S. 42-4-1301 ou página do DMV/CDOR.
- **L212** `[@colorado2023dui]`: Fonte não sustenta o modelo do Colorado descrito.
  - *Sugestão:* Idem.

### chapters/05-modelos-internacionais.md

- **L173** `[@autor2024]`: Placeholder usado para afirmação distinta (preferências de consumidores mercado legal/ilegal); sem fonte.
  - *Sugestão:* Citar estudo sobre escolha de mercado legal vs ilegal ou retirar.
- **L189** `[@apnews2022thailand]`: AP refere as primeiras 100 mudas; 1 milhão era plano, não distribuição pessoal em Buriram.
  - *Sugestão:* Corrigir para "planeou distribuir 1 milhão".
- **L197** `[@lexology2026thailand]`: Citação "estão a queimar o campo" não consta da fonte.
  - *Sugestão:* Remover ou citar fonte.
- **L224** `[@espad2023]`: 0,2%->1,3% e 6,5x não encontrados; ESPAD Portugal consumo de cannabis ~3,8% (2019) -> 3,7% (2023).
  - *Sugestão:* Corrigir/retirar.

### chapters/08-pilar-recreativa.md

- **L710** `[@healthcanada2024]`: O resumo do inquérito não refere campanhas "Don't Drive High".
  - *Sugestão:* Citar página de educação pública da Health Canada.

### chapters/12-conclusao.md

- **L14** `[@hanway2022]`: Página: "55% of Europeans in favour of legal and regulated cannabis sales to over-18s" (8 mercados); não contém 59% nem Portugal.
  - *Sugestão:* Corrigir para 55% (Europa) ou localizar sondagem portuguesa e citá-la.

### chapters/16-anexo-d-argumentacao.md

- **L488** `[@unnews2020]`: Uma notícia da UN News sobre a CND não é um "relatório da OMS" nem um estudo de danos.
  - *Sugestão:* Citar o documento da OMS (ECDD) ou retirar a referência.
- **L497** `[@unnews2020]`: Lista "Estudos sobre danos"; a fonte é notícia sobre decisão da CND, não estudo de danos da OMS.
  - *Sugestão:* Citar a recomendação/relatório ECDD da OMS ou retirar.

## Citações parcialmente apoiadas (254)


### 01-sumario-executivo.md

- **L36** `[@cannabislaw2024export]`: A fonte afirma 99,85% exportado vs 17 kg vendidos localmente (2023), mas fala de exportacoes vs vendas, nao de 'producao'.
  - *Sugestão:* 'Portugal exportou em 2023 cerca de 99,85% do que vendeu (exportacoes vs vendas no mercado interno)'; EUR 150/mes: ver nota sobre drug2024.
- **L49** `[@cambridge2022hemp]`: URL cam.ac.uk/stories/industrial-hemp devolve 404; sem acesso a pagina. Via alternativa: Dezeen (30/06/2021) cita o investigador de Cambridge Darshil Shah: 'Industrial hemp absorbs between 8 to 15 tonnes of CO2 per hectare of cultivation'; florestas 2-6 t/ha/ano; depende do metodo de cultivo. Nao diz 'por ciclo' nem 'condicoes UK/Irlanda'. '2-4x mais que florestas' e '8-12 t em Portugal' nao constam (8-12 vs 2-6 da 1,3 a 6x; e hemp por cultivo vs floresta por ano).
  - *Sugestão:* 'Estimativas de um investigador de Cambridge apontam 8-15 t CO2/ha de canhamo (vs 2-6 t/ha/ano em florestas) [@dezeen2021hemp]; nao ha estimativa verificada para Portugal.'
- **L49** `[@carboncredits2024hemp]`: carboncredits.com (autor 'Jennifer L', 2022, act. 2024): 'a hectare of hemp can absorb between 8-15 tonnes of CO2'; cita um investigador de Cambridge. E fonte secundaria da mesma afirmacao (nao e corroboracao independente); nao diz 'por ciclo' nem UK; nao 'validated by Cambridge research'.
  - *Sugestão:* Ver cambridge2022hemp.
- **L74** `[@statcan2019youth]`: Rotermann (Health Reports, 19/02/2020): 'Early indications from this NCS study suggests use among Canadian youth has not increased'; 'The cross-sectional nature of the data does not allow for causal inferences'. Dados 2018 vs 2019 (cerca de 1 ano pos-legalizacao). '6 anos de dados' nao corresponde; subida 36%->41-43% (CCS) nao esta nesta fonte.
  - *Sugestão:* 'Canada (dados 2018-2019): estudo da Statistics Canada indica que o consumo juvenil nao aumentou nesse primeiro ano; os dados CCS mais recentes: [citar fonte propria]'
- **L95** `[@statcan2019youth]`: Rotermann (Health Reports, 19/02/2020): 'Early indications from this NCS study suggests use among Canadian youth has not increased'; 'The cross-sectional nature of the data does not allow for causal inferences'. Dados 2018 vs 2019 (cerca de 1 ano pos-legalizacao). 'Canada (6 anos)' nao corresponde: fonte cobre ~1 ano.
  - *Sugestão:* 'Canada (primeiro ano pos-legalizacao)'
- **L95** `[@coley2024]`: JAMA Pediatrics 2024;178(6):622-625 (research letter, repeated cross-sectional, YRBS 2011-2021, 47 estados dos EUA): 'RCL was associated with modest decreases in cannabis, alcohol, and e-cigarette use'; RCR: 'lower likelihood but also increased frequency of cannabis use among users, leading to no overall change'; 'no net increases'. Estudo e sobre estados dos EUA, nao Colorado nem Canada.
  - *Sugestão:* Citar [@coley2024] para 'estados dos EUA' separadamente.
- **L101** `[@lancet2024germany]`: Paper: "In October of 2022, the Ministry of Health outlined the core pillars ... White Paper"; approved by parliament 23 Feb 2024, in effect 1 Apr 2024 (so ~18 months is own arithmetic). But the paper covers only step 1 (possession/home growing/clubs); step 2 (commercial) "remains uncertain whether ... will be realized at all"; no cabinet date.
  - *Sugestão:* Reformular: "Alemanha CanG 2024 (cerca de 18 meses entre o Eckpunktepapier de Outubro 2022 e a entrada em vigor em Abril 2024, apenas na 1.ª fase, sem mercado comercial)".

### 02-panorama-portugues.md

- **L19** `[@prohibition2025]`: Table 2023 value 11,973 kg matches page ("2023's 11.97 tonnes"), and page cites INFARMED as data source; but the 2024 value 32,558 kg is not there (page: "over 18 tonnes in the first three quarters of 2024").
  - *Sugestão:* Para 2024 citar a fonte que contém 32.558 kg (eco2024), não prohibition2025.
- **L65** `[@carapinha2024icad]`: O relatorio existe e contem os dados de consumo problematico, mas e de 2025 (dados 2022-2023), nao "ICAD, 2024"; os dados aqui listados (25-35%, 32%/19%, trauma) provem em parte do Observador.
  - *Sugestão:* "Um estudo recente do ICAD (2025)..."; corrigir texto/cabecalho "novos dados ICAD 2024".
- **L92** `[@observador2026cannabis]`: Citacao nao e literal. Original (dita ao Publico): "As raparigas que ja tem um percurso desviante ou que se encontram em situacoes de vulnerabilidade apresentam uma maior sobrecarga de fatores de risco, nomeadamente associada a experiencias e situacoes de trauma face aos rapazes". Sentido preservado, mas "carregam maior peso" e parafrase entre aspas; e a declaracao foi ao Publico, relatada pelo Observador.
  - *Sugestão:* Usar a citacao literal ou tirar as aspas; "(Carapinha, citada pelo Observador/Publico)".
- **L123** `[@greenwald2009]`: Supports (per Cato overview as reported): "no adverse effect on drug usage rates ... none of the nightmare scenarios" - but data end c.2007-2008, advocacy white paper by a lawyer/journalist, not peer-reviewed; 8.2% vs 8.3% is not from it. Full text unreachable (403 on cato.org, SSRN).
  - *Sugestão:* Marcar que Greenwald (2009) cobre só ~8 anos e é policy paper; manter springer2021pt.

### 03-contexto-historico.md

- **L21** `[@releaf2023]`: Página: cânhamo português usado para velas de navios na Época dos Descobrimentos. Não menciona chegada ao Brasil em 1500 nem caravelas.
  - *Sugestão:* Navios dos Descobrimentos usavam cordas e velas de cânhamo [@releaf2023]; fonte de baixa qualidade (loja), preferir fonte histórica.
- **L21** `[@topshelfhemp2024]`: Artigo genérico: velas de cânhamo "powered the Age of Exploration"; sem Portugal, caravelas, Brasil.
  - *Sugestão:* Retirar ou reformular para "navios da Era dos Descobrimentos usavam velas de cânhamo"; fontes de loja de baixa qualidade.
- **L49** `[@camara2015]`: DL 420/70, 3 Set 1970, Ministério da Justiça, existe e criou lista de estupefacientes com penas de 2 a 8 anos. Mas não é a "primeira" lei: actualizou o Decreto 12.210 (1926) e há a Lei 1687 (1923); uma fonte indica que a cannabis já constava em 1926, outra que surge pela primeira vez em 1970 (conflito, não resolvido).
  - *Sugestão:* Portugal reforçou a proibição da cannabis pelo Decreto-Lei n.º 420/70, de 3 de Setembro de 1970, que actualizou o regime de 1926 [@ministerio_justica1970].
- **L87** `[@springer2021pt]`: Springer/PMC (Rego et al. 2021): Estrategia Nacional 1999; Lei 30/2000 aprovada em 29/11/2000; entrada em vigor julho 2001; 'These tendencies cannot be, however, linearly related with the decriminalization law per se'; prevalencia 'stayed reasonably low'; criticas: contradicoes, 'modest ambitions', acordao do STJ 2008 e aumento da punitividade; sem percentagens 8,2%/8,3%. 'Referencia mundial' e mais forte do que o artigo: 'internationally recognized' mas 'screen onto which drug policy agendas are projected' e contradicoes.
  - *Sugestão:* 'modelo internacionalmente reconhecido, embora com contradicoes e limites apontados na literatura [@springer2021pt]'
- **L87** `[@parlamento2000lei30]`: Art. 29.º confirma entrada em vigor a 1 Jul 2001. A lei não pode apoiar "25 anos depois, referência mundial".
  - *Sugestão:* Lei entrou em vigor em Julho de 2001 [@parlamento2000lei30]; "referência mundial" apoiar com springer2021pt/transform2016pt.
- **L115** `[@cannareporter2024]`: 1.157 prescricoes em 2023 confirmado (757 a 2024 3T); 17 kg e 0,05% nao constam do artigo.
  - *Sugestão:* Ver eco2024 (corrigir 0,05% para ~0,15%).
- **L117** `[@sicad2018condenacoes]`: SICAD 2018: "84% só cannabis" nas ocorrências CDT; "consumidores ocasionais" não aparece; 75% não consta.
  - *Sugestão:* Criminalização persistente: 84% dos processos nas CDT em 2018 envolveram apenas cannabis [@sicad2018condenacoes]
- **L117** `[@dn2020condenacoes]`: Artigo de opinião (Redação DN): "75% foi condenada por consumo de canábis" (dados SICAD 2021). Mede condenados, não processos CDT, e não fala de consumidores ocasionais.
  - *Sugestão:* Citar o relatório SICAD directamente: 75% dos condenados em 2021 por consumo, canábis [@dn2020condenacoes]; separar de CDT.

### 04-ciencia.md

- **L22** `[@leung2020]`: Leung: 33% (IC 22-44%) e o risco de dependencia (CD) em jovens com consumo regular "(weekly or daily)" em estudos de coorte; nao distingue diario/quase diario, nem e CUD geral. Os autores notam falta de dados de coorte para CUD em consumidores regulares.
  - *Sugestão:* "~33% (IC 95% 22-44%) dos jovens com consumo regular (semanal ou diario) desenvolvem dependencia (estudos de coorte) [@leung2020]". Verificar coffeeshop2024cud em separado.
- **L47** `[@carapinha2024icad]`: Relatorio: entre consumidores nos Centros Educativos (12 meses antes do internamento) 49% dos rapazes e 100% das raparigas com consumo de risco elevado. A afirmacao omite que e entre CONSUMIDORES, que e amostra institucional (censo de centros educativos, n nao indicado no relatorio) e nao permite generalizar; a recomendacao (formacao em trauma-informed care, referenciacao prioritaria) nao vem da fonte.
  - *Sugestão:* "...(ICAD: entre as consumidoras internadas em Centros Educativos, 100% com consumo de risco elevado vs 49% dos rapazes consumidores)"; marcar a recomendacao como proposta propria.
- **L47** `[@observador2026cannabis]`: Os numeros 100%/49% estao no artigo ("Entre os consumidores, o consumo de risco elevado chega a 100% nas raparigas contra 49% dos rapazes") mas referem-se a consumidores em centros educativos; omitido no texto.
  - *Sugestão:* Ver carapinha2024icad.
- **L175** `[@rogeberg2019]`: Abstract: "average increase in crash risk is estimated at 1.28 (1.16-1.40)"; "attributable risk fraction... below 2% for all but two of the included studies"; "increased crash risk... is low". Mas 1,28 e o risco relativo total de acidente do modelo bayesiano, nao um OR; o OR agrupado de acidente culpado e 1,42 (1,11-1,75) (OR tradicional 1,46, 1,24-1,72). "abaixo de 2% na maioria" e "em todos menos dois" de 13 estudos.
  - *Sugestão:* "Meta-analise Rogeberg (2019): aumento medio do risco de acidente de 1,28 (IC 95%: 1,16-1,40); risco de acidente culpado 1,42 (1,11-1,75). O autor conclui que o aumento do risco e baixo e que a fracao atribuivel esta abaixo de 2% em todos os estudos menos dois."
- **L179** `[@bundesministerium2024]`: Fonte: "approved on 6 June 2024... statutory THC limit of 3.5 ng/ml in blood serum... effective on 22 August 2024". Mas a equivalencia a 0,2 permil de alcool nao esta na pagina (vem de BesserGrowen, que cita a comissao de peritos).
  - *Sugestão:* Acrescentar [@bessergrowen2025] para a equivalencia 0,2 permil.
- **L188** `[@bessergrowen2025]`: Piloto na Renania-Palatinado (Trier) desde maio 2025 e validacao pela Universidade de Mainz confirmados; "3 minutos" e "one documented case", nao regra; piloto ainda em curso em nov 2025 (sem resultados finais).
  - *Sugestão:* "...resultados em cerca de 3 minutos num caso documentado; piloto ainda em avaliacao".
- **L202** `[@bundesministerium2024]`: Apoiado: 3,5 ng/ml serico, entrada em vigor agosto 2024, proibicao de consumo misto cannabis+alcool. Nao estao na pagina: saliva/urina 1,0 ng/ml, subida de 1,0 para 3,5, coima EUR 500 + 1 mes (BesserGrowen indica essas sancoes para o regime ANTIGO de 1,0 ng/ml, nao para o novo limite).
  - *Sugestão:* Retirar as sancoes da coluna "Alemanha 2024" ou rotula-las como regime anterior; citar fonte para sancoes actuais.
- **L202** `[@bessergrowen2025]`: Confirmados: 1,0 ng/ml nos testes, limite 3,5 desde agosto 2024, equivalencia 0,2 permil. As sancoes "EUR 500 + 1 mes" sao descritas para o regime antigo (1,0 ng/ml).
  - *Sugestão:* Rotular sancoes como regime anterior.
- **L207** `[@rogeberg2019]`: OR/risco 1,28 e conclusao "baixo" estao na fonte; "qualquer aumento justifica regulacao" e opiniao do documento, nao conclusao do autor. Tambem 1,28 nao e OR (ver linha 175).
  - *Sugestão:* "...Autor conclui que o risco e baixo [@rogeberg2019]; o presente documento entende que mesmo um aumento pequeno justifica regulacao."
- **L212** `[@bundesministerium2024]`: A pagina descreve apenas a lei alema; nao valida modelos nem fala de adaptacao a Portugal.
  - *Sugestão:* "Baseada nos modelos alemao, do Colorado e canadiano (descritos em ...)".
- **L212** `[@bessergrowen2025]`: O artigo so descreve a Alemanha; nao fundamenta modelo para Portugal.
  - *Sugestão:* Ver bundesministerium2024.

### 05-modelos-internacionais.md

- **L5** `[@bundesministerium2024]`: Pagina descreve a lei (KCanG) e a avaliacao, mas nao diz "1 de abril de 2024" nem que seja "o modelo mais relevante para Portugal"; esse juizo e do documento.
  - *Sugestão:* Acrescentar fonte para a data de entrada em vigor e marcar a relevancia como opiniao.
- **L71** `[@businesscannabis2025b]`: Fonte: nenhum CSC na Baviera tem local atribuido; 44 pedidos, 8 licencas de cultivo, 14 retirados, 3 rejeitados, 19 em analise; zonamento so em zonas especiais. 'Apenas 3 aprovados' nao corresponde (3 sao rejeicoes); MMJ Daily (out 2025) fala em 8 clubes autorizados. Data 'ate Abril 2025' nao confirmada.
  - *Sugestão:* Baviera: de 44 pedidos, 8 licencas de cultivo e nenhum clube com terreno atribuido, com zonamento mais restritivo que outros Laender.
- **L81** `[@businesscannabis2025a]`: Artigo: 'approximately 100,000 criminal proceedings were avoided' nos meses apos a legalizacao parcial (via SPIEGEL). Omite que o Ministerio do Interior contesta a leitura.
  - *Sugestão:* ~100.000 processos criminais evitados nos meses seguintes a legalizacao parcial, segundo a SPIEGEL (valor contestado pelo Ministerio do Interior).
- **L82** `[@businesscannabis2025a]`: Artigo: crimes de cannabis na Baviera -56% para 15.270 casos. Omite reserva do Ministerio do Interior: a descida reflecte sobretudo que 'consumer offences' deixaram de ser crime, nao menos consumo.
  - *Sugestão:* Crimes relacionados com cannabis -56% na Baviera, em grande parte por condutas de consumo terem deixado de ser crime (Ministerio do Interior contesta interpretacao como reducao real).
- **L91** `[@marijuanamoment2025]`: Artigo: 'no significant changes in self-reported driving under the influence' - condução sob efeito auto-reportada, nao acidentes rodoviarios.
  - *Sugestão:* Sem alteracoes significativas na conducao sob efeito auto-reportada; dados de acidentes nao avaliados nesta fonte.
- **L162** `[@insolvency2025]`: Na pagina so se nomeiam Fire & Flower e Atlas como insolventes; BZAM, Heritage, Delta 9 e Tokyo Smoke nao aparecem (conteudo obtido via resumo).
  - *Sugestão:* Citar fonte(s) que nomeiem BZAM, Heritage, Delta 9, Tokyo Smoke.
- **L169** `[@latinamerica2024]`: Apoia limites <=9%, <=15%, <=20% THC; Gamma dez 2022, Epsilon out 2024. Nao diz que limites afastaram consumidores para o mercado negro nem que so entao o mercado legal ficou competitivo.
  - *Sugestão:* Limites de THC subiram de 9% para 15% (2022) e 20% (2024); fonte nao estabelece o efeito no mercado negro.
- **L169** `[@softsecrets2025]`: Artigo: 1a variedade 2% THC, Beta 9%, Gamma 15%, Epsilon 20%; Epsilon criada para atrair quem recorre ao mercado negro; 'black market subdued by half'. Nao ha data 2022 nem '37%'; 'so apos... ganhou competitividade' e inferencia do autor.
  - *Sugestão:* Reformular como interpretacao.
- **L176** `[@tni2018]`: Fonte: "at least 500 cannabis associations operating in Spain"; "de facto legalisation ... from persistent testing of legal boundaries"; jurisprudência sobre "closed-circle use" com maioria de absolvições. Apoia área cinzenta e jurisprudência, mas não 800-1.000 clubes (e é de 2015).
  - *Sugestão:* Espanha não legalizou cannabis, mas tolera centenas de clubes sociais (pelo menos 500 associações segundo registos oficiais citados pelo TNI em 2015) numa área cinzenta legal baseada em jurisprudência sobre consumo partilhado. Para 800-1.000 é preciso fonte própria.
- **L176** `[@transform2018]`: Fonte: "roughly 400 CSCs or similar associations in Spain" e zona regulatória cinzenta (ainda sujeitos a raides). Não apoia 800-1.000.
  - *Sugestão:* Usar ~400 (Transform, 2018) ou citar fonte para 800-1.000.
- **L183** `[@hightimes2024]`: Fonte: "at least 30 clubs are facing closure orders" (a Set 2025); sem ano 2024 e sem razão detalhada; descreve "war" da câmara.
  - *Sugestão:* Em 2025, pelo menos 30 clubes de Barcelona enfrentavam ordens de encerramento [@hightimes2024].
- **L205** `[@cdphe2024]`: Página CDPHE: 13% consumo no último mês (liceu 2023, sem mudança vs 2021); 40% acha fácil obter marijuana, sem mudança vs 2021. 22% em 2011 e queda de 42% para 12,8% só aparecem no comunicado do MPP que cita o inquérito. Queda de 14 p.p. na perceção de acesso não consta.
  - *Sugestão:* Consumo juvenil no Colorado caiu de 22% (2011) para 12,8% (2023) [MPP citando Healthy Kids Colorado]; retirar a queda de 14 p.p. na perceção de acesso (CDPHE mostra 40%, sem mudança face a 2021).
- **L206** `[@marijuanapolicy2025]`: Apoiado: "decreases in youth cannabis use in 19 of the 21 states with before-and-after data". Errado: "over 35%" refere-se a Washington e Colorado (os dois estados mais antigos), não média; e MPP é parte interessada, associação não causal ("corresponds").
  - *Sugestão:* MPP reporta queda do consumo juvenil em 19 dos 21 estados com dados antes/depois, e quedas superiores a 35% em Washington e Colorado.
- **L226** `[@coley2024]`: JAMA Pediatrics 2024;178(6):622-625 (research letter, repeated cross-sectional, YRBS 2011-2021, 47 estados dos EUA): 'RCL was associated with modest decreases in cannabis, alcohol, and e-cigarette use'; RCR: 'lower likelihood but also increased frequency of cannabis use among users, leading to no overall change'; 'no net increases'. 'longitudinal' esta errado (cross-sectional repetido); 'associacoes limitadas' omite reducoes modestas e o aumento de frequencia entre consumidores apos vendas retalhistas.
  - *Sugestão:* 'estudo transversal repetido (YRBS 2011-2021, 47 estados dos EUA) concluiu que nao houve aumento liquido do consumo juvenil, com reducoes modestas associadas a legalizacao; as vendas retalhistas associaram-se a maior frequencia entre quem ja consumia'

### 06-principios-orientadores.md

- **L17** `[@sicad2018condenacoes]`: Mesmo: 84% (CDT 2018), não 75%; e nas condenações 59% (cannabis) .
  - *Sugestão:* 84% dos processos nas CDT (2018) envolvem só cannabis
- **L17** `[@dn2020condenacoes]`: Idem: condenações, não processos CDT; opinião.
  - *Sugestão:* Ajustar para condenações por consumo (2021).
- **L20** `[@ribeiro2024economic]`: Paper estimates illegal market 36-58 t (supported). EUR 52.7-70.8M (conservative) to EUR 151.3M (optimistic) is projected fiscal revenue under legalization scenarios, not a current figure. Source seen only via search snippets (ResearchGate 403).
  - *Sugestão:* Say "receita fiscal projetada de 52-151 M EUR em cenarios de legalizacao".
- **L28** `[@cdays2025]`: Artigo refere variedade limitada, distribuicao desigual e THC limitado; registo biometrico nao confirmado; nao 'explica' causalmente a captura de 24-39%.
  - *Sugestão:* Reformular como factores apontados pela fonte, nao causa demonstrada.
- **L28** `[@talkingdrugs2024uruguay]`: Source gives about 37-40% legal use, not 24-39%. Does not contain the lower bound of 24%.
  - *Sugestão:* Ajustar o intervalo para 24-40% com as duas fontes, ou corrigir os numeros.
- **L29** `[@sciencedirect2025canada]`: Supports about 22% illegal in 2022 (78% legal capture). Does not support 96% (2018) or 3% (2024).
  - *Sugestão:* Citar apenas o valor de 2022 desta fonte.
- **L71** `[@mills2021cannabis]`: Mills gives 4,600 kg CO2 per kg final product; no 2,000-5,000 range. The 2,283-5,184 range is Summers 2021.
  - *Sugestão:* Atribuir o intervalo a Summers e usar Mills para 4.600 kg/kg.
- **L72** `[@sciencedirect2025tomato]`: Medians: 80 kg CO2e/t open field, 1709 kg CO2e/t climate-controlled (1.7 kg/kg). 1.7 is a median, not a range start; "5.6" not verified. Indoor cannabis at 2,283-5,184 kg/kg is about 1000x higher, so "comparavel ou pior" understates the gap.
  - *Sugestão:* Corrigir para "cerca de 1,7 kg CO2e/kg em estufa climatizada; cannabis indoor e ordens de grandeza superior".
- **L80** `[@cambridge2022hemp]`: URL cam.ac.uk/stories/industrial-hemp devolve 404; sem acesso a pagina. Via alternativa: Dezeen (30/06/2021) cita o investigador de Cambridge Darshil Shah: 'Industrial hemp absorbs between 8 to 15 tonnes of CO2 per hectare of cultivation'; florestas 2-6 t/ha/ano; depende do metodo de cultivo. Nao diz 'por ciclo' nem 'condicoes UK/Irlanda'. 'UK/Irlanda' e 'por ciclo' nao constam.
  - *Sugestão:* Remover 'UK/Irlanda' e 'por ciclo'.
- **L80** `[@carboncredits2024hemp]`: carboncredits.com (autor 'Jennifer L', 2022, act. 2024): 'a hectare of hemp can absorb between 8-15 tonnes of CO2'; cita um investigador de Cambridge. E fonte secundaria da mesma afirmacao (nao e corroboracao independente); nao diz 'por ciclo' nem UK; nao 'validated by Cambridge research'.
  - *Sugestão:* Ver cambridge2022hemp.
- **L112** `[@sicad2018condenacoes]`: Idem; número da fonte é 84%.
  - *Sugestão:* 84% dos processos CDT (2018) envolvem cannabis
- **L140** `[@sicad2018condenacoes]`: Idem; "consumidores ocasionais" não consta.
  - *Sugestão:* 84% dos processos CDT (2018) envolvem apenas cannabis
- **L140** `[@dn2020condenacoes]`: Idem; "consumidores ocasionais" não consta.
  - *Sugestão:* Ajustar.
- **L141** `[@euda2024cannabis]`: 24,8% e media UE de resina apreendida, nao 'mercado negro' local; 'sem rotulagem' nao e da fonte.
  - *Sugestão:* Resina apreendida na UE tem em media 24,8% THC (2022).

### 07-pilar-medicinal.md

- **L24** `[@prohibition2025]`: Page: seven extracts available and two flower products "currently marketed". Source (as extracted) does not state ACM status nor that the ACM process is "burocrático, moroso e dispendioso" (only "administrative complexity" generally).
  - *Sugestão:* "Existem sete extratos e dois produtos de flor comercializados; a complexidade administrativa é apontada como barreira."
- **L25** `[@rtp2019]`: Article: OPCM raising funds to train health professionals; doctors "continuam a recusar-se a ajudar os pacientes" because no product in pharmacy; "a canábis é uma droga". Endocannabinoid system/medical schools and "poucos médicos se sentem confortáveis" are not in it.
  - *Sugestão:* "Existe necessidade de formação médica (OPCM, 2019) e alguns médicos recusam prescrever."
- **L33** `[@cannabishealthnews2024]`: 80% private / 20% reimbursed after 1 Apr 2024 supported. "O acesso global aumentou enormemente" not in source.
  - *Sugestão:* Retirar a afirmacao sobre aumento enorme de acesso.
- **L34** `[@globenewswire2024]`: 4.5M users in Germany supported. "~370,000 prescriptions/year" not in source (nearest: 338,500 SHI prescriptions in 2022). "Hundreds of millions of euros" unverified.
  - *Sugestão:* Usar 338.500 (2022).
- **L46** `[@internationalcbc2021]`: Opinion piece: "Three hundred euros a month is about the amount of disposable cash a person on disability benefits gets to spend ... on food and other essentials." Document inverts it (income after essentials). The EUR 300/month cost is not verified.
  - *Sugestão:* Corrigir o sentido.
- **L60** `[@cannabishealthnews2024]`: 16 specialties without prior approval from Oct 2024 supported. "Cobre desde 2017" and the 5-10 EUR co-payment not in source.
- **L61** `[@prohibitionpartners2024israel]`: 137,940 patients (Dec 2023) and no-extra-licence reform supported. Subsidy claim not in source.
- **L62** `[@pmc2024canadainsurance]`: "Not covered by most provincial plans" and up to $500/month supported. "One of the biggest failures of the Canadian model" not in source; "nao e coberta" overstates "most".
- **L63** `[@levaclinic2024]`: GBP 151 is Leva Clinic average private prescription, not UK-wide; NHS does not cover. Commercial source.
  - *Sugestão:* Escrever "numa clinica privada, media de 151 libras".
- **L77** `[@prohibition2025]`: "last resort" supported; "o doente tem de demonstrar que todas as outras opções falharam" is CMS wording (conventional treatments not efficient); "burocrático e desumanizante" is editorial, not in source.
  - *Sugestão:* Retirar "desumanizante" ou marcar como opinião; acrescentar cmslaw2024.
- **L78** `[@rtp2019]`: Training gap and refusals supported; "apenas uma mão-cheia" prescribers is not in the article (no prescriber numbers) and "estigma" only loosely ("a canábis é uma droga").
  - *Sugestão:* Remover "apenas uma mão-cheia" ou citar fonte com número de prescritores.
- **L85** `[@cannabisbusinesstimes2025]`: Via search snippet (page 403): DocCheck survey of 500 physicians (6 Oct 2025); GPs rarely prescribe. The training conclusion is the document's inference, not the source's.
- **L118** `[@solmi2023]`: 101 meta-analyses correct. Review also found convincing evidence of harm (psychosis, pregnancy, driving) and recommends avoiding cannabis in adolescence; only benefits mentioned.
  - *Sugestão:* Mencionar os riscos.
- **L120** `[@nugent2017]`: Abstract: "low-strength evidence that cannabis alleviates neuropathic pain but insufficient evidence in other pain populations"; not "eficácia moderada"; and it is an Annals of Internal Medicine review (2017), not a "Cochrane 2024".
  - *Sugestão:* "Evidência de baixa força para dor neuropática e insuficiente noutras dores (Nugent et al., Ann Intern Med 2017)."
- **L121** `[@devinsky2017]`: Dravet: 12.4 to 5.9 vs 14.9 to 14.1 seizures; responder 43% vs 27% (P=0.08, not significant); no 44%. LGS: 41.9%/37.2% vs 17.2% placebo. Placebo response and adverse events omitted; "robust" overstates.
- **L122** `[@torresmoreno2023]`: 7 RCTs (1128 patients), OR 2.41 (1.39-4.18) for add-on nabiximols in MS spasticity refractory to standard treatment; omits "refractory" qualifier, "at least some concerns" on risk of bias and "further studies are needed".
  - *Sugestão:* "... eficaz como terapêutica adjuvante na espasticidade de EM refratária (meta-análise de 7 ECR, com algumas preocupações de risco de viés)."
- **L123** `[@national2017]`: NASEM: "insufficient evidence" that cannabinoids are effective or ineffective for PTSD (only one small nabilone trial, per secondary summaries); "promissora" and "estudos em veteranos mostram redução" go beyond (not verified in chapter text).
  - *Sugestão:* "A evidência é insuficiente para concluir sobre eficácia na PTSD (NASEM 2017); são necessários ensaios."
- **L124** `[@suraev2020]`: 5 studies, 219 participants, poor quality; results "do not reliably inform evidence-based practice". Names THC and nabilone, not CBN.
  - *Sugestão:* Corrigir para THC/nabilona e indicar a fraca evidencia.
- **L125** `[@norml2024]`: Supports an association, but effect is modest (about 6%).
- **L125** `[@rock2024]`: Narrative review of OUD treatment (cravings, withdrawal), not of opioid prescription reductions; notes a paucity of rigorous RCTs.
- **L139** `[@prohibition2025]`: Source: "over 18 tonnes in the first three quarters of 2024" (+54% vs 11.97 t in 2023), not the full year; table in 02 line 19 says 32.558 kg for 2024.
  - *Sugestão:* "Nos primeiros três trimestres de 2024, exportou mais de 18 toneladas"; ou usar o total anual de eco2024 (32,6 t) e corrigir a inconsistência.
- **L144** `[@cannabis2024_1]`: Source says "limited access", not "no access".
  - *Sugestão:* Reformular para "acesso limitado".
- **L158** `[@eurofins2024cannabis]`: Source is about consumer (club) cannabis in Germany, not medical cannabis in Portugal; states mandatory testing for pesticides, mycotoxins, heavy metals, microorganisms.
  - *Sugestão:* Citar fonte medicinal ou reformular.

### 08-pilar-recreativa.md

- **L113** `[@springer2024zurican]`: PHQ-9/GAD-7 (cutoff 10) and ERIraos used; participants with >1 positive ERIraos item or core psychosis symptom were referred to a study physician to exclude psychotic symptoms. This is research eligibility screening, not mandatory clinical admission screening with referral to clinical services.
  - *Sugestão:* Reformular: 'no estudo piloto, rastreio de elegibilidade com encaminhamento para médico do estudo'; não apresentar como modelo clínico obrigatório.
- **L273** `[@kcang2024]`: Section 26 supported; sections 24-25 do not impose a general cost-recovery regime.
  - *Sugestão:* Referir "section 1 Nr 13 e section 24"
- **L275** `[@cannabusinessplans2024cscs]`: Supports CSC non-profit character and annual general assembly with financial reports ('CSCs are characterised by transparency, democracy and non-profitability'); does not support the cost-only distribution of KCanG paras 24-25.
  - *Sugestão:* Para 'selbstkostendeckend' citar o FAQ do BMG (cang2024).
- **L276** `[@kcang2024]`: 5-year retention and authority access supported (section 26(2)); law lists average THC, not CBD; strains only for transports.
- **L277** `[@kcang2024]`: 31 January annual anonymised submission supported; list in text (strains, THC/CBD) differs from law.
- **L292** `[@cannabis420eu2024]`: Supported: club oversight by state authorities through random checks and on-site inspections. Not supported: random lab analyses of THC and contaminants; 'sem aviso prévio' not verified.
  - *Sugestão:* Retirar a referência a análises laboratoriais aleatórias ou citar outra fonte.
- **L304** `[@cang2024]`: Source only says the permit may be revoked after repeated violations of cultivation/distribution quantities. Suspension up to 30 days, EUR 500-2,000 fines, written warning with forced audit, immediate revocation for refusing accounts, revocation plus criminal proceedings for minors are not in the source.
  - *Sugestão:* Rotular o regime sancionatório como proposta específica para Portugal, ou citar a norma que o fundamente.
- **L326** `[@acog2025cannabis]`: Supports universal screening by interview, self-report or validated tools in prepregnancy, pregnancy and postpartum; 'Biologic testing should not be used as a screening assessment'. 'Em todas as consultas' and the midwives' role are not stated.
  - *Sugestão:* Dizer 'rastreio universal ... na pré-concepção, gravidez e pós-parto'.
- **L335** `[@cdc2024lactation]`: Supported: 'Breast milk can contain THC for up to 6 days after use, according to one study. Other studies have noted even longer duration.' Not in CDC: 'fetal ~10% of maternal', 'THC in milk of ALL consuming mothers'; '5 weeks' comes from ACOG; '>6 weeks' unverified.
  - *Sugestão:* Remover os números não suportados ou atribuí-los correctamente.
- **L335** `[@wsu2024thcmilk]`: Small study (20 mothers); does not contain 'fetal ~10% of maternal' nor 'THC in milk of all mothers'.
  - *Sugestão:* Remover estes números desta citação.
- **L344** `[@acog2025cannabis]`: ACOG supports referral to treatment and criticises punitive policies; 'sem penalização' only indirect. The club Prevention Officer is a Portuguese proposal, not ACOG.
  - *Sugestão:* Marcar o Oficial de Prevenção como proposta própria.
- **L358** `[@sciety2025illicit]`: Licensed aerobic count failure is 6% (not <5%); licensed yeast/mold 6% (within <10%); licensed pesticides 4%. Abstract also reports 20% of licensed products exceeding microbial limits and 48% deviating >20% from labelled THC, omitted in the chapter.
  - *Sugestão:* Corrigir 6% e incluir os 20% / 48%.
- **L373** `[@pmc2018contaminants]`: Supports pesticide health effects and heavy-metal bioaccumulation from soil. 'Pb, Cd, As enter the bloodstream directly' is not specific; paper only says inhaled contaminants bypass first-pass metabolism.
  - *Sugestão:* Suavizar para 'contaminantes inalados evitam o metabolismo de primeira passagem'.
- **L373** `[@frontiers2020cannabis]`: Supports microbial and heavy-metal contamination and Fusarium risk in the immunocompromised; 'phytoextraction' not found in this text.
  - *Sugestão:* Citar Dryburgh (pmc2018contaminants) para fitoextracção.
- **L395** `[@cannareporter2022]`: Source says 34 companies licensed by Infarmed, 11 EU-GMP certified; chapter says 37 and 'export cannabis tested to EU-GMP'.
  - *Sugestão:* Corrigir para 34 (11 com EU-GMP).
- **L422** `[@bagch2024pilots]`: Cannabis must be produced in Switzerland and 'if possible' per the Organic Farming Ordinance; not a certified requirement; no ban on synthetic pesticides stated.
  - *Sugestão:* Escrever 'se possível, segundo a Portaria de agricultura biológica'.
- **L510** `[@eurofins2024]`: Eurofins Germany page (10 Jul 2024): 'it is now mandatory to test the products for pesticides, mycotoxins, heavy metals and microorganisms'. Vendor page; 'cada lote' not in text; BMG FAQ has no equivalent lab mandate.
  - *Sugestão:* Atribuir como afirmação do laboratório e remover 'cada lote'.
- **L528** `[@bagch2024pilots]`: Seed-to-product supply-chain monitoring supported; organic cultivation as requirement overstated.
  - *Sugestão:* Retirar 'obrigatório' em cultivo orgânico.
- **L745** `[@cannabisnow2024]`: EUR 25-45M for Portugal is the authors' estimate; source only gives German totals.
  - *Sugestão:* Rotular como estimativa própria.
- **L833** `[@cbcnews2025]`: 5,4B$ CAD apoiado; conversao ~EUR 3,6B e 'provincias decidem afetacao' nao constam da fonte (conversao do autor).
  - *Sugestão:* Indicar taxa de conversao e data; fundamentar afetacao noutra fonte.
- **L1112** `[@internationalcbc2025]`: 88,4% = proporcao de inqueridos que geralmente compraram cannabis de producao legal (autocultivo, incluindo amigos, associacoes, farmacias) nos 6 meses; nao 'das fontes' entre quem tem acesso; amostra auto-seleccionada nao verificada.
  - *Sugestão:* Inquerito KonCanG (n=11.471): 88,4% dos inqueridos obteve geralmente cannabis de fontes legais (incl. autocultivo de amigos).

### 09-pilar-canhamo.md

- **L9** `[@marketdataforecast2025]`: Current page is the 2034 edition (USD 3.6B 2025, 4.47B 2026, 25.39B 2034, CAGR 24.24%); 2.9B (2024) and 20.44B (2033) not found in this version.
  - *Sugestão:* Actualizar para os valores da edição actual.
- **L15** `[@fortunebusinessinsights2025]`: Wayback: USD 9.47B 2024, 47.82B 2032, but CAGR 22.44% (not 22.7%); 7.90B 2023; Europe 31.01% in 2023.
  - *Sugestão:* Corrigir CAGR para 22,4%.
- **L87** `[@cambridge2022hemp]`: URL cam.ac.uk/stories/industrial-hemp devolve 404; sem acesso a pagina. Via alternativa: Dezeen (30/06/2021) cita o investigador de Cambridge Darshil Shah: 'Industrial hemp absorbs between 8 to 15 tonnes of CO2 per hectare of cultivation'; florestas 2-6 t/ha/ano; depende do metodo de cultivo. Nao diz 'por ciclo' nem 'condicoes UK/Irlanda'. 'Reino Unido/Irlanda' nao consta.
  - *Sugestão:* Remover o enquadramento geografico ou citar estudo primario.
- **L87** `[@carboncredits2024hemp]`: carboncredits.com (autor 'Jennifer L', 2022, act. 2024): 'a hectare of hemp can absorb between 8-15 tonnes of CO2'; cita um investigador de Cambridge. E fonte secundaria da mesma afirmacao (nao e corroboracao independente); nao diz 'por ciclo' nem UK; nao 'validated by Cambridge research'.
  - *Sugestão:* Ver cambridge2022hemp.
- **L89** `[@anthropocene2022]`: Carbon-negative stated, but 'continua a absorver durante décadas' is not; article also says hempcrete is not load-bearing.
  - *Sugestão:* Retirar 'durante décadas'.
- **L97** `[@pmc2022hemp]`: Paper: hemp takes up Cd, Ni, Pb; Zn tolerated and mostly retained in roots. No claim of soil removal of Zn.
  - *Sugestão:* Soften to 'tolera/acumula' rather than 'remove'.
- **L98** `[@mdpi2022hemp]`: Sardinia semiarid trial confirmed; abstract: Zn >950 and Cd >6.8 mg/kg in leaves; Pb high even on non-contaminated soil (atmospheric deposition). 'Comparable to Alentejo' not in source.
  - *Sugestão:* Mark Alentejo comparison as author inference; drop Pb claim or qualify.
- **L99** `[@pmc2019hemp]`: Six varieties on abandoned coal-mine soil in Pennsylvania: metal accumulation without growth change; CBD/CBDAS higher on mine soil. Remediation of the soil not demonstrated.
  - *Sugestão:* Say 'tolera e acumula metais', not 'remedeia'.
- **L100** `[@pmc2023phyto]`: Conclusion: hemp, kenaf, jute suitable for Pb and Zn remediation; hemp accumulates Zn most strongly; uptake mostly in roots, slow, weather-dependent.
  - *Sugestão:* 'Among the most effective' only holds for Zn.
- **L106** `[@stockholm2005]`: Cotton ~9,758 L/kg vs hemp 2,123-3,401 L/kg = ~65-78% less. '50-70%' is not in the source; report also calls hemp textile production unviable at scale.
  - *Sugestão:* Use 'cerca de 65-78% menos' or quote litres/kg.
- **L159** `[@marketdataforecast2025]`: France 23,000 ha / 28,000 t fiber present but only as 'a more recent market report indicates' (secondary of secondary).
  - *Sugestão:* Citar fonte primária.
- **L170** `[@enecta2024]`: Confirms 400 ha in 2013 growing tenfold to 4,000 ha in five years; does not mention Law 242/2016.
  - *Sugestão:* Cite usdaitaly2020 for the law.
- **L170** `[@usdaitaly2020]`: Supports Law 242/2016, ~800 farms, 4,000 ha in 2018/19; not the 400 ha in 2013.
  - *Sugestão:* Split citation: enecta for ha growth, usda for law.

### 10-posicoes-partidarias.md

- **L9** `[@eco2021]`: IL: much less state intervention, free open market, responsible legalisation. 'Excesso de regulacao estatal' as the stated reason is not in the text; stated reason is need and advantage of legalising.
  - *Sugestão:* Reword the IL rationale.
- **L11** `[@publico2023]`: Confirma grupo de trabalho na Comissão de Saúde anunciado por Brilhante Dias, proposta legislativa só em 2024; divisão referida é a de 2019 (bancada "muito dividida"). "Não concretizado" é posterior e não consta.
  - *Sugestão:* PS: anunciou grupo de trabalho em 2023 [@publico2023]; resultado posterior citar outra fonte.
- **L12** `[@publico2018a]`: Artigo: JSD anunciou referendo interno para Fev 2020; moção Baptista Leite 2018 e posição "CONTRA" do PSD não aparecem.
  - *Sugestão:* JSD anunciou referendo interno (planeado Fev 2020) [@publico2018a]; moção Baptista Leite com outra fonte.
- **L15** `[@cannareporter2024b]`: Confirma oposição do Chega à legalização recreativa; mas o fact-check classifica de "Falso" a ideia de que o Chega é o único partido contra (PCP e PSD também votaram contra). "Oposição ideológica total" não consta.
  - *Sugestão:* Chega: contra a legalização recreativa [@cannareporter2024b]; o fact-check nota que PCP e PSD também votaram contra.
- **L30** `[@publico2023ps]`: Brilhante Dias announced a projeto de resolucao for a working group (14 Sep 2023); group 'sera constituido'. 'Nunca concluiu / crise politica / eleicoes 2024' not in source.
  - *Sugestão:* Remove outcome claim or add source.
- **L30** `[@ps2023cannabis]`: PS page 14 Sep 2023 confirms announcement of projeto de resolucao; no information on conclusion or collapse.
  - *Sugestão:* Qualify.
- **L91** `[@malta2021]`: Secondary sources (gov.mt) state 7 g possession, 4 plants per household, non-profit associations 7 g/day, 50 g/month; no commercial sale. The Cap. 628 text fetched lacks those provisions.
  - *Sugestão:* Fix URL; cite gov.mt press release for limits.
- **L112** `[@marijuanamoment2024trudeau]`: Exact quote is 'nobody talked to us about this'; the Portuguese text puts a paraphrase in quotation marks.
  - *Sugestão:* Use the English quote or drop quotation marks.
- **L150** `[@cdphe2024]`: -42% Colorado só via MPP; "tendência nacional similar -38%" não está no CDPHE (os -38% do MPP são alunos do 12.º ano em Washington, 26,3% para 16,3%).
  - *Sugestão:* Colorado -42% (MPP/HKCS); queda nacional (CDC/MTF) citar fonte própria; retirar -38%.

### 13-anexo-a-clubes.md

- **L41** `[@greendream2024spain]`: Page: 2021-2023 jurisprudence ruled that clubs operating as businesses, taking tourists or advertising violate the law. 'Acusacoes criminais' and 'inspecoes regulares' only partly supported; 150 kg and residents-only not verified.
  - *Sugestão:* Cite the Supreme Court rulings directly.
- **L115** `[@kcang2024]`: Section 26 supported; "princípio cost-recovery (sections 24-25) que proibe lucro" overstated.
  - *Sugestão:* Remover a atribuicao.
- **L537** `[@cuna2025]`: Archived copy: businesses 'operate almost entirely in cash'. No '>70%' figure; a related search found 'over 70 percent report issues related to lack of access to financial services', a different statistic.
  - *Sugestão:* Drop >70% or cite the right stat. Live page 522.
- **L539** `[@healtheuropa2022]`: Reports Metro Bank closing accounts; one company uses Co-op ('I believe most non-profits are with the Co-Op'). 'Recusas sistematicas' overgeneralises one anecdote; UK only.
  - *Sugestão:* Say 'alguns bancos britanicos'.

### 15-anexo-c-suica.md

- **L25** `[@businessofcannabis2024zurican]`: Direct fetch failed. Secondary sources (swissinfo, others): >2,300 participants, ~CHF 7.5 million withdrawn from black market. 'Official estimate' label unverified; points of sale ~21 (10 pharmacies, DIZ, 10 social clubs), not '3 shops + 8 pharmacies'.
  - *Sugestão:* Cite swissinfo or the City of Zurich study report.
- **L137** `[@cannabisregulations2025switzerland]`: Search: 7 pilots ongoing; ~10,400 participants (June 2025); consultation on Cannabis Products Act opened 29 Aug 2025 by the National Council SGK-N commission, until 1 Dec 2025. Page itself not read.
  - *Sugestão:* Cite BAG pilot page; attribute consultation to SGK-N, not the Federal Council.

### 16-anexo-d-argumentacao.md

- **L54** `[@di2019]`: Abstract: consumo diario associado a OR 3,2 (IC 2,2-4,1), "increasing to nearly five-times increased odds for daily use of high-potency types of cannabis (4.8, 2.5-6.3)" vs nunca consumidores. A frase omite que o ~5x exige consumo DIARIO de alta potencia e que se trata de odds ratio num caso-controlo, nao de risco.
  - *Sugestão:* "O estudo Di Forti (EU-GEI): consumo diario de cannabis de alta potencia (THC >=10%) associado a quase 5x mais odds de perturbacao psicotica (OR 4,8)".
- **L60** `[@bundesministerium2024]`: A regra de 10% THC aplica-se a jovens adultos 18-20 anos membros de associacoes de cultivo (max. 30 g/mes); menores de 18 estao proibidos. "menores de 21" e impreciso e a regra nao cobre autocultivo domestico.
  - *Sugestão:* "Limite de 10% THC e 30 g/mes para jovens adultos (18-20) nos clubes - modelo alemao".
- **L71** `[@cdphe2024]`: -42% Colorado não está na página CDPHE (vem do MPP); 12,8% vs 13% na página.
  - *Sugestão:* Citar @marijuanapolicy2025 para -42%.
- **L82** `[@colorado2023]`: Apoiado: mais de 4.000 gémeos do Colorado e Minnesota; "found no changes in illicit drug use after legalization". Não apoiado: "mito dos anos 80 que a ciência já abandonou" (um estudo).
  - *Sugestão:* Um estudo da CU Boulder com mais de 4.000 gémeos não encontrou alterações no uso de drogas ilícitas após a legalização; evitar generalizar para "a ciência abandonou".
- **L98** `[@nabiximols2024]`: Neuropathic pain approval only for MS in Canada, conditional (NOC/c).
  - *Sugestão:* Qualify.
- **L98** `[@ncbi2024dronabinol]`: NCBI page behind reCAPTCHA. Search snippet of StatPearls confirms FDA approval in 1985 for CINV and AIDS anorexia; exact date 31 May 1985 and 1992 not confirmed.
- **L98** `[@sciencedirect2025sleep]`: Mao F, Hoepel SJW, Shahisavandi M, Luik AI, El Marroun H; Sleep Medicine Reviews 84:102189 (Dec 2025); abstract: current recreational use linked to poorer sleep quality, short/long duration, more insomnia symptoms, later chronotype in 102 observational studies; none in 19 experimental studies; may be affected by bias. 'Mais despertares nocturnos' and 'cronico' not stated; review excludes clinical/medicinal use.
  - *Sugestão:* Add bias caveat and null experimental results; drop 'contradiz ensaios clinicos'.
- **L106** `[@nabiximols2024]`: 'Precisamente porque o THC e essencial' not in source.
  - *Sugestão:* Remove causal clause.
- **L107** `[@ncbi2024dronabinol]`: same
- **L108** `[@ncbi2024dronabinol]`: same
- **L109** `[@leung2020]`: Mesma reserva: 33% refere-se a dependencia em jovens com consumo semanal ou diario; o intervalo "30-33% diarios/frequentes" nao esta em Leung (22% e a media global de CUD).
  - *Sugestão:* "~33% dos jovens com consumo regular (semanal/diario) desenvolvem dependencia [@leung2020]".
- **L109** `[@sciencedirect2025sleep]`: Mao F, Hoepel SJW, Shahisavandi M, Luik AI, El Marroun H; Sleep Medicine Reviews 84:102189 (Dec 2025); abstract: current recreational use linked to poorer sleep quality, short/long duration, more insomnia symptoms, later chronotype in 102 observational studies; none in 19 experimental studies; may be affected by bias. 'Mais despertares nocturnos' and 'cronico' not stated; review excludes clinical/medicinal use.
  - *Sugestão:* Add bias caveat and null experimental results; drop 'contradiz ensaios clinicos'.
- **L111** `[@solmi2023bmj]`: Review covers harms as well as benefits (psychosis, adolescents, pregnancy, driving); benefits are for cannabis-based medicines (CBD epilepsy, pain, spasticity, IBD, nausea), not THC specifically.
  - *Sugestão:* Do not say 'robust evidence for THC'.
- **L111** `[@hauser2022bmc]`: 152 RCTs, 12,123 participants; CBD effective for epilepsy (high) and Parkinsonism (moderate); dronabinol moderate for chronic pain, appetite, Tourette; nabiximols for pain, spasticity, sleep, SUD; others low/very low/no grade. Epilepsy and Parkinson are CBD effects.
  - *Sugestão:* Attribute correctly.
- **L115** `[@cannabislaw2024export]`: 99,85% e 17 kg confirmados; '11.973 kg' nao esta na pagina (diz 11 toneladas); 'da producao' impreciso.
  - *Sugestão:* Acrescentar [@infarmed2024] para 11.973 kg; trocar 'producao' por 'quantidades vendidas'.
- **L115** `[@cannabisesaude2024portugal]`: Article (23 Apr 2024): Portugal exported 11 tonnes in 2023, only 17 kg sold domestically. '11.973 kg' and '99.85%' not in it (Infarmed Quadro 2 shows 11,973 kg). 17 kg is 'vendidos', not 'dispensados localmente'.
  - *Sugestão:* Cite Infarmed for 11,973 kg; fix wording.
- **L117** `[@infarmed2024prescricoes]`: 1,157 counts packages of authorised (ACM) products only, not 'totais'.
  - *Sugestão:* Fix wording.
- **L120** `[@publico2019indicacoes]`: As 7 indicações coincidem (náuseas/vómitos, dor crónica, apetite em paliativos, espasticidade EM/lesão medular, Tourette, epilepsias graves infantis Dravet/Lennox-Gastaut, glaucoma resistente ao tratamento). Mas o texto simplifica: 'dor oncológica' omite dor crónica associada ao sistema nervoso (neuropática); 'glaucoma' omite 'resistente ao tratamento'; 'espasticidade MS' omite lesões medulares; náuseas não são só oncológicas (também VIH/hepatite C).
  - *Sugestão:* ... dor crónica (oncológica ou do sistema nervoso), glaucoma resistente ao tratamento, espasticidade (EM ou lesão medular), náuseas/vómitos (quimio, radioterapia, terapêutica VIH/hepatite C) ...
- **L120** `[@opcm2024]`: A página (opcm.pt/canabis-medicinal-aprovada) apoia só em parte: refere indicações como 'spasticity associated with multiple sclerosis or spinal cord injuries' e dor crónica; no conteúdo obtido não aparece a lista completa de 7 indicações nem a Deliberação 11/CD/2019 (página trata sobretudo de produtos aprovados e cultivadores).
  - *Sugestão:* Substituir/complementar por @infarmed2019deliberacao (Deliberação n.º 11/CD/2019, https://www.infarmed.pt/documents/15786/2893227/lista+das+indica%C3%A7%C3%B5es+terap%C3%AAuticas+aprovadas+para+as+prepara%C3%A7%C3%B5es+e+subst%C3%A2ncias+%C3%A0+base+da+planta+da+can%C3%A1bis/294b3a2d-326b-46c3-9c08-a3b57427d027)
- **L127** `[@ncbi2024dronabinol]`: same
  - *Sugestão:* Confirm dates via FDA label.
- **L128** `[@sciencedirect2025sleep]`: Mao F, Hoepel SJW, Shahisavandi M, Luik AI, El Marroun H; Sleep Medicine Reviews 84:102189 (Dec 2025); abstract: current recreational use linked to poorer sleep quality, short/long duration, more insomnia symptoms, later chronotype in 102 observational studies; none in 19 experimental studies; may be affected by bias. 'Mais despertares nocturnos' and 'cronico' not stated; review excludes clinical/medicinal use.
  - *Sugestão:* Add bias caveat and null experimental results; drop 'contradiz ensaios clinicos'.
- **L129** `[@cannabislaw2024export]`: 99,85% e 17 kg confirmados; valor exacto 11.973 kg so em Infarmed.
  - *Sugestão:* Acrescentar [@infarmed2024].
- **L131** `[@infarmed2024prescricoes]`: same
- **L132** `[@lei332018]`: A condição de falha de convencionais está no Art. 5.º n.º 3, mas a Lei 33/2018 não enumera indicações (o Art. 9.º n.º 3 e o Art. 11.º remetem para o Infarmed); as 7 indicações vêm da Deliberação n.º 11/CD/2019 (confirmada na lista do Infarmed e no Público).
  - *Sugestão:* Lei 33/2018: prescrição só após falha de convencionais [@lei332018]; Deliberação 11/CD/2019 do Infarmed: 7 indicações [@publico2019indicacoes]
- **L133** `[@solmi2023bmj]`: Review covers harms as well as benefits (psychosis, adolescents, pregnancy, driving); benefits are for cannabis-based medicines (CBD epilepsy, pain, spasticity, IBD, nausea), not THC specifically.
  - *Sugestão:* Do not say 'robust evidence for THC'.
- **L140** `[@norml2024opioids]`: A ficha apoia substituição de opióides (p.ex. 79% numa coorte da Florida reportou cessação/redução de medicação para dor; redução média 50-90%) mas não tem informação sobre custos: "Não há informações específicas sobre custo relativo". 'Medicação mais cara' / 'poupanças significativas' não está na fonte.
  - *Sugestão:* Cannabis pode substituir parcialmente opiáceos em doentes com dor crónica [@norml2024opioids] (remover 'mais cara' ou citar fonte de custos).
- **L140** `[@dea2024overdose]`: Frase DEA conhecida (via pesquisa web, página não aberta): 'No deaths from overdose of marijuana have been reported'. Mas é afirmação antiga, sem número, e contraditada por NASEM 2017 (3 mortes de exposição só a cannabis em dados de centros antivenenos 2012-2014) e Rock 2022 (um caso com toxicidade de cannabis citada).
  - *Sugestão:* não tem risco documentado de overdose fatal em adultos (casos extremamente raros) em vez de '0 mortes registadas'
- **L140** `[@rock2022deaths]`: Conclusão: 'Risk of death due to cannabis toxicity is negligible'. Mas 'cannabis toxicity cited in a single case' (não zero) e os autores ressalvam: 'cannabis can prove fatal in circumstances with risk of traumatic physical injury, or in individuals with cardiac pathophysiologies'.
  - *Sugestão:* risco de morte por toxicidade da cannabis é negligenciável (um caso em 3455 mortes com canabinóides detectados em Inglaterra), embora possa contribuir indirectamente (trauma, cardíaco)
- **L140** `[@cannareporter2022stress]`: 84% é 'reduzir o stress e relaxar', não stress/ansiedade (ansiedade/depressão é ~40%); é uma amostra online de 3188 utilizadores, não 'dos consumidores' em geral.
  - *Sugestão:* 84% dos inquiridos (amostra online de 3188 consumidores, SICAD 2021) usam cannabis para reduzir o stress e relaxar; cerca de 40% para ansiedade ou depressão
- **L148** `[@norml2024opioids]`: A ficha refere redução/cessação do uso de opióides em doentes com dor crónica e reconhece necessidade de 'estudos prospectivos de melhor qualidade'; fala de uso de opióides, não de 'dependência'. A fonte é mais assertiva ('evidência robusta') do que o texto, mas é advocacia.
  - *Sugestão:* ... pode reduzir o uso de opiáceos em doentes com dor crónica (estudos sobretudo observacionais) ...
- **L148** `[@rock2024opioids]`: Apoia 'pode reduzir cravings e efeitos de abstinência' em OUD (adjuvante ou isolada), mas a evidência vem de 'a large number of observational studies' com falta de RCTs; o tema é perturbação por uso de opióides, não dor crónica.
  - *Sugestão:* ... evidência preliminar, sobretudo observacional, de que cannabis pode reduzir craving/abstinência em perturbação por uso de opióides [@le2024opioids]; para dor crónica citar outra fonte.
- **L149** `[@dea2024overdose]`: Idem: '0 mortes' é mais forte do que a literatura (NASEM 3 mortes por exposição isolada; Rock 2022 um caso). Fonte DEA não verificada directamente.
  - *Sugestão:* Cannabis: risco de morte por toxicidade directa negligenciável (não nulo) [@rock2022deaths; @ncbi2017deaths]
- **L149** `[@rock2022deaths]`: Idem: não é '0 mortes'; omite reserva sobre danos indirectos e polidroga (96% dos casos).
  - *Sugestão:* Cannabis: toxicidade fatal directa negligenciável [@rock2022deaths]; mortes por opiáceos incomparavelmente superiores
- **L149** `[@ncbi2017deaths]`: Conclusão 9-4(a): "insufficient evidence to support or refute a statistical association between cannabis use and death due to cannabis overdose"; nenhum estudo identificou cannabis como causa directa, mas centros antivenenos reportaram 3 mortes de exposição só a cannabis (2012-2014) e há um caso clínico de intoxicação aguda fatal. Não é '0 mortes' e a conclusão formal é de evidência insuficiente.
  - *Sugestão:* Nenhum estudo identificou cannabis como causa directa de morte por overdose, mas a evidência é insuficiente para concluir (NASEM 2017); casos raros reportados
- **L154** `[@cannareporter2022stress]`: "84%" correcto, mas refere-se à amostra online auto-seleccionada de 3188, não a 'os consumidores'.
  - *Sugestão:* 84% dos 3188 inquiridos ...
- **L156** `[@sciencedirect2025sleep]`: Mao F, Hoepel SJW, Shahisavandi M, Luik AI, El Marroun H; Sleep Medicine Reviews 84:102189 (Dec 2025); abstract: current recreational use linked to poorer sleep quality, short/long duration, more insomnia symptoms, later chronotype in 102 observational studies; none in 19 experimental studies; may be affected by bias. 'Mais despertares nocturnos' and 'cronico' not stated; review excludes clinical/medicinal use.
  - *Sugestão:* Add bias caveat and null experimental results; drop 'contradiz ensaios clinicos'.
- **L157** `[@cannareporter2022stress]`: "Apenas 2 inquiridos consumiram canábis prescrita por um médico, o que equivale a 0,1%"; "3019 consumiram canábis ilegal (95%)" - consumiram, não 'recorrem exclusivamente'; 19% também usaram produtos legais CBD. Omite que 0,1% = 2 pessoas e que a amostra é online auto-seleccionada.
  - *Sugestão:* Apenas 2 dos 3188 inquiridos (0,1%) usaram cannabis prescrita; 95% consumiram cannabis ilegal (amostra online, não representativa)
- **L170** `[@azevedo2012chronic]`: 37% confere ("present in 37% of the Portuguese adult general population"; 36,7%, IC95% 35,3-38,2; n=5094, 2007-2008). Os '3,8 milhões de pessoas' não constam do resumo/fonte e os dados têm ~18 anos.
  - *Sugestão:* 37% da população adulta (36,7%; inquérito 2007-2008) [@azevedo2012chronic]; remover '3,8 milhões' ou citar outra fonte/cálculo
- **L172** `[@publico2025oe2026]`: Confirma orçamento da saúde 2026 = 17,3 mil milhões (+1,5% face a 2025) e transferências para o SNS 14,9 mil milhões (+2,6%). Os '€16 mil milhões/ano' de custo teórico não vêm desta fonte (16/17,3 = 92,5% é aritmética do documento). Comparado com a transferência do SNS (14,9) o custo excederia 100%.
  - *Sugestão:* Indicar a origem dos €16 mil milhões e a base de comparação (17,3 mil milhões de orçamento do sector vs 14,9 mil milhões de transferência SNS).
- **L192** `[@rock2024opioids]`: Fonte diz 'potential' e 'paucity of rigorous randomised controlled trials'; trata de OUD, não de 'substituir opiáceos' na dor.
  - *Sugestão:* Cannabis: potencial em OUD, evidência ainda insuficiente (poucos ECR) [@le2024opioids]
- **L193** `[@dea2024overdose]`: Idem linha 149.
  - *Sugestão:* Overdose fatal cannabis: risco negligenciável, casos raríssimos documentados
- **L193** `[@rock2022deaths]`: Idem.
  - *Sugestão:* Overdose fatal cannabis: risco negligenciável (1 caso com toxicidade citada em 3455)
- **L193** `[@ncbi2017deaths]`: Idem linha 149.
  - *Sugestão:* Overdose fatal cannabis: sem causa directa identificada em estudos, evidência insuficiente (NASEM 2017)
- **L194** `[@cannareporter2022stress]`: 84%, 40% apoiados por esta fonte; 51% sono e 38% vêm de outra amostra (consumidores de produtos CBD/baixo THC, n=928) e esta fonte dá 52%. Mistura populações.
  - *Sugestão:* Separar: amostra A (n=3188): 84% stress, 52% sono, 40% ansiedade/depressão; amostra B (n=928, produtos CBD): 71%, 51%, 38%.
- **L194** `[@publico2023consumidor]`: 51% sono e 38% ansiedade/depressão estão no artigo, mas o 84% não (71%) e o universo é o de produtos CBD/baixo THC.
  - *Sugestão:* SICAD 2021 (consumidores de produtos CBD, n=928): 71% stress, 51% sono, 38% ansiedade/depressão [@publico2023consumidor]
- **L195** `[@cannareporter2022stress]`: Idem linha 157: 0,1% = 2 inquiridos; 95% consumiu cannabis ilegal.
  - *Sugestão:* Apenas 2 inquiridos (0,1%) usaram cannabis prescrita; 95% consumiram cannabis ilegal
- **L216** `[@cannabislaw2024export]`: 99,85% e valor de 2023 (11,9 t exportadas); a frase junta 32.558 kg (2024) e 1.157 prescricoes (2023) e atribui 99,85% ao conjunto: anos misturados.
  - *Sugestão:* Separar: 'em 2023, 99,85% ... [@cannabislaw2024export]'; 32.558 kg e de 2024.
- **L216** `[@infarmed2024prescricoes]`: Comparing 1,157 packages with 32,558 kg exported is not like-for-like.
- **L226** `[@statcan2019youth]`: Rotermann (Health Reports, 19/02/2020): 'Early indications from this NCS study suggests use among Canadian youth has not increased'; 'The cross-sectional nature of the data does not allow for causal inferences'. Dados 2018 vs 2019 (cerca de 1 ano pos-legalizacao). Citacao de Health Canada 'nao ha tendencia clara' nao esta aqui.
  - *Sugestão:* '... segundo Statistics Canada (indicacao preliminar, sem inferencia causal)'
- **L228** `[@sarvet2018jama]`: O conteúdo confere (11 estudos; estimativa agregada não significativa -0,003, IC95% -0,012 a 0,007: sem aumento do consumo juvenil após leis de cannabis medicinal), mas a revista está errada: é a Addiction, não a JAMA Pediatrics. Abrange leis de cannabis medicinal até ~2018, não legalização recreativa.
  - *Sugestão:* Meta-análise publicada na Addiction (2018): leis de cannabis medicinal não se associaram a aumento do consumo juvenil nos EUA [@sarvet2018addiction]
- **L229** `[@coley2024]`: JAMA Pediatrics 2024;178(6):622-625 (research letter, repeated cross-sectional, YRBS 2011-2021, 47 estados dos EUA): 'RCL was associated with modest decreases in cannabis, alcohol, and e-cigarette use'; RCR: 'lower likelihood but also increased frequency of cannabis use among users, leading to no overall change'; 'no net increases'. Idem: 'longitudinal' errado; 'associacoes limitadas' vago.
  - *Sugestão:* Idem.
- **L230** `[@bundesgesundheit2024cannabis]`: Medidas de protecao juvenil confirmadas; 6,7%->6,1% nao esta na pagina (so diz que o consumo e mais frequente entre 18-24).
  - *Sugestão:* Citar so [@marijuanamoment2025] para os 6,7%->6,1% (se verificado) e retirar BMG dessa parte.
- **L237** `[@cannabislaw2024export]`: 99,85% e relativo a 2023 exportado vs vendido localmente, nao 'producao'; eco2024cannabis refere 2024.
  - *Sugestão:* Idem: 'em 2023'.
- **L237** `[@eco2024cannabis]`: Export figure supported; 99.85% comes from another key.
- **L239** `[@infarmed2024prescricoes]`: same
- **L241** `[@statcan2019youth]`: Rotermann (Health Reports, 19/02/2020): 'Early indications from this NCS study suggests use among Canadian youth has not increased'; 'The cross-sectional nature of the data does not allow for causal inferences'. Dados 2018 vs 2019 (cerca de 1 ano pos-legalizacao). Aspas apresentam como conclusao algo que e indicacao preliminar; palavras exactas diferem.
  - *Sugestão:* 'Statistics Canada refere que as indicacoes preliminares (early indications) sugerem que o consumo juvenil nao aumentou, sem inferencia causal'
- **L242** `[@mpp2024colorado]`: Pagina original bloqueada (HTTP 403 Cloudflare; arquivo inacessivel). Numeros confirmados por excertos de pesquisa do comunicado MPP e por Marijuana Moment (12,8% em 2023, 13,3% em 2021, HKCS) e Colorado Sun (429, nao aberto): 22% (2011) e queda de 42% so via resumo de pesquisa. Apresenta queda de 42% como 'pos-legalizacao' sem a ressalva de tendencia nacional da linha 227; 22% e de 2011 (antes de 2012).
  - *Sugestão:* Acrescentar 'tendencia nacional semelhante; causalidade nao demonstrada'.
- **L260** `[@marijuanamoment2025]`: Fonte apoia que consumo juvenil continuou a descer; nao liga ao autocultivo nem a menor dependencia do mercado negro.
  - *Sugestão:* Reformular: o consumo juvenil continuou a descer apos a legalizacao (tendencia anterior a lei); retirar a inferencia sobre autocultivo.
- **L269** `[@marijuanamoment2025]`: Idem: ausencia de nexo com autocultivo.
  - *Sugestão:* Alemanha: consumo juvenil continuou a descer apos legalizacao.
- **L285** `[@marijuanamoment2025]`: Idem.
  - *Sugestão:* Retirar a relacao causal com o autocultivo.
- **L293** `[@marijuanamoment2025]`: Idem.
  - *Sugestão:* Idem.
- **L302** `[@businesscannabis2025a]`: 56% so para a Baviera; '80%' nao aparece no artigo; nacionalmente crime de drogas caiu ~1/3 em 2024. Reserva do Ministerio do Interior omitida.
  - *Sugestão:* Na Baviera, os crimes de cannabis cairam 56% em 2024 (e o crime ligado a drogas cerca de um terco a nivel nacional), em boa parte porque condutas de consumo deixaram de ser crime.
- **L308** `[@businesscannabis2025a]`: '56% e 80%' - so 56% (Baviera) na fonte; 100.000 processos evitados apoiado como valor reportado; reserva omitida.
  - *Sugestão:* Corrigir para 'cerca de 56% na Baviera' e acrescentar a ressalva.
- **L316** `[@businesscannabis2025a]`: -80% nao esta na fonte; 56% so Baviera.
  - *Sugestão:* Alemanha (Baviera): crimes cannabis -56%; ressalva do Ministerio do Interior.
- **L317** `[@businesscannabis2025a]`: 100.000 processos evitados reportado, mas valor contestado e relativo a processos por condutas agora legais.
  - *Sugestão:* ~100.000 processos evitados (valor reportado, contestado).
- **L324** `[@marijuanamoment2025accidents]`: "no meaningful change in incidents on the roadways"; "no significant changes in self-reported driving under the influence ... or in the number of people killed or injured". Mas é relatório intercalar preliminar (relatório final previsto para Abril 2028); a frase afirma 'não aumentaram' sem esta reserva.
  - *Sugestão:* Os dados preliminares do primeiro relatório oficial não mostram alteração significativa nos acidentes rodoviários (avaliação final prevista para 2028)
- **L324** `[@businesscannabis2025traffic]`: "Initial data shows no clear rise in cannabis-related accidents, but monitoring is ongoing." Reservas omitidas: apenas os primeiros 12 meses, práticas de fiscalização variam por região, distinção entre uso medicinal e recreativo 'not feasible'.
  - *Sugestão:* Os dados iniciais não mostram aumento claro de acidentes relacionados com cannabis, mas a monitorização continua
- **L330** `[@bmg2024thclimit]`: 3,5 ng/ml confere; o grupo de peritos foi interdisciplinar (medicina, direito, transportes) sob liderança do BMDV, recomendações de 28/03/2024. A equivalência a 0,2‰ de álcool não consta desta página (aparece em fontes secundárias na pesquisa web).
  - *Sugestão:* estabelecido com base em recomendação de um grupo interdisciplinar de peritos liderado pelo Ministério dos Transportes (BMDV); equivalência a 0,2‰ requer outra fonte
- **L331** `[@bmg2024thclimit]`: A fonte só diz 'cannabis ban for novice drivers'; não define 'menos de 2 anos de carta' nem 'menores de 21' nem 'tolerância zero'. Fontes secundárias indicam que para condutores novos/menores de 21 se mantém o limite de 1 ng/ml (não zero).
  - *Sugestão:* Proibição de consumo de cannabis para condutores novos [@bmg2024thclimit]; detalhe de idade/limite (1 ng/ml) a citar do StVG §24c
- **L342** `[@bmg2024thclimit]`: Idem linha 330: 3,5 ng/ml no soro confere; equivalência 0,2‰ não está na fonte.
  - *Sugestão:* Limite alemão: 3,5 ng/ml THC no soro sanguíneo
- **L343** `[@bmg2024thclimit]`: "the Law, which became effective on 22 August 2024" refere-se à alteração da lei do trânsito; o Cannabis Act entrou em vigor a 1/04/2024.
  - *Sugestão:* Limite de THC no trânsito em vigor desde 22/08/2024 (Cannabis Act desde 1/04/2024)
- **L344** `[@bmg2024thclimit]`: Idem linha 331: só 'cannabis ban for novice drivers'; 'menores de 21' e 'tolerância zero' não estão na fonte.
  - *Sugestão:* Proibição de cannabis para condutores novos
- **L346** `[@marijuanamoment2025accidents]`: Sem a reserva de dados preliminares (primeiros 12 meses).
  - *Sugestão:* Dados alemães preliminares 2024-2025: sem aumento claro de acidentes
- **L346** `[@businesscannabis2025traffic]`: 'Acidentes não aumentaram' omite 'no clear rise' e o carácter preliminar.
  - *Sugestão:* Dados alemães preliminares 2024-2025: sem aumento claro de acidentes
- **L359** `[@tni2018]`: Zona cinzenta e ausência de legislação específica apoiados; número 800-1.000 não consta (fonte diz pelo menos 500, 2015). O briefing não fala de fragmentação Barcelona/Madrid nem de crime organizado.
  - *Sugestão:* Reduzir para "centenas de clubes" ou citar fonte para 800-1.000.
- **L359** `[@transform2018]`: Zona cinzenta e turismo (clubes de Barcelona admitem turistas) e deriva comercial: apoiados como "preocupações". Madrid restritivo e crime organizado: ausentes. Nº de clubes: ~400, não 800-1.000.
  - *Sugestão:* Atribuir a Transform só: "preocupações com deriva comercial e turismo (Barcelona)"; remover crime organizado ou citar outra fonte.
- **L361** `[@kcang2024]`: Section 26 supported; "princípio cost-recovery (sections 24-25)" overstated.
  - *Sugestão:* Remover a atribuicao.
- **L381** `[@tni2018]`: Mesma questão: fonte diz pelo menos 500 associações; sem regulação nacional é apoiado.
  - *Sugestão:* Espanha: centenas de clubes (>=500 em 2015) em zona cinzenta legal, sem regulação nacional
- **L381** `[@transform2018]`: Zona cinzenta apoiada; nº de clubes ~400 na fonte.
  - *Sugestão:* Ajustar número ou fonte.
- **L382** `[@transform2018]`: Fonte apresenta exploração comercial e turismo como "concerns", não como "problemas documentados"; crime organizado ausente.
  - *Sugestão:* Problemas apontados (preocupações): deriva comercial, turismo cannábico [@transform2018]
- **L383** `[@hightimes2024]`: Mesmo: ordens de encerramento em curso (30 clubes), não "encerramento em 2024 por desvios"; motivo não detalhado.
  - *Sugestão:* Barcelona: pelo menos 30 clubes com ordens de encerramento (2025)
- **L407** `[@cdphe2024]`: Página dá 13% em 2023 e não tem 2011; 22% e 12,8% vêm do MPP.
  - *Sugestão:* Colorado: 22% para 12,8% (MPP, a partir do HKCS 2011-2023)
- **L411** `[@marijuanapolicy2025]`: Fonte: 19 de 21 estados "com dados antes/depois", não todos os que legalizaram.
  - *Sugestão:* MPP: queda em 19 dos 21 estados com dados antes e depois da legalização
- **L418** `[@greenwald2009]`: "resounding success" is Greenwald's conclusion (author, published by Cato); presenting it as praise by Cato Institute "conservador" is imprecise: Cato is libertarian and the paper is by Glenn Greenwald (civil-liberties lawyer/journalist). Overdose/HIV figures are other keys.
  - *Sugestão:* "... num estudo publicado pelo Cato Institute (think tank libertário) pelo jurista Glenn Greenwald ..."
- **L428** `[@greenwald2009]`: Quote "resounding success judged by virtually every metric" exists (Greenwald, published by Cato) but is the author's, not Cato's institutional position; Cato is libertarian, not conservative.
  - *Sugestão:* "Um estudo publicado pelo Cato Institute (libertário) concluiu: sucesso retumbante por praticamente todas as métricas."
- **L435** `[@greenwald2009]`: Same: author is Greenwald; Cato is libertarian.
  - *Sugestão:* "Cato Institute (libertário; autor G. Greenwald)"
- **L456** `[@cdphe2024]`: Mesmo: -42% sem fonte directa no CDPHE; é associação temporal, não causal; Colorado é um estado, não "país".
  - *Sugestão:* Colorado: de 22% (2011) para 12,8% (2023) [@marijuanapolicy2025]; evitar sugerir causalidade.
- **L456** `[@marijuanapolicy2025]`: Idem; omite o qualificador "com dados antes/depois" e que é associação.
  - *Sugestão:* Em 19 dos 21 estados com dados comparáveis, o consumo juvenil diminuiu (MPP)
- **L464** `[@cdphe2024]`: Idem; "após legalização" é cronologia, e o MPP indica queda semelhante a nível nacional.
  - *Sugestão:* Colorado: 22% para 12,8% entre 2011 e 2023, em linha com a descida nacional
- **L466** `[@marijuanapolicy2025]`: Idem.
  - *Sugestão:* MPP: 19 de 21 estados com dados comparáveis mostram diminuição
- **L488** `[@marconi2016]`: Marconi e uma meta-analise de 10 estudos (66 816 individuos), nao um "estudo de coorte europeu"; Di Forti e caso-controlo. Apoia a associacao cannabis-psicose, mas a descricao do desenho esta errada.
  - *Sugestão:* "...estudos europeus (meta-analise e caso-controlo) sobre psicose e cannabis [@marconi2016; @di2019]".
- **L488** `[@di2019]`: Caso-controlo multicentrico, nao coorte (ver marconi2016).
  - *Sugestão:* "estudos europeus sobre psicose e cannabis".
- **L490** `[@greenwald2009]`: "A ciência diz" overstates: a 2009 advocacy white paper, no causal identification (the document itself says causality cannot be proven at 02:123).
  - *Sugestão:* "Os dados disponíveis são consistentes com a descriminalização não ter causado aumento de consumo [..]"
- **L490** `[@marijuanamoment2025]`: Fonte: consumo juvenil 'continued to decline' (tendencia previa); nao demonstra que a legalizacao o diminui.
  - *Sugestão:* '... nao aumentou (dados alemaes preliminares)'; evitar 'pelo contrario, diminui' como efeito.
- **L499** `[@greenwald2009]`: Same as 490: supportive but 2009, non-peer-reviewed.
- **L499** `[@businesscannabis2025a]`: Fonte reporta quedas de crime na Alemanha mas com disputa oficial; nao e evidencia conclusiva.
  - *Sugestão:* Indicar que os dados alemaes sao preliminares e contestados.
- **L499** `[@marijuanamoment2025]`: Apoia so a ausencia de aumento no consumo juvenil, em dados preliminares.
- **L507** `[@bundesministerium2024]`: Fonte: avaliacao independente (EKOCAN), relatorios intercalares e "final evaluation four years after the Act has entered into force"; o ano 2028 e inferencia (a pagina nao da a data de entrada em vigor) e e avaliacao legal, nao "programa".
  - *Sugestão:* "Avaliacao final prevista quatro anos apos a entrada em vigor (c. 2028)".
- **L511** `[@bundesministerium2024]`: Idem.
  - *Sugestão:* Idem.
- **L524** `[@bundesministerium2024]`: Idem.
  - *Sugestão:* Idem.
- **L552** `[@cannabisnow2024]`: EUR 40-80M and EUR 174M are not in the source.
  - *Sugestão:* Rotular como estimativa própria ou remover a citação.
- **L558** `[@bundesministerium2024]`: Avaliacao ate ~2028 apoiada em parte; "com financiamento garantido" nao consta da fonte.
  - *Sugestão:* Retirar "com financiamento garantido" ou citar fonte.
- **L565** `[@greenwald2009]`: Supports that decriminalisation was judged a success as of 2009; "ninguém tinha feito antes" is not in what could be checked.
- **L569** `[@greenwald2009]`: Qualitative success (falling overdoses/HIV, usage not above EU) per overview; specific 78% and 98% are not verifiable in the source (full text unreachable); 2009 data.
  - *Sugestão:* Atribuir percentagens apenas a bessergrowen2025/manthey2024.
- **L575** `[@cdphe2024]`: -42% só via MPP; 24 estados e 10+ anos não constam.
  - *Sugestão:* Citar @marijuanapolicy2025 para -42%.
- **L576** `[@bundesministerium2024]`: Apenas a Alemanha esta na fonte; Malta e Luxemburgo nao sao mencionados. A Alemanha despenalizou posse/autocultivo/clubes, sem vendas comerciais.
  - *Sugestão:* Acrescentar fontes para Malta e Luxemburgo (nao verificadas) e precisar "legalizacao parcial".
- **L588** `[@bundesministerium2024]`: Idem.
  - *Sugestão:* Idem.

### chapters/04-ciencia.md

- **L24** `[@jackson2016]`: Jackson 2016 conclui que não há evidência de efeito causal no QI (sem dose-resposta; gémeos consumidores sem maior declínio). Associação transversal/descritiva apenas.
  - *Sugestão:* Citar Jackson como contra-evidência/matizar; manter [@meier2012] para o risco cognitivo de início adolescente.
- **L24** `[@meier2012]`: Resumo: "Impairment was concentrated among adolescent-onset cannabis users"; trata de declínio neuropsicológico, não de risco psiquiátrico.
  - *Sugestão:* Restringir à vertente cognitiva.
- **L28** `[@aha2024]`: 434.104 respondentes; aOR 1,25 (EM) e 1,42 (AVC) para uso diário; estudo transversal, desfechos auto-reportados, 27 estados. O texto omite que a associação é com uso diário e não diz "fumada, ingerida ou vaporizada" na parte do resumo consultada.
  - *Sugestão:* Escrever "uso diário associado a" e indicar desenho transversal.
- **L29** `[@acc2025]`: Comunicado: utilizadores <50 anos, >6x enfarte, 4x AVC isquémico, 2x insuficiência cardíaca, seguimento médio >3 anos; participantes sem comorbilidades. O texto generaliza a "utilizadores de cannabis" sem a restrição <50 anos.
  - *Sugestão:* Acrescentar "com menos de 50 anos".
- **L30** `[@cheng2023]`: Resultado correcto: EAM OR 1,29 (IC95% 0,80-2,08), não significativo; mas o primeiro autor é Theerasuwipakorn, não "Cheng et al.".
  - *Sugestão:* Corrigir para "Theerasuwipakorn et al. (2023)" e renomear a chave.
- **L201** `[@canada2023cannabis]`: Confirmado: 2-5 ng (summary, máx. $1000), >=5 ng (mín. $1000; 30 dias 2ª). Não encontrados: 25 ng/ml oral fluid, 98% confirmação; "combinado: agravamento" não é descrito (mesmas penas, 2,5 ng+50 mg álcool). $1000 em 2-5 ng é máximo.
  - *Sugestão:* Corrigir "máx. $1000" e remover 98%.
- **L249** `[@grotenhermen2007pharmacokinetics]`: Resumo: inalação, efeitos psicotrópicos máximos aos 15-30 min; oral, máximo aos 2-3 h (texto diz 1-2 h) e duram 4-12 h; "3-4 h clearance" não consta do resumo.
  - *Sugestão:* Corrigir oral para 2-3 h; não atribuir 3-4 h.

### chapters/05-modelos-internacionais.md

- **L158** `[@healthcanada2024]`: Canadian Cannabis Survey 2024: 2024 = 72% fonte legal e 3% fonte ilegal; 2019 = 37% legal; 2018 = 28% fontes ilegais, legal indisponível. Não há 4% em 2018.
  - *Sugestão:* Escrever "37% (2019) -> 72% (2024); ilegal 28% (2018) -> 3% (2024)".
- **L160** `[@healthcanada2024]`: 16-19 anos, uso não médico 12 meses: 36% (2018), 44% (2019), 41% (2024); estável 37-44% desde 2019; "sem aumento atribuível" é interpretação.
  - *Sugestão:* Dizer "41% em 2024 vs 36% em 2018" sem atribuição causal.
- **L191** `[@apnews2022thailand]`: AP cita governo a dizer que só a cannabis medicinal foi legalizada; ausência de monitorização é leitura de críticos.
  - *Sugestão:* Atribuir a críticos.
- **L195** `[@lexology2026thailand]`: Regulação descrita como projecto/nova regulação; não confirmada como em vigor.
  - *Sugestão:* Dizer "projecto de regulação".

### chapters/06-principios-orientadores.md

- **L18** `[@cannareporter2023legalization]`: Página: 86% dos indiciados em 2021 tinham perfil "non-drug addict" (SICAD); "consumidores ocasionais" é interpretação.
  - *Sugestão:* Citar SICAD.

### chapters/08-pilar-recreativa.md

- **L5** `[@wikipedia2025]`: Fonte geral sobre o modelo alemão; sem verificação ponto a ponto.

### chapters/16-anexo-d-argumentacao.md

- **L270** `[@wikipedia2025]`: Prevê 3 plantas para cultivo privado; "não tráfico" é inferência.
  - *Sugestão:* Citar o texto legal.
- **L302** `[@healthcanada2024]`: Canadian Cannabis Survey 2024: 2024 = 72% fonte legal e 3% fonte ilegal; 2019 = 37% legal; 2018 = 28% fontes ilegais, legal indisponível. 4% incorrecto.
  - *Sugestão:* Usar 37% (2019).
- **L306** `[@healthcanada2024]`: Canadian Cannabis Survey 2024: 2024 = 72% fonte legal e 3% fonte ilegal; 2019 = 37% legal; 2018 = 28% fontes ilegais, legal indisponível. "4% do mercado legal antes de 2018" incorrecto.
  - *Sugestão:* Corrigir.
- **L314** `[@healthcanada2024]`: 4% inexistente; 72% correcto.
  - *Sugestão:* Corrigir baseline.

## Citações cuja fonte não foi possível abrir (33)


### 02-panorama-portugues.md

- **L23** `[@ribeiro2024]`: ResearchGate page returns 403 (WebFetch, curl, searxng reader); no archived copy; only abstract snippets via search, which concern tax revenue and market size, not SNS reimbursement. Not verified.
  - *Sugestão:* Se não houver confirmação, usar fonte sobre comparticipação (euronews2024 / Infarmed).
- **L123** `[@euda2024cannabis]`: Pagina EUDA devolve 403 a WebFetch/curl; pesquisa nao confirmou 8,2% (PT) vs 8,3% (UE); resultado de pesquisa indica 8,4% UE no EDR 2025 e outro valor para Portugal (12,2%, tipo de indicador nao verificado). Nao verificado; tambem o '2,8% anterior' nao verificado.

### 04-ciencia.md

- **L144** `[@euda2024cannabis]`: Idem: 8,2% para Portugal nao verificado.

### 06-principios-orientadores.md

- **L58** `[@euda2024cannabis]`: Extratos/edibles e adulteracao com canabinoides sinteticos nao verificados (pagina inacessivel).
- **L73** `[@motherjones2021carbon]`: URL 404 and no archive. Same-study coverage elsewhere mentions the data-center comparison, but could not verify at Mother Jones.
  - *Sugestão:* Substituir por fonte acessivel.

### 07-pilar-medicinal.md

- **L11** `[@lei2024]`: Could not read the pgdlisboa page (2 attempts) nor the DR portal (JS-only). Date and subject as commonly cited, but not verified from the source.
  - *Sugestão:* Corrigir URL e ano (2018).

### 08-pilar-recreativa.md

- **L1026** `[@bcav2025]`: bcav-deutschland.de returned empty on two attempts; Wayback near empty. 357 clubs (Nov 2025) not verified. Ratio 84M/357 ≈ 235,294 is arithmetically correct.
  - *Sugestão:* Verificar manualmente.
- **L1030** `[@ine2024pop]`: INE JSON API (indicator 0008273) returned 2023 = 11,204,347 as latest value and no 2024 value; page is JS-only. Conflicts with 10,749,635.
  - *Sugestão:* Verificar manualmente no INE; o valor 10,749,635 não confirmado.

### 09-pilar-canhamo.md

- **L89** `[@researchgate2017hempcrete]`: ResearchGate page blocked on two attempts; no Crossref match.
  - *Sugestão:* Substituir por paper com DOI.

### 10-posicoes-partidarias.md

- **L65** `[@businessofcannabis2025pillar2]`: Fetch failed (connection error); quote 'likely not coming to fruition' and CDU reverting progress not verified. Also 'CDU' should be 'CDU/CSU'.
  - *Sugestão:* Find alternate source or drop quote.
- **L90** `[@luxembourg2023]`: Gov URL 404. Secondary sources: law passed June 2023, in force 21 Jul 2023, 4 plants per household, sale not allowed; plan announced Oct 2021; 14 dispensary licences considered Apr 2023.
  - *Sugestão:* 'Legalizou autocultivo 2021' should read 2023 (in force 21 Jul 2023); 'estuda venda' only partly supported.

### 13-anexo-a-clubes.md

- **L41** `[@medium2024barcelona]`: Medium blocked (Cloudflare). Other sources confirm Barcelona ordered 30 clubs closed in July 2024 after 57 inspections, aiming at all 212. 15-day minimum residence unverified.
  - *Sugestão:* Replace with https://es.ara.cat/sociedad/barcelona/barcelona-ordena-cerrar-30-clubs-cannabicos_1_5084612.html

### 15-anexo-c-suica.md

- **L106** `[@businessofcannabis2024zurican]`: 7,500 target and '>90% bought only legally' not verified.
  - *Sugestão:* Find primary study report.

### 16-anexo-d-argumentacao.md

- **L98** `[@jazzpharma2024sativex]`: clinicaltrialsarena 403. Search: Sativex approved in Canada, UK, Spain; 1:1 THC:CBD mixture.
  - *Sugestão:* Retry via archive.
- **L106** `[@jazzpharma2024sativex]`: as above
- **L126** `[@jazzpharma2024sativex]`: as above (1:1 ratio supported by search results only)
- **L155** `[@sicnoticias2023consumidor]`: Fonte não aberta (WebFetch bloqueado, curl 403, pesquisa sem resultado). Artigo equivalente do Público dá 38% ansiedade/depressão, em consumidores de produtos CBD (n=928).
- **L156** `[@sicnoticias2023consumidor]`: Idem; o 51% sono vem de amostra de produtos CBD/baixo THC, não da amostra de 3188 do cannareporter.
  - *Sugestão:* Explicitar a população: 51% (consumidores de produtos CBD, n=928) vs 52% (n=3188).
- **L194** `[@sicnoticias2023consumidor]`: Idem.
- **L222** `[@dw2024clubs]`: Fonte inacessível (404, bloqueio WebFetch, sem arquivo; 2+ vias tentadas). O limite de THC de 10% para 18-21 anos está confirmado no site do BMG ("aged 18 or over but younger than 21 ... no more than 30 grams ... THC level that does not exceed ten percent"); os 200 m de escolas e o oficial de prevenção não foram verificados.
  - *Sugestão:* Citar o texto da lei (KCanG) para distância de 200 m e Präventionsbeauftragter, e @bundesgesundheit2024cannabis para o limite de THC de 10%.
- **L227** `[@cdc2023yrbs]`: Página CDC não aberta (Access Denied; 2 vias). Via pesquisa: 22% (2011) -> 12,8% (2023), -42% confere ((22-12,8)/22=41,8%) mas é do Healthy Kids Colorado Survey, não do YRBS/CDC; HKCS e YRBS não são directamente comparáveis. O '-38% nacional' não foi verificado.
  - *Sugestão:* Colorado (Healthy Kids Colorado Survey, CDPHE): consumo nos últimos 30 dias em estudantes do secundário de 22,0% (2011) para 12,8% (2023) [@mpp2024colorado; CDPHE]

### chapters/04-ciencia.md

- **L22** `[@coffeeshop2024cud]`: Artigo não localizado após Crossref e ScienceDirect. Leung 2020 (já citado) dá 33% (IC 22-44%) para risco de dependência em jovens com uso regular (semanal ou diário), não "diário/near-daily" em geral.
  - *Sugestão:* Identificar a referência correcta ou citar só [@leung2020] com a formulação "jovens com uso regular (semanal ou diário)".
- **L62** `[@casey2019]`: Chave sem entrada em references.bib; não é possível saber qual a obra pretendida. Candidata plausível, não confirmada quanto ao conteúdo: Casey, Heller, Gee, Cohen (2019), Neurosci Lett 693:29-34.
  - *Sugestão:* Adicionar entrada e verificar se sustenta "~25 anos".
- **L66** `[@casey2019]`: Idem; "23-26 anos" não verificado.
  - *Sugestão:* Idem.
- **L66** `[@bbrfoundation2023]`: Sem entrada no .bib e sem URL; fonte não identificável sem inventar.
  - *Sugestão:* Adicionar entrada com URL do artigo da BBRF ou retirar.
- **L69** `[@frontiers2025cannabis]`: Sem entrada no .bib; artigo da Frontiers não identificável sem inventar.
  - *Sugestão:* Adicionar entrada com DOI.
- **L70** `[@utdallas2023]`: Sem entrada no .bib; comunicado/estudo UT Dallas não identificável sem inventar.
  - *Sugestão:* Adicionar entrada com URL.
- **L71** `[@pmc2013adolescent]`: Sem entrada no .bib; candidata não confirmada: Arain et al. (2013), Maturation of the adolescent brain, Neuropsychiatr Dis Treat 9:449 (DOI 10.2147/NDT.S39776), que não é específica sobre cannabis/memória de trabalho.
  - *Sugestão:* Identificar o artigo PMC pretendido.

### chapters/05-modelos-internacionais.md

- **L195** `[@bangkokpost2025cannabis]`: Bangkok Post: redirecção/paywall 402; números confirmados noutra fonte (nationthailand2026).
  - *Sugestão:* Manter nationthailand2026.
- **L213** `[@monitoringthefuture2023]`: 38%/13% (2013-2023) não verificados após PDF (403) e comunicado NIDA.
  - *Sugestão:* Verificar ou retirar números.

### chapters/16-anexo-d-argumentacao.md

- **L109** `[@coffeeshop2024cud]`: Mesma fonte não verificada; "~30-33% dos utilizadores diários" só tem apoio parcial em Leung 2020 (33% em jovens com uso semanal/diário).
  - *Sugestão:* Ajustar a formulação e corrigir a referência.
- **L242** `[@cdphe2024monitoring]`: Relatório inacessível (403) e sem confirmação de 22%->12,8% por segunda via.
  - *Sugestão:* Verificar no relatório Healthy Kids Colorado.
- **L408** `[@monitoringthefuture2023]`: Idem.
  - *Sugestão:* Idem.


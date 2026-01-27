# GitHub Issues Prontas a Publicar

Este ficheiro contém issues formatadas e prontas a copiar-colar para GitHub. Organizadas por prioridade e expertise necessária.

## Como Usar

1. Vai a [github.com/bcamarneiro/cannabis-legalization/issues/new](https://github.com/bcamarneiro/cannabis-legalization/issues/new)
2. Escolhe template apropriado:
   - **"Fix Vulnerability (Técnico)"** para contribuidores com Git/GitHub
   - **"Proposta de Correção (Não-técnico)"** para contribuições via texto
3. Cola o conteúdo abaixo
4. Adiciona labels sugeridos

---

# 🔴 TIER 1 - PRIORIDADE MÁXIMA (4 issues)

## Issue #1: DEVIL 1 - The 2.6% Problem

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-critical`, `area-economics`, `tier-1`

```markdown
**ID:** DEVIL 1
**Tier/Categoria:** TIER 1 - Devastating Attack
**Prioridade:** 🔴 Crítica

## 🎯 Problema

Documento afirma que clubes vão servir 40-50% do mercado (282k-353k users), mas cálculo actual mostra:

- **46 clubes × 400 membros = 18.400 users**
- **18.400 ÷ 706.000 total = 2,6% do mercado**

**Gap explicativo de 15-17x sem modelo quantitativo.**

**Attack esperado:** *"Vocês afirmam clubes vão servir 282k-353k users mas os vossos próprios dados mostram 18.400. Como explicam isto?"*

## 🎯 Objectivo

Adicionar modelo quantitativo claro que explica como chegar a 40-50% de captura de mercado:

1. **% users que vão fazer autocultivo** (estimativa: 20-30%)
2. **Overlap clubes + autocultivo** (alguns users fazem ambos)
3. **Substitution rate do mercado negro** (gradual ao longo de anos)
4. **Expansão gradual número de clubes** (46 inicial → 150-200 em 5 anos?)

## 📋 Tarefas

- [ ] Pesquisar dados internacionais sobre split clube/autocultivo (Colorado, Canadá, Uruguai)
- [ ] Identificar assumptions razoáveis para Portugal (prevalência autocultivo, expansão clubes)
- [ ] Criar modelo Excel/Python com assumptions explícitas e projecções anos 1-10
- [ ] Escrever secção no documento explicando modelo (2-3 páginas)
- [ ] Adicionar gráficos/tabelas ilustrativas (crescimento clubes, captura mercado)
- [ ] Testar compilação PDF (`./scripts/build.sh`)

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Análise quantitativa / Modelação de dados
- Economia / Análise de mercados
- Excel/Python para projecções (pandas, matplotlib)
- Familiaridade com dados cannabis internacionais

## ⏱️ Esforço Estimado

6-8 horas (pesquisa + modelação + escrita)

## 📚 Recursos

- Colorado cannabis market data: [CDOR](https://cdor.colorado.gov/data-and-reports)
- Canadian cannabis statistics: [Statistics Canada](https://www150.statcan.gc.ca/n1/pub/13-610-x/13-610-x2019001-eng.htm)
- Uruguay club membership data: [IRCCA](https://www.ircca.gub.uy/)
- TASKS.md contexto completo: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #2: DEVIL 2 - Germany's 47% Operational Failure Rate

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-critical`, `area-international-policy`, `tier-1`

```markdown
**ID:** DEVIL 2
**Tier/Categoria:** TIER 1 - Devastating Attack
**Prioridade:** 🔴 Crítica

## 🎯 Problema

Documento trata Alemanha como "proven success" e modelo inspirador, mas realidade operacional:

- **357 clubes aprovados** (Novembro 2025)
- **Apenas 190 operacionais** (53% taxa operacional)
- **47% taxa de falha operacional**

Modelo português espelha CSCs alemães exactamente.

**Attack esperado:** *"Se o modelo alemão tem 47% failure rate após 9 meses, porque é que Portugal vai ter sucesso?"*

## 🎯 Objectivo

Escolher uma de duas estratégias (ou híbrido):

**Opção A - Acknowledge challenges + adjust expectativas:**
- Explicar porque alguns clubes alemães falharam (capital insuficiente, gestão, dificuldades operacionais)
- Ajustar expectativas portuguesas: 30-50% podem falhar também (realista)
- Mostrar que mesmo com 50% falha, ainda capturamos 20-25% mercado (suficiente para harm reduction)

**Opção B - Explicar diferenças Portugal vs Alemanha:**
- Portugal propõe **subsídio estatal €50-100k** (Alemanha não teve)
- **SICAD oversight mais forte** que modelo alemão descentralizado
- **Clima português favorece outdoor** (custos produção menores que Alemanha indoor)
- **Comunidade cannabis mais madura** em Portugal (25 anos descriminalização)

## 📋 Tarefas

- [ ] Pesquisar causas específicas de falha de clubes alemães (artigos, relatórios Bundesgesundheitsministerium)
- [ ] Ler alemão ou encontrar traduções de relatórios originais
- [ ] Decidir entre Opção A, B ou híbrido (consultar com equipa/comunidade)
- [ ] Escrever secção no documento (1-2 páginas)
- [ ] Adicionar referências alemãs atualizadas
- [ ] Ajustar secção "Modelos Internacionais - Alemanha" para refletir realidade operacional
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Análise política internacional
- Alemão (idioma) para ler relatórios originais (ou capacidade de usar traduções)
- Experiência em policy analysis comparada
- Familiaridade com implementação políticas públicas

## ⏱️ Esforço Estimado

4-6 horas (pesquisa + análise + escrita)

## 📚 Recursos

- Bundesgesundheitsministerium (BMG) relatórios: [Link](https://www.bundesgesundheitsministerium.de/)
- BCAv (Bundesverband Cannabis-versorgender Apotheken): 357 clubes aprovados dados
- Cannabis clubs Germany statistics: [Hanfverband](https://hanfverband.de/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #3: DEVIL 3 - Timeline Fantasy (3-4 anos realidade, não 18 meses)

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-critical`, `area-political-strategy`, `tier-1`

```markdown
**ID:** DEVIL 3
**Tier/Categoria:** TIER 1 - Devastating Attack
**Prioridade:** 🔴 Crítica

## 🎯 Problema

Documento claims timeline 12-18 meses até aprovação, citando:
- **Lei 30/2000** (descriminalização) - tinha consenso cross-party PS+PSD+comunidade médica
- **CanG 2024 Alemanha** - tinha supermajority

**Realidade Portugal 2026:**
- ❌ Sem consenso cross-party (PSD oposto, PS incerto)
- ❌ Sem supermajority (LIVRE minoria, depende coligações)
- ⏱️ Regulamentação secundária (INFARMED, IVV, SICAD, licensing) adiciona 18-24 meses

**Timeline realista:** 36-48 meses até aprovação, primeiros resultados piloto 2028-2030.

**Attack esperado:** *"Lei 30/2000 tinha apoio PS, PSD, consenso médico. Onde está o consenso agora? Vocês estão a enganar-se sobre a timeline."*

## 🎯 Objectivo

Revisar timeline para refletir cenário realista como primário (não optimista):

1. **Cenário Realista (primário):**
   - Proposta Q3-Q4 2026
   - Negociações/emendas/consultas públicas: 12-18 meses
   - Aprovação parlamentar: Q2-Q4 2027
   - Regulamentação secundária: 12-18 meses
   - Piloto operacional: 2028
   - Primeiros dados: 2028-2030

2. **Cenário Optimista (secundário):**
   - Timeline actual mantida como best-case scenario
   - Requer: apoio PS forte, negociação rápida, regulamentação paralela

3. **Cenário Pessimista:**
   - Mudanças governamentais, eleições intercalares
   - Oposição PSD/CDS bloqueia ou exige reformulações
   - Aprovação 2028-2029+

## 📋 Tarefas

- [ ] Analisar timelines de legislação controversa em Portugal (aborto, eutanásia, casamento igual)
- [ ] Pesquisar processo legislativo Lei 30/2000 (consensos necessários, tempo real)
- [ ] Pesquisar processo CanG Alemanha 2024 (supermajority SPD/Grüne, oposição CDU)
- [ ] Identificar bottlenecks prováveis em Portugal (regulamentação INFARMED, licenciamento, consultas)
- [ ] Reescrever secção Timeline com 3 cenários (optimista, realista, pessimista)
- [ ] Ajustar expectations documento (foco em "processo longo mas baseado em evidência")
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Experiência em processo legislativo português
- Ciência política / Análise política
- Familiaridade com Assembleia da República (comissões, negociações)
- Conhecimento de precedentes legislação controversa PT

## ⏱️ Esforço Estimado

4-6 horas (pesquisa + análise + reescrita)

## 📚 Recursos

- Processo legislativo Lei 30/2000: [@springer2021pt; @transform2016pt]
- Germany CanG timeline 2024: [@lancet2024germany]
- Assembleia da República processo legislativo: [parlamento.pt](https://www.parlamento.pt/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #4: DEVIL 4 - Colorado -42% Youth Drop é Tendência Nacional

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-critical`, `area-data-analysis`, `tier-1`

```markdown
**ID:** DEVIL 4
**Tier/Categoria:** TIER 1 - Devastating Attack
**Prioridade:** 🔴 Crítica

## 🎯 Problema

Documento claims legalização Colorado **causou** -42% queda consumo jovens (2011-2021).

**Realidade:**
- EUA inteiro (incluindo estados não-legalizados) viu **-38% decline** no mesmo período
- **Diferença de apenas 4 pontos percentuais** pode ser margin of error ou fatores regionais

**Attack esperado:** *"A queda aconteceu em todo o lado. Vocês estão claiming causation sem controlar para tendências nacionais. Correlation is not causation."*

## 🎯 Objectivo

Corrigir claim para ser defensável:

**Opção A - Remover claim causal:**
- Focar apenas em "consumo juvenil **não aumentou** pós-legalização" (isto é defensável)
- Remover language que sugere legalização causou queda

**Opção B - Reframe com contexto nacional:**
- "Colorado viu -42% enquanto média nacional foi -38%, sugerindo que legalização **não prejudicou** tendência positiva"
- Acknowledge tendência nacional, focar em "não causou epidemia temida"

**Opção C - Análise mais rigorosa:**
- Adicionar difference-in-differences analysis ou comparação com estados controlo
- Mostrar Colorado vs estados similares (demografia, políticas educação)

## 📋 Tarefas

- [ ] Pesquisar dados NIDA/SAMHSA consumo juvenil cannabis EUA 2011-2021 (estado por estado)
- [ ] Verificar margin of error nos surveys (YRBS, NSDUH)
- [ ] Identificar fatores confundidos (políticas educação, tendências culturais, vaping)
- [ ] Decidir entre Opção A, B ou C
- [ ] Reescrever secção Colorado no documento
- [ ] Adicionar referências atualizadas e metodologia clara
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Análise de dados / Estatística
- Familiaridade com metodologias epidemiológicas (difference-in-differences, controles)
- Experiência com dados survey (YRBS, NSDUH)
- Capacidade de identificar causal inference errors

## ⏱️ Esforço Estimado

3-5 horas (análise de dados + reescrita)

## 📚 Recursos

- NIDA national trends: [Link](https://nida.nih.gov/research-topics/trends-statistics/infographics/marijuana-use-among-youth-declining)
- SAMHSA NSDUH data: [Link](https://www.samhsa.gov/data/data-we-collect/nsduh-national-survey-drug-use-and-health)
- Colorado YRBS data: [Link](https://cdphe.colorado.gov/youth-risk-behavior-survey)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

# ⚖️ LEGAL - Para Advogados (9 issues)

## Issue #5: LEGAL 1 - International Treaty Obligations

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-critical`, `area-law`, `international-law`

```markdown
**ID:** LEGAL 1
**Tier/Categoria:** LEGAL - Critical Gap
**Prioridade:** 🔴 Crítica

## 🎯 Problema

Portugal é signatário de 3 convenções ONU sobre drogas:
- **1961 Single Convention on Narcotic Drugs**
- **1971 Psychotropic Substances Convention**
- **1988 Trafficking Convention**

Cannabis recreativa viola **Article 4** (limit to medical/scientific use only).

**Documento tem ZERO discussão sobre:**
- Treaty denunciation?
- Reinterpretation (Uruguay model)?
- Diplomatic consequences?
- EU-level challenges?

**Attack esperado:** *"Portugal vai violar tratados ONU assinados. Quais são as consequências internacionais? Isto é ilegal."*

## 🎯 Objectivo

Adicionar secção robusta (3-4 páginas) sobre estratégia tratados internacionais:

### 1. Precedente Uruguai
- Como interpretaram Article 4 (saúde pública justifica regulação estatal)
- Lei 19.172/2013 legal argumentation
- Reacção internacional: críticas mas **zero enforcement** (ONU não tem mecanismo punitivo)

### 2. Precedente Canadá
- Violou 3 tratados em 2018 (Cannabis Act)
- Trudeau revelou 2024: **"ONU nunca discutiu o tema"**
- Nenhuma sanção diplomática ou económica

### 3. Precedente Alemanha
- CanG 2024 também viola tratados
- Negociação EU-level ongoing
- CDU oposição citou tratados mas governo implementou mesmo assim

### 4. Opções Portugal
- **Opção A:** Reinterpretation (saúde pública justifica, seguir Uruguai)
- **Opção B:** Denunciation + re-ratification com reserva (complexo, lento)
- **Opção C:** Challenge coordenado EU-level (ideal mas requer coalition)

### 5. Análise Riscos
- Risco diplomático: baixo (precedentes sem sanções)
- Risco legal internacional: baixo (tratados sem enforcement real)
- Risco político interno: médio (oposição vai usar como argumento)

## 📋 Tarefas

- [ ] Ler Article 4 da Convenção 1961 (texto original + interpretações)
- [ ] Analisar caso Uruguai (Lei 19.172/2013, argumentação jurídica)
- [ ] Analisar caso Canadá (Cannabis Act 2018, declarações Trudeau 2024)
- [ ] Analisar caso Alemanha (CanG 2024, posição EU Commission)
- [ ] Consultar jurisprudência internacional (ICJ, UN bodies)
- [ ] Escrever secção no documento (3-4 páginas)
- [ ] Adicionar referências jurídicas apropriadas (tratados, casos, análises)
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

**ESSENCIAL:** Advogado com experiência em **Direito Internacional Público**

- Familiaridade com tratados ONU (Vienna Convention on Treaties)
- Experiência em análise jurídica internacional
- Capacidade de leitura crítica de precedentes (Uruguai, Canadá)

## ⏱️ Esforço Estimado

1-2 dias (pesquisa jurídica extensiva + escrita)

## 📚 Recursos

- UN Single Convention 1961: [Link](https://www.unodc.org/unodc/en/treaties/single-convention.html)
- Uruguay Lei 19.172/2013: [Link](https://www.impo.com.uy/bases/leyes/19172-2013)
- Canada Cannabis Act: [Link](https://laws-lois.justice.gc.ca/eng/acts/c-24.5/)
- Germany CanG 2024: [Link](https://www.bundesgesundheitsministerium.de/)
- Transform Drug Policy analysis: [Link](https://transformdrugs.org/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #6: LEGAL 2 - EU Law Conflicts (Schengen Free Movement)

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-law`, `eu-law`

```markdown
**ID:** LEGAL 2
**Tier/Categoria:** LEGAL - Structural Gap
**Prioridade:** 🟠 Alta

## 🎯 Problema

**Schengen free movement + cannabis legal PT mas ilegal ES/FR = nightmare enforcement fronteiras.**

Cenário problemático:
- Turista francês compra cannabis clube Lisboa
- Volta França de carro com cannabis no carro
- **= Tráfico internacional? Crime em França mas legal compra em PT?**

Documento não discute:
- Coordenação EU cross-border
- Liability legal para clubes que vendem a estrangeiros
- Enforcement fronteiras (GNR, Guardia Civil espanhola)
- Diplomatic incidents potenciais

**Attack esperado:** *"Vai criar zona Schengen lawless. França e Espanha vão pressionar Portugal diplomaticamente."*

## 🎯 Objectivo

Adicionar secção sobre coordenação EU e gestão de riscos cross-border:

1. **Modelo residência obrigatória** (6 meses mínimo, NIF português)
2. **Proibição turistas** aceder clubes (prevenir "Amsterdam problem")
3. **Warning clear** em clubes: "Transporte cross-border ilegal"
4. **Bilateral agreements** com Espanha/França (coordenação enforcement, não perseguição residentes PT)
5. **Schengen exemption** (como firearms - controlado mas legal em alguns estados)

## 📋 Tarefas

- [ ] Pesquisar Schengen law sobre substâncias controladas
- [ ] Analisar modelo Holanda (cannabis tolerado, problemas fronteiras Bélgica/Alemanha)
- [ ] Pesquisar bilateral agreements possíveis (precedentes EU)
- [ ] Consultar Direito UE sobre livre circulação vs harmonização penal
- [ ] Escrever secção no documento (2-3 páginas)
- [ ] Adicionar referências jurídicas EU
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

**ESSENCIAL:** Advogado com experiência em **Direito Europeu**

- Familiaridade com Schengen Agreement
- Conhecimento sobre livre circulação vs soberania penal
- Experiência em análise de conflitos de jurisdição

## ⏱️ Esforço Estimado

6-8 horas (pesquisa + análise + escrita)

## 📚 Recursos

- Schengen Agreement: [Link](https://ec.europa.eu/home-affairs/policies/schengen-borders-and-visa_en)
- Holanda cannabis policy: [Government.nl](https://www.government.nl/)
- EU drug laws: [EUDA](https://www.euda.europa.eu/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #7: LEGAL 5 - IVA Problem (Taxation Inconsistency)

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-law`, `tax-law`

```markdown
**ID:** LEGAL 5
**Tier/Categoria:** LEGAL - Structural Gap
**Prioridade:** 🟠 Alta

## 🎯 Problema

Documento afirma **"cost-recovery only, ZERO receitas fiscais"**, mas:

- **Portugal tem IVA 23% obrigatório** sobre bens e serviços
- Clubes são associações sem fins lucrativos mas fornecem produto

**Contradiction clara:**
- Se clubes pagam IVA 23% → **há tax revenue** (contradiz modelo "zero impostos")
- Se clubes exempt IVA → precisa **legislative exemption específica** (complica approval)

**Attack esperado:** *"Vocês dizem zero impostos mas IVA 23% é obrigatório em Portugal. Qual é a verdade? Estão a esconder receitas fiscais?"*

## 🎯 Objectivo

Clarificar regime fiscal dos clubes de cannabis:

### Opção A - Isenção IVA (modelo IPSS)
- Clubes como **IPSS (Instituições Particulares de Solidariedade Social)** - isentas IVA
- Requer alteração legislativa específica
- **Precedente:** Associações culturais/desportivas isentas

**Vantagens:** Coerente com "zero tax revenue"
**Desvantagens:** Complica approval (mais legislative hurdles)

### Opção B - IVA aplicável mas revenue minor
- Clubes pagam IVA 23% normalmente
- **Revenue estimado:** ~€2-3M/ano (46 clubes × €280k revenue × 23%)
- **Clarificar language:** "ZERO impostos diretos sobre cannabis" não "ZERO receitas fiscais"

**Vantagens:** Mais simples legislativamente
**Desvantagens:** Contradiz messaging "cost-recovery only"

## 📋 Tarefas

- [ ] Consultar **Código IVA** português (isenções IPSS, associações)
- [ ] Pesquisar regime fiscal associações sem fins lucrativos
- [ ] Calcular impact IVA 23% em pricing clubes (passa a consumidores?)
- [ ] Analisar precedentes: associações culturais, desportivas, IPSS
- [ ] Decidir entre Opção A ou B (consultar com equipa)
- [ ] Escrever secção "Regime Fiscal" no documento (1-2 páginas)
- [ ] Adicionar referências legislação fiscal
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

**ESSENCIAL:** Advogado **Tributarista** ou **Contabilista Certificado**

- Familiaridade com Código IVA português
- Experiência em regime fiscal associações/IPSS
- Conhecimento de isenções fiscais existentes

## ⏱️ Esforço Estimado

4-6 horas (pesquisa fiscal + análise + escrita)

## 📚 Recursos

- Código IVA Portugal: [Link](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa/)
- Regime IPSS: [Link](https://www.seg-social.pt/)
- Estatuto Benefícios Fiscais: [Link](https://info.portaldasfinancas.gov.pt/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #8: LEGAL 3 - Workplace Drug Testing

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-law`, `labor-law`

```markdown
**ID:** LEGAL 3
**Tier/Categoria:** LEGAL - Structural Gap
**Prioridade:** 🟠 Alta

## 🎯 Problema

**Cannabis legal mas employers podem despedir por positive test?**

Documento não address implicações Código do Trabalho português:

- Uso legal off-duty pode resultar em positive test dias depois
- THC metabolites detectáveis 7-30 dias após consumo
- **Precedente Colorado:** Coats v. Dish Network (2015) - employer CAN fire even for off-duty legal use

**Diferença Portugal vs EUA:**
- PT tem **stronger labor protections** (despedimento requer justa causa)
- Mas empresas podem argumentar "segurança" (motoristas, operadores máquinas)

**Attack esperado:** *"Trabalhadores vão ser despedidos por uso legal. Cannabis vai criar discriminação laboral."*

## 🎯 Objectivo

Adicionar secção sobre direitos laborais e drug testing:

1. **Análise Código Trabalho:**
   - Quando é que drug testing é permitido (safety-sensitive positions)
   - Justa causa despedimento vs uso legal off-duty
   - Protecções privacidade trabalhador (RGPD)

2. **Proposta Legislativa:**
   - Proibir discriminação por uso legal cannabis off-duty
   - **Exceção:** Safety-sensitive positions (pilotos, motoristas camiões, operadores)
   - Testes devem medir **impairment actual** não metabolites (difícil tecnicamente)

3. **Protecções Trabalhadores:**
   - Políticas workplace claras (quando testing é permitido)
   - Due process antes despedimento
   - Comparação com álcool (legal, mas impairment no trabalho é falta grave)

## 📋 Tarefas

- [ ] Analisar **Código do Trabalho** português (despedimento justa causa, testing)
- [ ] Pesquisar jurisprudência PT sobre drug testing (casos existentes)
- [ ] Estudar caso Coats v. Dish Network (Colorado) e implicações
- [ ] Pesquisar legislação Colorado/Washington sobre workplace protections
- [ ] Consultar RGPD implicações (privacidade dados saúde)
- [ ] Escrever secção no documento (2-3 páginas)
- [ ] Propor language legislativo para proteger trabalhadores
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

**ESSENCIAL:** Advogado especialista em **Direito do Trabalho**

- Familiaridade com Código do Trabalho PT
- Experiência em litígio laboral
- Conhecimento RGPD (dados de saúde)

## ⏱️ Esforço Estimado

6-8 horas (pesquisa jurídica + análise + proposta legislativa)

## 📚 Recursos

- Código do Trabalho: [Link](https://dre.pt/legislacao-consolidada/-/lc/123915628/202201072129/exportPdf/normal/1/cacheLevelPage?_LegislacaoConsolidada_WAR_drefrontofficeportlet_rp=indice)
- Coats v. Dish Network (2015): [Case law](https://www.lexisnexis.com/)
- Colorado workplace protections: [Link](https://cdle.colorado.gov/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

# 💊 HEALTH - Para Profissionais de Saúde (4 issues)

## Issue #9: HEALTH 1 - 10% THC Cap 18-20 vs Full THC 21+ Inconsistent

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-health`, `medical-review`

```markdown
**ID:** HEALTH 1
**Tier/Categoria:** HEALTH - Public Health Contradiction
**Prioridade:** 🟠 Alta

## 🎯 Problema

Documento justifica **10% THC limit 18-20 anos** para "proteger desenvolvimento cognitivo frontal cortex", MAS permite **full 20-25% THC aos 21+**.

**Evidência científica contraditória:**
- Brain development continua até **~25 anos** (Casey 2019, frontal cortex maturation)
- Se cognitive protection é rationale, limite deveria ser:
  - **10% THC até 25 anos**, OR
  - **Full THC 18+** (risco informado, autonomia adultos)

**Inconsistency arbitrária do limite aos 21 anos.**

**Attack esperado:** *"Se proteger o cérebro é importante, porque é que aos 21 podem usar 25% THC? O cérebro ainda se desenvolve até aos 25. Isto é inconsistente."*

## 🎯 Objectivo

Resolver inconsistência científica de uma de três formas:

### Opção A - Extend THC cap até 25 anos
- 10% THC limit até 25 anos (alinhado com evidência neurociência)
- **Problema:** Politicamente difícil (adultos 21-25 já podem votar, casar, etc.)

### Opção B - Remove THC cap (full THC 18+)
- Confiar em educação + Oficial de Prevenção monitoring
- Comparar com álcool (sem limits de "proof" por idade)
- **Problema:** Parece menos protector de jovens

### Opção C - Manter 21 mas justificar diferente
- Não usar "brain development" como rationale primário
- Focar em: "Transition period com monitoring" (18-20 entrada gradual)
- Aos 21+ assumir autonomia adulta plena (mesmo que brain ainda desenvolve)

## 📋 Tarefas

- [ ] Ler estudos brain development (Casey 2019, outros)
- [ ] Pesquisar evidência sobre high-THC cannabis e riscos cognitivos por idade
- [ ] Analisar políticas internacionais (Colorado, Canadá - têm THC caps por idade?)
- [ ] Consultar médicos/psiquiatras sobre idade apropriada para autonomia
- [ ] Decidir entre Opção A, B ou C
- [ ] Reescrever justificação científica no documento
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

**ESSENCIAL:** Médico (Psiquiatria, Neurologia, ou Saúde Pública)

- Familiaridade com literatura neurociência do desenvolvimento
- Experiência clínica com jovens e substâncias
- Capacidade de equilibrar evidência científica com pragmatismo político

## ⏱️ Esforço Estimado

4-6 horas (revisão literatura + análise + reescrita)

## 📚 Recursos

- Casey et al. (2019): Adolescent brain development
- Di Forti et al. (2019): High-potency cannabis and psychosis
- Colorado THC regulations: [Link](https://cdphe.colorado.gov/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #10: DEVIL 8 - Health Risks Vulnerabilities

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-health`, `medical-review`

```markdown
**ID:** DEVIL 8
**Tier/Categoria:** TIER 3 - Exploitable Gap
**Prioridade:** 🟠 Alta

## 🎯 Problema

Documento underplays riscos cardiovasculares e psiquiátricos:

**Missing completamente:**
- **Myocardial infarction +1.75x** 1h pós-consumo (Mittleman 2001) - NÃO MENCIONADO

**Presente mas underplayed:**
- **Psychosis +4.8x** young heavy users (Di Forti 2019) - mencionado mas não destacado

**Attack esperado:** *"Vocês escondem que cannabis aumenta ataques cardíacos 75% e psicose quase 5x. Documento desonesto sobre riscos."*

## 🎯 Objectivo

Criar secção "Riscos para Saúde" mais honesta e completa:

### 1. Riscos Cardiovasculares
- **MI +75% 1h pós-consumo** (Mittleman 2001)
- Risco absoluto baixo (jovens saudáveis), mas significativo >65 anos ou história cardíaca
- **Mitigação proposta:**
  - Screening cardíaco por Oficial Prevenção
  - Exclusão >65 anos ou história cardiovascular
  - Warning labels em produtos

### 2. Riscos Psiquiátricos
- **Psychosis +4.8x** heavy users <25 anos high-THC (Di Forti 2019)
- Dose-response relationship (daily use, high potency)
- **Mitigação proposta:**
  - THC cap 10% para 18-21 anos
  - Screening PHQ-9/GAD-7 (Oficial Prevenção)
  - Referenciação SNS se sintomas psicóticos

### 3. Apresentação Honesta
- **Upfront, primeira secção "Saúde"** (não esconder)
- Comparação com álcool (MI similar, psychosis similar)
- **Ênfase nas mitigações:** Controlo qualidade, screening, THC limits, idade

## 📋 Tarefas

- [ ] Ler estudos completos: Mittleman 2001, Di Forti 2019
- [ ] Pesquisar outros riscos major: respiratory, cognitive, CUD
- [ ] Escrever secção "Riscos Cardiovasculares e Psiquiátricos" (2-3 páginas)
- [ ] Adicionar referências médicas apropriadas
- [ ] Integrar com secção "Mitigações" (Oficial Prevenção role)
- [ ] Mover secção para início capítulo Saúde (não esconder no fim)
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

**ESSENCIAL:** Médico (Cardiologia, Psiquiatria, ou Saúde Pública)

- Familiaridade com literatura médica cannabis
- Experiência clínica com complicações cardiovasculares ou psiquiátricas
- Capacidade de comunicar riscos de forma honesta mas não alarmista

## ⏱️ Esforço Estimado

4-6 horas (revisão literatura + escrita + integração)

## 📚 Recursos

- Mittleman (2001): Triggering of myocardial infarction by marijuana
- Di Forti (2019): Daily use, high-potency cannabis and psychosis
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

# 📊 ECON - Para Economistas (5 issues)

## Issue #11: ECON 1 - ROI Sensitivity Analysis Missing

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-economics`, `financial-modeling`

```markdown
**ID:** ECON 1
**Tier/Categoria:** ECON - Financial Vulnerability
**Prioridade:** 🟠 Alta

## 🎯 Problema

Documento claims **ROI 120-753%**, mas:

- Baseado em assumption **100% clubes succeed operationally**
- Alemanha mostra **47% failure rate** nos primeiros 9 meses
- **Zero sensitivity analysis** para cenários piores

**Attack esperado:** *"Se 30-50% dos clubes portugueses falharem como na Alemanha, o ROI colapsa. Onde está a análise de cenários? Vocês só mostram best-case."*

## 🎯 Objectivo

Adicionar **análise de sensibilidade robusta** com múltiplos cenários:

### Cenário 1: Optimista (baseline actual)
- 90% clubes succeed operationally
- 45% market capture (ano 5-10)
- **ROI: 500-750%**

### Cenário 2: Realista
- 70% clubes succeed
- 30% market capture
- **ROI: 200-400%**

### Cenário 3: Pessimista (Germany-level)
- 50% clubes succeed
- 20% market capture
- **ROI: 50-150%**

### Cenário 4: Worst case
- 30% clubes succeed
- 10% market capture
- **ROI: -50% a +50%** (breakeven)

### Variáveis-chave a modelar:
- % clubes operational success
- Market capture rate (anos 1-10)
- Poupanças enforcement (dependem de market capture)
- Custos implementation (fixos vs variáveis)

## 📋 Tarefas

- [ ] Criar modelo Excel/Google Sheets com variáveis sensíveis
- [ ] Implementar 4 cenários (optimista, realista, pessimista, worst-case)
- [ ] Calcular ROI para cada cenário
- [ ] Criar gráficos ilustrativos:
  - Tornado chart (sensitivity variáveis)
  - Scenario comparison bar chart
  - ROI over time (anos 1-10) por cenário
- [ ] Escrever secção "Análise de Sensibilidade ROI" (2-3 páginas)
- [ ] Integrar no documento (Anexo ou secção Propostas)
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Economista ou Analista Financeiro
- Excel avançado / Python (pandas, matplotlib)
- Experiência em sensitivity analysis / scenario planning
- Familiaridade com modelação ROI

## ⏱️ Esforço Estimado

8-10 horas (modelação + gráficos + escrita)

## 📚 Recursos

- Documento atual modelo económico: Anexo A (L2585-2750)
- Germany club failure data: 357 approved, 190 operational
- Modelo Excel template: [pode ser criado do zero]
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #12: ECON 2 - Startup Capital Gap €68k-152k

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-economics`, `financial-modeling`

```markdown
**ID:** ECON 2
**Tier/Categoria:** ECON - Financial Vulnerability
**Prioridade:** 🟠 Alta

## 🎯 Problema

Documento diz clubes precisam **€168k-252k capital inicial**, propõe:

- **Subsídio Estado:** €50-100k (apenas 30-40% do needed)
- **Gap restante:** €68k-152k

**Proposta actual:** "Quotas fundadores €500-1000 × 200-300 pessoas = €100k-300k"

**Problema:** Assume 200-300 pessoas pagam €500-1000 upfront **antes clube existir**. Unrealistic.

**Realidade bancária:**
- Banks historically refuse cannabis business (mesmo legal)
- EUA: apenas 20% banks servem cannabis após 10+ anos
- Alemanha: 190 clubes operacionais mas desconhecido se tiveram banking access

**Attack esperado:** *"Clubes não vão conseguir capital inicial. Banks vão recusar. Modelo é letra morta - bom no papel, impossível na prática."*

## 🎯 Objectivo

Resolver capital gap com opções realistas:

### 1. Aumentar subsídio estatal
- De €50-100k para €100-150k (cobrir 60-80% capital)
- Justificação: investimento público em saúde pública
- **Problema:** Aumenta custos OE

### 2. Modelo faseado capital
- **Fase 1:** €50k inicial (facilities, licenças) - subsídio
- **Fase 2:** €50-100k operacional (6 meses giro) - quotas fundadores após clube aprovado
- **Fase 3:** Breakeven após 12-18 meses
- **Vantagem:** Fundadores pagam quando vêem clube aprovado (menos risco)

### 3. Banking solution proativa
- **Diálogo pré-emptive com Banco de Portugal** (regulatory clarity)
- **Safe harbor legislativo** para bancos servindo clubes (protecção legal)
- **Banca pública/cooperativa:** CGD, Crédito Agrícola (missão social)

### 4. Crowdfunding cooperativo
- Plataformas PPL (Pessoas, Projectos, Lugares)
- Comunidade cannabis financia clubes (pre-membership)

## 📋 Tarefas

- [ ] Calcular capital mínimo viável (MVP clube pequeno 200 membros)
- [ ] Pesquisar banking access Alemanha (190 clubes - como financiaram?)
- [ ] Analisar modelos faseamento capital (startup literature)
- [ ] Consultar Banco de Portugal sobre regulatory clarity (informal/formal)
- [ ] Propor alteração subsídio ou modelo faseado
- [ ] Escrever secção "Financiamento Inicial Clubes" (1-2 páginas)
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Economista, Analista Financeiro, ou Empreendedor
- Experiência em startup financing
- Familiaridade com crowdfunding / cooperative models
- Conhecimento banking regulations (bonus)

## ⏱️ Esforço Estimado

6-8 horas (análise + pesquisa + proposta)

## 📚 Recursos

- Documento modelo económico atual: Anexo A
- Germany cannabis club financing: [pesquisa necessária]
- Banking cannabis EUA: SAFER Banking Act
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

# 🎯 STRATEGIC - Para Analistas Políticos (4 issues)

## Issue #13: STRATEGIC 1 - EU Blocked Germany's Pillar 2 Commercial Sales

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-critical`, `area-political-strategy`, `strategic`

```markdown
**ID:** STRATEGIC 1
**Tier/Categoria:** STRATEGIC - Critical Blind Spot
**Prioridade:** 🔴 Crítica

## 🎯 Problema

Documento menciona "transição para modelo comercial" como possibilidade futura, MAS:

**Realidade Alemanha:**
- **CanG Pillar 2** (commercial retail) foi **BLOQUEADO by EU Commission**
- Razão: Schengen violations (turismo cannabis cross-border)
- **Status 2025:** 49 municípios aplicaram pilotos comerciais, **todos bloqueados**
- **CDU assumiu governo 2025, reversing progress**

**Attack esperado:** *"Vocês prometem venda comercial futura mas UE bloqueou exactamente isso na Alemanha. Estão a iludir pessoas. Clubes são endpoint permanente, não transição."*

## 🎯 Objectivo

Clarificar strategic positioning sobre modelo comercial futuro:

### Opção A - Commit apenas a clubes (honestidade)
- Explicar que venda comercial requer **coordenação EU-level** (não depende só PT)
- Alemanha blocked = precedente difícil
- **Clubes non-profit são endpoint realista** (pelo menos próximos 10-15 anos)

### Opção B - Challenge EU law (ambicioso)
- Portugal pode propor challenge coordenado EU-level
- Argumentar: Schengen já tem inconsistências (drogas, firearms, etc.)
- **Requer coalition** com outros estados (Alemanha?, Holanda?, Luxemburgo?)
- Timeline: 10-20 anos minimum

### Opção C - Two-phase conditional (pragmático)
- **Fase 1:** Clubes (implementação 2027-2030)
- **Decisão Fase 2 baseada em:**
  1. Dados piloto positivos (2028-2030)
  2. Evolução contexto EU (outros países legalizam?)
  3. Approval parlamentar renovada pós-avaliação
- **Honesto:** "Não prometemos comercial, apenas avaliamos se viável"

## 📋 Tarefas

- [ ] Pesquisar CanG Pillar 2 Alemanha (49 municípios, bloqueios EU)
- [ ] Analisar argumentos EU Commission (Schengen violations)
- [ ] Pesquisar posição outros estados EU (Holanda, Luxemburgo, Malta)
- [ ] Decidir entre Opção A, B ou C (consultar equipa)
- [ ] Escrever secção "Modelo Comercial Futuro: Realismo vs Ambição" (2-3 páginas)
- [ ] Ajustar Executive Summary com strategic phasing explícito
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Analista político com experiência EU policy
- Familiaridade com Schengen Agreement
- Conhecimento de processo legislativo EU (Commission, Parliament)
- Experiência em policy advocacy EU-level (bonus)

## ⏱️ Esforço Estimado

6-8 horas (pesquisa + análise + escrita estratégica)

## 📚 Recursos

- Germany CanG Pillar 2: [BMG reports](https://www.bundesgesundheitsministerium.de/)
- EU Commission position on cannabis: [pesquisa necessária]
- Schengen Agreement: [Link](https://ec.europa.eu/home-affairs/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

## Issue #14: POLITIC 3 - Media Strategy Completely Absent

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-political-strategy`, `media`

```markdown
**ID:** POLITIC 3
**Tier/Categoria:** POLITIC - Political Naivety
**Prioridade:** 🟠 Alta

## 🎯 Problema

**Documento não menciona media relations, communications strategy.**

**Realidade media portuguesa:**
- **TVI, SIC, principais jornais** lean conservative em temas drogas
- **Tabloids** vão explorar every club failure, youth access incident, traffic accident
- Headlines inevitáveis: *"Clubes cannabis = narcotráfico disfarçado"*

**Precedentes:**
- Descriminalização 2001: initial media hysteria ("Portugal vai ser narco-state")
- Eutanásia: cobertura sensacionalista, oposição amplificada

**Sem estratégia media proativa:**
- Narrativa dominada por oposição (Chega, PSD conservadores, Igreja)
- Casos negativos amplificados, casos positivos ignorados
- Public opinion shift contra proposta antes de implementar

**Attack esperado:** *"Vocês não têm plano para lidar com media. Vão ser massacrados na opinião pública."*

## 🎯 Objectivo

Desenvolver **estratégia media completa** como anexo do documento:

### 1. Proactive Media Relations
- **Spokesperson training:** Médicos, especialistas addiction, não políticos
- **Press kit:** Fact sheets, infographics, Q&A antecipando perguntas difíceis
- **Media partnerships:** Outlets progressive/centrist (Público, Expresso)

### 2. Rapid Response Team
- **Monitoring:** Track cobertura 24/7 (Google Alerts, Slack channel)
- **Response protocol:** <2h response a claims falsos (fact-checking)
- **Spokespeople available:** Médico, economista, jurista (não só políticos)

### 3. Sympathetic Voices Preparadas
- **Medical community:** Médicos Sem Fronteiras, especialistas addiction SICAD
- **Academic community:** Criminólogos, economistas, sociólogos
- **Patient advocates:** Cannabis medicinal patients (humanizar narrativa)

### 4. Counter-Narratives
- **Frame positivo:** "Saúde pública, não liberalização drogas"
- **Precedente 2001:** "Descriminalização funcionou, mundo admirou"
- **Evidence-based:** "Decisão baseada 25 anos dados, não ideologia"

### 5. Crisis Management
- **Worst-case scenarios:** Youth overdose, traffic accident, club diversion
- **Response protocols:** Acknowledge, context, mitigations
- **Never:** Defensive/dismissive (aprende com eutanásia rollout)

## 📋 Tarefas

- [ ] Analisar cobertura media descriminalização 2001 (narrativas, frames)
- [ ] Identificar journalists sympathetic (Público, Expresso, Visão)
- [ ] Identificar spokespeople credíveis (médicos, académicos, não políticos)
- [ ] Desenvolver Q&A antecipando 20-30 perguntas difíceis
- [ ] Criar press kit (fact sheets, infographics, 1-pagers)
- [ ] Escrever secção "Estratégia Comunicação e Media" (3-4 páginas, Anexo)
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Jornalista ou Communications strategist
- Experiência em media relations (política ou advocacy)
- Familiaridade com media portuguesa (outlets, journalists)
- Crisis management experience (bonus)

## ⏱️ Esforço Estimado

1-2 dias (análise media landscape + estratégia completa)

## 📚 Recursos

- Media coverage Lei 30/2000: [arquivo jornais 2000-2001]
- Transform Drug Policy communications: [Link](https://transformdrugs.org/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

# ⚙️ IMPLEMENTATION - Para Especialistas Técnicos (7 issues)

## Issue #15: IMPLEMENT 2 - Laboratory Testing Infrastructure Undefined

**Template:** Fix Vulnerability (Técnico)
**Labels:** `help-wanted`, `priority-high`, `area-implementation`, `technical`

```markdown
**ID:** IMPLEMENT 2
**Tier/Categoria:** IMPLEMENT - Operational Gap
**Prioridade:** 🟠 Alta

## 🎯 Problema

Documento exige **testes obrigatórios ISO 17025** para todos os lotes clubes:

Testes necessários:
- THC/CBD (HPLC)
- Pesticidas (GC-MS, LC-MS)
- Metais pesados (ICP-MS)
- Micotoxinas (LC-MS/MS)
- Microorganismos (culture)

**Questões não respondidas:**
- Quantos labs ISO 17025 em Portugal podem test cannabis **actualmente**?
- Precisam build capacity? Quanto custa equipment? (HPLC, GC-MS, LC-MS, ICP-MS = **€500k-2M**)
- Timeline accreditation (ISO 17025 process = **12-18 meses**)
- **Gap pode delay piloto inteiro**

**Attack esperado:** *"Vocês exigem testes mas não há labs em Portugal. Piloto vai atrasar anos só para build infrastructure."*

## 🎯 Objectivo

Mapear laboratory infrastructure atual e propor solução:

### 1. Survey Labs Actuais
- Identificar labs ISO 17025 Portugal (IPAC accreditation)
- Quais podem test cannabis? (alguns recusam por estigma)
- Capacity actual (quantos testes/mês?)

### 2. Gap Analysis
- **Demand estimado:** 46 clubes × 12 lotes/ano = **552 testes/ano**
- **Capacity actual:** ??? (pesquisa necessária)
- **Gap:** Se capacity < demand, quanto investment needed?

### 3. Build-Out Plan
- **Opção A:** Expand existing labs (IPAC, university labs)
- **Opção B:** Create dedicated cannabis testing lab (INFARMED?)
- **Opção C:** Use existing medicinal cannabis labs (Tilray, Bedrocan)

### 4. Timeline e Custos
- Equipment costs (se new lab needed)
- Accreditation timeline (12-18 meses)
- Operating costs (€150-300/teste)
- **Build into pilot timeline** (testing infrastructure ready Q2 2027)

## 📋 Tarefas

- [ ] Contactar IPAC (Instituto Português de Acreditação) - lista labs ISO 17025
- [ ] Survey labs: capacidade test cannabis? (phone/email)
- [ ] Pesquisar costs equipment (HPLC, GC-MS, etc.)
- [ ] Consultar INFARMED - labs medicinal cannabis podem scale?
- [ ] Calcular demand total (46 clubes × 12 lotes/ano)
- [ ] Propor solution (expand existing vs build new)
- [ ] Escrever secção "Infrastructure Testes Laboratoriais" (1-2 páginas)
- [ ] Adicionar a cronograma (testing ready Q2 2027)
- [ ] Testar compilação PDF

## 🧠 Expertise Recomendada

- **ESSENCIAL:** Químico analítico ou Técnico laboratório
- Familiaridade com ISO 17025 accreditation
- Experiência em analytical chemistry (HPLC, GC-MS, etc.)
- Conhecimento de cannabis testing (bonus)

## ⏱️ Esforço Estimado

8-10 horas (survey labs + análise gap + proposta)

## 📚 Recursos

- IPAC (Instituto Português de Acreditação): [Link](https://www.ipac.pt/)
- ISO 17025 standard: [Link](https://www.iso.org/standard/66912.html)
- Cannabis testing protocols: [AOAC](https://www.aoac.org/)
- TASKS.md contexto: [Link](https://github.com/bcamarneiro/cannabis-legalization/blob/main/docs/TASKS.md)

---

**Para contribuir:** Ver [CONTRIBUTING.md](https://github.com/bcamarneiro/cannabis-legalization/blob/main/CONTRIBUTING.md)
```

---

# 📊 RESUMO ISSUES POR EXPERTISE

Para facilitar recrutamento, aqui está a distribuição por expertise:

## ⚖️ Advogados (9 issues)
- **Issue #5:** LEGAL 1 - International Treaty Obligations (Direito Internacional) - 🔴 Crítica
- **Issue #6:** LEGAL 2 - EU Law Conflicts (Direito Europeu) - 🟠 Alta
- **Issue #7:** LEGAL 5 - IVA Problem (Direito Tributário) - 🟠 Alta
- **Issue #8:** LEGAL 3 - Workplace Drug Testing (Direito Trabalho) - 🟠 Alta
- LEGAL 4: Autocultivo Enforcement Paradox
- LEGAL 6: Product Liability Insurance
- LEGAL 7: Child Custody Weaponization
- LEGAL 8: Clube Location Zoning
- LEGAL 9: Medical Cannabis Patient Stigma

## 💊 Médicos/Saúde Pública (4 issues)
- **Issue #9:** HEALTH 1 - THC Cap Inconsistency (Neurologia/Psiquiatria) - 🟠 Alta
- **Issue #10:** DEVIL 8 - Health Risks (Cardiologia/Psiquiatria) - 🟠 Alta
- HEALTH 2: Harm Reduction vs Dual Use
- HEALTH 3: Oficial Prevenção Role
- HEALTH 4: Youth Access Social Supply

## 📊 Economistas (5 issues)
- **Issue #1:** DEVIL 1 - The 2.6% Problem (Modelação quantitativa) - 🔴 Crítica
- **Issue #11:** ECON 1 - ROI Sensitivity Analysis (Financial modeling) - 🟠 Alta
- **Issue #12:** ECON 2 - Startup Capital Gap (Financiamento) - 🟠 Alta
- ECON 3: Oficial Prevenção Salário Subdimensionado
- ECON 4: Churn Rate Not Modeled
- ECON 5: Laboratory Testing Costs Underestimated

## 🎯 Analistas Políticos (10 issues)
- **Issue #2:** DEVIL 2 - Germany Failure Rate (Policy analysis internacional) - 🔴 Crítica
- **Issue #3:** DEVIL 3 - Timeline Fantasy (Processo legislativo PT) - 🔴 Crítica
- **Issue #13:** STRATEGIC 1 - EU Blocked Pillar 2 (EU policy) - 🔴 Crítica
- **Issue #14:** POLITIC 3 - Media Strategy (Communications) - 🟠 Alta
- POLITIC 1: PS 2024 ≠ PS 2000
- POLITIC 2: PSD "Dados Convencem" Naive
- POLITIC 4: Catholic Church Influence
- POLITIC 5: Pharmaceutical Lobbying
- POLITIC 6: Referendum Risk
- STRATEGIC 2: Phased Implementation Reversal Risk

## 📈 Analistas de Dados (2 issues)
- **Issue #4:** DEVIL 4 - Colorado Youth Drop (Estatística/causal inference) - 🔴 Crítica
- DEVIL 9: Canada 72% Survey-Based

## ⚙️ Técnicos/Implementação (7 issues)
- **Issue #15:** IMPLEMENT 2 - Laboratory Infrastructure (Química analítica) - 🟠 Alta
- IMPLEMENT 1: Oficial Prevenção Training Pipeline
- IMPLEMENT 3: SICAD Capacity Expansion
- IMPLEMENT 4: Seed Certification Body
- IMPLEMENT 5: Municipal Coordination
- IMPLEMENT 6: IT Infrastructure
- IMPLEMENT 7: Cross-Border EU Coordination

---

# 📣 COMO DIVULGAR

## Twitter/X

```
🚨 Procuram-se especialistas para melhorar proposta regulação cannabis @LivrePartido

Precisamos de:
⚖️ Advogados (Direito Internacional, Tributário, Trabalho, EU)
💊 Médicos (Cardiologia, Psiquiatria, Saúde Pública)
📊 Economistas (Modelação financeira, ROI analysis)
🎯 Analistas Políticos (Media strategy, EU policy)
⚙️ Técnicos (Labs ISO 17025, IT infrastructure)

15 issues prioritárias documentadas, prontas para contribuir.

📂 GitHub: github.com/bcamarneiro/cannabis-legalization
✉️ Contacto: bruno@camarneiro.com

#PolíticasDeDrogas #HarmReduction #EvidenceBasedPolicy
```

## LinkedIn

```
**Chamada para Especialistas: Regulação Cannabis em Portugal**

O LIVRE está a desenvolver uma proposta de regulação da cannabis baseada em evidência científica e direitos humanos. Identificámos 50+ vulnerabilidades técnicas que precisam de expertise especializada.

**15 issues prioritárias prontas para contribuir:**

⚖️ **ADVOGADOS** (9 issues)
- Tratados internacionais ONU (CRÍTICO)
- Conflitos Direito EU / Schengen (CRÍTICO)
- Regime fiscal IVA (ALTA)
- Direito do trabalho & drug testing (ALTA)

💊 **MÉDICOS** (4 issues)
- Riscos cardiovasculares (Mittleman 2001)
- Riscos psiquiátricos (Di Forti 2019)
- Inconsistências THC limits por idade

📊 **ECONOMISTAS** (5 issues)
- Modelação quantitativa market capture (CRÍTICO)
- ROI sensitivity analysis (ALTA)
- Capital gap financing (ALTA)

🎯 **ANALISTAS POLÍTICOS** (10 issues)
- Análise Germany 47% failure rate (CRÍTICO)
- Timeline realista processo legislativo (CRÍTICO)
- Estratégia media (ALTA)
- EU Pillar 2 blocking (CRÍTICO)

⚙️ **TÉCNICOS** (7 issues)
- Laboratory ISO 17025 infrastructure
- IT infrastructure base dados nacional
- Seed certification system

**Modelo de contribuição:**
✅ Técnicos: Pull Requests GitHub (Git/Markdown)
✅ Não-técnicos: Issues template (apenas texto, sem código)
✅ Creditação transparente em todos os commits
✅ Review colaborativa antes de publicação

**Documentação completa:**
📂 github.com/bcamarneiro/cannabis-legalization
📧 bruno@camarneiro.com

Contribuir para uma política de drogas baseada em evidência científica e direitos humanos. 🌿

#PolicyMaking #EvidenceBasedPolicy #HarmReduction #CannabisRegulation #PublicHealth
```

## Email para Organizações

```
Assunto: Colaboração Técnica - Proposta Regulação Cannabis (LIVRE)

Exmo(a). Senhor(a) [Nome],

O LIVRE está a desenvolver uma proposta de posição sobre regulação da cannabis em Portugal, com foco rigoroso em evidência científica e redução de danos.

Após análise "devil's advocate", identificámos 50+ vulnerabilidades técnicas que beneficiariam da vossa expertise especializada. Documentámos 15 issues prioritárias prontas para contribuir:

**Para [Organização Específica]:**

[Se Ordem dos Advogados:]
- LEGAL 1 (CRÍTICO): International Treaty Obligations (UN Conventions 1961/1971/1988)
- LEGAL 5 (ALTA): Regime fiscal IVA - isenção vs aplicação
- LEGAL 3 (ALTA): Workplace drug testing - Código do Trabalho

[Se Ordem dos Médicos:]
- DEVIL 8 (ALTA): Riscos cardiovasculares (Mittleman 2001: MI +75%)
- HEALTH 1 (ALTA): THC cap inconsistency (brain development até 25 anos)

[Se Associação Economistas:]
- DEVIL 1 (CRÍTICO): Modelação quantitativa market capture (gap 15-17x)
- ECON 1 (ALTA): ROI sensitivity analysis (cenários failure rate)

**Modelo de contribuição flexível:**
✅ Contribuição via GitHub Issues (não requer conhecimento técnico)
✅ Creditação transparente em todos os commits
✅ Revisão prévia antes de publicação (controlo qualidade)
✅ Documentação passo-a-passo: CONTRIBUTING.md

**Documentação completa:**
📂 github.com/bcamarneiro/cannabis-legalization
📋 Issues prioritárias: docs/GITHUB-ISSUES-READY.md

Estaríamos honrados com a vossa colaboração técnica neste documento de política pública baseada em evidência.

Disponível para reunião/videochamada para discutir em detalhe.

Cumprimentos,
Bruno Camarneiro
Equipa LIVRE - Políticas de Drogas
✉️ bruno@camarneiro.com
📱 [Telefone se aplicável]
```

---

## Organizações a Contactar

### Direito
- **Ordem dos Advogados**
  - Secção Direito Internacional
  - Secção Direito Tributário
  - Secção Direito do Trabalho
  - Secção Direito Europeu

### Medicina/Saúde
- **Ordem dos Médicos**
  - Colégio Psiquiatria
  - Colégio Cardiologia
  - Colégio Saúde Pública
- **Associação Portuguesa de Psiquiatria**
- **Sociedade Portuguesa de Cardiologia**

### Economia
- **Ordem dos Economistas**
- **Associação Portuguesa de Economistas**
- **ISEG, FEP, Nova SBE** (departamentos académicos)

### Advocacy/Policy
- **SICAD** (contactos informais, não oficial)
- **Transform Drug Policy Foundation** (UK, expertise internacional)
- **ENCOD** (European NGO Council on Drugs)
- **Rede Portuguesa de Redução de Riscos**

### Académico
- **CIES-ISCTE** (Centro Investigação Estudos Sociologia)
- **CES Coimbra** (Centro de Estudos Sociais)
- **Criminólogos** (ISCSP, UMinho)

---

**Última atualização:** 2026-01-27
**Versão:** 1.0
**Contacto:** bruno@camarneiro.com

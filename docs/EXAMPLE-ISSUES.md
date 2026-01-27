# Issues de Exemplo para Recrutamento

Este ficheiro contém templates de issues prontas a criar no GitHub para recrutar voluntários específicos.

## Como Usar

1. Vai a [github.com/bcamarneiro/cannabis-legalization/issues/new](https://github.com/bcamarneiro/cannabis-legalization/issues/new)
2. Clica "Get started" no template apropriado
3. Cola o conteúdo abaixo (adaptado)
4. Adiciona labels: `help-wanted`, `priority-high`, `area-X`

---

## 🔴 TIER 1 - Prioridade Máxima

### Issue: DEVIL 1 - The 2.6% Problem

**Template**: Fix Vulnerability (Técnico)

```markdown
**ID:** DEVIL 1
**Tier/Categoria:** TIER 1 - Devastating Attack
**Prioridade:** Crítica

## Problema

Documento afirma que clubes vão servir 40-50% do mercado (282k-353k users), mas cálculo actual mostra apenas 46 clubes × 400 membros = 18.400 users (2,6% de 706.000 total).

**Gap explicativo 15-17x sem modelo quantitativo.**

**Attack esperado:** "Vocês afirmam clubes vão servir 282k-353k users mas os vossos próprios dados mostram 18.400. Como explicam isto?"

## Objectivo

Adicionar modelo quantitativo claro que explica:
- % users que vão fazer autocultivo (estimativa: 20-30%)
- Overlap clubes + autocultivo
- Substitution rate do mercado negro
- Expansão gradual número de clubes (46 inicial → 150-200 em 5 anos?)

## Tarefas

- [ ] Pesquisar dados internacionais (Colorado, Canadá) sobre split clube/autocultivo
- [ ] Criar modelo Excel/Python com assumptions explícitas
- [ ] Escrever secção no documento explicando modelo
- [ ] Adicionar gráficos/tabelas ilustrativas
- [ ] Testar compilação PDF

## Expertise Recomendada

- Análise quantitativa / Modelação de dados
- Economia / Análise de mercados
- Excel/Python para projecções

## Esforço Estimado

4-6 horas (pesquisa + modelação + escrita)

## Recursos

- Colorado market data: [URL]
- Canadian cannabis statistics: [URL]
- Uruguay club membership data: [URL]
```

**Labels**: `help-wanted`, `priority-critical`, `area-economics`, `tier-1`

---

### Issue: DEVIL 2 - Germany's 47% Operational Failure Rate

**Template**: Fix Vulnerability (Técnico)

```markdown
**ID:** DEVIL 2
**Tier/Categoria:** TIER 1 - Devastating Attack
**Prioridade:** Crítica

## Problema

Documento cita Alemanha como "modelo comprovado", mas realidade:
- 357 clubes aprovados (Nov 2025)
- Apenas 190 operacionais (53%)
- **47% taxa de falha operacional**

Modelo português espelha CSCs alemães exactamente.

**Attack esperado:** "Se o modelo alemão tem 47% failure rate após 9 meses, porque é que Portugal vai ter sucesso?"

## Objectivo

Duas opções:

**A) Acknowledge challenges + adjust expectativas:**
- Explicar porque alguns clubes falharam (capital insuficiente, gestão, local)
- Ajustar expectativas portuguesas: 30-50% podem falhar também
- Mostrar que mesmo com 50% falha, ainda capturamos 20-25% mercado

**B) Explicar diferenças Portugal vs Alemanha:**
- Portugal propõe subsídio estatal €50-100k (Alemanha não teve)
- SICAD oversight mais forte que Alemanha
- Clima português favorece outdoor (custos menores)

## Tarefas

- [ ] Pesquisar causas falha clubes alemães (artigos, relatórios)
- [ ] Decidir entre opção A ou B (ou híbrido)
- [ ] Escrever secção no documento
- [ ] Adicionar referências alemãs atualizadas
- [ ] Ajustar secção "Modelos Internacionais - Alemanha"

## Expertise Recomendada

- Análise política internacional
- Alemão (idioma) para ler relatórios originais
- Experiência em policy analysis

## Esforço Estimado

3-5 horas

## Recursos

- Bundesgesundheitsministerium relatórios: [URL]
- Cannabis clubs Germany statistics: [URL]
```

**Labels**: `help-wanted`, `priority-critical`, `area-international-policy`, `tier-1`

---

## ⚖️ LEGAL - Para Advogados

### Issue: LEGAL 1 - International Treaty Obligations

**Template**: Fix Vulnerability (Técnico)

```markdown
**ID:** LEGAL 1
**Tier/Categoria:** LEGAL - Critical Gap
**Prioridade:** Crítica

## Problema

Portugal é signatário de 3 convenções ONU sobre drogas:
- 1961 Single Convention on Narcotic Drugs
- 1971 Psychotropic Substances Convention
- 1988 Trafficking Convention

**Cannabis recreativa viola Article 4** (limit to medical/scientific use).

Documento tem ZERO discussão sobre:
- Treaty denunciation?
- Reinterpretation (Uruguay model)?
- Diplomatic consequences?

**Attack esperado:** "Portugal vai violar tratados ONU assinados. Quais são as consequências internacionais?"

## Objectivo

Adicionar secção robusta sobre estratégia tratados internacionais:

1. **Precedente Uruguai:**
   - Como interpretaram Article 4 (saúde pública justifica)
   - Reacção internacional (críticas mas zero enforcement)

2. **Precedente Canadá:**
   - Violou 3 tratados em 2018
   - Trudeau revelou 2024: "ONU nunca discutiu o tema"

3. **Opções Portugal:**
   - Reinterpretation (saúde pública)
   - Denunciation + re-ratification com reserva
   - Challenge coordenado UE-level

## Tarefas

- [ ] Pesquisar Article 4 da Convenção 1961 (texto original)
- [ ] Analisar caso Uruguai (Lei 19.172/2013)
- [ ] Analisar caso Canadá (Cannabis Act 2018)
- [ ] Consultar jurisprudência internacional
- [ ] Escrever secção no documento (3-4 páginas)
- [ ] Adicionar referências jurídicas apropriadas

## Expertise Recomendada

**ESSENCIAL**: Advogado com experiência em Direito Internacional

## Esforço Estimado

1-2 dias (pesquisa jurídica + escrita)

## Recursos

- UN Single Convention 1961: [URL]
- Uruguay legal analysis: [URL]
- Canada treaty position: [URL]
```

**Labels**: `help-wanted`, `priority-critical`, `area-law`, `international-law`

---

### Issue: LEGAL 5 - IVA Problem (Taxation Inconsistency)

**Template**: Fix Vulnerability (Técnico)

```markdown
**ID:** LEGAL 5
**Tier/Categoria:** LEGAL - Structural Gap
**Prioridade:** Alta

## Problema

Documento afirma "cost-recovery only, ZERO receitas fiscais", mas:
- **Portugal tem IVA 23% obrigatório** sobre bens/serviços
- Clubes são associações mas fornecem produto

**Contradiction:**
- Se clubes pagam IVA → há tax revenue (contradiz modelo)
- Se clubes exempt IVA → precisa legislative exemption (complica approval)

**Attack esperado:** "Vocês dizem zero impostos mas IVA 23% é obrigatório. Qual é a verdade?"

## Objectivo

Clarificar regime fiscal clubes:

**Opção A - Isenção IVA:**
- Clubes como IPSS (isentas IVA)
- Requer alteração legislativa específica
- Precedente: associações culturais/desportivas

**Opção B - IVA aplicável mas revenue minor:**
- Clubes pagam IVA 23%
- Revenue ~€2-3M/ano (46 clubes × €280k revenue × 23%)
- Claim "ZERO impostos directos" não "ZERO receitas fiscais"

## Tarefas

- [ ] Consultar Código IVA (isenções IPSS)
- [ ] Pesquisar regime fiscal associações sem fins lucrativos
- [ ] Calcular impact IVA 23% em pricing clubes
- [ ] Decidir opção A ou B
- [ ] Escrever secção "Regime Fiscal" no documento

## Expertise Recomendada

**ESSENCIAL**: Advogado tributarista ou Contabilista Certificado

## Esforço Estimado

4-6 horas

## Recursos

- Código IVA Portugal: [URL]
- Regime IPSS: [URL]
- Precedentes isenção IVA: [URL]
```

**Labels**: `help-wanted`, `priority-high`, `area-law`, `tax-law`

---

## 💊 HEALTH - Para Profissionais de Saúde

### Issue: DEVIL 8 - Health Risks Vulnerabilities

**Template**: Fix Vulnerability (Técnico)

```markdown
**ID:** DEVIL 8
**Tier/Categoria:** TIER 3 - Exploitable Gap
**Prioridade:** Alta

## Problema

Documento underplays riscos cardiovasculares e psiquiátricos:

**Missing:**
- Myocardial infarction +1.75x (Mittleman 2001) - NÃO MENCIONADO
- Psychosis +4.8x young heavy users (Di Forti 2019) - presente mas underplayed

**Attack esperado:** "Vocês escondem que cannabis aumenta ataques cardíacos 75% e psicose quase 5x."

## Objectivo

Secção "Riscos para Saúde" mais honesta e completa:

1. **Riscos Cardiovasculares:**
   - MI +75% 1h pós-consumo (Mittleman 2001)
   - Mitigação: Screening cardíaco Oficial Prevenção, excluir >65 anos ou história cardíaca

2. **Riscos Psiquiátricos:**
   - Psychosis +4.8x heavy users <25 anos (Di Forti 2019)
   - Mitigação: THC cap 10% para 18-21 anos, screening PHQ-9/GAD-7

3. **Apresentação:**
   - Upfront, primeira secção "Saúde"
   - Comparação com álcool (MI +1.5x, psychosis similar)
   - Ênfase em mitigações (controlo qualidade, screening, idade)

## Tarefas

- [ ] Ler estudos Mittleman 2001, Di Forti 2019 (full text)
- [ ] Pesquisar outros riscos major (respiratory, cognitive)
- [ ] Escrever secção "Riscos Cardiovasculares e Psiquiátricos"
- [ ] Adicionar referências médicas
- [ ] Integrar com secção "Mitigações" (Oficial Prevenção)

## Expertise Recomendada

**ESSENCIAL**: Médico (Cardiologia, Psiquiatria, Saúde Pública)

## Esforço Estimado

3-4 horas

## Recursos

- Mittleman (2001): Triggering of myocardial infarction by marijuana
- Di Forti (2019): Daily use, high-potency cannabis and psychosis
```

**Labels**: `help-wanted`, `priority-high`, `area-health`, `medical-review`

---

## 📊 ECON - Para Economistas

### Issue: ECON 1 - ROI Sensitivity Analysis Missing

**Template**: Fix Vulnerability (Técnico)

```markdown
**ID:** ECON 1
**Tier/Categoria:** ECON - Financial Vulnerability
**Prioridade:** Alta

## Problema

Documento claims ROI 120-753%, mas:
- Baseado em assumption **100% clubes succeed operationally**
- Alemanha mostra **47% failure rate**
- **Zero sensitivity analysis**

**Attack esperado:** "Se 30-50% clubes portugueses falharem como na Alemanha, o ROI colapsa. Onde está a análise de cenários?"

## Objectivo

Adicionar análise de sensibilidade robusta:

**Cenários:**

1. **Optimista (baseline actual):**
   - 90% clubes succeed
   - 45% market capture
   - ROI: 500-750%

2. **Realista:**
   - 70% clubes succeed
   - 30% market capture
   - ROI: 200-400%

3. **Pessimista:**
   - 50% clubes succeed (Germany-level)
   - 20% market capture
   - ROI: 50-150%

4. **Worst case:**
   - 30% clubes succeed
   - 10% market capture
   - ROI: -50% a +50% (breakeven)

## Tarefas

- [ ] Criar modelo Excel/Python com variáveis
- [ ] Calcular ROI para 4 cenários
- [ ] Gráficos ilustrativos (tornado chart, scenario analysis)
- [ ] Escrever secção "Análise de Sensibilidade ROI"
- [ ] Integrar no documento (Anexo ou secção Propostas)

## Expertise Recomendada

- Economista / Analista Financeiro
- Excel avançado / Python (pandas)
- Experiência em sensitivity analysis

## Esforço Estimado

6-8 horas (modelação + escrita)

## Recursos

- Documento atual modelo económico: Anexo A
- Germany club failure data: [URL]
```

**Labels**: `help-wanted`, `priority-high`, `area-economics`, `financial-modeling`

---

## 📣 Como Divulgar Issues

### Twitter/X

```
🚨 Procuram-se especialistas para melhorar proposta cannabis @LivrePartido

Advogados (Direito Internacional/Tributário)
Médicos (Cardiologia/Psiquiatria)
Economistas (Análise ROI)

Contribuir: github.com/bcamarneiro/cannabis-legalization
Contacto: bruno.camarneiro@livre.pt

#PolíticasDeDrogas #HarmReduction
```

### LinkedIn

```
O LIVRE está a desenvolver uma proposta de regulação da cannabis baseada em evidência científica e direitos humanos.

Precisamos de expertise especializada:

⚖️ ADVOGADOS: Tratados internacionais ONU, regime fiscal, direito UE
💊 MÉDICOS: Revisão riscos cardiovasculares e psiquiátricos
📊 ECONOMISTAS: Análise de sensibilidade ROI, modelação financeira

Modelo de contribuição híbrido:
- Técnicos: Pull Requests no GitHub
- Não-técnicos: Submissão via Issues (explicado passo-a-passo)

Interessados: bruno.camarneiro@livre.pt ou github.com/bcamarneiro/cannabis-legalization

#PolicyMaking #EvidenceBasedPolicy #HarmReduction
```

### Email para Organizações

```
Assunto: Colaboração - Proposta Regulação Cannabis (LIVRE)

Caro/a [Nome Organização],

O LIVRE está a desenvolver uma proposta de posição sobre regulação da cannabis em Portugal, com foco em evidência científica e redução de danos.

Identificámos várias vulnerabilidades no documento actual que beneficiariam da vossa expertise:
- [Listar 2-3 issues relevantes para a organização]

Modelo de contribuição:
- Flexível (contribuição via GitHub Issues para não-técnicos)
- Creditação transparente em todos os commits
- Revisão prévia antes de publicação

Documentação: github.com/bcamarneiro/cannabis-legalization
Contacto: bruno.camarneiro@livre.pt

Cumprimentos,
Bruno Camarneiro
```

**Organizações a contactar:**
- Ordem dos Advogados (secções Direito Internacional, Tributário)
- Ordem dos Médicos (colégio Psiquiatria, Cardiologia, Saúde Pública)
- Associações de Economistas
- SICAD (informal, contactos pessoais)
- Transform Drug Policy Foundation
- ENCOD (European NGO Council on Drugs)

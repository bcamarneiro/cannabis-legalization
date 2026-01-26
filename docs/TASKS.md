# Tarefas Pendentes - Documento Cannabis

Este ficheiro rastreia melhorias identificadas para o documento de posição.

## 🔴 URGENTE

### Red-Team Vulnerabilities (CRÍTICO - Análise Adversarial 2026-01-25)

**Fonte:** Análise multi-dimensional por especialistas ambientais, médicos, psiquiatras, psicólogos, e oposição política

- [x] **CRÍTICO 1: Impacto cognitivo em jovens** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Adicionada secção "Proteção do Desenvolvimento Cognitivo em Jovens Adultos" em FUNDAMENTAÇÃO
  - **Conteúdo implementado:**
    - Cita Meier 2012 (declínio 8pt QI utilizadores persistentes adolescentes)
    - Cita Jackson 2016 (nuance: efeito concentrado em persistentes/dependentes, não casuais)
    - Mantém modelo alemão **10% THC para 18-20 anos** (não reduz para 5%)
    - Compara favoravelmente com Suíça (permite até 20% THC aos 18+)
    - Justifica medida como precaução razoável baseada em evidência
  - **Referências adicionadas:** Meier 2012 PNAS, Jackson 2016 PNAS
  - **Decisão estratégica:** 10% alemão mais conservador que Suíça, equilibrado vs. proibicionista
  - Commit: [76b680e](../../commit/76b680e)

- [x] **CRÍTICO 2: Rastreio psiquiátrico e Oficial de Prevenção** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Adicionada subsecção "Oficial de Prevenção e Monitorização de Saúde Mental" em Propostas > Clubes Sociais
  - **Conteúdo implementado:**
    - **Modelo alemão como base:** Präventionsbeauftragter com educação admissão, monitorização contínua, referenciação SNS
    - **Qualificações:** Psicologia/serviço social/enfermagem + formação adição 40h
    - **Rácio:** 1 oficial por 200-300 membros, salário €28-35k/ano
    - **Sessões educação:** Trimestral sobre consumo consciente e redução de danos
    - **Modelo suíço mencionado:** Screening formal PHQ-9/GAD-7/ERIraos como alternativa mais rigorosa (se necessário)
    - **Contra-exemplo:** Canadá sem screening = aumento consultas psicose (Wootten 2023)
  - **Referências adicionadas:** Springer 2024 Züri Can, Wootten 2023 Ontario
  - **Decisão estratégica:** Modelo alemão (educação + monitorização) vs suíço (screening formal). Alemão equilibra proteção com praticabilidade
  - Commit: [d49f2ad](../../commit/d49f2ad)

- [x] **CRÍTICO 3: Sistemas de monitorização completamente vagos** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Adicionada subsecção "Sistema de Monitorização e Transparência Financeira" em Propostas > Clubes Sociais
  - **Conteúdo implementado:**
    - **Tracking de distribuições:** Registo individual obrigatório (modelo alemão), rastreabilidade "da semente à distribuição"
    - **Privacidade:** Dados apenas acessíveis a autoridades em fiscalização, não públicos
    - **Transparência financeira:** Relatório anual + Assembleia Geral + auditoria externa independente (>300 membros)
    - **Fiscalizações estatais:** Inspeções aleatórias sem aviso, análises laboratoriais THC/contaminantes
    - **Consequências graduais:** Advertência → suspensão licença → revogação (conforme gravidade)
    - **Penalizações específicas:** Sem Oficial Prevenção = suspensão + coima €500-2k; falta transparência = revogação imediata
  - **Referências adicionadas:** CanG 2024 (lei alemã), JustBob 2024 (rastreabilidade), Cannabis Business Plans 2024 (transparência CSCs), 420+ Software 2024 (fiscalização)
  - **Decisão estratégica:** Tracking individual necessário (limites legais) mas dados privados salvo fiscalização. Modelo alemão demonstra funcionalidade sem criar mercado paralelo

- [x] **CRÍTICO 4: Sistema "sementes certificadas" indefinido** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Adicionada subsecção "Sistema de Sementes Certificadas" em Propostas > Autocultivo
  - **Conteúdo implementado:**
    - **Modelo híbrido Alemanha + Suíça:** Clubes distribuem 7 sementes/mês (modelo alemão), produtores licenciados por Infarmed/DGAV (rigor suíço)
    - **Licenciamento produtores:** Testes obrigatórios (pesticidas, metais, micotoxinas, microorganismos), cultivo orgânico, auditoria anual
    - **Rastreabilidade seed-to-sale:** Cada lote com código rastreável (variedade, THC esperado, origem)
    - **Variedades autorizadas:** THC máximo 10% apenas para 18-20 anos. Maiores de 21 sem restrição THC. Catálogo aprovado, rotulagem obrigatória
    - **Enforcement:** Clubes documentam origem sementes, autocultivo independente proibido (mas enforcement reactivo), coimas €5k-50k produtores ilegais
    - **Reconhecimento:** Impossível eliminar 100% sementes ilegais, mas redução risco significativa vs. mercado negro
  - **Referências adicionadas:** Bundesgesundheit 2024 FAQ (7 sementes/mês alemão), BAG Switzerland 2024 (pilots seed-to-sale), Eurofins 2024 (testes obrigatórios)
  - **Decisão estratégica:** Alemanha distribui via clubes sem certificação formal (pragmático). Suíça exige licenciamento produtores + testes + orgânico (rigoroso). Portugal combina praticabilidade alemã com controlo qualidade suíço
  - Commit: [f11342b](../../commit/f11342b)

- [ ] **CRÍTICO 5: Gravidez/Amamentação - NÃO MENCIONADO** 🚨
  - **Problema:** Zero avisos sobre THC em gravidez/aleitamento (danos desenvolvimento fetal)
  - **Ataque esperado:** "Ignoram completamente saúde materno-infantil"
  - **Acção:** Adicionar secção de proteção materno-infantil
  - **Conteúdo necessário:**
    - Rótulos obrigatórios: "Cannabis na gravidez pode causar danos ao feto"
    - Screening: grávidas encorajadas a parar uso, referência para tratamento
    - Amamentação: avisos que THC passa para leite materno
    - Guidance de associações de obstetrícia
  - **Validar:** Dados sobre THC e desenvolvimento fetal (ACOG, RCOG guidelines)

### Incoerências de dados (bloqueante para credibilidade)
- [x] **Dados alemães inconsistentes** ✅ RESOLVIDO (2026-01-24)
  - Anexo A atualizado para Nov 2025: 791 candidaturas, 357 aprovados
  - Fonte validada: BCAv, ICBC, High Times

- [x] **Números do mercado negro contraditórios** ✅ RESOLVIDO (2026-01-24)
  - Removida estimativa €100M de 2017 (não validável)
  - Mantida apenas estimativa 2024: 36-58 toneladas, receitas fiscais potenciais €52-151M
  - Fonte validada: ResearchGate 2024 "Cannabis for Recreational Use by Adults in Portugal"

- [x] **Número de prescrições inconsistente** ✅ RESOLVIDO (2026-01-24)
  - Padronizado para 1.157 prescrições em todo o documento

## 🟡 ARGUMENTAÇÃO (alta prioridade)

### Red-Team Vulnerabilities (ALTA PRIORIDADE)

- [ ] **ALTA 1: Comparação ambiental CO₂ intelectualmente desonesta** ⚠️
  - **Problema:** Compara produção cannabis (2.300-5.200 kg CO₂/kg) com lifecycle completo carne (99 kg)
  - **Ataque esperado:** "Não é apples-to-apples. Lifecycle carne é 27 kg CO₂, não 99 kg"
  - **Acção:** Corrigir comparação com honestidade intelectual
  - **Fix:**
    - Comparar com tomates greenhouse (0,2-0,5 kg CO₂/kg) - mais apropriado
    - Adicionar: "Estas emissões assumem grid energético actual. Com 50% renováveis, redução de 50-70%"
    - Propor requisito vinculativo: "Cultivadores licenciados: 50% renováveis até 2030, 100% até 2035"
  - **Validar:** Lifecycle analysis cannabis com renewables (estudos 2022-2024)

- [ ] **ALTA 2: Risco psicose vs. acesso 18-20 anos - CONTRADITÓRIO** ⚠️
  - **Problema:** Documento cita OR 4-5 psicose para 18-20 anos, depois permite-lhes acesso a clubes
  - **Ataque esperado:** "Citam risco psicose depois deixam jovens de 18 usar. Qual é?"
  - **Acção:** Resolver contradição
  - **Opções:**
    - A) Idade mínima absoluta 21 anos (sem excepções)
    - B) 18-20 requer autorização psiquiátrica + monitorização mensal
    - C) 18-20 apenas THC <5% (não 10%)
  - **Validar:** Políticas idade mínima em jurisdições que legalizaram (Finlândia propôs 25 anos)

- [ ] **ALTA 3: Projeções económicas sobrestimadas** ⚠️
  - **Problema:** €174M savings extrapolados da Alemanha sem análise específica PT
  - **Ataque esperado:** "Custos alemães incluem prisões/tribunais. PT talvez €20M, não €174M"
  - **Acção:** Análise custo-benefício específica de Portugal
  - **Conteúdo necessário:**
    - Custos actuais processos cannabis 2021-2024 (Ministério Justiça, PSP, GNR)
    - Estimativa conservadora: €40-50M/ano (não €174M)
    - Reconhecer: custos regulatórios compensam parte das poupanças
    - Poupança líquida realista: ~€30-40M/ano para prevenção
  - **Validar:** Dados orçamentais específicos PT (enforcement cannabis vs. outras drogas)

- [ ] **ALTA 4: Colorado youth decline (42%) - CONFUNDIDO** ⚠️
  - **Problema:** Atribuído a legalização, mas Canadá (legal 2018) teve consumo juvenil estável
  - **Ataque esperado:** "Se legalização reduz consumo, porque Canadá não viu declínios?"
  - **Acção:** Reconhecer confounds, claim mais modesto
  - **Fix:**
    - "Colorado mostra declínio 2011-2023, mas causalidade não provada (outros factores: regulação vaping 2018, programas prevenção)"
    - "Canadá: consumo estável pós-legalização. Declínio Colorado não universal"
    - "Legalização + regulação forte + prevenção pode reduzir consumo juvenil. Não garantido por legalização sozinha"
  - **Validar:** Meta-análise 2023-2024 sobre consumo juvenil em jurisdições legalizadas

- [ ] **ALTA 5: Claims terapêuticos para sono baseados em 6 trials** ⚠️
  - **Problema:** Meta-análise apenas 6 ensaios, sem menção risco dependência
  - **Ataque esperado:** "Melatonina tem 50+ RCTs. CBT-I é primeira linha. Cannabis não comprovada"
  - **Acção:** Reframe honesto sobre evidência sono
  - **Fix:**
    - "Evidência emergente para THC/CBN em insónia, mas requer mais investigação"
    - "Eficácia comparável a melatonina low-dose, mas mais efeitos secundários"
    - "Recomendado apenas segunda linha após CBT-I falhar"
    - "Risco Cannabis Use Disorder em uso crónico para sono: 15-25%"
  - **Validar:** Guidelines internacionais sono (AASM, ESRS) sobre cannabis

- [ ] **ALTA 6: "Sem incentivo comercial" depende de enforcement inexistente** ⚠️
  - **Problema:** Clubes "sem fins lucrativos" mas sem auditorias, caps de preço, transparência
  - **Ataque esperado:** "Espanha tentou clubes non-profit. Tornaram-se criminosos. Porque PT será diferente?"
  - **Acção:** Definir governance rigorosa
  - **Conteúdo necessário:**
    - Auditoria financeira anual independente (resultados públicos)
    - Price cap: máximo €6/grama (média alemã)
    - Transparência: divulgação mensal custos/vendas/pagamentos membros
    - Surplus proibido: excedentes doados automaticamente a SICAD (não retidos)
    - Whistleblower program: membros reportam suspeitas, recompensas
    - Inspecções surpresa: 10% clubes auditados trimestralmente
  - **Validar:** Problemas Espanha com clubes (Barcelona, Madrid) - casos documentados

- [ ] **ALTA 7: Oposição indústria cannabis não endereçada** ⚠️
  - **Problema:** 37 empresas licenciadas querem mercado doméstico - clubes são competição directa
  - **Ataque esperado:** "Propõem cortar mercado doméstico de empresas que exportam 32.500 kg. Irracional"
  - **Acção:** Plano transição para indústria
  - **Conteúdo necessário:**
    - Produtores licenciados podem fornecer clubes (wholesale, preço custo + 20%)
    - Produtores podem operar 1-2 clubes cada (requisito non-profit mantém-se)
    - Reconhecer: alguma perda empregos enforcement, offset por administração clubes
  - **Validar:** Modelo económico produtores → clubes (margens, custos)

### Red-Team Vulnerabilities (MÉDIA PRIORIDADE)

- [ ] **MÉDIA 1: Taxa dependência ambígua (9% vs 15-25%)** ℹ️
  - **Problema:** Documento cita 9% Cannabis Use Disorder geral, depois 15-25% para uso crónico sono
  - **Ataque esperado:** "Qual é a taxa verdadeira? 9% ou 25%? Dados contraditórios"
  - **Acção:** Clarificar contextos
  - **Fix:**
    - 9% é lifetime CUD para todos os utilizadores
    - 15-25% é taxa para uso terapêutico crónico (superior porque diário)
    - Adicionar: "Risco dependência aumenta com frequência uso: ocasional 5%, diário 20-30%"
  - **Validar:** Meta-análises sobre CUD por padrão uso (occasional vs daily)

- [ ] **MÉDIA 2: Dados potência desactualizados (Freeman 2019)** ℹ️
  - **Problema:** Cita estudo 2019 quando potência continua a aumentar
  - **Ataque esperado:** "Usam dados de 5 anos atrás. THC agora é 20-30%, não 17%"
  - **Acção:** Actualizar com dados 2023-2024
  - **Validar:** EMCDDA 2024 report sobre potência THC na Europa

- [ ] **MÉDIA 3: Claims sequestração carbono cânhamo potencialmente exagerados** ℹ️
  - **Problema:** 8-22 toneladas CO₂/hectare - range enorme, pode ser optimista
  - **Ataque esperado:** "Sequestração depende de solo, clima, variedade. Números irrealistas para PT"
  - **Acção:** Adicionar contexto
  - **Fix:**
    - "Estudos mostram 8-22 t CO₂/ha em condições óptimas (UK, solos férteis)"
    - "Portugal: clima mediterrânico pode reduzir para 5-10 t CO₂/ha"
    - "Mesmo metade da sequestração UK, offset significativo vs. indoor"
  - **Validar:** Estudos cânhamo em clima mediterrânico (Espanha, Itália)

- [ ] **MÉDIA 4: Timeline implementação irrealista** ℹ️
  - **Problema:** Propõe Q3-Q4 2026 quando Alemanha demorou anos
  - **Ataque esperado:** "Alemanha levou 3 anos. Portugal em 6 meses? Impossível"
  - **Acção:** Timeline faseado mais realista
  - **Proposta:**
    - Q3 2026: Proposta legislativa apresentada
    - Q1 2027: Aprovação Lei-Quadro Experimental (se consenso)
    - Q3 2027: Primeiro programa piloto (2-3 clubes Lisboa/Porto)
    - 2028-2030: Avaliação piloto, expansão gradual
  - **Validar:** Processos legislativos comparáveis em PT (descriminalização 2001, quanto tempo?)

- [ ] **MÉDIA 5: "95% mercado ilegal continua" - lógica circular** ℹ️
  - **Problema:** Diz 95% mercado negro Portugal → propõe clubes → assume continuará ilegal
  - **Ataque esperado:** "Se clubes são eficazes, mercado ilegal deveria reduzir. Qual é?"
  - **Acção:** Projeção mais realista
  - **Fix:**
    - "Actualmente: 95% mercado ilegal"
    - "Com clubes + autocultivo: redução esperada para 60-70% em 5 anos (modelo Uruguai)"
    - "Legalização total comercial (Colorado): 25-30% mercado ilegal persiste"
  - **Validar:** Dados mercado negro pós-legalização (Uruguai, Colorado, Canadá)

- [ ] **MÉDIA 6: Descriminalização vs. consumo - correlação não causalidade** ℹ️
  - **Problema:** Implica descriminalização 2001 não aumentou consumo, mas outros factores podem explicar
  - **Ataque esperado:** "Consumo estável pode ser moda, prevenção, economia - não prova descriminalização funciona"
  - **Acção:** Linguagem mais cautelosa
  - **Fix:**
    - "Portugal descriminalizou 2001. Consumo não aumentou significativamente"
    - "Impossível provar causalidade (factores confundidos), mas dados sugerem descriminalização não causou epidemia"
    - "Modelo português reconhecido internacionalmente, mas efeito específico da descriminalização vs. investimento prevenção é debatido"
  - **Validar:** Literatura académica sobre causalidade descriminalização PT (análise crítica)

- [ ] **MÉDIA 7: €52M financiamento clubes depende de execução perfeita** ℹ️
  - **Problema:** Propõe realocar 30% poupanças enforcement (€52M) mas enforcement pode não terminar
  - **Ataque esperado:** "Clubes podem funcionar mal. Enforcement continua. Orçamento fantasma"
  - **Acção:** Plano financiamento conservador
  - **Fix:**
    - "Financiamento inicial: €10M (OE, não poupanças)"
    - "Anos 2-5: transição gradual para poupanças enforcement conforme clubes provam eficácia"
    - "Se clubes falharem, enforcement mantém-se + financiamento cortado"
  - **Validar:** Modelos financiamento saúde pública PT (programas experimentais)

- [ ] **MÉDIA 8: Comparação álcool arriscada politicamente** ℹ️
  - **Problema:** Documento usa álcool como comparador 3+ vezes
  - **Ataque esperado:** "Se cannabis é como álcool, vamos restringir álcool também? Querem proibição?"
  - **Acção:** Reduzir uso comparação álcool
  - **Fix:**
    - Manter APENAS na secção científica (Lancet harm index)
    - Remover de argumentação política/estratégia
    - Substituir por: "Modelo regulatório baseado em saúde pública, não proibição"
  - **Validar:** N/A (decisão estratégica)

- [ ] **MÉDIA 9: "Modelo alemão" usado circularmente** ℹ️
  - **Problema:** Justifica clubes citando Alemanha, mas Alemanha ainda não tem resultados (2024)
  - **Ataque esperado:** "Alemanha aprovou há 6 meses. Zero dados eficácia. Como é modelo comprovado?"
  - **Acção:** Separar aspiração vs. evidência
  - **Fix:**
    - "Alemanha aprovou clubes 2024 (Cannabis Act) mas implementação em curso"
    - "Modelo baseado em evidência: Uruguai (2013), Canadá (2018) - mais de 5 anos dados"
    - "Alemanha citada como modelo legislativo (framework legal), não eficácia comprovada"
  - **Validar:** Resultados Uruguai/Canadá (redução mercado negro, consumo juvenil, etc.)

- [ ] **MÉDIA 10: Enforcement autocultivo "limite 3 plantas" indefinido** ℹ️
  - **Problema:** Como polícia fiscaliza 3 plantas? Inspecções domiciliares? Denuncia vizinhos?
  - **Ataque esperado:** "3 plantas é impraticável fiscalizar sem vigilância orwelliana"
  - **Acção:** Reconhecer limite imperfect
  - **Fix:**
    - "Limite 3 plantas não implica fiscalização porta-a-porta"
    - "Enforcement reactivo: queixas vizinhos, investigações existentes descobrem excesso"
    - "Penalidade: excesso = apreensão plantas, multa administrativa (não criminal)"
    - "Modelo: vinho caseiro (limite 4.000L não fiscalizado proactivamente)"
  - **Validar:** Como Alemanha/Malta fiscalizam autocultivo (modelo reactivo vs. proactivo)

- [ ] **MÉDIA 11: Oficial de Prevenção - role vago** ℹ️
  - **Problema:** Mencionado 3+ vezes mas sem definir exactamente o que faz dia-a-dia
  - **Ataque esperado:** "€35k/ano para fazer o quê? Conversar com membros? Custo injustificado"
  - **Acção:** Job description completo
  - **Conteúdo necessário:**
    - Responsabilidades: screening admissão, sessões educação mensal, monitorização high-risk users
    - Qualificações: psicologia ou serviço social licenciado, formação adicional em addiction
    - Rácio: 1 oficial por 200-300 membros
    - Accountability: relatórios trimestrais a SICAD, auditoria anual
  - **Validar:** Präventionsbeauftragter alemão - job description oficial, formação, regulação

- [ ] **MÉDIA 12: Dual diagnosis (cannabis + outras substâncias) não discutido** ℹ️
  - **Problema:** Muitos utilizadores cannabis também usam álcool, tabaco, outras drogas
  - **Ataque esperado:** "Propõem screening mas ignoram poliuso. Análise incompleta"
  - **Acção:** Adicionar secção poliuso
  - **Conteúdo:**
    - "Clubes devem screening para uso concorrente álcool/tabaco/outras drogas"
    - "Risco aumentado: cannabis + álcool → maior impairment que isolado"
    - "Oficial Prevenção refere casos dual diagnosis para serviços especializados"
  - **Validar:** Prevalência poliuso cannabis em Portugal (SICAD data)

- [ ] **MÉDIA 13: Peer influences e pressão social não abordados** ℹ️
  - **Problema:** Clubes = ambiente social pró-cannabis, pode normalizar uso excessivo
  - **Ataque esperado:** "Clubes criam echo chambers. Normalization leva a aumento consumo"
  - **Acção:** Reconhecer + mitigação
  - **Fix:**
    - "Clubes podem normalizar uso - risco reconhecido"
    - "Mitigação: Oficial Prevenção promove 'consumo consciente', não abstinência mas moderação"
    - "Regras: proibido consumo no local (take-home only, reduz ambiente social pró-uso)"
    - "Educação: limites seguros, sinais dependência, quando parar"
  - **Validar:** Pesquisa sobre social contagion em clubes Espanha (problemas documentados)

- [ ] **MÉDIA 14: Dados fiscais Canadá/Colorado podem não aplicar a PT** ℹ️
  - **Problema:** Culturas consumo diferentes, preços diferentes, impostos diferentes
  - **Ataque esperado:** "Colorado tem consumo 2x maior per capita. Receitas não transferíveis"
  - **Acção:** Ajustes conservadores
  - **Fix:**
    - "Projeções baseadas em pop-adjusted Colorado/Canadá são estimativas, não garantias"
    - "Portugal: prevalência 8,2% vs Colorado 15% → receitas proporcionalmente menores"
    - "Modelo clubes (não comercial) gera ZERO receitas fiscais directas - poupanças vêm de enforcement"
  - **Validar:** Prevalência uso cannabis PT vs Colorado vs Canadá (dados EMCDDA, NSDUH)

- [ ] **MÉDIA 15: Falta discussão sobre turismo cannabis** ℹ️
  - **Problema:** Clubes "apenas residentes" mas como enforcement? Amsterdam problema turismo
  - **Ataque esperado:** "Turistas vão procurar clubes. Lisboa torna-se Amsterdam. Querem isso?"
  - **Acção:** Política turismo explícita
  - **Fix:**
    - "Adesão clubes: residência PT comprovada (6+ meses), não turistas"
    - "Enforcement: clubes verificam NIF/Cartão Cidadão na admissão"
    - "Penalidade: clubes que admitem turistas perdem licença"
    - "Autocultivo: legal apenas para residentes fiscais PT"
  - **Validar:** Problemas turismo Amsterdam, políticas Barcelon clubes (tentaram restringir turistas)

- [ ] **MÉDIA 16: Cannabis e condução - lacuna regulatória** ℹ️
  - **Problema:** Documento não menciona driving under influence
  - **Ataque esperado:** "Legalizam mas ignoram segurança rodoviária. Irresponsável"
  - **Acção:** Adicionar secção driving
  - **Conteúdo:**
    - "THC prejudica condução - risco acidente 2x (dose-dependente)"
    - "Limite legal: <1ng/mL THC sangue (zero tolerance) ou >5ng/mL (impairment threshold)"
    - "Testes roadside: saliva tests (já usados em PT para álcool)"
    - "Penalidades: iguais a álcool (multa, pontos carta, possível criminal)"
    - "Educação: rótulos obrigatórios "Não conduzir sob influência THC - até 4h após uso"
  - **Validar:** Legislação DUI cannabis em jurisdições legalizadas (Colorado, Canadá, Alemanha)

### Reforço do autocultivo
- [ ] **Desenvolver comparação vinho caseiro vs. cannabis** [linhas 374-382](../documento.md#L374-L382)
  - Adicionar: custos de fiscalização (proibir é impraticável)
  - Adicionar: exemplos de outros países EU com autocultivo legal (Alemanha, Malta, Luxemburgo)
  - Reforçar: sementes certificadas = mais controlo que mercado negro
  - **Validar:** Confirmar limite legal vinho caseiro em PT (4.000L/ano?)

- [ ] **Nova secção: "Controlo de Qualidade"** (contra-argumentos)
  - Mercado negro: risco de pesticidas, metais pesados, fungos
  - Clubes: testes obrigatórios (modelo alemão)
  - Comparar com segurança alimentar
  - **Validar:** Requisitos de testagem na Alemanha (fontes oficiais)

### Projeções e estimativas

- [ ] **Nova secção: "Impacto Fiscal Estimado"**
  - Receitas projetadas (baseado em Canadá/Colorado ajustado à população PT)
  - Comparar com €52-151M do estudo
  - Custos de implementação (licenciamento, fiscalização)
  - ROI de 30% para prevenção/tratamento
  - **Validar:** Dados fiscais Colorado 2024, Canadá 2024, ajustar à pop. PT

- [ ] **Estimar clubes necessários em Portugal**
  - Alemanha: 357 clubes / 84M habitantes = 1 clube / 235.000 hab
  - Portugal: 10,3M → ~44 clubes necessários
  - Distribuição regional (8-10 Lisboa, 5-7 Porto, resto disperso)
  - **Validar:** População PT 2025, dados alemães Nov 2025

## 🟢 ESTRUTURA (média prioridade)

### Reorganização de conteúdo
- [ ] Mover secção cânhamo [linhas 534-549](../documento.md#L534-L549)
  - De: após propostas cannabis recreativa
  - Para: após cannabis medicinal (fica mais lógico)
  - Ou: desenvolver como pilar autónomo no início

- [ ] Integrar cânhamo no cronograma
  - Atualmente não mencionado no timeline
  - Propor programa piloto com data específica

### Financiamento dos clubes

- [ ] **Expandir modelo económico no Anexo A**
  - Estrutura de custos (instalações, energia, pessoal, oficial prevenção)
  - Como cobrem custos se sem fins lucrativos? (quotas membros)
  - Regulação de preços: quem define? SICAD/Infarmed?
  - Fiscalização: SICAD (licenciamento), Infarmed (qualidade), ASAE (instalações)
  - Problemas alemães documentados (clubes com dificuldades financeiras)
  - **Validar:** Modelo de custos real de clubes alemães operacionais

## 🔵 REFINAMENTOS (baixa prioridade)

### Tom e framing

- [ ] **Simplificar "Resposta ao Chega"** [linhas 416-421](../documento.md#L416-L421)
  - Actual: 5 linhas, muito defensivo
  - Proposta: "Respeitamos que o Chega discorde. A evidência de 25 anos de descriminalização portuguesa e dados da Alemanha (consumo juvenil -9%) mostram que políticas baseadas em saúde pública funcionam."
  - Máximo 1-2 frases, directo ao ponto

- [ ] **Rever uso repetitivo de comparação com álcool**
  - Risco: oposição responde "então vamos restringir álcool também"
  - Aparece em 3+ lugares no documento
  - **Fix:** Usar APENAS na secção "Comparação de riscos (Lancet)"
  - Remover de argumentação principal

### Dados complementares

- [ ] Timeline de implementação
  - Avaliar se 6 meses (proposta legislativa Q3-Q4 2026) é realista
  - Alemanha: processo demorou anos
  - Considerar faseamento alternativo

## ✅ CONCLUÍDAS

- [x] **Custos de enforcement da proibição** ✅ ADICIONADO (2026-01-24)
  - Secção expandida com dados alemães validados (Heinrich Heine University 2021)
  - Estimativa Portugal: ~€174M/ano poupanças (€134M enforcement + €40M judicial)
  - Proposta: 30% (~€52M/ano) para prevenção/tratamento
  - Fonte: Cannabis Now 2024, população INE/Statista
- [x] **Modelo fiscal alinhado com clubes sociais** ✅ CORRIGIDO (2026-01-24)
  - Removidas referências a receitas fiscais significativas
  - Foco mudado para: redução mercado negro + poupanças enforcement
  - Financiamento via Orçamento do Estado (não receitas fiscais dos clubes)
- [x] Anexo A: Funcionamento dos Clubes Sociais (adicionado 2026-01-24)
- [x] Anexo B: Sistema de Sementes Certificadas (adicionado 2026-01-24)
- [x] Corrigir formatação das referências (brackets duplos)
- [x] Resolver overflow de URLs na bibliografia
- [x] Ajustar espaçamento entre palavras nas referências
- [x] **Impacto ambiental e realidade económica** ✅ INTEGRADO (2026-01-25)
  - **Feedback crítico de Luísa Álvares (experiência suíça):**
  - **Catástrofe ambiental:** Cultivo indoor 2.300-5.200 kg CO₂/kg (23-52x pior que carne) [@summers2021cannabis; @mills2021cannabis]
  - **Solução sustentável:** Cânhamo captura 8-22 toneladas CO₂/hectare [@cambridge2022hemp; @britishhemp2024carbon]
  - **Realidade económica SNS:** 37% população com dor crónica [@azevedo2012chronic], custo €350/mês/paciente = €16B/ano (92% do OE Saúde 2026 [@publico2025oe2026])
  - **Conclusão:** Comparticipação universal impossível sem moeda soberana — reforça necessidade de modelo selectivo
  - Adicionada secção ambiental em "0. FUNDAMENTAÇÃO" (documento.md)
  - Actualizado Sumário Executivo Fase 2 com argumento ambiental
  - Actualizada secção custo-benefício com dados realistas de prevalência dor crónica
  - 8 novas referências validadas (Nature Sustainability, Cambridge, Azevedo 2012, OE2026)
- [x] **Reestruturação arquitetural - Priorização correta** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Guia de debate (715 linhas, 49%) aparecia antes das propostas, enterrando substância política
  - **Adicionado RESUMO PARA DECISORES** (2 páginas, linhas 5-85) - síntese executiva para CTs ocupados
  - **Movida FUNDAMENTAÇÃO** de linha 710 → linha 140 (logo após Sumário Executivo)
  - **Movidas PROPOSTAS CONCRETAS + CRONOGRAMA** de linhas 1275-1372 → linha 591 (antes de estratégias políticas)
  - **Relegado guia de debate** de "SECÇÃO II" → "ANEXO I: Guia de Argumentação"
  - **Estrutura final:** Resumo → Sumário → Fundamentação → Evidência → Propostas (40%) → Estratégias → Anexos
  - **Impacto:** CTs podem decidir em 15min vs 60min, propostas visíveis antes de táticas
  - PDF compila sem erros (267K), todas cross-references preservadas
  - Commit: [17c2c21](../../commit/17c2c21)

---

## Notas

- **Priorização:** Urgente > Alta > Média > Baixa
- **Anexos A e B são bloqueantes** - documento referencia-os explicitamente
- Outras tarefas podem ser implementadas incrementalmente
- **Feedback externo:** Integração de experiência prática suíça (Luísa Álvares) alterou fundamentação ambiental e económica

**Última atualização:** 2026-01-26

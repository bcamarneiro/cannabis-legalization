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

- [x] **CRÍTICO 5: Gravidez/Amamentação - NÃO MENCIONADO** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Adicionada subsecção "Proteção Materno-Infantil" em Propostas > Clubes Sociais (após Sistema de Monitorização)
  - **Conteúdo implementado:**
    - **Avisos obrigatórios:** Rótulos "Cannabis durante gravidez pode causar baixo peso ao nascer e danos desenvolvimento fetal" + "THC passa para leite materno. Não usar durante amamentação". Pictograma universal gravidez barrado. Tamanho mínimo 20% superfície embalagem (padrão tabaco UE)
    - **Screening universal:** Obstetras/parteiras devem perguntar sobre uso cannabis em todas consultas pré-natais/pós-parto (modelo ACOG 2025)
    - **Screening por entrevista:** Testes biológicos NÃO devem ser usados como screening primário (evitar estigma)
    - **Aconselhamento cessação:** Profissionais aconselham riscos (baixo peso, NICU, mortalidade perinatal) e recomendam cessação total
    - **Evidência transferência:** THC cruza placenta (feto ~10% concentração materna, receptores desde 5 semanas). THC leite materno persiste 6 dias-6+ semanas, sem pico claro (impossível "evitar pico")
    - **Sem penalização:** Grávidas que auto-reportem uso NÃO penalizadas legalmente (evitar sub-reporte)
    - **Redução danos:** Se cessação impossível, reduzir para menor quantidade possível (SOGC Canadá)
  - **Referências adicionadas:** ACOG 2025 Clinical Consensus No. 10, PMC 2024 German midwives study, CDC 2024 lactation guidance, WSU 2024 THC breast milk study, SOGC 2022 Canada guidelines
  - **Decisão estratégica:** ACOG 2025 (EUA) demonstra riscos dose-dependentes gravidez. Alemanha enfrenta desafio similar pós-legalização Abril 2024. Portugal implementa proteções ab initio (não reactivamente)

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

- [x] **ALTA 1: Comparação ambiental CO₂ intelectualmente desonesta** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Comparação "apples-to-apples" corrigida - cannabis indoor 2.300-5.200 kg CO₂/kg vs. tomates greenhouse 0,2-0,5 kg (não carne)
  - **Conteúdo implementado:**
    - Comparação honesta com culturas greenhouse similares (tomates, pepinos)
    - Adicionado contexto: emissões assumem grid energético actual PT (57% renováveis 2023)
    - Projeção: Com 100% renováveis, redução para 1.000-2.300 kg CO₂/kg
    - Requisito proposto: Clubes devem certificar redução progressiva pegada carbono em auditoria anual, priorizar outdoor/greenhouse vs indoor
  - **Referências validadas:** Summers 2021 Nature Sustainability, Mills 2021 PLOS ONE (indoor emissions)
  - Commit: [anterior, parte de integração ambiental 2026-01-25]

- [x] **ALTA 2: Risco psicose vs. acesso 18-20 anos - CONTRADITÓRIO** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Contradição endereçada - documento reconhece risco aumentado 18-20 anos MAS justifica acesso limitado (10% THC, clubes apenas) como harm reduction vs. mercado negro
  - **Solução escolhida:** Opção C+ (18-20 anos THC máximo 10%, apenas via clubes com Oficial de Prevenção)
  - **Justificação adicionada:**
    - Risco psicose é dose-dependente (alta potência é o problema, não cannabis per se)
    - 10% THC alemão é conservador (Suíça permite 20% aos 18+)
    - Clubes oferecem protecção que mercado negro não tem: screening, educação, monitorização, referenciação SNS
    - Proibir 18-20 completamente empurra-os para mercado negro sem protecções
  - **Dados:** Di Forti 2019 (risco 5x com alta potência), Marconi 2016 (OR 3-5 para 18-24 anos uso pesado)
  - Conteúdo em: Fundamentação, Propostas Clubes, Guia Argumentação
  - Commits: [múltiplos, integrado em CRÍTICO 1-2]

- [x] **ALTA 3: Projeções económicas sobrestimadas** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** €174M alemães não extrapolados directamente - análise PT-específica conservadora implementada
  - **Conteúdo implementado:**
    - Estimativa conservadora PT: €40-80M/ano custos enforcement (PSP/GNR €25-45M, judicial €10-20M, prisional €5-15M)
    - Reconhecimento: PT tem custos menores que Alemanha (descriminalização desde 2001)
    - Custos regulatórios: €10-15M/ano (licenciamento, fiscalização, análises laboratoriais, formação)
    - **Poupança líquida realista: €30-65M/ano**
    - Afetação proposta: 50-70% para prevenção = **€20-40M/ano** (não €52M)
    - Aviso explícito: "Valores são ESTIMATIVAS. Análise rigorosa requer dados orçamentais específicos PT"
  - Secção: Financiamento de prevenção e tratamento (linha 845+)
  - Commit: [2026-01-26, commit específico ALTA 3]

- [x] **ALTA 4: Colorado youth decline (42%) - CONFUNDIDO** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Atribuição causal corrigida - adicionada secção "Contexto crítico — tendência nacional, não apenas estados legalizados"
  - **Conteúdo implementado:**
    - Declínio Colorado 42% (2011-2023) MANTIDO mas contextualizado
    - **Monitoring the Future:** Declínio nacional EUA 38% nos 8º/10º anos, 13% no 12º ano (2013-2023) - padrão semelhante ao Colorado
    - **Confounds identificados:** Mudanças geracionais, campanhas anti-tabaco/vaping, aumento prevenção nacional, mudanças metodológicas pós-COVID
    - **Canadá contra-exemplo:** Declínio 15-17 anos (19,8%→10,4%) mas magnitude diferente sugere factores locais
    - **Interpretação honesta:** "Legalização não causou aumento que opositores previam" (claim defensável) vs. "Legalização causou declínio" (causalidade não provada)
  - **Referência adicionada:** Monitoring the Future 2023 (Univ. Michigan)
  - Secções actualizadas: Impacto consumo juvenil (linha 599+), Guia Argumentação (linha 1350+)
  - Commit: [2026-01-26, commit específico ALTA 4]

- [x] **ALTA 5: Claims terapêuticos para sono baseados em 6 trials** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Reframed como "evidência limitada e contraditória" com caveats completos sobre uso crónico
  - **Conteúdo implementado:**
    - Secção terapêutica principal: "Meta-análise de **apenas 6 ensaios clínicos** (1.077 pacientes) sugere THC/CBN podem melhorar sono a curto prazo, **CONTUDO** meta-análises 2025 de estudos observacionais mostram uso recreativo crónico associado a **PIOR qualidade do sono**"
    - Adicionado: Risco dependência 15-25% utilizadores frequentes, tolerância com uso crónico
    - Conclusão honesta: "Evidência para uso crónico é fraca; uso a curto prazo pode ajudar, mas risco dependência + tolerância não justificam recomendação generalizada"
    - Resposta curta debate: "Insónia (evidência LIMITADA)" em maiúsculas
    - Dados suporte: "6 trials sugerem melhoria a curto prazo, mas uso crónico piora sono"
  - **Referência adicionada:** Gates et al. 2025 Sleep Medicine Reviews (recreational use worsens sleep)
  - Secções: Terapêutica (linha 1086), Manual Debate (linhas 1075, 1105, 1133)
  - Commit: [de045f9, 2026-01-26]

- [x] **ALTA 6: "Sem incentivo comercial" depende de enforcement inexistente** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Governance rigorosa definida, distinguindo modelo alemão real de safeguards adicionais PT
  - **IMPORTANTE:** Após validação web, separado:
    - **Modelo alemão base:** §§24-26 KCanG (cost-recovery, documentação obrigatória, submissão anual, inspecções)
    - **Safeguards adicionais PT:** Auditorias externas anuais obrigatórias, price cap €6/g, excedentes doados automaticamente a SICAD, whistleblowing, meta 10% inspecções/trimestre
  - **Conteúdo implementado:**
    - Anexo A secção "Governance e Prevenção de Desvios Comerciais" com 6 mecanismos
    - Clubes principais: Reestruturado "Modelo base alemão" + "Safeguards adicionais PT"
    - Transparência financeira: Separada em modelo alemão (§§24-26 KCanG) vs safeguards PT
    - Fiscalizações: Modelo alemão (inspecções aleatórias) vs safeguards PT (10% trimestre, whistleblowing)
    - Q&A manual debate: "Espanha tentou clubes. Porque PT será diferente?" - resposta completa 2min
  - **Referência adicionada:** @kcang2024 (texto legal alemão §§24-26)
  - **Fontes validadas:** Web search sobre §26 KCanG (documentação), §§24-25 KCanG (cost-recovery)
  - Secções: Clubes (linha 659+), Transparência (linha 706+), Anexo A (linha 1721+), Debate (linha 1351+)
  - Commit: [07f9eaa, 2026-01-26]

- [x] **ALTA 7: Oposição indústria cannabis não endereçada** ✅ CONCLUÍDO (2026-01-26)
  - **Problema resolvido:** Nova secção "Integração da Indústria Licenciada Existente" com 3 opções de integração
  - **Conteúdo implementado:**
    - **Contexto:** 37 empresas licenciadas, 32.558 kg exportação 2024, infraestrutura estabelecida
    - **Opção 1 - Fornecimento wholesale:** Produtores fornecem cannabis a clubes (custo + margem máx 20%), padrões EU-GMP, rastreabilidade seed-to-sale, clubes escolhem auto-cultivo/fornecimento/mix
    - **Opção 2 - Operar clubes (limitado):** Máximo 1-2 clubes/produtor, requisito non-profit mantém-se, separação contabilística, price cap €6/g aplica-se, governance idêntica
    - **Opção 3 - Parcerias técnicas:** Consultoria agrícola, formação pessoal, partilha genéticas, SEM controlo operacional
    - **Impacto laboral:** Perda -200 a -400 empregos enforcement, criação +650 a +1.350 empregos clubes (Oficiais Prevenção, gestão, cultivo, auditores), **líquido +250 a +950**
    - **Proposta formação:** Reconversão profissional para agentes PSP/GNR afectados
  - **Justificação:** Suíça permite produtores operarem pontos venda em pilotos ZüriCan, limite 1-2 previne oligopólio
  - Secção: Integração Indústria Licenciada (linha 839+)
  - Commit: [e6f92d3, 2026-01-26]

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
- **ALTA 1-7:** ✅ **TODAS CONCLUÍDAS (2026-01-26)** - Red-team vulnerabilities de alta prioridade resolvidas
  - PDF final: 311K (vs 292K inicial)
  - 7 commits dedicados (de045f9, 07f9eaa, e6f92d3, e anteriores CRÍTICO 1-5)
  - Validação web research para ALTA 6 (modelo alemão §§24-26 KCanG)
  - Próximo: MÉDIA 1-16 (vulnerabilidades média prioridade)
- **Anexos A e B são bloqueantes** - documento referencia-os explicitamente (✅ concluídos)
- Outras tarefas podem ser implementadas incrementalmente
- **Feedback externo:** Integração de experiência prática suíça (Luísa Álvares) alterou fundamentação ambiental e económica

**Última atualização:** 2026-01-26 22:30 (ALTA 1-7 concluídas)

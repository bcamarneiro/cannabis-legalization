# Como Contribuir

**Este é um projeto aberto a TODOS** — independentemente de filiação partidária, ideologia política, ou background.

Embora desenvolvido inicialmente no contexto do LIVRE, esta proposta pretende ser **abrangente e colaborativa**:

- ✅ **Outros partidos políticos** (PS, PSD, BE, PAN, IL, etc.)
- ✅ **Juventudes partidárias** (JS, JSD, Jovens do BE, etc.)
- ✅ **Associações e ONGs** (redução de danos, direitos humanos, saúde pública)
- ✅ **Pessoas singulares** (advogados, médicos, economistas, ativistas, cidadãos)
- ✅ **Grupos de trabalho** (académicos, profissionais, movimentos sociais)

**O que importa:** Concordar com os princípios de **política baseada em evidência**, **redução de danos**, e **direitos humanos**. A tua filiação política não é um entrave — contribuições são avaliadas pelo mérito, não pela ideologia.

---

## 📋 Estrutura do Projeto

```
cannabis-legalization/
├── chapters/                    # 📂 Capítulos individuais (SOURCE OF TRUTH)
│   ├── 00-metadata.md           #   Metadados do documento
│   ├── 01-sumario-executivo.md  #   Sumário executivo
│   ├── 02-panorama-portugues.md #   Panorama português
│   ├── ...                      #   (capítulos 03-16)
│   └── 17-referencias.md        #   Referências
├── documento.md                 # Documento completo (gerado por scripts/merge-chapters.sh)
├── references.bib               # Bibliografia (citações [@autor2024])
├── scripts/
│   ├── build-pdf.sh             # Gera PDF
│   ├── build-docx.sh            # Gera DOCX
│   └── merge-chapters.sh        # Regenera documento.md a partir dos capítulos
├── docs/TASKS.md                # Lista de vulnerabilidades/melhorias pendentes
└── CONTRIBUTING.md              # Este ficheiro
```

> **⚠️ Nota:** Os ficheiros em `chapters/` são a fonte de verdade. Edita sempre o capítulo
> apropriado em vez de `documento.md` directamente. O `documento.md` é regenerado
> automaticamente com `scripts/merge-chapters.sh`.
>
> **Convenção de numeração:** Os capítulos usam prefixo numérico `00`-`17` para garantir
> a ordem correcta de concatenação (ex: `04-ciencia.md`, `08-pilar-recreativa.md`).

## 🎯 Como Escolher Uma Tarefa

1. **Consulta [docs/TASKS.md](docs/TASKS.md)** para ver vulnerabilidades identificadas
2. **Prioridades:**
   - **TIER 1 (DEVIL 1-4)**: Ataques devastadores - prioridade máxima
   - **LEGAL 1-9**: Questões legais críticas (ideal para advogados)
   - **ECON 1-5**: Modelo económico (ideal para economistas)
   - **HEALTH 1-4**: Saúde pública (ideal para profissionais de saúde)
   - **POLITIC 1-6**: Estratégia política (ideal para ativistas/cientistas políticos)

3. **Expertise recomendada por área:**
   - **Direito**: LEGAL 1-9, IMPLEMENT 7
   - **Economia**: ECON 1-5, DEVIL 6
   - **Medicina/Saúde Pública**: HEALTH 1-4, DEVIL 8
   - **Política**: POLITIC 1-6, DEVIL 2-3
   - **Análise de Dados**: DEVIL 1, 4, 9

---

## 👤 Para Contribuidores Não-Técnicos

**Não sabes usar Git? Não há problema!** Podes contribuir apenas escrevendo texto.

### 💬 Como Funciona (Simples)

1. **Participa numa Discussion** existente ou abre uma nova
2. **Escreve livremente** - não precisa seguir template rígido
3. **Comunidade discute e refina** a proposta colaborativamente
4. **Maintainers criam Issues** quando proposta está madura
5. **Implementação** por quem tiver capacidade técnica
6. **Todos os contribuidores são creditados**

### 🔄 Workflow Completo

```
Discussions (abertas, conversacionais)
    ↓
Discussão colaborativa e refinamento
    ↓
Issues (estruturadas, prontas para trabalhar)
    ↓
Project Board (tracking activo)
    ↓
Pull Request → Review → Merge → Crédito
```

---

## 💬 Opção 1: Participar em Discussions (RECOMENDADO)

**Melhor para:** Reportar problemas, sugerir melhorias, discutir abordagens

### Passo 1: Criar conta GitHub (grátis, 2 minutos)

Se ainda não tens:

1. Vai a [github.com](https://github.com)
2. Clica "Sign up"
3. Segue as instruções (email, password, username)

### Passo 2: Abrir ou participar numa Discussion

1. Vai a [github.com/bcamarneiro/cannabis-legalization/discussions](https://github.com/bcamarneiro/cannabis-legalization/discussions)
2. **Explorar discussions existentes:**
   - 15 discussions prioritárias já abertas (DEVIL 1-4, LEGAL 1-5, HEALTH, ECON, etc.)
   - Podes comentar, adicionar insights, responder perguntas
3. **Criar nova discussion:**
   - Clica "New discussion"
   - Escolhe categoria:
     - 💡 **Ideas** - Sugestões de melhorias
     - ❓ **Q&A** - Perguntas, problemas identificados
     - 💬 **General** - Discussão geral
   - Escreve livremente (sem template rígido)

### Passo 3: O que escrever?

**Formato livre, mas útil incluir:**

- **Qual o problema/sugestão?** (descrição clara)
- **Porque é importante?** (impacto, vulnerabilidade)
- **Tens expertise nesta área?** (advogado, médico, economista)
- **Fontes/referências?** (se aplicável)
- **Ideias de solução?** (opcional)

**Exemplo:**

> Encontrei inconsistência no documento sobre THC limits por idade.
>
> O documento justifica 10% THC para 18-20 anos devido a "desenvolvimento cerebral", mas permite 25% THC aos 21+. Evidência científica (Casey 2019) mostra que o cérebro continua a desenvolver até ~25 anos.
>
> Sou neurologista e acho que isto é vulnerabilidade científica. Sugestões:
> 1. Extend limit até 25 anos (cientificamente consistente)
> 2. Remover limit (autonomia adultos)
> 3. Mudar justificação (não usar brain development)
>
> Fontes: Casey et al. 2019, Di Forti 2019

### O Que Acontece Depois?

1. **Comunidade discute** - outros contribuem, debatem, refinam
2. **Consenso emerge** - proposta é validada colaborativamente
3. **Issue criada** - Maintainers formatam como Issue estruturada (quando madura)
4. **Project Board** - Issue entra em tracking quando pronta para implementar
5. **Implementação** - Alguém com capacidade técnica implementa
6. **Crédito** - Todos os contribuidores creditados: `Co-Authored-By: Teu Nome <email>`

---

## 📋 Opção 2: Abrir Issue Diretamente

**Melhor para:** Propostas muito estruturadas, quem já sabe exactamente o que quer mudar

### Quando usar Issues vs Discussions?

- **Discussions:** Problemas vagos, brainstorming, não sabes solução exacta
- **Issues:** Proposta específica, texto pronto, solução clara

### Como abrir Issue

1. Vai a [github.com/bcamarneiro/cannabis-legalization/issues](https://github.com/bcamarneiro/cannabis-legalization/issues)
2. Clica **"New issue"**
3. Escolhe template **"Proposta de Correção (Não-técnico)"**
4. Preenche:

```markdown
## 👤 Sobre Ti
Nome: Dr. João Silva
Expertise: Advogado (Direito Internacional)
Email: joao.silva@exemplo.pt

## 🎯 Qual Vulnerabilidade Addresses?
LEGAL 1 - International Treaty Obligations

## 📝 Proposta de Alteração
[Texto específico proposto]

## 📚 Fontes/Referências
[Lista de fontes]

## 💡 Justificação
[Porque esta alteração é importante]
```

---

## 📧 Opção 3: Email Privado

**Melhor para:** Feedback confidencial antes de tornar público

- **Email:** <bruno@camarneiro.com>
- Review privada antes de publicar

---

## 🎯 Exemplos de Contribuições Valiosas

**Por área de expertise:**

- **Advogado:** Análise LEGAL 1-9 (tratados ONU, lei UE, IVA, Código Trabalho, Schengen)
- **Médico:** Revisão HEALTH 1-4, DEVIL 8 (riscos cardiovasculares, psicose, THC limits)
- **Economista:** Modelação ECON 1-5 (ROI sensitivity, capital gap, market capture)
- **Analista Político:** DEVIL 2-3, POLITIC 1-6, STRATEGIC 1 (timeline, media, EU)
- **Jornalista:** POLITIC 3 (estratégia media, rapid response, counter-narratives)
- **Data Scientist:** DEVIL 1, 4 (modelação quantitativa, causal inference)

**Discussions prioritárias já abertas:** [Ver todas](https://github.com/bcamarneiro/cannabis-legalization/discussions)

---

## 📝 Workflow de Contribuição (Técnico)

### 1. Fork e Clone

```bash
git clone https://github.com/bcamarneiro/cannabis-legalization.git
cd cannabis-legalization
git checkout -b fix/devil-2-germany-failure-rate
```

### 2. Edita o Capítulo Apropriado

Abre o ficheiro correspondente em `chapters/` e faz as alterações necessárias.
Por exemplo, para editar o modelo recreativo, edita `chapters/08-pilar-recreativa.md`.

> **Não edites `documento.md` directamente** — é gerado automaticamente.
> Após editar capítulos, regenera com: `bash scripts/merge-chapters.sh`

**⚠️ IMPORTANTE sobre referências internas:**

#### Como Funcionam as Âncoras Markdown

**✅ Funcionam BEM no documento final:**
```markdown
## Descriminalização 2001 {#desc-2001}

[Ver secção descriminalização](#desc-2001)  ← Funciona no PDF final
```

**❌ Limitação durante edição:**
- IDEs (VSCode, etc.) não conseguem seguir links para âncoras no mesmo ficheiro
- Preview não mostra links funcionais
- **Isto é normal** - só funciona após compilação PDF

#### Boas Práticas para Cross-References

**Preferir referências textuais simples:**

```markdown
❌ EVITAR: Como vimos na [secção anterior](#desc-2001)
✅ MELHOR: Como vimos na secção "Descriminalização 2001"
✅ MELHOR: Conforme discutido no capítulo "Panorama Português"
```

**Se precisares de âncoras específicas:**
```markdown
<!-- ANCHOR: desc-2001 -->
## Descriminalização 2001 {#desc-2001}

<!-- Mais tarde no documento -->
<!-- LINK: desc-2001 - Ver secção Panorama Português -->
Como vimos na [descriminalização](#desc-2001)...
```

Comentários ajudam outros contribuidores a encontrar contexto mesmo que IDE não siga links.

### 3. Adiciona Citações (se necessário)

**Para adicionar nova fonte:**

1. Edita [references.bib](references.bib)
2. Adiciona entrada no formato BibTeX:

```bibtex
@online{autor2024,
  author = {Nome Autor},
  title = {Título do Artigo},
  year = {2024},
  url = {https://exemplo.com/artigo},
  note = {Breve descrição do conteúdo relevante},
  urldate = {2026-01-27}
}
```

3. Cita no documento: `[@autor2024]`

**Tipos de entradas:**
- `@online`: Artigos web, blogs
- `@article`: Artigos científicos peer-reviewed
- `@legislation`: Leis, decretos-lei
- `@report`: Relatórios oficiais (SICAD, EUDA, etc.)
- `@book`: Livros

### 4. Testa Localmente

```bash
# Gera PDF e verifica compilação
./scripts/build-pdf.sh

# Verifica ficheiro gerado
open output/Documento_Cannabis.pdf  # macOS
xdg-open output/Documento_Cannabis.pdf  # Linux
```

**Verifica:**
- ✅ PDF compila sem erros
- ✅ Citações aparecem correctamente
- ✅ Formatação está correcta
- ✅ Links internos funcionam (clica para testar)

### 5. Commit e Pull Request

```bash
git add chapters/ references.bib
git commit -m "Fix DEVIL 2: Acknowledge Germany 47% club failure rate

- Adiciona contexto sobre 357 aprovados vs 190 operacionais
- Explica diferenças PT vs DE (subsídio estatal, SICAD oversight)
- Ajusta expectativas realistas para modelo português
- Adiciona referências [@bundesgesundheit2024clubs]

Fixes #2"

git push origin fix/devil-2-germany-failure-rate
```

**No GitHub:**
1. Cria Pull Request
2. **Título:** Usa formato "Fix DEVIL/LEGAL/ECON X: Descrição curta"
3. **Descrição:** Explica:
   - Qual vulnerabilidade addresses
   - O que mudou
   - Porque a solução funciona
   - Links para fontes usadas

## 📐 Convenções de Estilo

### Formatação Markdown

- **Secções principais**: `#` (H1) - reservado para capítulos
- **Subsecções**: `##` (H2)
- **Sub-subsecções**: `###` (H3)
- **Listas**: Use `-` para bullet points, `1.` para numeradas
- **Ênfase**: `**negrito**` para conceitos importantes, `*itálico*` para ênfase leve

### Linguagem

- **Tom**: Profissional mas acessível, baseado em evidência
- **Evitar**: Linguagem emotiva, superlatives excessivos, whataboutism
- **Preferir**: Dados concretos, citações académicas, comparações internacionais
- **Números**: Usar formato português (€52-151M, 46 clubes, 18.400 utilizadores)

### Citações

```markdown
✅ CORRETO: Portugal exportou 32.558 kg em 2024 [@infarmed2024]
❌ ERRADO: Portugal exportou muito [@infarmed2024]

✅ CORRETO: Colorado registou -42% consumo juvenil [@mpp2024colorado]
❌ ERRADO: Colorado viu queda massiva [@mpp2024colorado]
```

### Tabelas

```markdown
| Métrica | Valor | Fonte |
|---------|-------|-------|
| Exportação 2024 | 32.558 kg | [@infarmed2024] |
| Prescrições internas | 1.157 | [@eco2024] |
```

## 🔍 Checklist Antes de Submeter

- [ ] Li a vulnerabilidade/tarefa em [TASKS.md](docs/TASKS.md)
- [ ] Editei o capítulo correcto em `chapters/` (não `documento.md`)
- [ ] Regenerei `documento.md` com `bash scripts/merge-chapters.sh`
- [ ] Minhas alterações addressam o problema identificado
- [ ] Adicionei citações para claims novos
- [ ] Testei compilação PDF (`./scripts/build-pdf.sh`)
- [ ] Verifiquei que PDF compila sem warnings
- [ ] Commit message descreve claramente as mudanças
- [ ] Pull Request referencia issue/vulnerability (ex: "Fixes DEVIL 2")

## 🐛 Problemas Comuns

### Erro: "Citeproc: citation X not found"

**Solução:** Adiciona a referência a [references.bib](references.bib)

### PDF não compila (pdflatex errors)

**Causas comuns:**
- Caracteres especiais não escapados (`%`, `$`, `&`, `#`)
- Tabelas mal formatadas
- Links quebrados

**Solução:** Revê a secção editada, testa incrementalmente.

### Links internos não funcionam no IDE

**Isto é normal!** Âncoras markdown só funcionam no documento final compilado. Ver secção "Como Funcionam as Âncoras Markdown" acima.

## 💬 Perguntas?

- **Issues GitHub**: Para bugs, vulnerabilidades específicas
- **Discussions GitHub**: Para questões gerais, ideias, discussão de abordagens

## 📜 Código de Conduta

- Respeito mútuo em todas as interações
- Feedback construtivo, baseado em evidência
- Foco em melhorar o documento, não em atacar contribuições anteriores
- Reconhecer trabalho de outros contribuidores

## 🎓 Recursos Úteis

### Sobre Cannabis e Políticas de Drogas
- [EUDA - European Monitoring Centre for Drugs](https://www.euda.europa.eu/)
- [SICAD - Serviço de Intervenção nos Comportamentos Aditivos](https://www.sicad.pt/)
- [Transform Drug Policy Foundation](https://transformdrugs.org/)

### Ferramentas
- [Pandoc Documentation](https://pandoc.org/MANUAL.html) - Conversão Markdown→PDF
- [BibTeX Format](https://www.bibtex.com/g/bibtex-format/) - Formato citações
- [Markdown Guide](https://www.markdownguide.org/) - Sintaxe markdown

## 🙏 Agradecimentos

Obrigado por contribuires para uma política de drogas baseada em evidência científica e direitos humanos!

---

**Versão:** 1.0 (2026-01-27)

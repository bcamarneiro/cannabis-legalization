# Como Contribuir

Obrigado pelo interesse em contribuir para o documento de posição do LIVRE sobre regulação da cannabis! Este guia ajuda-te a começar.

## 📋 Estrutura do Projeto

```
cannabis-legalization/
├── documento.md                 # Documento final completo (gerado automaticamente)
├── references.bib               # Bibliografia (citações [@autor2024])
├── scripts/build-pdf.sh         # Gera PDF a partir do documento.md
├── docs/TASKS.md                # Lista de vulnerabilidades/melhorias pendentes
└── CONTRIBUTING.md              # Este ficheiro
```

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

### Como Funciona (Simples)

1. **Lê [TASKS.md](docs/TASKS.md)** e escolhe uma vulnerabilidade que matches a tua expertise
2. **Abre uma "Issue"** no GitHub usando o template "Proposta de Correção (Não-técnico)"
3. **Escreve** a tua proposta de texto/alteração diretamente na issue
4. **Aguarda revisão** - alguém da equipa técnica vai implementar e creditar-te

### Passo-a-Passo Detalhado

#### 1. Criar conta GitHub (grátis, 2 minutos)

Se ainda não tens:

1. Vai a [github.com](https://github.com)
2. Clica "Sign up"
3. Segue as instruções (email, password, username)

#### 2. Abrir uma Issue

1. Vai a [github.com/bcamarneiro/cannabis-legalization/issues](https://github.com/bcamarneiro/cannabis-legalization/issues)
2. Clica botão verde **"New issue"**
3. Escolhe template **"Proposta de Correção (Não-técnico)"**
4. Clica **"Get started"**

#### 3. Preencher o Template

```markdown
## 👤 Sobre Ti
Nome: Dr. João Silva
Expertise: Advogado (Direito Internacional)
Email: joao.silva@exemplo.pt

## 🎯 Qual Vulnerabilidade Addresses?
LEGAL 1 - International Treaty Obligations

## 📝 Proposta de Alteração

### Texto Proposto
Portugal ratificou três convenções ONU sobre drogas (1961, 1971, 1988),
mas o Artigo 4 da Convenção de 1961 permite interpretação flexível.
O Uruguai usou a mesma convenção para legalizar cannabis em 2013,
argumentando que a saúde pública justifica regulação estatal.

Recomendação: Adicionar secção no documento explicando...
[continua com a tua proposta]

## 📚 Fontes/Referências
- Convenção Única sobre Estupefacientes (1961), Artigo 4
- Caso Uruguai: Lei 19.172/2013
- Análise jurídica: [URL ou citação]

## 💡 Justificação
Esta secção é crítica porque oponentes vão argumentar que Portugal
viola tratados internacionais. Precisamos mostrar que...
```

#### 4. Submeter

1. Clica **"Submit new issue"** (botão verde)
2. Vais receber notificação por email quando alguém responder
3. Podes acompanhar discussão e fazer ajustes se necessário

### O Que Acontece Depois?

1. **Revisão**: Equipa técnica revê a proposta (normalmente 2-3 dias)
2. **Discussão**: Podem pedir clarificações ou sugerir ajustes
3. **Implementação**: Alguém implementa a alteração no documento
4. **Crédito**: Serás creditado no commit e no documento final

### Exemplos de Contribuições Não-Técnicas Valiosas

- **Advogado**: Análise de LEGAL 1-9 (tratados ONU, lei UE, Código Trabalho)
- **Médico**: Revisão HEALTH 1-4 (riscos cardiovasculares, desenvolvimento cerebral)
- **Economista**: Modelação ECON 1-5 (sensitivity analysis ROI, custos realistas)
- **Político**: Estratégia POLITIC 1-6 (referendos, media, Igreja Católica)
- **Jornalista**: POLITIC 3 (estratégia media, rapid response)

### Não Queres Abrir Issue Pública?

Se preferires feedback privado primeiro:

- **Email**: <bruno.camarneiro@livre.pt>
- Enviamos-te review antes de tornares pública

---

## 📝 Workflow de Contribuição (Técnico)

### 1. Fork e Clone

```bash
git clone https://github.com/bcamarneiro/cannabis-legalization.git
cd cannabis-legalization
git checkout -b fix/devil-2-germany-failure-rate
```

### 2. Edita o Documento

Abre [documento.md](documento.md) e faz as alterações necessárias.

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
git add documento.md references.bib
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

# Exemplo de Uso - Sistema de Referências Dinâmicas

## Como Funciona

### 1. Sistema Atual (Hardcoded) ❌

```markdown
A cannabis medicinal em Portugal[^1] cresceu exponencialmente[^3].

...

[^1]: [[1] Infarmed (2024). "Canábis Medicinal – Evolução da Atividade". https://...]
[^3]: [[3] ECO (2024). "Exportações de canábis quase triplicam em 2024". https://...]
```

**Problemas:**
- Tens de numerar manualmente
- Renumerar se adicionar/remover referência
- Secção REFERÊNCIAS duplicada
- Footnotes duplicam informação

### 2. Sistema Novo (Dinâmico) ✅

```markdown
A cannabis medicinal em Portugal [@infarmed2024] cresceu
exponencialmente [@eco2024].
```

**Vantagens:**
- Pandoc numera automaticamente
- Adicionar/remover ref não quebra numeração
- Bibliografia gerada automaticamente
- Uma única fonte de verdade (references.bib)

## Exemplo Prático

### Documento Markdown (editado por ti)

```markdown
# CAPÍTULO 1: Contexto Português

## 1.1 Cannabis Medicinal

Portugal tornou-se o segundo maior exportador mundial de cannabis
medicinal [@cannareporter2024], produzindo toneladas para exportação
[@euronews2024], enquanto os pacientes locais enfrentam dificuldades
de acesso [@infarmed2024; @eco2024].

A Lei 33/2018 [@cmslaw2024] estabeleceu o quadro regulatório, mas
segundo @greenwald2009, a descriminalização portuguesa...

## 1.2 Evidência Científica

A meta-análise da National Academies [@nasem2017] demonstrou...
Estudos recentes [@ribeiro2024, p. 42] estimam receitas modestas...
```

### Resultado no DOCX (gerado automaticamente)

```
# CAPÍTULO 1: Contexto Português

## 1.1 Cannabis Medicinal

Portugal tornou-se o segundo maior exportador mundial de cannabis
medicinal (CannaReporter, 2024), produzindo toneladas para exportação
(Euronews Health, 2024), enquanto os pacientes locais enfrentam
dificuldades de acesso (Infarmed, 2024; ECO, 2024).

A Lei 33/2018 (CMS Law, 2024) estabeleceu o quadro regulatório, mas
segundo Greenwald (2009), a descriminalização portuguesa...

## 1.2 Evidência Científica

A meta-análise da National Academies (2017) demonstrou...
Estudos recentes (Ribeiro et al., 2024, p. 42) estimam receitas modestas...

───────────────────────────────────────────────

# Referências

CMS Law. (2024). Cannabis law and legislation in Portugal.
https://cms.law/en/int/expert-guides/...

ECO. (2024). Exportações de canábis quase triplicam em 2024.
https://eco.sapo.pt/especiais/...

Euronews Health. (2024). Portugal grows tonnes of medical cannabis
for export but it remains out of reach for local patients.
https://www.euronews.com/health/2024/04/21/...

Greenwald, G. (2009). Drug Decriminalization in Portugal: Lessons
for Creating Fair and Successful Drug Policies. Cato Institute.
https://www.cato.org/publications/white-paper/...

Infarmed. (2024). Canábis Medicinal – Evolução da Atividade.
https://www.infarmed.pt/documents/...

National Academies of Sciences, Engineering, and Medicine. (2017).
The Health Effects of Cannabis and Cannabinoids.
https://www.nationalacademies.org/read/24625

Ribeiro, S., et al. (2024). Cannabis for Recreational Use by Adults
in Portugal: Economic Impact. ResearchGate.
https://www.researchgate.net/publication/...

[... ordenado alfabeticamente, formatado em APA ...]
```

## Sintaxe Completa de Citações

| Uso | Markdown | Resultado |
|-----|----------|-----------|
| **Citação básica** | `[@infarmed2024]` | (Infarmed, 2024) |
| **Múltiplas citações** | `[@infarmed2024; @eco2024]` | (Infarmed, 2024; ECO, 2024) |
| **Citação narrativa** | `@greenwald2009 demonstrou...` | Greenwald (2009) demonstrou... |
| **Sem autor** | `[-@infarmed2024]` | (2024) |
| **Com página** | `[@ribeiro2024, p. 42]` | (Ribeiro et al., 2024, p. 42) |
| **Com capítulo** | `[@nasem2017, cap. 3]` | (NASEM, 2017, cap. 3) |
| **Prefixo** | `[ver @greenwald2009]` | (ver Greenwald, 2009) |
| **Sufixo** | `[@infarmed2024, figura 2]` | (Infarmed, 2024, figura 2) |

## Adicionar Nova Referência

### Opção 1: Manualmente no references.bib

```bibtex
@online{novachave2026,
  author = {{Nome do Autor}},
  title = {Título do Artigo ou Documento},
  year = {2026},
  month = {1},
  url = {https://exemplo.com/artigo},
  urldate = {2026-01-22}
}
```

### Opção 2: Migrar de hardcoded

1. Adiciona a referência hardcoded no documento (formato atual)
2. Executa: `python3 build/migrate-references.py`
3. Script atualiza `references.bib` automaticamente

### Usar no documento:

```markdown
Segundo estudo recente [@novachave2026], ...
```

## Tipos de Entrada BibTeX

### Website/Online
```bibtex
@online{chave2024,
  author = {{Organização}},
  title = {Título},
  year = {2024},
  url = {https://...},
  urldate = {2026-01-22}
}
```

### Artigo científico
```bibtex
@article{autor2024,
  author = {Sobrenome, Nome},
  title = {Título do Artigo},
  journal = {Nome da Revista},
  year = {2024},
  volume = {10},
  number = {2},
  pages = {123--145},
  doi = {10.1234/exemplo}
}
```

### Relatório/White Paper
```bibtex
@report{autor2024,
  author = {Sobrenome, Nome},
  title = {Título do Relatório},
  institution = {Nome da Instituição},
  type = {White Paper},
  year = {2024},
  url = {https://...}
}
```

### Livro
```bibtex
@book{autor2024,
  author = {Sobrenome, Nome},
  title = {Título do Livro},
  publisher = {Editora},
  year = {2024},
  address = {Lisboa}
}
```

## Workflow Completo

### 1. Setup inicial (uma vez)
```bash
# Instalar ferramentas
./build/setup.sh

# Converter referências existentes
python3 build/migrate-references.py
```

### 2. Editar documento
```markdown
# No teu editor (VS Code, etc.)

# ANTES:
produção aumentou significativamente[^3] nos últimos anos[^5].

[^3]: [[3] ECO (2024). "Exportações..."]
[^5]: [[5] Prohibition Partners..."]

# DEPOIS:
produção aumentou significativamente [@eco2024] nos últimos
anos [@prohibition2025].

# (Podes apagar a secção REFERÊNCIAS E FONTES - será gerada automaticamente)
```

### 3. Build
```bash
./build/convert.sh
```

### 4. Upload para Google Docs
1. Abre [Google Drive](https://drive.google.com)
2. Upload `output/Documento_Cannabis.docx`
3. Botão direito → Abrir com → Google Docs
4. Partilha e recolhe feedback com comentários

### 5. Incorporar feedback
1. Edita o Markdown original (não o DOCX)
2. Faz commit das mudanças: `git add . && git commit -m "Incorpora feedback..."`
3. Rebuild: `./build/convert.sh`
4. Re-upload para Google Docs (sobrescrever)

## Índice Automático

Não precisas de escrever o índice! Pandoc gera automaticamente:

```markdown
# SECÇÃO I: CONTEXTO PORTUGUÊS
## CAPÍTULO 1: Introdução
### 1.1 Cannabis Medicinal
### 1.2 Cannabis Recreativa

# SECÇÃO II: PROPOSTA
## PARTE I: Cannabis Medicinal
### Medidas Concretas
```

Gera:

```
Índice

1. SECÇÃO I: CONTEXTO PORTUGUÊS
   1.1. CAPÍTULO 1: Introdução
        1.1.1. Cannabis Medicinal
        1.1.2. Cannabis Recreativa
2. SECÇÃO II: PROPOSTA
   2.1. PARTE I: Cannabis Medicinal
        2.1.1. Medidas Concretas
```

**Vantagem:** Se reordenares secções, numeração atualiza automaticamente!

## Dicas

### ✅ Boas Práticas

1. **Chaves descritivas:** `@greenwald2009` melhor que `@ref1`
2. **Consistência:** Sempre `{Autor}` ou `{{Organização}}`
3. **URLs limpos:** Sem caracteres markdown (`](` etc.)
4. **Uma ref = um ficheiro:** Não duplicar em `.bib` e hardcoded

### ⚠️ Evitar

1. **Não renumerar manualmente:** Pandoc faz isso
2. **Não duplicar bibliografia:** Apaga secção hardcoded
3. **Não misturar sistemas:** Ou BibTeX ou hardcoded, não ambos
4. **Não esquecer urldate:** Importante para fontes online

## Troubleshooting

### "Citação não resolvida [@chave]"
- Verifica que chave existe em `references.bib`
- Sintaxe correta: `[@chave]` não `[chave]`
- Rebuild: `./build/convert.sh`

### "Bibliografia não aparece"
- Flag `--bibliography` em `convert.sh`?
- Ficheiro `references.bib` existe?

### "Estilo errado (quero Chicago em vez de APA)"
```bash
cd build/csl
curl -O https://raw.githubusercontent.com/citation-style-language/styles/master/chicago.csl

# Editar build/convert.sh:
CSL_STYLE="csl/chicago.csl"
```

### "Quero adicionar footnotes normais também"
Podes misturar! Citações BibTeX + footnotes Markdown:

```markdown
Segundo @greenwald2009, a descriminalização[^nota] foi um sucesso.

[^nota]: Apesar de críticas iniciais de setores conservadores.
```

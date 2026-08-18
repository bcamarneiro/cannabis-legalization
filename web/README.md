# Web — Versão Interactiva do Documento

Versão web interactiva do documento de posição "Regulação da Cannabis em Portugal" (LIVRE, Janeiro 2026).

## Funcionalidades

- **Texto completo**: Todas as secções do documento navegáveis com índice lateral
- **Citações interactivas**: Clique em qualquer citação para ver detalhes da fonte (autor, ano, URL, notas)
- **Glossário**: Tooltip ao passar sobre termos chave + página dedicada (`glossary.html`) com pesquisa
- **Pesquisa full-text**: Barra de pesquisa no topo encontra e destaca correspondências no texto
- **Design responsivo**: Funciona em desktop e mobile

## Como usar

Abra `index.html` num browser — é um site estático, sem dependências de servidor.

```bash
# Ou sirva localmente:
cd web/
python3 -m http.server 8080
# Visite http://localhost:8080
```

## Estrutura

```
web/
├── index.html          # Página principal com todo o conteúdo
├── glossary.html       # Página dedicada do glossário
├── css/
│   └── style.css       # Estilos (responsivo)
└── js/
    └── app.js          # Interactividade (citações, pesquisa, glossário)
```

## Geração

O conteúdo é gerado a partir dos ficheiros `chapters/*.md` e `references.bib`.
Para regenerar, execute o script de build (ficheiros de dados embutidos no HTML).

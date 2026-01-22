#!/usr/bin/env python3
"""
Script para migrar referências hardcoded para BibTeX

Lê o documento Markdown atual, extrai todas as referências [1], [2], etc.
e gera um ficheiro references.bib automaticamente.

Uso: python3 build/migrate-references.py
"""

import re
import sys
from pathlib import Path
from typing import List, Dict
from datetime import datetime


def parse_reference(ref_lines: List[str], ref_number: int) -> Dict[str, str]:
    """
    Parse referência que pode ocupar múltiplas linhas.

    Formato esperado:
    **[1]** Autor (Ano). "Título".
    URL ou [URL](URL)
    """
    # Juntar todas as linhas
    full_text = ' '.join(ref_lines)

    # Extrair número da referência
    num_match = re.search(r'\*\*\\\[(\d+)\\\]\*\*', full_text)
    if not num_match:
        return None

    number = int(num_match.group(1))

    # Extrair autor e ano (pode ter mês: "Dezembro 2024" ou só "2024")
    author_year = re.search(r'\*\*\\\[\d+\\\]\*\*\s+(.+?)\s+\((?:\w+\s+)?(\d{4})\)', full_text)
    if not author_year:
        return None

    author = author_year.group(1).strip()
    year = author_year.group(2)

    # Extrair título (entre ** ou entre **)
    title_match = re.search(r'\*\*["""](.+?)["""]\*\*', full_text)
    if not title_match:
        # Formato alternativo sem aspas
        title_match = re.search(r'\(\d{4}\)\.\s+\*\*(.+?)\*\*', full_text)

    title = title_match.group(1).strip() if title_match else "Sem título"

    # Extrair URL
    url_match = re.search(r'https?://[^\s\)]+', full_text)
    url = url_match.group(0).strip() if url_match else ""

    return {
        'number': number,
        'author': author,
        'year': year,
        'title': title,
        'url': url
    }


def generate_bibtex_key(author: str, year: str, existing_keys: set) -> str:
    """
    Gera uma chave BibTeX única (e.g., 'infarmed2024', 'eco2024a').
    """
    # Limpar autor (remover parênteses, vírgulas, etc.)
    author_clean = re.sub(r'[^\w\s]', '', author).lower()

    # Pegar primeira palavra significativa
    words = author_clean.split()
    first_word = words[0] if words else 'ref'

    # Substituir acrónimos comuns
    replacements = {
        'sicad': 'sicad',
        'euda': 'euda',
        'cms': 'cmslaw',
        'eco': 'eco',
        'rtp': 'rtp',
        'infarmed': 'infarmed',
        'euronews': 'euronews',
        'cannareporter': 'cannareporter',
    }

    for abbr, full in replacements.items():
        if abbr in first_word:
            first_word = full
            break

    base_key = f"{first_word}{year}"

    # Evitar duplicados
    key = base_key
    suffix = ord('a')
    while key in existing_keys:
        key = f"{base_key}{chr(suffix)}"
        suffix += 1

    existing_keys.add(key)
    return key


def reference_to_bibtex(ref: Dict[str, str], key: str) -> str:
    """
    Converte dicionário de referência para entrada BibTeX.
    """
    # Determinar tipo de entrada
    entry_type = "online"  # Maioria são URLs

    # Escapar caracteres especiais no título
    title = ref['title'].replace('{', '\\{').replace('}', '\\}')
    author = ref['author']

    # Se autor é organização, envolver em {{}}
    if any(org in author.lower() for org in ['infarmed', 'sicad', 'euda', 'eco', 'rtp', 'euronews']):
        author = f"{{{{{author}}}}}"

    bibtex = f"""@{entry_type}{{{key},
  author = {author},
  title = {{{title}}},
  year = {{{ref['year']}}},
  url = {{{ref['url']}}},
  urldate = {{{datetime.now().strftime('%Y-%m-%d')}}}
}}"""

    return bibtex


def main():
    # Paths
    doc_path = Path(__file__).parent.parent / "Documento_Posicao_Cannabis_LIVRE-REV-CTS.md"
    output_path = Path(__file__).parent / "references.bib"

    if not doc_path.exists():
        print(f"❌ Documento não encontrado: {doc_path}", file=sys.stderr)
        sys.exit(1)

    print("📖 Lendo documento...")
    content = doc_path.read_text(encoding='utf-8')
    lines = content.split('\n')

    # Encontrar secção de referências (linha ~778, não o índice)
    ref_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('# ') and 'REFERÊNCIAS E FONTES' in line:
            ref_start = i + 2  # Pular linha vazia
            break

    if ref_start is None:
        print("❌ Secção REFERÊNCIAS E FONTES não encontrada", file=sys.stderr)
        sys.exit(1)

    print(f"📍 Referências encontradas na linha {ref_start}")

    # Parsear referências até encontrar nova secção
    references = []
    existing_keys = set()

    i = ref_start
    while i < min(ref_start + 250, len(lines)):
        line = lines[i].strip()

        # Parar se encontrar nova secção (# ANEXOS, etc.)
        if line.startswith('# ') and 'REFERÊNCIAS' not in line:
            break

        # Processar linhas com referências
        if line.startswith('**\\['):
            ref_num = len(references) + 1

            # Coletar linhas da referência (até próxima ref ou linha vazia dupla)
            ref_lines = [line]
            j = i + 1
            while j < len(lines):
                next_line = lines[j].strip()
                # Parar em nova referência ou linha vazia seguida de vazia
                if next_line.startswith('**\\[') or (next_line == '' and j+1 < len(lines) and lines[j+1].strip() == ''):
                    break
                if next_line:  # Ignorar linhas vazias simples
                    ref_lines.append(next_line)
                j += 1

            ref_data = parse_reference(ref_lines, ref_num)

            if ref_data:
                key = generate_bibtex_key(ref_data['author'], ref_data['year'], existing_keys)
                references.append((key, ref_data))

            i = j  # Avançar para depois da referência processada
        else:
            i += 1

    print(f"✅ {len(references)} referências parseadas")

    # Gerar ficheiro BibTeX
    print(f"📝 Gerando {output_path}...")

    with output_path.open('w', encoding='utf-8') as f:
        f.write("% Ficheiro de referências bibliográficas\n")
        f.write("% Gerado automaticamente por migrate-references.py\n")
        f.write(f"% Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("%\n")
        f.write("% Como usar no documento Markdown:\n")
        f.write("%   - Citação simples: [@key]\n")
        f.write("%   - Múltiplas: [@key1; @key2]\n")
        f.write("%   - No texto: @key afirma que...\n")
        f.write("%   - Suprimir autor: [-@key]\n")
        f.write("\n\n")

        for key, ref_data in references:
            bibtex = reference_to_bibtex(ref_data, key)
            f.write(bibtex)
            f.write("\n\n")

    print(f"✅ Ficheiro gerado: {output_path}")
    print()
    print("📋 Mapa de referências:")
    print("   [Número] → @chave")
    print("   " + "─" * 40)

    for key, ref_data in references[:10]:  # Mostrar primeiras 10
        print(f"   [{ref_data['number']}] → @{key}")

    if len(references) > 10:
        print(f"   ... e mais {len(references) - 10} referências")

    print()
    print("ℹ️  Próximos passos:")
    print("   1. Substituir [^1], [^2], etc. por [@chave] no documento")
    print("   2. Remover secção REFERÊNCIAS E FONTES (será gerada automaticamente)")
    print("   3. Executar: ./build/convert.sh")


if __name__ == '__main__':
    main()

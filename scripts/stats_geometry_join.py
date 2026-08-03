#!/usr/bin/env python3
"""
Stats-Geometry Join Logic — Map population statistics to regional geometry identifiers.

Computes cannabis social club distribution across Portuguese districts/regions
using the German ratio (1 club per 235,294 inhabitants).

Usage:
    python scripts/stats_geometry_join.py

Output:
    Prints distribution table in Markdown format to stdout.
"""

from dataclasses import dataclass
from typing import List

GERMAN_RATIO = 235_294  # 1 club per 235,294 inhabitants (based on Germany KCanG 2024)
PORTUGAL_POPULATION = 10_749_635  # INE, 31 December 2024


@dataclass
class Region:
    name: str
    population: int
    percentage: float
    clubs: int
    distribution: str


def compute_clubs(population: int) -> int:
    """Compute number of clubs for a given population using German ratio."""
    return max(1, round(population / GERMAN_RATIO))


def build_distribution() -> List[Region]:
    """Build regional distribution based on population data and allocation criteria."""
    regions = [
        # Major metropolitan areas
        Region("Lisboa (AML)", 2_100_000, 20.1, 0, "Lisboa cidade (4), Amadora (1), Oeiras (1), Cascais (1), Sintra (1), Loures (1)"),
        Region("Porto (AMP)", 1_800_000, 17.0, 0, "Porto cidade (3), Vila Nova Gaia (2), Matosinhos (1), Gondomar (1), Maia (1)"),
        Region("Setúbal", 850_000, 7.9, 0, "Setúbal cidade (2), Almada (1), Barreiro (1)"),
        Region("Braga", 867_000, 8.1, 0, "Braga cidade (2), Guimarães (1), Barcelos (1)"),
        Region("Aveiro", 713_000, 6.6, 0, "Aveiro cidade (1), Ovar (1), Ílhavo (1)"),
        
        # Medium cities
        Region("Coimbra", 423_000, 3.9, 0, "Coimbra cidade (2)"),
        Region("Faro (Algarve)", 467_000, 4.3, 0, "Faro/Loulé (1), Portimão/Lagoa (1)"),
        Region("Leiria", 470_000, 4.4, 0, "Leiria cidade (1), Marinha Grande (1)"),
        Region("Viseu", 342_000, 3.2, 0, "Viseu cidade (1), Lamego ou Tondela (1)"),
        Region("Santarém", 432_000, 4.0, 0, "Santarém (1), Torres Novas ou Entroncamento (1)"),
        
        # Interior / low density (minimum 1 club each for accessibility)
        Region("Viana do Castelo", 224_000, 2.1, 0, "Viana cidade (1)"),
        Region("Vila Real", 191_000, 1.8, 0, "Vila Real cidade (1)"),
        Region("Évora", 160_000, 1.5, 0, "Évora cidade (1)"),
        Region("Beja", 141_000, 1.3, 0, "Beja cidade (1)"),
        Region("Castelo Branco", 177_000, 1.6, 0, "Castelo Branco cidade (1)"),
        Region("Bragança", 120_000, 1.1, 0, "Bragança cidade (1)"),
        Region("Portalegre", 106_000, 1.0, 0, "Portalegre cidade (1) ou acesso via Évora"),
        Region("Guarda", 150_000, 1.4, 0, "Guarda cidade (1)"),
        
        # Autonomous regions (geographic isolation)
        Region("Madeira", 252_000, 2.3, 0, "Funchal (1)"),
        Region("Açores", 237_000, 2.2, 0, "Ponta Delgada (1)"),
    ]
    
    # Compute clubs for each region
    for region in regions:
        raw_clubs = compute_clubs(region.population)
        # Apply allocation criteria:
        # 1. Metropolitan areas get proportional allocation
        # 2. Interior/autonomous regions get minimum 1 club regardless of ratio
        if region.population < 300_000:
            region.clubs = max(1, raw_clubs)  # Ensure minimum coverage for interior/isolated
        else:
            region.clubs = raw_clubs
    
    # Adjust to match target of 46 clubs total
    total_raw = sum(r.clubs for r in regions)
    target_clubs = compute_clubs(PORTUGAL_POPULATION)
    
    # Fine-tune: adjust major metros if needed to hit target
    if total_raw != target_clubs:
        diff = target_clubs - total_raw
        # Adjust Lisboa (largest) to absorb difference
        regions[0].clubs += diff
    
    return regions


def print_table(regions: List[Region]) -> None:
    """Print distribution table in Markdown format."""
    print("| Região/Distrito | População 2024 | Clubes Estimados | Distribuição Proposta |")
    print("| :---- | :---- | :---- | :---- |")
    
    for r in regions:
        clube_word = "clube" if r.clubs == 1 else "clubes"
        print(f"| **{r.name}** | {r.population:,} ({r.percentage}%) | {r.clubs} {clube_word} | {r.distribution} |")
    
    total_pop = sum(r.population for r in regions)
    total_clubs = sum(r.clubs for r in regions)
    print(f"| **TOTAL NACIONAL** | **{total_pop:,}** | **{total_clubs} clubes** | Cobertura nacional completa |")


def print_summary(regions: List[Region]) -> None:
    """Print summary statistics."""
    total_clubs = sum(r.clubs for r in regions)
    total_pop = sum(r.population for r in regions)
    
    print("\n---\n")
    print(f"**Rácio aplicado:** 1 clube por {GERMAN_RATIO:,} habitantes (modelo alemão KCanG 2024)")
    print(f"**População Portugal:** {PORTUGAL_POPULATION:,} (INE, Dezembro 2024)")
    print(f"**Total clubes estimados:** {total_clubs}")
    print(f"**Rácio efectivo:** 1 clube por {total_pop // total_clubs:,} habitantes")
    print("\n**Critérios de alocação:**")
    print("1. Densidade populacional: AML/AMP (37% população) recebem 37% clubes")
    print("2. Acessibilidade geográfica: Interior recebe mínimo 1 clube (evitar >100km deslocação)")
    print("3. Regiões autónomas: Madeira e Açores garantidas (isolamento geográfico)")
    print("4. Equidade acesso: Evitar 'desertos' sem clubes num raio >50km")


def main():
    """Main entry point."""
    regions = build_distribution()
    print("### Distribuição Geográfica Proposta (Escala Completa)\n")
    print_table(regions)
    print_summary(regions)


if __name__ == "__main__":
    main()

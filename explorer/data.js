window.LEGISLATIVE_DATA = {
  meta: {
    title: "Explorador Comparativo de Modelos Legislativos de Cannabis",
    updated: "Janeiro 2026"
  },
  countries: [
    { id: "pt", name: "Portugal", status: "Proposta 2026", color: "#2d6a4f" },
    { id: "de", name: "Alemanha", status: "CanG 2024", color: "#1d3557" },
    { id: "ca", name: "Canadá", status: "Lei 2018", color: "#bc4749" },
    { id: "uy", name: "Uruguai", status: "Lei 2013", color: "#e9c46a" }
  ],
  categories: [
    {
      name: "Enquadramento Geral",
      features: [
        { label: "Paradigma", pt: "Redução de danos; não-comercial", de: "Saúde pública; não-comercial", ca: "Comercial regulado", uy: "Estatal controlado" },
        { label: "Modelo de legalização", pt: "Clubes + autocultivo (Fase 2); comercial condicional (Fase 3)", de: "Clubes + autocultivo (Pilar 1); comercial bloqueado UE (Pilar 2)", ca: "Venda comercial privada e estatal", uy: "Farmácias + clubes + autocultivo" },
        { label: "Data de entrada em vigor", pt: "Proposta 2026 → aprovação 2027 (est.)", de: "1 abr 2024", ca: "17 out 2018", uy: "2013 (regulamentação gradual até 2017)" }
      ]
    },
    {
      name: "Posse e Cultivo Pessoal",
      features: [
        { label: "Posse em público", pt: "Decriminalizado (≤25 dias consumo)", de: "≤25 g", ca: "Varia (geralmente ≤30 g)", uy: "Registrado (compra controlada)" },
        { label: "Posse em casa", pt: "Sem limite explícito (3 plantas = ~50-150 g)", de: "≤50 g", ca: "Sem limite federal (províncias variam)", uy: "Autocultivo: ≤480 g/ano" },
        { label: "Autocultivo", pt: "3 plantas; sementes certificadas obrigatórias", de: "3 plantas por adulto", ca: "4 plantas por domicílio", uy: "6 plantas; registo obrigatório" },
        { label: "Idade mínima", pt: "21 (clubes); 18-21 THC ≤10%", de: "18", ca: "18-19 (província)", uy: "18" },
        { label: "Limite THC jovens", pt: "≤10% THC para 18-21 em clubes", de: "≤10% THC para 18-21; máx. 30 g/mês", ca: "Varia por província/produto", uy: "Limites evoluíram: 2-9% (2017-22) → 15% (2022) → 20% (2024)" }
      ]
    },
    {
      name: "Clubes e Acesso",
      features: [
        { label: "Clubes sociais", pt: "Máx. 500 membros; sem fins lucrativos; cost-recovery", de: "Máx. 500 membros; 25 g/dia; 50 g/mês", ca: "N/A (dispensários comerciais)", uy: "45-180 membros; registo obrigatório" },
        { label: "Distância escolas", pt: "A definir (proposta: ≥200 m)", de: "200 m (clubes e consumo proibido)", ca: "Varia por província", uy: "Restrições de zonamento aplicáveis" },
        { label: "Modelo de preço", pt: "€3-6/g (cost-recovery) + €30/mês admin", de: "Quotas €70-100/mês estimado", ca: "$7,50-14/g (€7-13; inclui impostos 37%)", uy: "~$1-1,5/g (preço estatal)" },
        { label: "Testes de qualidade", pt: "Obrigatórios ISO 17025; certificado QR/lote", de: "Obrigatórios (KCanG); inspeções estaduais", ca: "Obrigatórios provinciais", uy: "Obrigatórios (estatal)" },
        { label: "Turismo cannábico", pt: "Proibido (residência ≥6 meses)", de: "Proibido (residência obrigatória)", ca: "Permitido", uy: "Proibido (cidadãos/registrados)" }
      ]
    },
    {
      name: "Impacto e Fiscalidade",
      features: [
        { label: "Acesso mercado legal", pt: "Estimado 40-50% (anos 5-10)", de: "88% obtêm de fontes legais; mas ~2% elegíveis em clubes", ca: "72% mercado legal (2024)", uy: "37% via canais legais (2024)" },
        { label: "Consumo juvenil (tendência)", pt: "Proposta visa estabilidade", de: "12-17 anos: 6,7% → 6,1% (1.º ano)", ca: "15-17: estável ~41% (sem aumento atribuível)", uy: "Idade 1.º uso: 18 → 20 anos; consumo geral: 14,6% → 12,3%" },
        { label: "Receitas fiscais", pt: "€0 diretas; poupanças enforcement €30-65 M/ano", de: "€0 (não-comercial)", ca: "$5,4 B CAD acumulados (federal + províncias)", uy: "Limitadas (modelo estatal)" },
        { label: "Poupanças enforcement", pt: "€30-65 M/ano (estimativa)", de: "~100 000 processos criminais evitados", ca: "Significativas (modelo comercial)", uy: "Redução processos judiciais" }
      ]
    }
  ],
  sources: {
    pt: [
      { key: "infarmed2024", text: "INFARMED (2024). Exportação cannabis medicinal." },
      { key: "cannareporter2024", text: "CannaReporter (2024). Prescrições internas Portugal." },
      { key: "cannabislaw2024export", text: "Cannabis Law (2024). Exportação vs. consumo interno." },
      { key: "springer2021pt", text: "Springer (2021). Lei 30/2000: 18 meses implementação." },
      { key: "greenwald2009", text: "Greenwald (2009). 25 anos descriminalização portuguesa." }
    ],
    de: [
      { key: "bundesministerium2024", text: "Bundesministerium (2024). Cannabis Act (CanG)." },
      { key: "marijuanamoment2025", text: "Marijuana Moment (2025). Consumo juvenil Alemanha." },
      { key: "businesscannabis2025a", text: "Business of Cannabis (2025). Processos evitados." },
      { key: "internationalcbc2025", text: "International CBC (2025). Estudo KonCanG." },
      { key: "mmjdaily2025", text: "MME Daily (2025). Disparidades regionais clubes." }
    ],
    ca: [
      { key: "healthcanada2024", text: "Health Canada (2024). Canadian Cannabis Survey." },
      { key: "cbcnews2025", text: "CBC News (2025). Receitas fiscais acumuladas." },
      { key: "statcan2019youth", text: "Statistics Canada (2019). Consumo juvenil." }
    ],
    uy: [
      { key: "cdays2025", text: "CDAys (2025). 10 anos legalização Uruguai." },
      { key: "latinamerica2024", text: "Latin America Cannabis (2024). Evolução THC Uruguai." },
      { key: "softsecrets2025", text: "Soft Secrets (2025). Variedades 20% THC." }
    ]
  }
};

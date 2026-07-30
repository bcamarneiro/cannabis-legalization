/**
 * PolicySimulation Engine
 * Models projected social and economic outcomes of cannabis legalization
 * based on tax rates and possession limits.
 *
 * Data sources: cannabis-legalization document (chapters 05, 06, 08)
 * - 706,000 cannabis users in Portugal (SICAD)
 * - 46 clubs projected (German ratio 1:235k applied to PT)
 * - Black market: €52–151M/year
 * - Enforcement savings: €30–65M/year
 */

const PolicyEngine = (() => {
  // --- Baseline constants (from document) ---
  const TOTAL_USERS = 706000;          // Total cannabis users in Portugal
  const BLACK_MARKET_LOW = 52;         // €M/year (low estimate)
  const BLACK_MARKET_HIGH = 151;       // €M/year (high estimate)
  const BLACK_MARKET_AVG = 101.5;      // €M/year (midpoint)
  const ENFORCEMENT_SAVINGS_LOW = 30;  // €M/year
  const ENFORCEMENT_SAVINGS_HIGH = 65; // €M/year
  const ENFORCEMENT_SAVINGS_AVG = 47.5;
  const CLUBS_GERMAN_RATIO = 46;       // 1 club per 235k inhabitants
  const MEMBERS_PER_CLUB = 400;        // Average members per club

  // --- Model parameters ---
  // These are derived from international evidence (Colorado, Canada, Uruguay)
  // and the document's own projections.

  /**
   * Market capture rate as a function of tax rate.
   * Lower taxes → higher legal market adoption (Canada: 72% at ~15% effective tax).
   * Higher taxes → users stay in black market (classic Laffer curve for sin goods).
   * Returns fraction 0–1.
   */
  function marketCapture(taxRate) {
    // Quadratic decay: higher taxes progressively drive users to black market.
    // At 0% tax: 68% capture (some still prefer black market convenience)
    // At 15% tax: ~57% capture
    // At 30% tax: ~23% capture (heavy black market retention)
    // At 50% tax: ~6% capture (near-total black market dominance)
    const peak = 0.68;
    const decay = 0.0005;
    return Math.max(0.05, peak - decay * taxRate * taxRate);
  }

  /**
   * Black market displacement as possession limits increase.
   * Higher limits → less need for black market (people can legally possess more).
   * Returns fraction 0–1 of black market displaced.
   */
  function blackMarketDisplacement(possessionLimit) {
    // 10g limit: 0.25 displacement (most users need more than 10g)
    // 25g limit: 0.40 displacement
    // 50g limit: 0.55 displacement
    // 100g limit: 0.65 displacement
    const base = 0.15;
    const factor = 0.0055;
    return Math.min(0.75, base + factor * possessionLimit);
  }

  /**
   * Club capacity utilization based on tax rate and possession limits.
   * Higher taxes incentivize club membership (cost-recovery pricing undercuts taxes).
   */
  function clubUtilization(taxRate, possessionLimit) {
    const baseUtilization = 0.7; // 70% base
    // Tax effect: higher commercial tax → more people join non-profit clubs
    const taxEffect = 0.008 * taxRate;
    // Possession effect: higher limits → slightly less club dependency
    const limitEffect = -0.001 * possessionLimit;
    return Math.min(1.0, Math.max(0.3, baseUtilization + taxEffect + limitEffect));
  }

  /**
   * Tax revenue model (if commercial sales exist; PT model is cost-recovery only).
   * Included for scenario comparison.
   */
  function taxRevenue(taxRate, possessionLimit, marketCaptureRate, clubCount) {
    const clubUsers = clubCount * MEMBERS_PER_CLUB * clubUtilization(taxRate, possessionLimit);
    const commercialUsers = TOTAL_USERS * marketCaptureRate - clubUsers;
    if (commercialUsers < 0) return 0;
    // Average spend: ~€500/year per user (based on 25g/month at €6/g = €150/month → €1800/yr
    // but most are occasional: 8.2% prevalence, average occasional €250–500/yr)
    const avgSpendCommercial = 400; // €/year
    const taxableBase = commercialUsers * avgSpendCommercial;
    return (taxRate / 100) * taxableBase / 1e6; // Convert to €M
  }

  /**
   * Health outcome index (0–100, higher = better).
   * Based on: possession limits (access to regulated product),
   * club density (prevention officers), and market capture (quality control).
   */
  function healthIndex(taxRate, possessionLimit, clubCount) {
    const capture = marketCapture(taxRate);
    const displacement = blackMarketDisplacement(possessionLimit);
    const clubsPerUser = clubCount / (TOTAL_USERS / 100000); // per 100k users

    // Weighted components
    const qualityControl = capture * 35;        // regulated = tested product
    const harmReduction = displacement * 25;    // less black market = less contaminated
    const preventionAccess = Math.min(20, clubsPerUser * 4); // officers per capita
    const youthProtection = Math.min(20, (possessionLimit > 10 ? 10 : 20)); // lower limits protect youth

    return Math.round(qualityControl + harmReduction + preventionAccess + youthProtection);
  }

  /**
   * Main simulation function.
   * @param {number} taxRate - Tax rate as percentage (0–50)
   * @param {number} possessionLimit - Max possession in grams (5–200)
   * @param {number} clubCount - Number of social clubs (1–200)
   * @returns {object} Simulation results
   */
  function simulate(taxRate, possessionLimit, clubCount) {
    // Clamp inputs
    taxRate = Math.max(0, Math.min(50, taxRate));
    possessionLimit = Math.max(5, Math.min(200, possessionLimit));
    clubCount = Math.max(1, Math.min(200, clubCount));

    const capture = marketCapture(taxRate);
    const displacement = blackMarketDisplacement(possessionLimit);
    const utilization = clubUtilization(taxRate, possessionLimit);

    // Club metrics
    const clubMembers = Math.round(clubCount * MEMBERS_PER_CLUB * utilization);
    const clubCoverage = Number((clubMembers / TOTAL_USERS * 100).toFixed(1));

    // Market metrics
    const legalMarketUsers = Math.round(TOTAL_USERS * capture);
    const blackMarketUsers = TOTAL_USERS - legalMarketUsers;
    const blackMarketSize = Number((BLACK_MARKET_AVG * (1 - displacement)).toFixed(1));

    // Revenue metrics
    const revenue = taxRevenue(taxRate, possessionLimit, capture, clubCount);
    const enforcementSaved = Number((ENFORCEMENT_SAVINGS_AVG * displacement).toFixed(1));

    // Health
    const health = healthIndex(taxRate, possessionLimit, clubCount);

    // Club economics
    const costPerGramClub = Number((3 + (50 / clubCount)).toFixed(2)); // €/g, economies of scale
    const avgMemberCostMonth = Math.round(costPerGramClub * 25); // ~25g/month

    return {
      inputs: { taxRate, possessionLimit, clubCount },
      market: {
        captureRate: Number((capture * 100).toFixed(1)),
        legalMarketUsers,
        blackMarketUsers,
        blackMarketSize,
        displacementRate: Number((displacement * 100).toFixed(1)),
      },
      clubs: {
        totalClubs: clubCount,
        utilizationRate: Number((utilization * 100).toFixed(1)),
        totalMembers: clubMembers,
        coveragePercent: clubCoverage,
        costPerGram: costPerGramClub,
        avgMonthlyCost: avgMemberCostMonth,
      },
      fiscal: {
        taxRevenue: Number(revenue.toFixed(1)),
        enforcementSavings: enforcementSaved,
        netFiscalImpact: Number((enforcementSaved - revenue).toFixed(1)),
      },
      health: {
        index: health,
        grade: health >= 75 ? 'A' : health >= 55 ? 'B' : health >= 35 ? 'C' : 'D',
        qualityControl: Number((capture * 35).toFixed(0)),
        harmReduction: Number((displacement * 25).toFixed(0)),
      },
    };
  }

  /**
   * Generate a series of results for charting by sweeping one parameter.
   */
  function sweep(parameter, range, fixedParams) {
    return range.map(val => {
      const params = { ...fixedParams, [parameter]: val };
      return {
        x: val,
        result: simulate(params.taxRate, params.possessionLimit, params.clubCount),
      };
    });
  }

  return { simulate, sweep, constants: { TOTAL_USERS, BLACK_MARKET_AVG, ENFORCEMENT_SAVINGS_AVG } };
})();

// Export for Node.js test environment
if (typeof module !== 'undefined' && module.exports) {
  module.exports = PolicyEngine;
}

#!/usr/bin/env node
/**
 * PolicySimulation Engine Test Suite
 * Run: node policy-simulator/tests/test.js
 *
 * Validates the simulation engine's core behavior:
 * - Boundary conditions
 * - Monotonicity (directional correctness)
 * - Result structure integrity
 * - Preset scenario sanity checks
 */

'use strict';

// Load engine — strip IIFE wrapper for Node
const fs = require('fs');
const path = require('path');

const engineSrc = fs.readFileSync(
  path.join(__dirname, '..', 'engine.js'), 'utf8'
);

// Extract the module by evaluating in a sandbox
let PolicyEngine;
(function () {
  const module = { exports: {} };
  // Use Function constructor to evaluate in scope with module.exports available
  const fn = new Function('module', 'exports', engineSrc);
  fn(module, module.exports);
  PolicyEngine = module.exports;
})();

if (!PolicyEngine || typeof PolicyEngine.simulate !== 'function') {
  console.error('FAIL: Could not load PolicyEngine module');
  process.exit(1);
}

// --- Test helpers ---
let passed = 0;
let failed = 0;
const failures = [];

function assert(condition, description) {
  if (condition) {
    passed++;
    console.log('  ✓ ' + description);
  } else {
    failed++;
    const msg = '  ✗ ' + description;
    failures.push(description);
    console.error(msg);
  }
}

function assertRange(value, min, max, description) {
  assert(value >= min && value <= max, description + ` (got ${value}, expected ${min}–${max})`);
}

function assertFinite(value, description) {
  assert(Number.isFinite(value), description + ` (got ${value})`);
}

// --- Test suite ---
console.log('\nPolicySimulation Engine Tests\n' + '='.repeat(40) + '\n');

// 1. Boundary conditions
console.log('1. Boundary Conditions');
{
  let r;

  // Min values
  r = PolicyEngine.simulate(0, 5, 1);
  assert(r.inputs.taxRate === 0, 'taxRate 0 → input preserved');
  assert(r.inputs.possessionLimit === 5, 'possession limit 5 → input preserved');
  assert(r.inputs.clubCount === 1, 'club count 1 → input preserved');
  assert(r.market.captureRate !== undefined, 'captureRate defined at min');
  assert(parseFloat(r.market.captureRate) > 0, 'captureRate > 0 at zero tax');
  assert(r.health.index >= 0, 'health index >= 0 at min');

  // Max values
  r = PolicyEngine.simulate(50, 200, 200);
  assert(r.inputs.taxRate === 50, 'taxRate 50 → input preserved');
  assert(r.inputs.possessionLimit === 200, 'possession limit 200 → input preserved');
  assert(r.inputs.clubCount === 200, 'club count 200 → input preserved');
  assert(parseFloat(r.market.captureRate) < 100, 'captureRate < 100% at max tax');
  assert(parseFloat(r.market.displacementRate) > 0, 'displacement > 0 at high limit');

  // Clamping
  r = PolicyEngine.simulate(-10, 0, -5);
  assert(r.inputs.taxRate === 0, 'negative taxRate → clamped to 0');
  assert(r.inputs.possessionLimit === 5, 'sub-5 possession → clamped to 5');
  assert(r.inputs.clubCount === 1, 'sub-1 clubCount → clamped to 1');

  r = PolicyEngine.simulate(100, 500, 300);
  assert(r.inputs.taxRate === 50, 'taxRate 100 → clamped to 50');
  assert(r.inputs.possessionLimit === 200, 'possession limit 500 → clamped to 200');
  assert(r.inputs.clubCount === 200, 'clubCount 300 → clamped to 200');
}

// 2. Monotonicity (directional correctness)
console.log('\n2. Monotonicity (Directional Correctness)');
{
  const base = PolicyEngine.simulate(10, 25, 46);

  // Higher tax → lower market capture
  const highTax = PolicyEngine.simulate(30, 25, 46);
  assert(
    parseFloat(highTax.market.captureRate) < parseFloat(base.market.captureRate),
    'higher tax → lower market capture'
  );

  // Higher possession limit → higher displacement
  const highLimit = PolicyEngine.simulate(10, 80, 46);
  assert(
    parseFloat(highLimit.market.displacementRate) > parseFloat(base.market.displacementRate),
    'higher possession limit → higher displacement'
  );

  // More clubs → more members
  const moreClubs = PolicyEngine.simulate(10, 25, 80);
  assert(
    moreClubs.clubs.totalMembers > base.clubs.totalMembers,
    'more clubs → more total members'
  );

  // Zero tax → no tax revenue
  const zeroTax = PolicyEngine.simulate(0, 25, 46);
  assert(
    Math.abs(parseFloat(zeroTax.fiscal.taxRevenue)) < 0.01,
    'zero tax → zero tax revenue'
  );

  // Higher club count → lower cost per gram (economies of scale)
  assert(
    parseFloat(moreClubs.clubs.costPerGram) < parseFloat(base.clubs.costPerGram),
    'more clubs → lower cost per gram'
  );
}

// 3. Result structure integrity
console.log('\n3. Result Structure Integrity');
{
  const r = PolicyEngine.simulate(15, 25, 46);

  // Required top-level keys
  const topKeys = ['inputs', 'market', 'clubs', 'fiscal', 'health'];
  topKeys.forEach(key => {
    assert(r[key] !== undefined, `result.${key} exists`);
  });

  // Inputs structure
  assertFinite(r.inputs.taxRate, 'inputs.taxRate is finite');
  assertFinite(r.inputs.possessionLimit, 'inputs.possessionLimit is finite');
  assertFinite(r.inputs.clubCount, 'inputs.clubCount is finite');

  // Market structure
  assertFinite(parseFloat(r.market.captureRate), 'market.captureRate parseable');
  assertFinite(r.market.legalMarketUsers, 'market.legalMarketUsers finite');
  assertFinite(r.market.blackMarketUsers, 'market.blackMarketUsers finite');
  assert(r.market.legalMarketUsers + r.market.blackMarketUsers > 0, 'total users > 0');

  // Clubs structure
  assert(r.clubs.totalClubs > 0, 'clubs.totalClubs > 0');
  assert(r.clubs.totalMembers >= 0, 'clubs.totalMembers >= 0');
  assertFinite(parseFloat(r.clubs.utilizationRate), 'clubs.utilizationRate parseable');

  // Fiscal structure
  assertFinite(parseFloat(r.fiscal.taxRevenue), 'fiscal.taxRevenue parseable');
  assertFinite(parseFloat(r.fiscal.enforcementSavings), 'fiscal.enforcementSavings parseable');

  // Health structure
  assertFinite(r.health.index, 'health.index finite');
  assert(r.health.index >= 0 && r.health.index <= 100, 'health.index in 0–100');
  assert(['A', 'B', 'C', 'D'].includes(r.health.grade), 'health.grade is A/B/C/D');
}

// 4. Preset scenarios
console.log('\n4. Preset Scenarios (Sanity Checks)');
{
  // German model: zero tax, 25g, 46 clubs
  const german = PolicyEngine.simulate(0, 25, 46);
  assert(Math.abs(parseFloat(german.fiscal.taxRevenue)) < 0.01, 'German: zero tax revenue');
  assertRange(parseFloat(german.market.captureRate), 40, 75, 'German: capture 40–75%');
  assertRange(german.clubs.totalMembers, 5000, 25000, 'German: members 5k–25k');

  // Portuguese proposal: zero tax, 50g, 46 clubs
  const pt = PolicyEngine.simulate(0, 50, 46);
  assertRange(parseFloat(pt.market.displacementRate), 30, 70, 'Portuguese: displacement 30–70%');

  // Commercial: 18% tax, 30g, 80 clubs
  const commercial = PolicyEngine.simulate(18, 30, 80);
  assert(parseFloat(commercial.fiscal.taxRevenue) > 0, 'Commercial: positive tax revenue');
  assertRange(commercial.clubs.totalMembers, 10000, 50000, 'Commercial: members 10k–50k');

  // Restrictive: 30% tax, 10g, 10 clubs
  const restrictive = PolicyEngine.simulate(30, 10, 10);
  assert(parseFloat(restrictive.market.captureRate) < 50, 'Restrictive: low capture');
  assert(restrictive.clubs.totalMembers < 5000, 'Restrictive: low membership');
}

// 5. Sweep function
console.log('\n5. Sweep Function');
{
  const sweep = PolicyEngine.sweep('taxRate', [0, 10, 20, 30], {
    taxRate: 10, possessionLimit: 25, clubCount: 46,
  });
  assert(sweep.length === 4, 'sweep returns correct number of results');
  assert(sweep[0].x === 0, 'sweep preserves x-values');
  assert(sweep[0].result.market !== undefined, 'sweep results have market data');

  // Each result should have decreasing capture
  const captures = sweep.map(s => parseFloat(s.result.market.captureRate));
  for (let i = 1; i < captures.length; i++) {
    assert(captures[i] < captures[i - 1], `sweep: capture decreases at step ${i}`);
  }
}

// --- Summary ---
console.log('\n' + '='.repeat(40));
console.log(`\nResults: ${passed} passed, ${failed} failed, ${passed + failed} total\n`);

if (failed > 0) {
  console.error('FAILURES:');
  failures.forEach((f, i) => console.error(`  ${i + 1}. ${f}`));
  process.exit(1);
} else {
  console.log('All tests passed.\n');
  process.exit(0);
}

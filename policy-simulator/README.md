# Policy Impact Simulator

Interactive simulation tool that lets users model cannabis policy parameters — tax rates, possession limits, and club density — and visualize projected social and economic outcomes in real time.

## Overview

The Policy Impact Simulator is part of the [cannabis-legalization](https://github.com/bcamarneiro/cannabis-legalization) position document. It transforms passive reading into active advocacy by allowing stakeholders to explore policy scenarios and see how different regulatory choices affect:

- **Market capture** — percentage of users moving from black market to regulated channels
- **Tax revenue** — projected annual fiscal revenue (€M)
- **Enforcement savings** — reduction in policing and judicial costs
- **Black market displacement** — how possession limits shrink the illicit economy
- **Health outcomes** — composite index covering quality control, harm reduction, and prevention access
- **Club economics** — membership, coverage, and cost-per-gram projections

## How to Use

Open `policy-simulator/index.html` in any modern browser. No build step, no server required.

Adjust the three sliders:
- **Tax Rate** (0–50%) — effective tax on commercial sales
- **Possession Limit** (5–100g) — max grams for personal possession
- **Social Clubs** (5–150) — number of licensed non-profit clubs

Charts update in real time as you adjust any parameter. Use the preset buttons to jump to common scenarios.

## Technical Architecture

```
policy-simulator/
├── index.html      Main page — UI, controls, and layout
├── engine.js       Simulation logic engine — pure functions, no DOM dependency
├── charts.js       Chart.js visualization layer
├── styles.css      Dark-themed responsive styles
├── README.md       This file
└── tests/
    ├── test.html   Browser-based test runner
    └── test.js     Test suite for the engine
```

### Engine (`engine.js`)

Pure JavaScript module (IIFE). All model functions are deterministic and side-effect-free. Exposes:
- `PolicyEngine.simulate(taxRate, possessionLimit, clubCount)` → full result object
- `PolicyEngine.sweep(parameter, range, fixedParams)` → array of results for charting

Data sources: SICAD prevalence data, international benchmarks (Colorado, Canada, Uruguay, Germany), and projections from the position document.

### Charts (`charts.js`)

Built on Chart.js 4.x (loaded from CDN). Renders five visualizations:
1. Bar chart — legal vs black market user distribution
2. Doughnut — market capture rate gauge
3. Line chart — tax sweep showing capture rate vs revenue trade-off
4. Line chart — possession limit sweep showing displacement and health effects
5. Radar chart — health outcome component breakdown

## Testing

Run the test suite:

```bash
# Node.js (from repo root)
node policy-simulator/tests/test.js

# Or open in browser:
open policy-simulator/tests/test.html
```

The test suite validates:
- Boundary conditions (min/max inputs produce valid outputs)
- Monotonicity (higher taxes → lower capture, etc.)
- Result structure consistency
- Preset scenarios match expected ranges

## Design Decisions

- **No framework dependency** — vanilla JS keeps the module self-contained and embeddable
- **Dark theme** — matches the document's serious, evidence-based tone
- **Sticky controls panel** — allows exploring charts while adjusting parameters
- **Presets** — German model, Portuguese proposal, commercial, and restrictive scenarios provide context
- **Real-time updates** — sliders trigger instant chart re-rendering (debounced by Chart.js animation)

## License

CC BY-SA 4.0 — matches the parent repository license.

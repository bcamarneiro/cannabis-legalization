/**
 * PolicySimulation Charts
 * Chart.js visualization layer for simulation results.
 * Requires Chart.js (loaded from CDN) and PolicyEngine.
 */
const PolicyCharts = (() => {
  let chartInstances = {};

  const COLORS = {
    green: 'rgba(76, 175, 80, 0.8)',
    greenLight: 'rgba(76, 175, 80, 0.2)',
    blue: 'rgba(33, 150, 243, 0.8)',
    blueLight: 'rgba(33, 150, 243, 0.2)',
    orange: 'rgba(255, 152, 0, 0.8)',
    orangeLight: 'rgba(255, 152, 0, 0.2)',
    red: 'rgba(244, 67, 54, 0.8)',
    redLight: 'rgba(244, 67, 54, 0.2)',
    purple: 'rgba(156, 39, 176, 0.8)',
    grey: 'rgba(158, 158, 158, 0.8)',
    greyLight: 'rgba(158, 158, 158, 0.2)',
    white: 'rgba(255, 255, 255, 0.9)',
  };

  const chartDefaults = {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 400 },
    plugins: {
      legend: {
        labels: { color: '#b0b0b0', font: { size: 11 } },
      },
    },
  };

  function destroyAll() {
    Object.values(chartInstances).forEach(c => c.destroy());
    chartInstances = {};
  }

  function create(id, config) {
    const canvas = document.getElementById(id);
    if (!canvas) return null;
    const ctx = canvas.getContext('2d');
    const chart = new Chart(ctx, { ...chartDefaults, ...config });
    chartInstances[id] = chart;
    return chart;
  }

  /**
   * Bar chart: Market Distribution (legal vs black market users)
   */
  function renderMarketDistribution(result) {
    const id = 'chart-market';
    destroyChart(id);

    const data = {
      labels: ['Legal Market', 'Black Market'],
      datasets: [{
        label: 'Users',
        data: [result.market.legalMarketUsers, result.market.blackMarketUsers],
        backgroundColor: [COLORS.green, COLORS.red],
        borderColor: [COLORS.green, COLORS.red],
        borderWidth: 1,
      }],
    };

    create(id, {
      type: 'bar',
      data,
      options: {
        scales: {
          y: {
            beginAtZero: true,
            ticks: { color: '#b0b0b0', callback: v => (v / 1000).toFixed(0) + 'k' },
            grid: { color: 'rgba(255,255,255,0.05)' },
          },
          x: { ticks: { color: '#b0b0b0' }, grid: { display: false } },
        },
        plugins: {
          tooltip: { callbacks: { label: ctx => ctx.raw.toLocaleString() + ' users' } },
          legend: { display: false },
        },
      },
    });
  }

  /**
   * Doughnut: Market capture rate
   */
  function renderCaptureGauge(result) {
    const id = 'chart-capture';
    destroyChart(id);

    const capture = parseFloat(result.market.captureRate);
    const remaining = 100 - capture;

    create(id, {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [capture, remaining],
          backgroundColor: [COLORS.green, COLORS.greyLight],
          borderColor: ['#1a1a2e', '#1a1a2e'],
          borderWidth: 3,
        }],
        labels: ['Legal', 'Illicit'],
      },
      options: {
        cutout: '70%',
        plugins: {
          legend: { display: false },
        },
      },
    });
  }

  /**
   * Line chart: Tax rate sweep → market capture
   */
  function renderTaxSweep(fixedParams) {
    const id = 'chart-tax-sweep';
    destroyChart(id);

    const rates = [];
    for (let i = 0; i <= 45; i += 3) rates.push(i);

    const sweepData = PolicyEngine.sweep('taxRate', rates, fixedParams);

    create(id, {
      type: 'line',
      data: {
        labels: rates.map(r => r + '%'),
        datasets: [{
          label: 'Market Capture',
          data: sweepData.map(d => parseFloat(d.result.market.captureRate)),
          borderColor: COLORS.green,
          backgroundColor: COLORS.greenLight,
          fill: true,
          tension: 0.3,
          pointRadius: 3,
        }, {
          label: 'Tax Revenue (€M)',
          data: sweepData.map(d => parseFloat(d.result.fiscal.taxRevenue)),
          borderColor: COLORS.blue,
          backgroundColor: COLORS.blueLight,
          fill: true,
          tension: 0.3,
          pointRadius: 3,
          yAxisID: 'y1',
        }],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            max: 80,
            title: { display: true, text: 'Market Capture (%)', color: '#b0b0b0' },
            ticks: { color: '#b0b0b0', callback: v => v + '%' },
            grid: { color: 'rgba(255,255,255,0.05)' },
          },
          y1: {
            position: 'right',
            beginAtZero: true,
            title: { display: true, text: 'Revenue (€M)', color: '#b0b0b0' },
            ticks: { color: '#b0b0b0', callback: v => '€' + v + 'M' },
            grid: { display: false },
          },
          x: {
            ticks: { color: '#b0b0b0' },
            grid: { display: false },
          },
        },
      },
    });
  }

  /**
   * Line chart: Possession limit sweep → outcomes
   */
  function renderPossessionSweep(fixedParams) {
    const id = 'chart-possession-sweep';
    destroyChart(id);

    const limits = [5, 10, 15, 20, 25, 30, 40, 50, 65, 80, 100];
    const sweepData = PolicyEngine.sweep('possessionLimit', limits, fixedParams);

    create(id, {
      type: 'line',
      data: {
        labels: limits.map(l => l + 'g'),
        datasets: [{
          label: 'Black Market Displacement',
          data: sweepData.map(d => parseFloat(d.result.market.displacementRate)),
          borderColor: COLORS.orange,
          backgroundColor: COLORS.orangeLight,
          fill: true,
          tension: 0.3,
          pointRadius: 3,
        }, {
          label: 'Health Index',
          data: sweepData.map(d => d.result.health.index),
          borderColor: COLORS.purple,
          backgroundColor: 'rgba(156, 39, 176, 0.1)',
          fill: true,
          tension: 0.3,
          pointRadius: 3,
        }],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
            title: { display: true, text: 'Score (0–100)', color: '#b0b0b0' },
            ticks: { color: '#b0b0b0' },
            grid: { color: 'rgba(255,255,255,0.05)' },
          },
          x: {
            ticks: { color: '#b0b0b0' },
            grid: { display: false },
          },
        },
      },
    });
  }

  /**
   * Radar chart: Health outcome breakdown
   */
  function renderHealthRadar(result) {
    const id = 'chart-health';
    destroyChart(id);

    create(id, {
      type: 'radar',
      data: {
        labels: ['Quality Control', 'Harm Reduction', 'Prevention Access', 'Youth Protection'],
        datasets: [{
          label: 'Health Score',
          data: [
            parseInt(result.health.qualityControl),
            parseInt(result.health.harmReduction),
            Math.min(20, (result.clubs.totalClubs / 7) * 4),
            Math.min(20, result.inputs.possessionLimit > 10 ? 10 : 20),
          ],
          backgroundColor: 'rgba(76, 175, 80, 0.2)',
          borderColor: COLORS.green,
          pointBackgroundColor: COLORS.green,
          pointBorderColor: '#fff',
          borderWidth: 2,
        }],
      },
      options: {
        scales: {
          r: {
            beginAtZero: true,
            max: 40,
            ticks: { color: '#b0b0b0', backdropColor: 'transparent', stepSize: 10 },
            pointLabels: { color: '#b0b0b0', font: { size: 10 } },
            grid: { color: 'rgba(255,255,255,0.1)' },
            angleLines: { color: 'rgba(255,255,255,0.1)' },
          },
        },
        plugins: { legend: { display: false } },
      },
    });
  }

  function destroyChart(id) {
    if (chartInstances[id]) {
      chartInstances[id].destroy();
      delete chartInstances[id];
    }
  }

  function renderAll(result) {
    destroyAll();
    renderMarketDistribution(result);
    renderCaptureGauge(result);
    renderTaxSweep(result.inputs);
    renderPossessionSweep(result.inputs);
    renderHealthRadar(result);
  }

  return { renderAll, destroyAll };
})();

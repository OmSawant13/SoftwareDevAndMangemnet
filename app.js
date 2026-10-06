/**
 * SalesLens — Unified Sales Reporting & SEPM Platform Logic
 * Handles interactive charts, role-based views, 4-tier data cleaning engine, and filter state.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Global App State
  const state = {
    currentRole: 'director',
    activeTab: 'tab-overview',
    theme: 'dark',
    filter: {
      dateRange: 'mtd',
      region: 'ALL',
      category: 'ALL'
    },
    charts: {}
  };

  // Sample Datasets for 9 Views
  const dataStore = {
    regions: [
      { id: 'North', name: 'North Zone', manager: 'Rajesh Sharma', target: 1200000, actual: 1245000, accounts: 420, growth: '+14.2%', aov: '$2,964' },
      { id: 'South', name: 'South Zone', manager: 'Ananya Nair', target: 1100000, actual: 1085000, accounts: 390, growth: '+9.8%', aov: '$2,782' },
      { id: 'West', name: 'West Zone', manager: 'Vikram Patel', target: 1300000, actual: 1320000, accounts: 460, growth: '+16.5%', aov: '$2,869' },
      { id: 'East', name: 'East Zone', manager: 'Debanjan Sen', target: 800000, actual: 698000, accounts: 280, growth: '+4.1%', aov: '$2,492' },
      { id: 'Central', name: 'Central Zone', manager: 'Pooja Verma', target: 600000, actual: 504400, accounts: 210, growth: '+6.3%', aov: '$2,401' }
    ],
    topProducts: [
      { rank: 1, sku: 'SKU-BEV-101', name: 'Sparkling Citrus Tonic 500ml', category: 'Beverages', revenue: 642000, margin: '34.2%' },
      { rank: 2, sku: 'SKU-FOO-204', name: 'Organic Almond Butter Crunch', category: 'Packaged Foods', revenue: 512000, margin: '41.0%' },
      { rank: 3, sku: 'SKU-DAI-309', name: 'Greek Artisanal Yogurt 200g', category: 'Dairy', revenue: 489000, margin: '28.5%' },
      { rank: 4, sku: 'SKU-PER-412', name: 'Botanical Moisture Shampoo 300ml', category: 'Personal Care', revenue: 421000, margin: '52.1%' },
      { rank: 5, sku: 'SKU-HOM-505', name: 'Eco Concentrated Laundry Gel', category: 'Home Care', revenue: 398000, margin: '38.0%' },
      { rank: 6, sku: 'SKU-BEV-108', name: 'Cold Brew Roast Coffee 250ml', category: 'Beverages', revenue: 365000, margin: '44.8%' },
      { rank: 7, sku: 'SKU-FOO-215', name: 'Multigrain Crisp Wafers 150g', category: 'Packaged Foods', revenue: 310000, margin: '31.2%' }
    ],
    bottomProducts: [
      { sku: 'SKU-BEV-199', name: 'Diet Herbal Soda 250ml', category: 'Beverages', revenue: 14200, shelfDays: 84, action: 'Bundle Discount 25%' },
      { sku: 'SKU-FOO-290', name: 'Dried Fig & Sesame Paste', category: 'Packaged Foods', revenue: 18500, shelfDays: 92, action: 'SKU Delist Candidate' },
      { sku: 'SKU-PER-488', name: 'Clay Facial Cleanser (Legacy)', category: 'Personal Care', revenue: 21000, shelfDays: 78, action: 'Repackage / Promo' },
      { sku: 'SKU-HOM-592', name: 'Pine Scent Floor Wax 500ml', category: 'Home Care', revenue: 24800, shelfDays: 65, action: 'Distributor Rebate' },
      { sku: 'SKU-DAI-380', name: 'Low-Fat Flavored Curd Cup', category: 'Dairy', revenue: 29100, shelfDays: 45, action: 'Short Shelf Clearance' }
    ],
    auditLogs: [
      { txId: 'TX-98421', date: '2026-10-02', amount: '$4,280.00', raw: '[NULL]', rule: 'Rule 2 (Postal 110001)', clean: 'North Zone', confidence: '99.4%' },
      { txId: 'TX-98422', date: '2026-10-02', amount: '$12,450.00', raw: '[NULL]', rule: 'Rule 3 (Customer Master)', clean: 'West Zone', confidence: '98.8%' },
      { txId: 'TX-98423', date: '2026-10-02', amount: '$1,890.00', raw: '[NULL]', rule: 'Rule 4 (Sales Rep Territory)', clean: 'South Zone', confidence: '95.0%' },
      { txId: 'TX-98424', date: '2026-10-02', amount: '$620.00', raw: '[NULL]', rule: 'Rule 5 (Unassigned Queue)', clean: 'Unassigned-Audit', confidence: 'Manual' },
      { txId: 'TX-98425', date: '2026-10-02', amount: '$8,940.00', raw: 'EAST', rule: 'Rule 1 (Direct Pass)', clean: 'East Zone', confidence: '100.0%' }
    ]
  };

  // Initialize UI
  initTabs();
  initCharts();
  populateTables();
  initSimulator();
  initFilters();
  initThemeAndExports();

  // Tab Navigation Handling
  function initTabs() {
    const navButtons = document.querySelectorAll('.sidebar .nav-item');
    navButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetTab = btn.getAttribute('data-tab');
        if (!targetTab) return;

        navButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        document.querySelectorAll('.tab-pane').forEach(pane => {
          pane.classList.remove('active');
        });

        const activePane = document.getElementById(targetTab);
        if (activePane) activePane.classList.add('active');

        state.activeTab = targetTab;

        // Resize charts on tab change
        setTimeout(() => {
          Object.values(state.charts).forEach(chart => {
            if (chart) chart.resize();
          });
        }, 100);
      });
    });
  }

  // Populate Tables
  function populateTables() {
    // Quota Table
    const quotaBody = document.getElementById('quotaTableBody');
    if (quotaBody) {
      quotaBody.innerHTML = '';
      dataStore.regions.forEach(r => {
        const variance = r.actual - r.target;
        const attainment = ((r.actual / r.target) * 100).toFixed(1);
        const isPositive = variance >= 0;
        const statusBadge = isPositive 
          ? `<span class="badge-pill bg-success"><i class="fa-solid fa-check"></i> On Target</span>`
          : `<span class="badge-pill bg-danger"><i class="fa-solid fa-arrow-down"></i> Under</span>`;

        const row = document.createElement('tr');
        row.innerHTML = `
          <td><strong>${r.name}</strong> (${r.manager})</td>
          <td>$${r.target.toLocaleString()}</td>
          <td><strong>$${r.actual.toLocaleString()}</strong></td>
          <td class="${isPositive ? 'text-success' : 'text-danger'} font-bold">
            ${isPositive ? '+' : ''}$${variance.toLocaleString()}
          </td>
          <td>
            <div class="d-flex align-center gap-2">
              <span class="font-bold">${attainment}%</span>
              <div class="progress-bar-container" style="width: 80px; height: 6px;">
                <div class="progress-bar" style="width: ${Math.min(attainment, 100)}%; background: ${isPositive ? 'var(--color-success)' : 'var(--color-danger)'};"></div>
              </div>
            </div>
          </td>
          <td>${statusBadge}</td>
        `;
        quotaBody.appendChild(row);
      });
    }

    // Top Products
    const topBody = document.getElementById('topProductsBody');
    if (topBody) {
      topBody.innerHTML = '';
      dataStore.topProducts.forEach(p => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td><span class="badge-mini font-bold">#${p.rank}</span></td>
          <td><strong>${p.sku}</strong><br><span class="text-xs text-muted">${p.name}</span></td>
          <td><span class="badge-mini">${p.category}</span></td>
          <td><strong>$${p.revenue.toLocaleString()}</strong></td>
          <td class="text-success font-bold">${p.margin}</td>
        `;
        topBody.appendChild(row);
      });
    }

    // Bottom Products
    const bottomBody = document.getElementById('bottomProductsBody');
    if (bottomBody) {
      bottomBody.innerHTML = '';
      dataStore.bottomProducts.forEach(p => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td><strong>${p.sku}</strong><br><span class="text-xs text-muted">${p.name}</span></td>
          <td><span class="badge-mini">${p.category}</span></td>
          <td>$${p.revenue.toLocaleString()}</td>
          <td class="text-warning font-bold">${p.shelfDays} Days</td>
          <td><span class="badge-pill bg-danger">${p.action}</span></td>
        `;
        bottomBody.appendChild(row);
      });
    }

    // Regional Matrix Table
    const matrixBody = document.getElementById('regionalMatrixBody');
    if (matrixBody) {
      matrixBody.innerHTML = '';
      dataStore.regions.forEach(r => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td><strong>${r.name}</strong></td>
          <td>${r.manager}</td>
          <td>${r.accounts} Distributors</td>
          <td><strong>$${r.actual.toLocaleString()}</strong></td>
          <td class="text-success font-bold">${r.growth}</td>
          <td>${r.aov}</td>
          <td><span class="badge-pill bg-primary">Tier 1 Core</span></td>
        `;
        matrixBody.appendChild(row);
      });
    }

    // Audit Log Table
    const auditBody = document.getElementById('auditLogTableBody');
    if (auditBody) {
      auditBody.innerHTML = '';
      dataStore.auditLogs.forEach(l => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td class="font-mono"><strong>${l.txId}</strong></td>
          <td>${l.date}</td>
          <td>${l.amount}</td>
          <td><span class="badge-mini text-danger">${l.raw}</span></td>
          <td><span class="font-mono text-sm">${l.rule}</span></td>
          <td><span class="badge-pill bg-success">${l.clean}</span></td>
          <td class="font-bold">${l.confidence}</td>
        `;
        auditBody.appendChild(row);
      });
    }
  }

  // Chart Initializations
  function initCharts() {
    // 1. Daily Sales vs Target Chart
    const dailyCtx = document.getElementById('dailySalesChart');
    if (dailyCtx) {
      state.charts.dailySales = new Chart(dailyCtx, {
        type: 'line',
        data: {
          labels: ['Oct 01', 'Oct 02', 'Oct 03', 'Oct 04', 'Oct 05', 'Oct 06', 'Oct 07', 'Oct 08', 'Oct 09', 'Oct 10', 'Oct 11', 'Oct 12', 'Oct 13', 'Oct 14', 'Oct 15'],
          datasets: [
            {
              label: 'Actual Daily Sales ($)',
              data: [154000, 168000, 149000, 172000, 185000, 162000, 190000, 178000, 195000, 210000, 189000, 205000, 220000, 215000, 230000],
              borderColor: '#6366f1',
              backgroundColor: 'rgba(99, 102, 241, 0.12)',
              fill: true,
              tension: 0.35,
              borderWidth: 3,
              pointBackgroundColor: '#6366f1'
            },
            {
              label: 'Pacing Target Line ($)',
              data: [160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000, 160000],
              borderColor: '#f59e0b',
              borderDash: [6, 6],
              fill: false,
              borderWidth: 2,
              pointRadius: 0
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { labels: { color: '#9ca3af', font: { family: 'Plus Jakarta Sans' } } }
          },
          scales: {
            x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } },
            y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } }
          }
        }
      });
    }

    // 2. Region Share Pie Chart
    const pieCtx = document.getElementById('regionPieChart');
    if (pieCtx) {
      state.charts.regionPie = new Chart(pieCtx, {
        type: 'doughnut',
        data: {
          labels: ['West Zone', 'North Zone', 'South Zone', 'East Zone', 'Central Zone'],
          datasets: [{
            data: [1320000, 1245000, 1085000, 698000, 504400],
            backgroundColor: ['#6366f1', '#3b82f6', '#10b981', '#f59e0b', '#ec4899'],
            borderWidth: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { color: '#9ca3af' } }
          },
          cutout: '70%'
        }
      });
    }

    // 3. Quota Bar Chart
    const quotaCtx = document.getElementById('quotaBarChart');
    if (quotaCtx) {
      state.charts.quotaBar = new Chart(quotaCtx, {
        type: 'bar',
        data: {
          labels: ['North', 'South', 'West', 'East', 'Central'],
          datasets: [
            {
              label: 'Target ($)',
              data: [1200000, 1100000, 1300000, 800000, 600000],
              backgroundColor: 'rgba(156, 163, 175, 0.3)',
              borderRadius: 6
            },
            {
              label: 'Actual Sales ($)',
              data: [1245000, 1085000, 1320000, 698000, 504400],
              backgroundColor: ['#10b981', '#f59e0b', '#10b981', '#ef4444', '#ef4444'],
              borderRadius: 6
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: '#9ca3af' } } },
          scales: {
            x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } },
            y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } }
          }
        }
      });
    }

    // 4. Regional Trend Area Chart
    const regTrendCtx = document.getElementById('regionalTrendChart');
    if (regTrendCtx) {
      state.charts.regTrend = new Chart(regTrendCtx, {
        type: 'line',
        data: {
          labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
          datasets: [
            { label: 'West', data: [980000, 1050000, 1150000, 1220000, 1280000, 1320000], borderColor: '#6366f1', tension: 0.3 },
            { label: 'North', data: [920000, 990000, 1060000, 1140000, 1190000, 1245000], borderColor: '#3b82f6', tension: 0.3 },
            { label: 'South', data: [880000, 930000, 980000, 1020000, 1050000, 1085000], borderColor: '#10b981', tension: 0.3 },
            { label: 'East', data: [610000, 630000, 650000, 670000, 680000, 698000], borderColor: '#f59e0b', tension: 0.3 },
            { label: 'Central', data: [420000, 440000, 460000, 480000, 490000, 504400], borderColor: '#ec4899', tension: 0.3 }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: '#9ca3af' } } },
          scales: {
            x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } },
            y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } }
          }
        }
      });
    }

    // 5. Category Pie Chart
    const catCtx = document.getElementById('categoryChart');
    if (catCtx) {
      state.charts.category = new Chart(catCtx, {
        type: 'pie',
        data: {
          labels: ['Beverages', 'Packaged Foods', 'Dairy Products', 'Personal Care', 'Home Care'],
          datasets: [{
            data: [1680000, 1240000, 890000, 620000, 422400],
            backgroundColor: ['#6366f1', '#3b82f6', '#10b981', '#ec4899', '#f59e0b']
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { position: 'bottom', labels: { color: '#9ca3af' } } }
        }
      });
    }

    // 6. Channel Bar Chart
    const chanCtx = document.getElementById('channelChart');
    if (chanCtx) {
      state.charts.channel = new Chart(chanCtx, {
        type: 'bar',
        data: {
          labels: ['Supermarket Chains', 'Wholesale Distributors', 'Local Retail / Kirana', 'E-Commerce Hubs'],
          datasets: [{
            label: 'Channel Revenue ($)',
            data: [2150000, 1420000, 890000, 392400],
            backgroundColor: '#3b82f6',
            borderRadius: 6
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { display: false } },
          scales: {
            x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } },
            y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9ca3af' } }
          }
        }
      });
    }
  }

  // 14% Missing Region Live Decision Simulator
  function initSimulator() {
    const samples = {
      postal: { raw: '[NULL / MISSING]', postal: '110001', cust: 'CUST-4091', rep: 'REP-NORTH-04' },
      customer: { raw: '[NULL / MISSING]', postal: '[INVALID]', cust: 'CUST-8821', rep: 'REP-WEST-09' },
      rep: { raw: '[NULL / MISSING]', postal: '[EMPTY]', cust: '[NEW_UNREGISTERED]', rep: 'REP-SOUTH-02' },
      orphan: { raw: '[NULL / MISSING]', postal: '[EMPTY]', cust: '[EMPTY]', rep: '[UNASSIGNED]' }
    };

    document.querySelectorAll('.sample-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const type = btn.getAttribute('data-sample');
        if (!samples[type]) return;

        document.getElementById('simRawRegion').value = samples[type].raw;
        document.getElementById('simPostal').value = samples[type].postal;
        document.getElementById('simCustId').value = samples[type].cust;
        document.getElementById('simRepId').value = samples[type].rep;

        runSimulation();
      });
    });

    const runBtn = document.getElementById('runSimBtn');
    if (runBtn) {
      runBtn.addEventListener('click', runSimulation);
    }

    function runSimulation() {
      const raw = document.getElementById('simRawRegion').value.trim();
      const postal = document.getElementById('simPostal').value.trim();
      const cust = document.getElementById('simCustId').value.trim();
      const rep = document.getElementById('simRepId').value.trim();

      const badge = document.getElementById('simStatusBadge');
      const ruleText = document.getElementById('simRuleApplied');
      const details = document.getElementById('simResultDetails');

      // Rule 1: Raw Region Present
      if (raw !== '[NULL / MISSING]' && raw !== '[NULL]' && raw !== '' && raw !== '[EMPTY]') {
        badge.className = 'badge-pill bg-success';
        badge.innerHTML = '<i class="fa-solid fa-check"></i> Resolved Direct (Native)';
        ruleText.innerText = 'Rule 1: Direct Raw Value Pass-Through';
        details.innerHTML = `<strong>Outcome:</strong> Assigned directly to <code>${raw}</code>.<br><span class="text-xs text-muted">Confidence: 100% | No transformation required.</span>`;
        return;
      }

      // Rule 2: Postal Code Mapping
      if (postal === '110001' || postal === '110002') {
        badge.className = 'badge-pill bg-success';
        badge.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles"></i> Cleaned via Postal Directory';
        ruleText.innerText = 'Rule 2: Postal-to-Region Lookup Hierarchy';
        details.innerHTML = `<strong>Hierarchy Evaluation:</strong> Missing region detected (14% data issue).<br>
          &rarr; Priority 1: Postal <code>${postal}</code> resolved to <strong>North Zone</strong>.<br>
          <span class="text-xs text-success font-bold">&check; Audit log recorded. Confidence: 99.4%</span>`;
        return;
      }

      // Rule 3: Customer Master Lookup
      if (cust === 'CUST-8821' || cust === 'CUST-4091') {
        badge.className = 'badge-pill bg-primary';
        badge.innerHTML = '<i class="fa-solid fa-address-card"></i> Cleaned via Customer Master';
        ruleText.innerText = 'Rule 3: Customer Master Registration Lookup';
        details.innerHTML = `<strong>Hierarchy Evaluation:</strong> Postal invalid/missing.<br>
          &rarr; Priority 2: Customer ID <code>${cust}</code> matched to registered headquarters in <strong>West Zone</strong>.<br>
          <span class="text-xs text-primary font-bold">&check; Audit log recorded. Confidence: 98.8%</span>`;
        return;
      }

      // Rule 4: Sales Rep Territory
      if (rep && rep !== '[UNASSIGNED]' && rep.includes('REP-')) {
        const assignedZone = rep.includes('SOUTH') ? 'South Zone' : 'Central Zone';
        badge.className = 'badge-pill bg-warning';
        badge.innerHTML = '<i class="fa-solid fa-user-tie"></i> Cleaned via Sales Rep Territory';
        ruleText.innerText = 'Rule 4: Sales Rep Territory Mapping';
        details.innerHTML = `<strong>Hierarchy Evaluation:</strong> Postal and Customer profile unindexed.<br>
          &rarr; Priority 3: Assigned through Sales Rep territory <code>${rep}</code> to <strong>${assignedZone}</strong>.<br>
          <span class="text-xs text-warning font-bold">&check; Audit log recorded. Confidence: 95.0%</span>`;
        return;
      }

      // Fallback: Rule 5
      badge.className = 'badge-pill bg-danger';
      badge.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Sent to Unassigned Audit Queue';
      ruleText.innerText = 'Rule 5: True Orphan Fallback to Exception Queue';
      details.innerHTML = `<strong>Hierarchy Evaluation:</strong> All 3 priority lookups failed.<br>
        &rarr; Fallback: Tagged as <strong>Unassigned-Audit</strong> (0.3% of total data).<br>
        <span class="text-xs text-danger font-bold">&check; Revenue included in National Totals without distorting regional quotas.</span>`;
    }
  }

  // Role Switcher & Filtering
  function initFilters() {
    const roleSelector = document.getElementById('roleSelector');
    if (roleSelector) {
      roleSelector.addEventListener('change', (e) => {
        state.currentRole = e.target.value;
        applyRoleRestrictions();
      });
    }

    const regionFilter = document.getElementById('regionFilter');
    const applyBtn = document.getElementById('applyFiltersBtn');
    const resetBtn = document.getElementById('resetFiltersBtn');

    if (applyBtn) {
      applyBtn.addEventListener('click', () => {
        const selectedRegion = regionFilter.value;
        filterDashboardByRegion(selectedRegion);
      });
    }

    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        regionFilter.value = 'ALL';
        filterDashboardByRegion('ALL');
      });
    }

    function applyRoleRestrictions() {
      const regionSelect = document.getElementById('regionFilter');
      if (state.currentRole === 'manager_north') {
        regionSelect.value = 'North';
        regionSelect.disabled = true;
        filterDashboardByRegion('North');
        showToast('RBAC Active: Locked to North Zone Territory');
      } else if (state.currentRole === 'manager_south') {
        regionSelect.value = 'South';
        regionSelect.disabled = true;
        filterDashboardByRegion('South');
        showToast('RBAC Active: Locked to South Zone Territory');
      } else {
        regionSelect.disabled = false;
        regionSelect.value = 'ALL';
        filterDashboardByRegion('ALL');
        showToast(`Role switched: ${state.currentRole.toUpperCase()} (Full National Visibility)`);
      }
    }

    function filterDashboardByRegion(region) {
      const kpiRev = document.getElementById('kpiRevenue');
      const kpiAttain = document.getElementById('kpiAttainment');
      const kpiVol = document.getElementById('kpiVolume');

      if (region === 'North') {
        kpiRev.innerText = '$1,245,000';
        kpiAttain.innerText = '103.75%';
        kpiVol.innerText = '92,400';
      } else if (region === 'South') {
        kpiRev.innerText = '$1,085,000';
        kpiAttain.innerText = '98.63%';
        kpiVol.innerText = '79,500';
      } else if (region === 'West') {
        kpiRev.innerText = '$1,320,000';
        kpiAttain.innerText = '101.53%';
        kpiVol.innerText = '98,200';
      } else if (region === 'East') {
        kpiRev.innerText = '$698,000';
        kpiAttain.innerText = '87.25%';
        kpiVol.innerText = '46,100';
      } else if (region === 'Central') {
        kpiRev.innerText = '$504,400';
        kpiAttain.innerText = '84.06%';
        kpiVol.innerText = '32,720';
      } else {
        kpiRev.innerText = '$4,852,400';
        kpiAttain.innerText = '97.05%';
        kpiVol.innerText = '348,920';
      }
    }
  }

  // Theme & Export
  function initThemeAndExports() {
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        document.body.classList.toggle('theme-light');
        const isLight = document.body.classList.contains('theme-light');
        themeBtn.innerHTML = isLight ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
      });
    }

    const exportBtn = document.getElementById('exportBriefingBtn');
    if (exportBtn) {
      exportBtn.addEventListener('click', () => {
        window.print();
      });
    }
  }

  function showToast(message) {
    const existing = document.getElementById('toastNotification');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'toastNotification';
    toast.style.position = 'fixed';
    toast.style.bottom = '20px';
    toast.style.right = '20px';
    toast.style.background = 'linear-gradient(135deg, #6366f1, #4f46e5)';
    toast.style.color = '#fff';
    toast.style.padding = '0.75rem 1.25rem';
    toast.style.borderRadius = '8px';
    toast.style.boxShadow = '0 8px 24px rgba(0,0,0,0.4)';
    toast.style.fontSize = '0.85rem';
    toast.style.fontWeight = '600';
    toast.style.zIndex = '9999';
    toast.style.animation = 'fadeIn 0.3s ease';
    toast.innerHTML = `<i class="fa-solid fa-bell mr-2"></i> ${message}`;

    document.body.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      setTimeout(() => toast.remove(), 300);
    }, 3000);
  }
});

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function main() {
  const screenshotsDir = '/Users/omsawant/Desktop/Software!/screenshots';
  if (!fs.existsSync(screenshotsDir)) {
    fs.mkdirSync(screenshotsDir, { recursive: true });
  }

  console.log('Launching headless browser...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900, deviceScaleFactor: 2 });

  const htmlPath = 'file:///Users/omsawant/Desktop/Software!/index.html';
  console.log(`Navigating to ${htmlPath}...`);
  await page.goto(htmlPath, { waitUntil: 'networkidle0' });

  // Helper to wait
  const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  // List of tabs to capture
  const tabs = [
    { tab: 'tab-overview', name: '01_executive_daily_pulse.png', label: 'View 1: Executive Daily Pulse' },
    { tab: 'tab-quota', name: '02_target_vs_actual_quotas.png', label: 'View 2: Target vs Actual Quotas' },
    { tab: 'tab-products', name: '03_top_and_bottom_skus.png', label: 'Views 3 & 4: Top 20 & Bottom 10 SKUs' },
    { tab: 'tab-regions', name: '04_regional_matrix_and_drill.png', label: 'Views 5 & 6: Regional Matrix & Territory Drill' },
    { tab: 'tab-categories', name: '05_category_and_channels.png', label: 'Views 7 & 8: Category Mix & Distributor Channels' },
    { tab: 'tab-data-quality', name: '06_data_cleaning_and_audit.png', label: 'View 9: 14% Data Cleaning Simulator & Audit Queue' },
    { tab: 'tab-srs', name: '10_sepm_srs_view.png', label: 'SEPM Deliverable 1: IEEE 830 SRS & MoSCoW' },
    { tab: 'tab-uml', name: '11_sepm_uml_view.png', label: 'SEPM Deliverable 2: UML Architecture Package' },
    { tab: 'tab-cpm', name: '12_sepm_cpm_view.png', label: 'SEPM Deliverable 3: CPM Schedule & Gantt' },
    { tab: 'tab-estimation', name: '13_sepm_estimation_view.png', label: 'SEPM Deliverable 4: Mathematical Estimation Sheet' },
    { tab: 'tab-testing', name: '14_sepm_testing_view.png', label: 'SEPM Deliverable 5: Test Plan, BVA & DRE' },
    { tab: 'tab-risk', name: '15_sepm_risk_view.png', label: 'SEPM Deliverable 6: Risk Register & RMMM' },
  ];

  for (const item of tabs) {
    console.log(`Capturing ${item.label}...`);
    await page.evaluate((tabId) => {
      const btn = document.querySelector(`.sidebar .nav-item[data-tab="${tabId}"]`);
      if (btn) btn.click();
    }, item.tab);

    await wait(600); // Allow Chart.js animation & DOM update

    const savePath = path.join(screenshotsDir, item.name);
    await page.screenshot({ path: savePath, fullPage: false });
    console.log(`Saved screenshot: ${savePath}`);
  }

  // Also capture RBAC simulation for Regional Manager (North)
  console.log('Capturing RBAC Simulation (North Regional Manager)...');
  await page.evaluate(() => {
    const selector = document.getElementById('roleSelector');
    if (selector) {
      selector.value = 'manager_north';
      selector.dispatchEvent(new Event('change'));
    }
    const btn = document.querySelector('.sidebar .nav-item[data-tab="tab-overview"]');
    if (btn) btn.click();
  });
  await wait(600);
  await page.screenshot({ path: path.join(screenshotsDir, '07_rbac_north_manager_view.png'), fullPage: false });

  // Capture RBAC simulation for Data Analyst
  console.log('Capturing RBAC Simulation (Data Analyst)...');
  await page.evaluate(() => {
    const selector = document.getElementById('roleSelector');
    if (selector) {
      selector.value = 'analyst';
      selector.dispatchEvent(new Event('change'));
    }
    const btn = document.querySelector('.sidebar .nav-item[data-tab="tab-data-quality"]');
    if (btn) btn.click();
  });
  await wait(600);
  await page.screenshot({ path: path.join(screenshotsDir, '09_rbac_data_analyst_view.png'), fullPage: false });

  await browser.close();
  console.log('All UI screenshots successfully captured!');
}

main().catch(err => {
  console.error('Error during screenshot capture:', err);
  process.exit(1);
});

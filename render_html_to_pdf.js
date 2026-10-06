const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function renderHtmlToPdf() {
  console.log('Launching Puppeteer for HTML-to-PDF generation...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files']
  });

  const page = await browser.newPage();
  const htmlFile = 'file:///Users/omsawant/Desktop/Software!/saleslens_ui_and_sepm_master_showcase.html';
  
  console.log(`Loading HTML document: ${htmlFile}`);
  await page.goto(htmlFile, { waitUntil: 'networkidle0' });

  // Wait for web fonts and images to load completely
  await page.evaluateHandle('document.fonts.ready');

  const pdfPath1 = '/Users/omsawant/Desktop/Software!/SalesLens_Complete_UI_Walkthrough.pdf';
  const pdfPath2 = '/Users/omsawant/Desktop/Software!/pdf_deliverables/SalesLens_Complete_UI_Walkthrough.pdf';

  console.log(`Rendering PDF: ${pdfPath1}`);
  await page.pdf({
    path: pdfPath1,
    format: 'A4',
    printBackground: true,
    margin: {
      top: '10mm',
      bottom: '10mm',
      left: '12mm',
      right: '12mm'
    }
  });

  // Copy to deliverables folder as well
  fs.copyFileSync(pdfPath1, pdfPath2);
  console.log(`Saved copy to: ${pdfPath2}`);

  await browser.close();
  console.log('HTML-to-PDF rendering finished successfully!');
}

renderHtmlToPdf().catch(err => {
  console.error('Error rendering HTML to PDF:', err);
  process.exit(1);
});

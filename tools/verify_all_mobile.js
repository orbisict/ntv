const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 375, height: 812, isMobile: true });
  await page.goto('http://127.0.0.1:5500/index.html', { waitUntil: 'networkidle0' });

  // 1. Pillar cards
  const pillarGrid = await page.$('.pillars-grid') || await page.$('.pillar-card');
  if (pillarGrid) {
    await pillarGrid.screenshot({ path: 'C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/test_pillar_grid.png' });
  }

  // 2. Timeline filter click
  const filterBtn = await page.$('.agenda-filter-btn:nth-child(2)');
  if (filterBtn) {
    await filterBtn.click();
    await new Promise(r => setTimeout(r, 400));
  }
  const timelineNode = await page.$('.timeline-node');
  if (timelineNode) {
    await timelineNode.screenshot({ path: 'C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/test_timeline_node.png' });
  }

  // 3. Cost legend
  const costCard = await page.$('.finance-overview-card');
  if (costCard) {
    await costCard.screenshot({ path: 'C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/test_cost_legend.png' });
  }

  // 4. Budget table
  const tableWrap = await page.$('.budget-table-wrap');
  if (tableWrap) {
    await tableWrap.screenshot({ path: 'C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/test_budget_table.png' });
  }

  // 5. Appendix tabs
  const appTabs = await page.$('.appendix-tabs');
  if (appTabs) {
    await appTabs.screenshot({ path: 'C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/test_appendix_tabs.png' });
  }

  // 6. VIP Ticket
  const ticket = await page.$('.live-ticket-card');
  if (ticket) {
    await ticket.screenshot({ path: 'C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/test_ticket_mobile.png' });
  }

  console.log('Mobile screenshots captured successfully!');
  await browser.close();
})();

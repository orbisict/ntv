const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const filePath = 'http://127.0.0.1:5500/index.html';
  const tmpDir = path.resolve(__dirname, '../.chrome_verify_tmp_' + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=9333',
    '--window-size=375,812',
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch('http://127.0.0.1:9333/json');
    const tabs = await listRes.json();
    const targetTab = tabs.find(t => t.type === 'page' && !t.url.startsWith('chrome-extension')) || tabs[0];
    const wsUrl = targetTab.webSocketDebuggerUrl;

    const ws = new WebSocket(wsUrl);

    let id = 1;
    const pending = new Map();
    ws.onmessage = e => {
      const d = JSON.parse(e.data);
      if (d.id && pending.has(d.id)) {
        pending.get(d.id)(d.result);
        pending.delete(d.id);
      }
    };
    await new Promise(r => ws.onopen = r);

    const call = (method, params = {}) => new Promise(resolve => {
      const curId = id++;
      pending.set(curId, resolve);
      ws.send(JSON.stringify({ id: curId, method, params }));
    });

    await call('Page.enable');
    await call('Runtime.enable');
    await call('Emulation.setDeviceMetricsOverride', {
      width: 375,
      height: 812,
      deviceScaleFactor: 2,
      mobile: true
    });

    await sleep(600);

    const evalJs = async (expr) => {
      const r = await call('Runtime.evaluate', { 
        expression: `(() => {
          try {
            ${expr}
          } catch(e) {
            return { error: e.toString(), stack: e.stack };
          }
        })()`, 
        returnByValue: true 
      });
      return r?.result?.value;
    };

    // 1. Pillar Cards
    await evalJs(`
      const el = document.querySelector('.pillars-grid');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(400);
    const snapPillars = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_1_pillars.png', Buffer.from(snapPillars.data, 'base64'));
    console.log('Saved verify_fix_1_pillars.png');

    // 2. Timeline Filter Click & Badge stretch check
    const filterRes = await evalJs(`
      const btns = document.querySelectorAll('.agenda-filter-btn');
      if (btns.length > 1) {
        btns[1].click();
      }
      const node = document.querySelector('.timeline-node');
      const badge = node ? node.querySelector('.timeline-time-badge') : null;
      return {
        badgeHeight: badge ? badge.getBoundingClientRect().height : 0,
        nodeDisplay: node ? window.getComputedStyle(node).display : 'none'
      };
    `);
    console.log('2. Timeline Filter Test:', filterRes);
    await sleep(400);
    const snapTimeline = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_2_timeline.png', Buffer.from(snapTimeline.data, 'base64'));
    console.log('Saved verify_fix_2_timeline.png');

    // 3. Cost Breakdown Legend
    await evalJs(`
      const el = document.querySelector('.finance-overview-card');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(400);
    const snapCost = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_3_cost.png', Buffer.from(snapCost.data, 'base64'));
    console.log('Saved verify_fix_3_cost.png');

    // 4. Budget Table
    await evalJs(`
      const el = document.querySelector('.budget-table-wrap');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(400);
    const snapBudget = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_4_budget.png', Buffer.from(snapBudget.data, 'base64'));
    console.log('Saved verify_fix_4_budget.png');

    // 5. Appendix Tabs
    await evalJs(`
      const el = document.querySelector('.appendix-tabs');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(400);
    const snapApp = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_5_appendix.png', Buffer.from(snapApp.data, 'base64'));
    console.log('Saved verify_fix_5_appendix.png');

    // 6. Ticket
    await evalJs(`
      const el = document.getElementById('ticket') || document.querySelector('.live-ticket-card');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(400);
    const snapTicket = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_6_ticket.png', Buffer.from(snapTicket.data, 'base64'));
    console.log('Saved verify_fix_6_ticket.png');

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

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
    const ws = new WebSocket(targetTab.webSocketDebuggerUrl);

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
      const r = await call('Runtime.evaluate', { expression: expr, returnByValue: true });
      return r?.result?.value;
    };

    // 1. Sponsorship tier cards metrics
    const tierMetrics = await evalJs(`
      (() => {
        const grid = document.querySelector('.sponsor-tier-grid');
        const cards = Array.from(document.querySelectorAll('.sponsor-tier-card')).map((c, i) => {
          const r = c.getBoundingClientRect();
          return {
            index: i + 1,
            title: c.querySelector('.tier-badge')?.innerText,
            price: c.querySelector('.tier-price')?.innerText,
            left: Math.round(r.left),
            right: Math.round(r.right),
            width: Math.round(r.width),
            overflows: r.right > 375
          };
        });
        const gridR = grid ? grid.getBoundingClientRect() : null;
        return {
          gridWidth: gridR ? Math.round(gridR.width) : 0,
          cards
        };
      })()
    `);
    console.log('1. Sponsorship Tier Cards:', JSON.stringify(tierMetrics, null, 2));

    // Scroll to Sponsorship Tiers & Snap
    await evalJs(`
      (() => {
        const el = document.querySelector('.sponsor-tiers-container');
        if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      })()
    `);
    await sleep(500);
    const snapTiers = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_tiers_1col.png', Buffer.from(snapTiers.data, 'base64'));
    console.log('Saved verify_fix_tiers_1col.png');

    // 2. Table Footer Status Bar metrics & Snap
    const footerMetrics = await evalJs(`
      (() => {
        const footer = document.querySelector('.table-footer-status');
        const countTag = footer?.querySelector('.status-count-tag');
        const currTag = footer?.querySelector('.status-currency-tag');
        const cr = countTag ? countTag.getBoundingClientRect() : null;
        const ur = currTag ? currTag.getBoundingClientRect() : null;
        return {
          footerWidth: footer ? Math.round(footer.getBoundingClientRect().width) : 0,
          countText: countTag?.innerText,
          countRect: cr ? { top: Math.round(cr.top), bottom: Math.round(cr.bottom) } : null,
          currText: currTag?.innerText,
          currRect: ur ? { top: Math.round(ur.top), bottom: Math.round(ur.bottom) } : null,
          isStackedWithGap: (ur && cr) ? ur.top >= cr.bottom : false
        };
      })()
    `);
    console.log('2. Table Footer Status:', JSON.stringify(footerMetrics, null, 2));

    // Scroll to Table Footer & Snap
    await evalJs(`
      (() => {
        const el = document.querySelector('.table-footer-status');
        if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      })()
    `);
    await sleep(500);
    const snapFooter = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_table_footer.png', Buffer.from(snapFooter.data, 'base64'));
    console.log('Saved verify_fix_table_footer.png');

    // 3. Mobile Fixed Header Test at various scroll positions
    const scrollTest = await evalJs(`
      (() => {
        const header = document.querySelector('.site-header');
        const initial = {
          position: window.getComputedStyle(header).position,
          top: window.getComputedStyle(header).top,
          rectTop: Math.round(header.getBoundingClientRect().top),
          height: Math.round(header.getBoundingClientRect().height)
        };

        window.scrollTo(0, 2500);
        const scrolled = {
          rectTop: Math.round(header.getBoundingClientRect().top),
          height: Math.round(header.getBoundingClientRect().height),
          visible: header.getBoundingClientRect().top === 0
        };

        return { initial, scrolled };
      })()
    `);
    console.log('3. Mobile Header Fixed Test:', JSON.stringify(scrollTest, null, 2));

    await sleep(500);
    const snapHeader = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_fix_mobile_header_scrolled.png', Buffer.from(snapHeader.data, 'base64'));
    console.log('Saved verify_fix_mobile_header_scrolled.png');

    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

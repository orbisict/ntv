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

    await sleep(500);

    const evalJs = async (expr) => {
      const r = await call('Runtime.evaluate', { expression: expr, returnByValue: true });
      return r?.result?.value;
    };

    const sections = [
      { name: 'agenda', sel: '#agenda' },
      { name: 'cost', sel: '.budget-legend-grid' },
      { name: 'table', sel: '#budget-master-table' },
      { name: 'appendix', sel: '.appendix-nav-pill-group' },
      { name: 'ticket', sel: '.live-ticket-card' }
    ];

    for (const sec of sections) {
      const res = await evalJs(`
        (() => {
          const el = document.querySelector('${sec.sel}');
          if (!el) return { found: false };
          const rect = el.getBoundingClientRect();
          window.scrollTo(0, window.scrollY + rect.top - 80);
          return { found: true, y: window.scrollY, top: rect.top };
        })()
      `);
      console.log('Section', sec.name, res);
      await sleep(500);
      const snap = await call('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(`C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_section_${sec.name}.png`, Buffer.from(snap.data, 'base64'));
    }

    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

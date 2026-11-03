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

    const res = await call('Runtime.evaluate', {
      expression: `(() => {
        const grid = document.querySelector('.sponsor-tier-grid');
        const cards = Array.from(document.querySelectorAll('.sponsor-tier-card')).map(c => {
          const r = c.getBoundingClientRect();
          return { left: Math.round(r.left), right: Math.round(r.right), width: Math.round(r.width) };
        });
        const gridR = grid ? grid.getBoundingClientRect() : null;
        return {
          grid: gridR ? { left: Math.round(gridR.left), right: Math.round(gridR.right), width: Math.round(gridR.width) } : null,
          cards
        };
      })()`,
      returnByValue: true
    });

    console.log('Sponsor tiers metrics:', res?.result?.value);

    // Also inspect tab-nav-wrapper metrics
    const tabWrappers = await call('Runtime.evaluate', {
      expression: `(() => {
        return Array.from(document.querySelectorAll('.tab-nav-wrapper')).map(w => {
          const r = w.getBoundingClientRect();
          const btns = Array.from(w.querySelectorAll('button')).map(b => {
            const br = b.getBoundingClientRect();
            return { text: b.innerText, left: Math.round(br.left), right: Math.round(br.right), width: Math.round(br.width) };
          });
          return {
            left: Math.round(r.left),
            right: Math.round(r.right),
            width: Math.round(r.width),
            scrollWidth: w.scrollWidth,
            btns
          };
        });
      })()`,
      returnByValue: true
    });
    console.log('Tab wrappers metrics:', JSON.stringify(tabWrappers?.result?.value, null, 2));

    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const filePath = 'http://127.0.0.1:5500/index.html';
  const tmpDir = path.resolve(__dirname, '../.chrome_tl_tmp_' + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=9344',
    '--window-size=375,812',
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch('http://127.0.0.1:9344/json');
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

    await sleep(400);

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

    const tlCard = await evalJs(`
      const stream = document.querySelector('.timeline-stream');
      const node = stream.querySelector('.timeline-node');
      const card = node.querySelector('.timeline-card');
      const badge = node.querySelector('.timeline-time-badge');
      const pt = node.querySelector('.timeline-point');
      
      const sr = stream.getBoundingClientRect();
      const cr = card.getBoundingClientRect();
      const br = badge.getBoundingClientRect();
      const pr = pt.getBoundingClientRect();

      return {
        stream: { left: Math.round(sr.left), width: Math.round(sr.width) },
        badge: { left: Math.round(br.left), width: Math.round(br.width), text: badge.innerText.trim() },
        point: { left: Math.round(pr.left) },
        card: { left: Math.round(cr.left), right: Math.round(cr.right), width: Math.round(cr.width) }
      };
    `);
    console.log('Timeline dimensions on mobile:', JSON.stringify(tlCard, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

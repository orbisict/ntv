const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const filePath = 'http://127.0.0.1:5500/index.html';
  const tmpDir = path.resolve(__dirname, '../.chrome_overflow_tmp_' + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=9288',
    '--window-size=375,812',
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch('http://127.0.0.1:9288/json');
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

    // Temporarily hide mobile drawer to see what else overflows
    const otherOverflows = await evalJs(`
      const drawer = document.getElementById('mobile-nav-drawer');
      if (drawer) drawer.style.display = 'none';

      const vw = window.innerWidth;
      const elements = Array.from(document.querySelectorAll('*'));
      const overflowing = [];

      for (const el of elements) {
        if (el.offsetParent === null) continue;
        const rect = el.getBoundingClientRect();
        if (rect.right > vw + 1) {
          overflowing.push({
            tag: el.tagName.toLowerCase(),
            id: el.id,
            className: (el.className && el.className.toString) ? el.className.toString() : '',
            right: Math.round(rect.right),
            width: Math.round(rect.width),
            text: el.innerText ? el.innerText.trim().substring(0, 30) : ''
          });
        }
      }

      return {
        vw,
        docWidth: document.documentElement.scrollWidth,
        bodyWidth: document.body.scrollWidth,
        overflowCount: overflowing.length,
        overflowing: overflowing.slice(0, 20)
      };
    `);

    console.log('Without drawer report:', JSON.stringify(otherOverflows, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

const { spawn } = require('child_process');
const fs = require('fs');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9231',
    '--window-size=375,812',
    'http://127.0.0.1:5500/index.html'
  ]);

  await sleep(2000);

  try {
    const res = await (await fetch('http://127.0.0.1:9231/json')).json();
    const ws = new WebSocket(res[0].webSocketDebuggerUrl);

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
      const r = await call('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true });
      return r?.result?.value;
    };

    // Click mobile menu button
    await evalJs(`
      const btn = document.getElementById('mobile-menu-btn');
      if (btn) btn.click();
    `);
    await sleep(500);

    const { data } = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('verify_mobile_drawer_open.png', Buffer.from(data, 'base64'));
    console.log('Saved verify_mobile_drawer_open.png');

    ws.close();
  } catch (err) {
    console.error("Error:", err);
  } finally {
    chrome.kill();
  }
}

main();

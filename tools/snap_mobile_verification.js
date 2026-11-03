const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const filePath = 'http://127.0.0.1:5500/index.html';
  const tmpDir = path.resolve(__dirname, '../.chrome_snap_tmp_' + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=9290',
    '--window-size=375,812',
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch('http://127.0.0.1:9290/json');
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

    // 1. Capture Hero at 375px
    await sleep(600);
    const snap1 = await call('Page.captureScreenshot', { format: 'png' });
    const heroSnapPath = path.resolve('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/mobile_hero_fixed.png');
    fs.writeFileSync(heroSnapPath, Buffer.from(snap1.data, 'base64'));
    console.log('Saved mobile_hero_fixed.png');

    // 2. Open drawer and capture
    await call('Runtime.evaluate', { 
      expression: `(() => {
        const btn = document.getElementById('mobile-menu-btn');
        if (btn) btn.click();
      })()` 
    });
    await sleep(600);
    const snap2 = await call('Page.captureScreenshot', { format: 'png' });
    const drawerSnapPath = path.resolve('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/mobile_drawer_fixed.png');
    fs.writeFileSync(drawerSnapPath, Buffer.from(snap2.data, 'base64'));
    console.log('Saved mobile_drawer_fixed.png');

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

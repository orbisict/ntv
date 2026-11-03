const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function captureDevice(device) {
  const filePath = 'http://127.0.0.1:5500/index.html';
  const tmpDir = path.resolve(__dirname, `../.chrome_dev_${device.name}_` + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=' + device.port,
    `--window-size=${device.width},${device.height}`,
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch(`http://127.0.0.1:${device.port}/json`);
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
      width: device.width,
      height: device.height,
      deviceScaleFactor: 2,
      mobile: true
    });

    await sleep(600);

    // 1. Capture Hero
    const heroSnap = await call('Page.captureScreenshot', { format: 'png' });
    const heroPath = path.resolve(`C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/${device.name}_hero.png`);
    fs.writeFileSync(heroPath, Buffer.from(heroSnap.data, 'base64'));
    console.log(`Saved ${device.name}_hero.png`);

    // 2. Open drawer
    await call('Runtime.evaluate', { 
      expression: `(() => {
        const btn = document.getElementById('mobile-menu-btn');
        if (btn) btn.click();
      })()` 
    });
    await sleep(600);
    const drawerSnap = await call('Page.captureScreenshot', { format: 'png' });
    const drawerPath = path.resolve(`C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/${device.name}_drawer.png`);
    fs.writeFileSync(drawerPath, Buffer.from(drawerSnap.data, 'base64'));
    console.log(`Saved ${device.name}_drawer.png`);

    ws.close();
  } catch (err) {
    console.error(`Error on ${device.name}:`, err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

async function main() {
  await captureDevice({ name: 'iphone_375', width: 375, height: 812, port: 9311 });
  await captureDevice({ name: 'android_360', width: 360, height: 780, port: 9312 });
}

main();

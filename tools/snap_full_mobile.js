const { spawn } = require('child_process');
const fs = require('fs');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9227',
    '--window-size=375,812',
    'http://127.0.0.1:5500/index.html'
  ]);

  await sleep(2500);

  try {
    const res = await (await fetch('http://127.0.0.1:9227/json')).json();
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
    await call('DOM.enable');

    // Get layout metrics
    const metrics = await call('Page.getLayoutMetrics');
    const width = 375;
    const height = Math.min(Math.round(metrics.cssContentSize.height), 30000);
    console.log(`Mobile full page dimensions: ${width} x ${height}`);

    await call('Emulation.setDeviceMetricsOverride', {
      width: width,
      height: height,
      deviceScaleFactor: 1,
      mobile: true
    });
    await sleep(800);

    const { data } = await call('Page.captureScreenshot', {
      format: 'png',
      captureBeyondViewport: true
    });
    fs.writeFileSync('mobile_full_375.png', Buffer.from(data, 'base64'));
    console.log('Saved mobile_full_375.png, file size:', fs.statSync('mobile_full_375.png').size);

    ws.close();
  } catch (err) {
    console.error("Error:", err);
  } finally {
    chrome.kill();
  }
}

main();

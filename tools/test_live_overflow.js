const { spawn } = require('child_process');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function testViewport(w, h) {
  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    `--remote-debugging-port=9230`,
    `--window-size=${w},${h}`,
    'http://127.0.0.1:5500/index.html'
  ]);

  await sleep(2000);

  try {
    const res = await (await fetch('http://127.0.0.1:9230/json')).json();
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

    const result = await evalJs(`
      (() => {
        const winW = window.innerWidth;
        const docW = document.documentElement.scrollWidth;
        const bodyW = document.body.scrollWidth;
        const offenders = [];
        for (const el of document.querySelectorAll('*')) {
          const rect = el.getBoundingClientRect();
          if (rect.right > winW + 2) {
            offenders.push({
              tag: el.tagName,
              cls: el.className ? el.className.toString().slice(0, 30) : '',
              right: Math.round(rect.right),
              width: Math.round(rect.width)
            });
          }
        }
        return {
          winW, docW, bodyW,
          hasHorizontalScroll: docW > winW || bodyW > winW,
          offenderCount: offenders.length,
          offenders: offenders.slice(0, 8)
        };
      })()
    `);

    console.log(`Viewport ${w}x${h}:`, JSON.stringify(result));
    ws.close();
  } catch (err) {
    console.error(`Error at ${w}x${h}:`, err.message);
  } finally {
    chrome.kill();
  }
}

async function main() {
  await testViewport(375, 812);
  await sleep(1000);
  await testViewport(414, 896);
  await sleep(1000);
  await testViewport(768, 1024);
  await sleep(1000);
  await testViewport(1024, 768);
}

main();

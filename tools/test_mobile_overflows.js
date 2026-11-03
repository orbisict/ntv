const { spawn } = require('child_process');
const fs = require('fs');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9226',
    '--window-size=375,812',
    'http://127.0.0.1:5500/index.html'
  ]);

  await sleep(2500);

  try {
    const res = await (await fetch('http://127.0.0.1:9226/json')).json();
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
      const r = await call('Runtime.evaluate', { expression: expr, returnByValue: true });
      return r?.result?.value;
    };

    console.log("Checking 375px mobile viewport...");

    const overflowInfo = await evalJs(`
      (() => {
        const docWidth = document.documentElement.scrollWidth;
        const winWidth = window.innerWidth;
        const overflows = [];
        const all = document.querySelectorAll('*');
        for (const el of all) {
          const rect = el.getBoundingClientRect();
          if (rect.right > winWidth + 1) {
            overflows.push({
              tag: el.tagName,
              id: el.id,
              className: el.className,
              right: rect.right,
              width: rect.width,
              text: el.textContent ? el.textContent.trim().slice(0, 30) : ''
            });
          }
        }
        return { docWidth, winWidth, hasHorizontalScroll: docWidth > winWidth, overflows: overflows.slice(0, 20) };
      })()
    `);

    console.log("Overflow Info:", JSON.stringify(overflowInfo, null, 2));

    // Also check tablet 768px
    await call('Emulation.setDeviceMetricsOverride', {
      width: 768,
      height: 1024,
      deviceScaleFactor: 1,
      mobile: false
    });
    await sleep(500);

    const tabletOverflow = await evalJs(`
      (() => {
        const docWidth = document.documentElement.scrollWidth;
        const winWidth = window.innerWidth;
        return { docWidth, winWidth, hasHorizontalScroll: docWidth > winWidth };
      })()
    `);
    console.log("Tablet 768px Info:", JSON.stringify(tabletOverflow, null, 2));

    // Capture screenshots of sections on 375px
    await call('Emulation.setDeviceMetricsOverride', {
      width: 375,
      height: 812,
      deviceScaleFactor: 2,
      mobile: true
    });
    await sleep(500);

    async function snap(name) {
      const { data } = await call('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(name, Buffer.from(data, 'base64'));
      console.log('Saved', name);
    }

    await snap('check_mobile_hero.png');

    await evalJs('window.scrollTo(0, 800)');
    await sleep(400);
    await snap('check_mobile_s1.png');

    await evalJs('window.scrollTo(0, 1600)');
    await sleep(400);
    await snap('check_mobile_s2.png');

    await evalJs('window.scrollTo(0, 2800)');
    await sleep(400);
    await snap('check_mobile_agenda.png');

    await evalJs('window.scrollTo(0, 5000)');
    await sleep(400);
    await snap('check_mobile_budget.png');

    await evalJs('window.scrollTo(0, 8000)');
    await sleep(400);
    await snap('check_mobile_ticket.png');

    ws.close();
  } catch (err) {
    console.error("Error:", err);
  } finally {
    chrome.kill();
  }
}

main();

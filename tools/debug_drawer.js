const { spawn } = require('child_process');
const fs = require('fs');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9232',
    '--window-size=375,812',
    'http://127.0.0.1:5500/index.html'
  ]);

  await sleep(2500);

  try {
    const res = await (await fetch('http://127.0.0.1:9232/json')).json();
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

    // Click menu
    const info = await evalJs(`
      (() => {
        const btn = document.getElementById('mobile-menu-btn');
        btn.click();
        const drawer = document.getElementById('mobile-nav-drawer');
        const comp = window.getComputedStyle(drawer);
        const rect = drawer.getBoundingClientRect();
        
        const links = Array.from(drawer.querySelectorAll('a')).map(a => {
          const ac = window.getComputedStyle(a);
          return { text: a.innerText, color: ac.color, bg: ac.backgroundColor, display: ac.display, rect: a.getBoundingClientRect() };
        });

        return {
          drawerBg: comp.backgroundColor,
          drawerBackground: comp.background,
          drawerColor: comp.color,
          rect,
          linksCount: links.length,
          links: links.slice(0, 3)
        };
      })()
    `);

    console.log("Drawer Info:", JSON.stringify(info, null, 2));

    await sleep(400);
    const { data } = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('debug_drawer_screenshot.png', Buffer.from(data, 'base64'));
    console.log("Saved debug_drawer_screenshot.png");

    ws.close();
  } catch (err) {
    console.error("Error:", err);
  } finally {
    chrome.kill();
  }
}

main();

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const filePath = 'http://127.0.0.1:5500/index.html';
  console.log('Testing URL:', filePath);
  const tmpDir = path.resolve(__dirname, '../.chrome_tmp_' + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=9266',
    '--window-size=375,812',
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch('http://127.0.0.1:9266/json');
    const tabs = await listRes.json();
    console.log('Tabs:', tabs.map(t => ({ title: t.title, url: t.url, type: t.type })));
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

    const clickRes = await evalJs(`
      const btn = document.getElementById('mobile-menu-btn');
      if (!btn) return { error: 'mobile-menu-btn not found' };
      const btnRect = btn.getBoundingClientRect();
      const btnStyle = window.getComputedStyle(btn);
      
      // Let's trigger click
      btn.click();

      const drawer = document.getElementById('mobile-nav-drawer');
      const drawerRect = drawer.getBoundingClientRect();
      const drawerStyle = window.getComputedStyle(drawer);

      const linksBox = document.querySelector('.mobile-drawer-links');
      const linksBoxStyle = linksBox ? window.getComputedStyle(linksBox) : null;
      const linksBoxRect = linksBox ? linksBox.getBoundingClientRect() : null;

      const links = Array.from(document.querySelectorAll('.mobile-drawer-links a')).map(a => {
        const s = window.getComputedStyle(a);
        return {
          text: a.innerText.trim(),
          display: s.display,
          color: s.color,
          bg: s.backgroundColor,
          height: s.height,
          rect: a.getBoundingClientRect()
        };
      });

      return {
        url: window.location.href,
        btnDisplay: btnStyle.display,
        drawerClass: drawer.className,
        drawerRect,
        drawerBg: drawerStyle.backgroundColor,
        drawerBgImage: drawerStyle.backgroundImage,
        drawerColor: drawerStyle.color,
        linksBoxRect,
        linksBoxBg: linksBoxStyle ? linksBoxStyle.backgroundColor : null,
        linksCount: links.length,
        links: links.slice(0, 5)
      };
    `);

    console.log('Click Result:', JSON.stringify(clickRes, null, 2));

    await sleep(600);

    const { data } = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('test_mobile_drawer_snap.png', Buffer.from(data, 'base64'));
    console.log('Saved test_mobile_drawer_snap.png');

    ws.close();
  } catch (err) {
    console.error('Error in script:', err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

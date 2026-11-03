const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const filePath = 'http://127.0.0.1:5500/index.html';
  const tmpDir = path.resolve(__dirname, '../.chrome_hero_tmp_' + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=9299',
    '--window-size=375,812',
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch('http://127.0.0.1:9299/json');
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

    const heroReport = await evalJs(`
      const vw = window.innerWidth;
      const hero = document.querySelector('.hero-banner');
      const els = [
        'header.site-header',
        '.hero-banner',
        '.hero-banner .container',
        '.hero-widescreen-grid',
        '.hero-main-col',
        '.hero-badge-row',
        '.hero-partner-badge',
        '.hero-pill-badge',
        '.theme-title-grand',
        '.hero-theme-sub-line',
        '.theme-lotus-divider',
        '.hero-lead-desc',
        '.hero-meta-bar',
        '.hero-meta-item',
        '.hero-cta-group',
        '.hero-showcase-master-card',
        '.hero-stats-ribbon'
      ];

      const results = {};
      els.forEach(sel => {
        const el = document.querySelector(sel);
        if (!el) {
          results[sel] = 'NOT_FOUND';
          return;
        }
        const r = el.getBoundingClientRect();
        const s = window.getComputedStyle(el);
        results[sel] = {
          left: Math.round(r.left),
          right: Math.round(r.right),
          width: Math.round(r.width),
          paddingLeft: s.paddingLeft,
          paddingRight: s.paddingRight,
          marginLeft: s.marginLeft,
          marginRight: s.marginRight,
          overflow: s.overflow
        };
      });

      return {
        vw,
        scrollWidth: document.documentElement.scrollWidth,
        results
      };
    `);

    console.log('Hero Mobile Report:', JSON.stringify(heroReport, null, 2));

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

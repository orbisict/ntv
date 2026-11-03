const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const filePath = 'http://127.0.0.1:5500/index.html';
  const tmpDir = path.resolve(__dirname, '../.chrome_verify_tmp_' + Date.now());
  fs.mkdirSync(tmpDir, { recursive: true });

  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--user-data-dir=' + tmpDir,
    '--remote-debugging-port=9333',
    '--window-size=375,812',
    filePath
  ]);

  await sleep(2500);

  try {
    const listRes = await fetch('http://127.0.0.1:9333/json');
    const tabs = await listRes.json();
    const targetTab = tabs.find(t => t.type === 'page' && !t.url.startsWith('chrome-extension')) || tabs[0];
    const ws = new WebSocket(targetTab.webSocketDebuggerUrl);

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
      width: 375,
      height: 812,
      deviceScaleFactor: 2,
      mobile: true
    });

    await sleep(600);

    const evalJs = async (expr) => {
      const r = await call('Runtime.evaluate', { expression: expr, returnByValue: true });
      return r?.result?.value;
    };

    // Test 1: Click Phase-2 filter (08:40 - 10:05) exactly as user did
    const resPhase2 = await evalJs(`
      (() => {
        const btn = document.querySelector('.agenda-filter-btn[data-filter="phase-2"]');
        if (!btn) return { error: 'Button phase-2 not found' };
        btn.click();
        const allNodes = Array.from(document.querySelectorAll('.timeline-node'));
        const visibleNodes = allNodes.filter(n => n.getBoundingClientRect().height > 0);
        return {
          clicked: btn.innerText,
          totalNodes: allNodes.length,
          visibleCount: visibleNodes.length,
          visibleTimes: visibleNodes.map(n => n.querySelector('.timeline-time-badge')?.innerText)
        };
      })()
    `);
    console.log('Filter Phase-2 result:', resPhase2);

    // Scroll to Agenda and capture screenshot of filtered Phase-2
    await evalJs(`
      (() => {
        const el = document.getElementById('agenda');
        if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
      })()
    `);
    await sleep(500);
    const snap = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_agenda_filter_phase2.png', Buffer.from(snap.data, 'base64'));
    console.log('Saved verify_agenda_filter_phase2.png');

    // Test 2: Click Phase-1 filter (07:30 - 08:40)
    const resPhase1 = await evalJs(`
      (() => {
        const btn = document.querySelector('.agenda-filter-btn[data-filter="phase-1"]');
        btn.click();
        const visibleNodes = Array.from(document.querySelectorAll('.timeline-node')).filter(n => n.getBoundingClientRect().height > 0);
        return {
          clicked: btn.innerText,
          visibleCount: visibleNodes.length,
          visibleTimes: visibleNodes.map(n => n.querySelector('.timeline-time-badge')?.innerText)
        };
      })()
    `);
    console.log('Filter Phase-1 result:', resPhase1);

    // Test 3: Click All filter
    const resAll = await evalJs(`
      (() => {
        const btn = document.querySelector('.agenda-filter-btn[data-filter="all"]');
        btn.click();
        const visibleNodes = Array.from(document.querySelectorAll('.timeline-node')).filter(n => n.getBoundingClientRect().height > 0);
        return {
          clicked: btn.innerText,
          visibleCount: visibleNodes.length
        };
      })()
    `);
    console.log('Filter All result:', resAll);

    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

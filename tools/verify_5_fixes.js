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
      width: 375,
      height: 812,
      deviceScaleFactor: 2,
      mobile: true
    });

    await sleep(600);

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

    // 1. Inspect Agenda Controls position
    const agendaCheck = await evalJs(`
      const controls = document.querySelector('.agenda-controls');
      const firstBtn = controls.querySelector('button');
      const firstRect = firstBtn.getBoundingClientRect();
      const controlsRect = controls.getBoundingClientRect();
      return {
        controlsLeft: Math.round(controlsRect.left),
        controlsScrollLeft: controls.scrollLeft,
        firstBtnText: firstBtn.innerText,
        firstBtnLeft: Math.round(firstRect.left),
        firstBtnRight: Math.round(firstRect.right),
        firstBtnWidth: Math.round(firstRect.width)
      };
    `);
    console.log('1. Agenda Filter Check:', JSON.stringify(agendaCheck, null, 2));

    // 2. Inspect Finance Cards
    const financeCheck = await evalJs(`
      const cards = Array.from(document.querySelectorAll('.finance-kpi-card')).map(c => {
        const val = c.querySelector('.card-finance-value');
        const vr = val.getBoundingClientRect();
        return {
          text: val.innerText.trim(),
          width: Math.round(vr.width),
          height: Math.round(vr.height),
          cardWidth: Math.round(c.getBoundingClientRect().width)
        };
      });
      return cards;
    `);
    console.log('2. Finance Cards Check:', JSON.stringify(financeCheck, null, 2));

    // 3. Inspect Stacked Bar
    const stackedBarCheck = await evalJs(`
      const bar = document.querySelector('.stacked-bar');
      const segments = Array.from(bar.querySelectorAll('.bar-segment')).map(s => {
        return {
          className: s.className,
          text: s.innerText.trim(),
          width: Math.round(s.getBoundingClientRect().width)
        };
      });
      return {
        barHeight: Math.round(bar.getBoundingClientRect().height),
        segments
      };
    `);
    console.log('3. Stacked Bar Check:', JSON.stringify(stackedBarCheck, null, 2));

    // 4. Capture screenshot of Agenda
    await evalJs(`
      const el = document.getElementById('agenda');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(500);
    const snapAgenda = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_agenda_fix.png', Buffer.from(snapAgenda.data, 'base64'));
    console.log('Saved verify_agenda_fix.png');

    // 5. Capture screenshot of Finance & Progress Bar
    await evalJs(`
      const el = document.getElementById('budget');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(500);
    const snapFinance = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_finance_fix.png', Buffer.from(snapFinance.data, 'base64'));
    console.log('Saved verify_finance_fix.png');

    // 6. Capture screenshot of Artists section & Wave
    await evalJs(`
      const el = document.getElementById('artists');
      if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
    `);
    await sleep(500);
    const snapArtists = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_artists_fix.png', Buffer.from(snapArtists.data, 'base64'));
    console.log('Saved verify_artists_fix.png');

    ws.close();
  } catch (err) {
    console.error('Error:', err);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

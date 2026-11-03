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
    '--window-size=1440,900',
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

    // Scroll to transition 1: Hero to Overview
    await call('Runtime.evaluate', {
      expression: `(() => {
        const el = document.querySelector('.hero-bottom-curve');
        if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      })()`
    });
    await sleep(400);
    const snap1 = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_transition_hero_overview.png', Buffer.from(snap1.data, 'base64'));

    // Scroll to transition 2: Overview to Artists
    await call('Runtime.evaluate', {
      expression: `(() => {
        const el = document.querySelector('.divider-overview-to-navy');
        if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      })()`
    });
    await sleep(400);
    const snap2 = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_transition_overview_artists.png', Buffer.from(snap2.data, 'base64'));

    // Scroll to transition 3: Artists to Agenda
    await call('Runtime.evaluate', {
      expression: `(() => {
        const el = document.querySelector('.divider-artists-to-agenda');
        if (el) el.scrollIntoView({ behavior: 'instant', block: 'center' });
      })()`
    });
    await sleep(400);
    const snap3 = await call('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('C:/Users/Anonymous/.gemini/antigravity/brain/376b2e55-66c9-4742-93de-0ae10297c59f/verify_transition_artists_agenda.png', Buffer.from(snap3.data, 'base64'));

    console.log('Saved all 3 transition screenshots!');
    ws.close();
  } catch (e) {
    console.error(e);
  } finally {
    chrome.kill();
    try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch (e) {}
  }
}

main();

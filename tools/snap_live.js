const { spawn } = require('child_process');
const fs = require('fs');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9225',
    '--window-size=1440,1200',
    'http://127.0.0.1:5500/index.html'
  ]);

  await sleep(2500);

  try {
    const res = await (await fetch('http://127.0.0.1:9225/json')).json();
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

    console.log("Title:", await evalJs('document.title'));

    async function snap(name) {
      const shot = await call('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(name, Buffer.from(shot.data, 'base64'));
      console.log('Snapped:', name);
    }

    // 1. Jump to Appendix (#appendices)
    await evalJs(`document.getElementById('appendices').scrollIntoView({block: 'start'})`);
    await sleep(600);
    await snap('screen_verify_appendices_doc.png');

    // 2. Click Appendix Tab 2
    await evalJs(`document.querySelector('.app-tab-btn[data-app-target="app-2"]').click()`);
    await sleep(600);
    await snap('screen_verify_appendix_tab2.png');

    // 3. Jump to Agenda (#agenda)
    await evalJs(`document.getElementById('agenda').scrollIntoView({block: 'start'})`);
    await sleep(600);
    await snap('screen_verify_agenda_all.png');

    // 4. Click Phase 1 button
    await evalJs(`document.querySelector('.agenda-filter-btn[data-filter="phase-1"]').click()`);
    await sleep(600);
    await snap('screen_verify_agenda_phase1.png');

    // 5. Click Phase 3 button (10:05 - 11:10)
    await evalJs(`document.querySelector('.agenda-filter-btn[data-filter="phase-3"]').click()`);
    await sleep(600);
    await snap('screen_verify_agenda_phase3.png');

    // 6. Jump to Budget (#budget)
    await evalJs(`document.getElementById('budget').scrollIntoView({block: 'start'})`);
    await sleep(600);
    // Filter to Group A
    await evalJs(`
      const s = document.getElementById('budget-group-select');
      s.value = 'A';
      s.dispatchEvent(new Event('change'));
    `);
    await sleep(600);
    await snap('screen_verify_budget_filtered_a.png');

    // 7. Jump to Ticket (#register-contact)
    await evalJs(`document.getElementById('register-contact').scrollIntoView({block: 'start'})`);
    await sleep(600);
    await snap('screen_verify_ticket_studio.png');

    ws.close();
  } catch (err) {
    console.error("Snap error:", err);
  } finally {
    chrome.kill();
    console.log("Finished all snaps!");
  }
}

main();

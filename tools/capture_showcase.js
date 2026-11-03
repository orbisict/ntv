const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

function startServer(port) {
  const mimeTypes = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.svg': 'image/svg+xml'
  };

  const server = http.createServer((req, res) => {
    let reqPath = decodeURI(req.url.split('?')[0]);
    if (reqPath === '/' || reqPath === '') reqPath = '/index.html';
    const filePath = path.join(process.cwd(), reqPath);

    if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
      const ext = path.extname(filePath).toLowerCase();
      res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
      res.end(fs.readFileSync(filePath));
    } else {
      res.writeHead(404);
      res.end('Not found');
    }
  });

  server.listen(port, '127.0.0.1');
  return server;
}

async function main() {
  const serverPort = 5566;
  const cdpPort = 9222;
  const server = startServer(serverPort);
  console.log(`HTTP Server running at http://127.0.0.1:${serverPort}`);

  const chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
  const chrome = spawn(chromePath, [
    '--headless=new',
    '--disable-gpu',
    `--remote-debugging-port=${cdpPort}`,
    '--window-size=1440,1200',
    'about:blank'
  ]);

  await sleep(1500);

  try {
    const listRes = await fetch(`http://127.0.0.1:${cdpPort}/json`);
    const tabs = await listRes.json();
    const wsUrl = tabs[0].webSocketDebuggerUrl;
    console.log("Connected to Chrome CDP");

    const ws = new WebSocket(wsUrl);
    let msgId = 1;
    const pending = new Map();
    let loadFiredResolve = null;

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id && pending.has(msg.id)) {
        pending.get(msg.id)(msg.result);
        pending.delete(msg.id);
      }
      if (msg.method === 'Page.loadEventFired' && loadFiredResolve) {
        loadFiredResolve();
        loadFiredResolve = null;
      }
    };

    await new Promise(r => ws.onopen = r);

    function send(method, params = {}) {
      const id = msgId++;
      return new Promise((resolve) => {
        pending.set(id, resolve);
        ws.send(JSON.stringify({ id, method, params }));
      });
    }

    await send('Page.enable');
    await send('DOM.enable');
    await send('Runtime.enable');

    console.log("Navigating to site...");
    const loadPromise = new Promise(resolve => { loadFiredResolve = resolve; });
    await send('Page.navigate', { url: `http://127.0.0.1:${serverPort}/index.html` });
    await loadPromise;
    console.log("Page load event fired!");
    await sleep(1500);

    async function evaluate(expression) {
      const res = await send('Runtime.evaluate', { expression, returnByValue: true });
      return res?.result?.value;
    }

    const title = await evaluate(`document.title`);
    console.log("Page loaded. Title:", title);

    async function captureElement(selector, filename, maxH = 1000) {
      await evaluate(`
        (() => {
          const el = document.querySelector('${selector}');
          if (el) el.scrollIntoView({ block: 'start' });
        })()
      `);
      await sleep(500);

      const box = await evaluate(`
        (() => {
          const el = document.querySelector('${selector}');
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return {
            x: Math.max(0, Math.floor(r.left)),
            y: Math.max(0, Math.floor(r.top)),
            width: Math.min(1440, Math.ceil(r.width)),
            height: Math.min(${maxH}, Math.ceil(r.height))
          };
        })()
      `);

      if (!box || box.width <= 0 || box.height <= 0) {
        console.error("Invalid box for selector:", selector, box);
        return;
      }

      const shot = await send('Page.captureScreenshot', {
        format: 'png',
        clip: {
          x: box.x,
          y: box.y,
          width: box.width,
          height: box.height,
          scale: 1
        }
      });

      fs.writeFileSync(filename, Buffer.from(shot.data, 'base64'));
      console.log(`Saved screenshot: ${filename} (${box.width}x${box.height})`);
    }

    // 1. Capture Section 8 (Official Appendix Paper Document)
    console.log("1. Capturing Section 8 (Official Appendix Paper)...");
    await captureElement('#appendices', 'verify_section8_appendix_doc.png', 1100);

    // 2. Capture Agenda Phase 1 (07:30 - 08:40)
    console.log("2. Capturing Agenda Phase 1...");
    await evaluate(`document.querySelector('.agenda-filter-btn[data-filter="phase-1"]').click()`);
    await sleep(400);
    await captureElement('#agenda', 'verify_agenda_phase1.png', 900);

    // 3. Capture Agenda Phase 3 (10:05 - 11:10)
    console.log("3. Capturing Agenda Phase 3...");
    await evaluate(`document.querySelector('.agenda-filter-btn[data-filter="phase-3"]').click()`);
    await sleep(400);
    await captureElement('#agenda', 'verify_agenda_phase3.png', 900);

    // 4. Reset Agenda to All
    console.log("4. Resetting Agenda to All...");
    await evaluate(`document.querySelector('.agenda-filter-btn[data-filter="all"]').click()`);
    await sleep(300);

    // 5. Capture Budget Filter: Group A
    console.log("5. Testing Budget Filter Group A...");
    await evaluate(`
      (() => {
        const s = document.getElementById('budget-group-select');
        s.value = 'A';
        s.dispatchEvent(new Event('change'));
      })()
    `);
    await sleep(400);
    await captureElement('#budget', 'verify_budget_group_a.png', 800);

    // 6. Capture Risk Filter: Severity Cao
    console.log("6. Testing Risk Severity Filter 'cao'...");
    await evaluate(`
      (() => {
        const s = document.getElementById('risk-severity-select');
        s.value = 'cao';
        s.dispatchEvent(new Event('change'));
      })()
    `);
    await sleep(400);
    await captureElement('#risks-kpi', 'verify_risk_severity_cao.png', 850);

    // 7. Capture Appendix Tab 2
    console.log("7. Testing Appendix Tab 2...");
    await evaluate(`document.querySelector('.app-tab-btn[data-app-target="app-2"]').click()`);
    await sleep(400);
    await captureElement('#appendices', 'verify_appendix_tab2.png', 1100);

    // 8. Capture Ticket Section
    console.log("8. Capturing Ticket Section...");
    await captureElement('#register-contact', 'verify_ticket_section.png', 900);

    ws.close();
  } catch (err) {
    console.error("Error in capture:", err);
  } finally {
    chrome.kill();
    server.close();
    console.log("Done! Chrome and server closed.");
  }
}

main();

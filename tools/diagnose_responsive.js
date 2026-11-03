const { spawn } = require('child_process');
const fs = require('fs');

async function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const chrome = spawn("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9229',
    '--window-size=375,812'
  ]);

  await sleep(1500);

  try {
    const res = await (await fetch('http://127.0.0.1:9229/json')).json();
    const ws = new WebSocket(res[0].webSocketDebuggerUrl);

    let id = 1;
    const pending = new Map();
    const events = [];
    ws.onmessage = e => {
      const d = JSON.parse(e.data);
      if (d.id && pending.has(d.id)) {
        pending.get(d.id)(d.result);
        pending.delete(d.id);
      }
      if (d.method) {
        events.push(d);
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

    console.log("Navigating to page...");
    await call('Page.navigate', { url: 'http://127.0.0.1:5500/index.html' });
    await sleep(2000);

    const evalJs = async (expr) => {
      const r = await call('Runtime.evaluate', { expression: expr, returnByValue: true });
      return r?.result?.value;
    };

    console.log("Diagnosing 375px mobile responsiveness...");

    const diag = await evalJs(`
      (() => {
        const winW = window.innerWidth;
        const scrollW = document.documentElement.scrollWidth;
        const bodyW = document.body.scrollWidth;

        const offenders = [];
        const all = document.querySelectorAll('*');
        for (const el of all) {
          const rect = el.getBoundingClientRect();
          if (rect.right > winW + 2) {
            offenders.push({
              tag: el.tagName,
              id: el.id,
              cls: el.className,
              rectRight: Math.round(rect.right),
              rectWidth: Math.round(rect.width),
              text: el.innerText ? el.innerText.slice(0, 35).replace(/\\n/g, ' ') : ''
            });
          }
        }

        // Also check elements with fixed widths or bad flex/grid
        const buttonGroups = Array.from(document.querySelectorAll('.filter-bar, .timeline-filter-bar, .appendix-tabs-bar, .kpi-tabs-bar')).map(b => ({
          cls: b.className,
          scrollW: b.scrollWidth,
          clientW: b.clientWidth,
          hasScroll: b.scrollWidth > b.clientWidth
        }));

        // Check tables
        const tables = Array.from(document.querySelectorAll('table')).map(t => {
          const p = t.parentElement;
          return {
            tableCls: t.className,
            parentCls: p.className,
            parentOverflowX: window.getComputedStyle(p).overflowX,
            tableW: Math.round(t.getBoundingClientRect().width),
            parentW: Math.round(p.getBoundingClientRect().width)
          };
        });

        // Check ticket preview
        const ticketCard = document.querySelector('.vip-ticket-card');
        const ticketW = ticketCard ? Math.round(ticketCard.getBoundingClientRect().width) : null;

        return {
          winW,
          scrollW,
          bodyW,
          hasHorizontalScroll: scrollW > winW || bodyW > winW,
          offenderCount: offenders.length,
          topOffenders: offenders.slice(0, 15),
          buttonGroups,
          tables: tables.slice(0, 5),
          ticketW
        };
      })()
    `);

    console.log("Diagnosis Result:\n", JSON.stringify(diag, null, 2));

    ws.close();
  } catch (err) {
    console.error("Error:", err);
  } finally {
    chrome.kill();
  }
}

main();

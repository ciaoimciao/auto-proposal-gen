// ═══════════════════════════════════════
// Slide HTML Renderer (Browser Preview)
// ═══════════════════════════════════════

import { Slide, ThemeColors } from '../types';

/**
 * 產生完整投影片的 HTML（用於主預覽區）
 */
export function renderSlide(sl: Slide, c: ThemeColors): string {
  const base = [
    `width:100%`, `height:100%`, `position:relative`, `overflow:hidden`,
    `background:${c.bg}`, `color:${c.tx}`, `font-family:'DM Sans',sans-serif`
  ].join(';') + ';';

  switch (sl.type) {
    case 'cover':  return renderCover(sl, c, base);
    case 'metric': return renderMetric(sl, c, base);
    case 'budget': return renderTable(sl, c, base);
    default:       return renderContent(sl, c, base);
  }
}

/**
 * 產生縮圖用的精簡 HTML（sidebar thumbnails）
 */
export function renderMini(sl: Slide, c: ThemeColors): string {
  const pts = sl.points || [];
  return `<div style="width:100%;height:100%;background:${c.bg};padding:10% 12%;position:relative;overflow:hidden;">
    <div style="position:absolute;top:0;left:0;right:0;height:2px;background:${c.ac};"></div>
    <div style="font-size:5px;font-weight:700;color:${c.ac};margin-bottom:3px;text-transform:uppercase;letter-spacing:.08em;">${sl.type}</div>
    <div style="font-size:6.5px;font-weight:800;color:${c.tx};line-height:1.3;font-family:'Syne',sans-serif;margin-bottom:4px;">${sl.title.substring(0, 40)}</div>
    ${pts.slice(0, 3).map(p => `
      <div style="font-size:4.5px;color:${c.tx2};display:flex;gap:3px;margin-bottom:2px;">
        <span style="color:${c.ac};">▸</span>
        <span>${p.substring(0, 35)}</span>
      </div>`).join('')}
  </div>`;
}

// ─── Internal renderers ────────────────

function renderCover(sl: Slide, c: ThemeColors, base: string): string {
  const date = new Date().toLocaleDateString('zh-TW');
  const meta = sl.points ? sl.points.join('  ·  ') : '';
  return `<div style="${base}padding:7% 9%;">
    <div style="position:absolute;left:0;top:0;width:5px;height:100%;background:${c.ac};"></div>
    <div style="font-size:clamp(9px,1.3vw,12px);font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:${c.ac};margin-bottom:6%;">${date}</div>
    <h1 style="font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(18px,4.2vw,40px);line-height:1.1;letter-spacing:-.04em;margin-bottom:3%;max-width:85%;">${sl.title}</h1>
    ${sl.subtitle ? `<p style="font-size:clamp(11px,1.8vw,17px);color:${c.tx2};line-height:1.55;max-width:70%;margin-bottom:8%;">${sl.subtitle}</p>` : ''}
    <div style="position:absolute;bottom:7%;left:9%;right:9%;border-top:1px solid ${c.tx2};padding-top:3%;font-size:clamp(9px,1.2vw,11px);color:${c.tx2};">${meta}</div>
  </div>`;
}

function renderContent(sl: Slide, c: ThemeColors, base: string): string {
  const pts = sl.points || [];
  return `<div style="${base}padding:5.5% 7%;">
    <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,${c.ac},${c.ac2});"></div>
    <div style="font-size:clamp(7px,1vw,10px);font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:${c.ac};margin-bottom:1.5%;">${sl.type}</div>
    <h2 style="font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(14px,2.8vw,26px);letter-spacing:-.03em;margin-bottom:${sl.body ? '1.5%' : '3%'};line-height:1.15;">${sl.title}</h2>
    ${sl.body ? `<p style="font-size:clamp(9px,1.3vw,12px);color:${c.tx2};margin-bottom:2.5%;line-height:1.6;max-width:90%;">${sl.body}</p>` : ''}
    <ul style="list-style:none;display:flex;flex-direction:column;gap:1.2%;">
      ${pts.map(p => `
        <li style="display:flex;align-items:flex-start;gap:1.5%;font-size:clamp(9px,1.35vw,13px);line-height:1.5;">
          <span style="color:${c.ac};margin-top:.1em;flex-shrink:0;font-size:.9em;">▸</span>
          <span style="color:${c.tx};">${p}</span>
        </li>`).join('')}
    </ul>
    ${sl.highlight ? `
      <div style="position:absolute;bottom:6%;right:7%;background:${c.ac};color:#fff;padding:1.8% 2.5%;border-radius:8px;text-align:center;min-width:80px;">
        <div style="font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(13px,2.2vw,20px);">${sl.highlight}</div>
        ${sl.highlightLabel ? `<div style="font-size:clamp(7px,.9vw,9px);opacity:.85;margin-top:.2em;">${sl.highlightLabel}</div>` : ''}
      </div>` : ''}
  </div>`;
}

function renderMetric(sl: Slide, c: ThemeColors, base: string): string {
  return `<div style="${base}padding:5% 7%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;">
    <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,${c.ac},${c.ac2});"></div>
    <h2 style="font-family:'Syne',sans-serif;font-weight:700;font-size:clamp(11px,1.8vw,16px);color:${c.tx2};margin-bottom:5%;letter-spacing:-.02em;">${sl.title}</h2>
    <div style="font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(38px,9.5vw,88px);color:${c.ac};letter-spacing:-.04em;line-height:1;">${sl.highlight || '—'}</div>
    ${sl.highlightLabel ? `<div style="font-size:clamp(11px,1.8vw,16px);color:${c.tx2};margin-top:2%;">${sl.highlightLabel}</div>` : ''}
    ${sl.body ? `<p style="font-size:clamp(9px,1.3vw,12px);color:${c.tx2};margin-top:4%;max-width:55%;line-height:1.6;">${sl.body}</p>` : ''}
  </div>`;
}

function renderTable(sl: Slide, c: ThemeColors, base: string): string {
  if (!sl.table) return renderContent(sl, c, base);
  const { headers, rows } = sl.table;
  const border = c.isDark ? 'rgba(255,255,255,.1)' : 'rgba(17,17,16,.1)';
  const rowAlt  = c.isDark ? 'rgba(255,255,255,.04)' : 'rgba(17,17,16,.03)';
  return `<div style="${base}padding:5.5% 7%;">
    <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,${c.ac},${c.ac2});"></div>
    <h2 style="font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(14px,2.5vw,22px);letter-spacing:-.03em;margin-bottom:${sl.highlight ? '1%' : '3%'};">${sl.title}</h2>
    ${sl.highlight ? `<p style="font-size:clamp(9px,1.3vw,12px);color:${c.ac};font-weight:600;margin-bottom:2.5%;">總計：${sl.highlight}</p>` : ''}
    <table style="width:100%;border-collapse:collapse;font-size:clamp(8px,1.2vw,11px);">
      <thead>
        <tr style="border-bottom:2px solid ${c.ac};">
          ${headers.map(h => `<th style="text-align:left;padding:1.5% 2%;font-weight:700;color:${c.ac};">${h}</th>`).join('')}
        </tr>
      </thead>
      <tbody>
        ${rows.map((row, i) => `
          <tr style="${i % 2 ? `background:${rowAlt};` : ''}border-bottom:1px solid ${border};">
            ${row.map(cell => `<td style="padding:1.5% 2%;color:${c.tx};">${cell}</td>`).join('')}
          </tr>`).join('')}
      </tbody>
    </table>
  </div>`;
}

// ═══════════════════════════════════════
// PPTX Export — powered by PptxGenJS
// ═══════════════════════════════════════
// Slide canvas: 13.33" × 7.5" (16:9 LAYOUT_WIDE)

import { Slide, ThemeColors } from '../types';

declare const PptxGenJS: any;

// ─── Helpers ───────────────────────────

/** Strip leading # from hex colour for pptxgenjs */
function hex(color: string): string {
  return color.replace('#', '');
}

/** Add a thin accent bar (vertical for cover, horizontal for others) */
function accentBar(pptx: any, s: any, AC: string, vertical = false) {
  if (vertical) {
    s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:0.1, h:7.5, fill:{color:AC}, line:{color:AC} });
  } else {
    s.addShape(pptx.ShapeType.rect, { x:0, y:0, w:13.33, h:0.05, fill:{color:AC}, line:{color:AC} });
  }
}

// ─── Slide renderers ───────────────────

function renderCover(pptx: any, s: any, sl: Slide, c: Record<string, string>) {
  const { TX, TX2, AC } = c;
  accentBar(pptx, s, AC, true);

  s.addText(new Date().toLocaleDateString('zh-TW'), {
    x:.45, y:.8, w:12, h:.35,
    fontSize:10, bold:true, color:AC, fontFace:'Arial', charSpacing:4
  });

  s.addText(sl.title, {
    x:.45, y:1.4, w:11, h:2.6,
    fontSize:36, bold:true, color:TX, fontFace:'Arial', charSpacing:-1, wrap:true
  });

  if (sl.subtitle) {
    s.addText(sl.subtitle, {
      x:.45, y:3.8, w:9.5, h:1,
      fontSize:15, color:TX2, fontFace:'Arial', wrap:true
    });
  }

  // Divider line
  s.addShape(pptx.ShapeType.rect, {
    x:.45, y:5.35, w:12.4, h:0.01, fill:{color:TX2}, line:{color:TX2}
  });

  // Meta info row
  const meta = sl.points ? sl.points.join('   ·   ') : '';
  if (meta) {
    s.addText(meta, { x:.45, y:5.6, w:12, h:.4, fontSize:10, color:TX2, fontFace:'Arial' });
  }
}

function renderContent(pptx: any, s: any, sl: Slide, c: Record<string, string>) {
  const { TX, TX2, AC } = c;
  accentBar(pptx, s, AC);

  s.addText((sl.type || 'content').toUpperCase(), {
    x:.6, y:.3, w:12, h:.3,
    fontSize:9, bold:true, color:AC, fontFace:'Arial', charSpacing:5
  });

  s.addText(sl.title, {
    x:.6, y:.65, w:11.5, h:1.1,
    fontSize:24, bold:true, color:TX, fontFace:'Arial', charSpacing:-.5, wrap:true
  });

  let y = 1.75;

  if (sl.body) {
    s.addText(sl.body, {
      x:.6, y, w:11.5, h:.65, fontSize:12, color:TX2, fontFace:'Arial', wrap:true
    });
    y += .75;
  }

  if (sl.points && sl.points.length > 0) {
    const items = sl.points.map(p => ({
      text: p,
      options: { bullet:{type:'bullet'}, paraSpaceAfter:6, fontSize:13, color:TX, fontFace:'Arial' }
    }));
    s.addText(items, { x:.6, y, w:10.8, h:7.5 - y - .8, valign:'top', wrap:true });
  }

  if (sl.highlight) {
    s.addShape(pptx.ShapeType.rect, {
      x:10.85, y:5.85, w:2.0, h:1.1, fill:{color:AC}, line:{color:AC}, rounding:.08
    });
    s.addText(sl.highlight, {
      x:10.85, y:5.9, w:2.0, h:.58,
      fontSize:18, bold:true, color:'FFFFFF', align:'center', fontFace:'Arial'
    });
    if (sl.highlightLabel) {
      s.addText(sl.highlightLabel, {
        x:10.85, y:6.45, w:2.0, h:.38,
        fontSize:9, color:'FFFFFF', align:'center', fontFace:'Arial'
      });
    }
  }
}

function renderMetric(pptx: any, s: any, sl: Slide, c: Record<string, string>) {
  const { TX, TX2, AC } = c;
  accentBar(pptx, s, AC);

  s.addText(sl.title, {
    x:1, y:.45, w:11, h:.7,
    fontSize:18, bold:true, color:TX2, align:'center', fontFace:'Arial'
  });

  s.addText(sl.highlight || '—', {
    x:1, y:1.3, w:11, h:3.2,
    fontSize:90, bold:true, color:AC, align:'center', fontFace:'Arial', charSpacing:-3
  });

  if (sl.highlightLabel) {
    s.addText(sl.highlightLabel, {
      x:1, y:4.3, w:11, h:.65, fontSize:17, color:TX2, align:'center', fontFace:'Arial'
    });
  }

  if (sl.body) {
    s.addText(sl.body, {
      x:2.5, y:5.1, w:8, h:.8,
      fontSize:12, color:TX2, align:'center', fontFace:'Arial', wrap:true
    });
  }
}

function renderTable(pptx: any, s: any, sl: Slide, c: Record<string, string>) {
  if (!sl.table) { renderContent(pptx, s, sl, c); return; }
  const { TX, TX2, AC } = c;
  accentBar(pptx, s, AC);

  s.addText(sl.title, {
    x:.6, y:.3, w:11.5, h:.85, fontSize:22, bold:true, color:TX, fontFace:'Arial'
  });

  if (sl.highlight) {
    s.addText(`總計：${sl.highlight}`, {
      x:.6, y:1.1, w:12, h:.45, fontSize:13, bold:true, color:AC, fontFace:'Arial'
    });
  }

  const { headers, rows } = sl.table;
  const colW = headers.map(() => 12.1 / headers.length);

  const tData = [
    headers.map(h => ({ text: h, options: { bold:true, color:AC, fill:{color: AC + '22'} } })),
    ...rows.map(row => row.map(cell => ({ text: String(cell || ''), options: { color:TX } })))
  ];

  s.addTable(tData, {
    x:.6, y: sl.highlight ? 1.65 : 1.3,
    w:12.1, colW,
    fontSize:11, fontFace:'Arial',
    border:{ type:'solid', color:TX2, pt:.5 },
    rowH:.45
  });
}

// ─── Public API ────────────────────────

/**
 * 將投影片陣列匯出為 .pptx 檔案並觸發下載
 */
export async function exportToPptx(
  slides: Slide[],
  title: string,
  colors: ThemeColors
): Promise<void> {
  const pptx = new PptxGenJS();
  pptx.layout = 'LAYOUT_WIDE';

  const c = {
    BG:  hex(colors.bg),
    TX:  hex(colors.tx),
    TX2: colors.isDark ? 'AAAAAA' : '777777',
    AC:  hex(colors.ac),
    AC2: hex(colors.ac2)
  };

  for (const sl of slides) {
    const s = pptx.addSlide();
    s.background = { color: c.BG };

    switch (sl.type) {
      case 'cover':  renderCover(pptx, s, sl, c);   break;
      case 'metric': renderMetric(pptx, s, sl, c);  break;
      case 'budget': renderTable(pptx, s, sl, c);   break;
      default:       renderContent(pptx, s, sl, c); break;
    }
  }

  const fname = title.replace(/[^\w\u4e00-\u9fa5]/g, '_').substring(0, 40) || 'proposal';
  await pptx.writeFile({ fileName: `${fname}.pptx` });
}

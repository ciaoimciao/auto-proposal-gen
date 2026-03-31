#!/usr/bin/env python3
"""Redesign slide theming: 70% monochrome + 30% brand accent.
Key change: rewrite getThemeVars() so all slides use stone/neutral backgrounds
with brand color only as accent (badges, dots, borders, highlights)."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Rewrite getThemeVars() — the master switch ───
old_theme = """function getThemeVars(slideId){
  const c1=STATE.color1,c2=STATE.color2,ct=STATE.colorTxt;

  // Slides that use BRAND COLOR as background (high visual impact)
  const BRAND_BG_SLIDES=['s-cover','s-mdesign','s-thankyou','s-mopt'];
  // Slides that use a LIGHTER shade of brand for subtle warmth
  const BRAND_TINT_SLIDES=['s-pain','s-chat','s-emotion'];

  let mode=STATE.slideTheme;
  // In 'brand' mode, auto-assign per slide type
  if(mode==='brand'){
    if(BRAND_BG_SLIDES.includes(slideId)) mode='brand-full';
    else if(BRAND_TINT_SLIDES.includes(slideId)) mode='brand-tint';
    else mode='dark'; // remaining slides: dark background
  }

  if(mode==='brand-full'){
    return {
      BG:c1, BG2:darken(c1,.07),
      TX:ct, TX2:alpha(ct,.72), TX3:alpha(ct,.42),
      CARD:alpha(ct,.07), CARD_BDR:alpha(ct,.16),
      TAG_COL:ct, TAG_BDR:alpha(ct,.55),
      HEADING:ct, BODY:alpha(ct,.72),
      ACCENT:c2, ACCENT_ALPHA:alpha(c2,.3),
      META_BDR:alpha(ct,.28), NUM_COL:alpha(ct,.07),
      CARD_ACCENT:alpha(c2,.18),
    };
  } else if(mode==='brand-tint'){
    // Dark bg with strong brand color accents
    return {
      BG:'#111110', BG2:'#1e1e1c',
      TX:'#F5F2EC', TX2:'rgba(245,242,236,.68)', TX3:'rgba(245,242,236,.38)',
      CARD:alpha(c1,.06), CARD_BDR:alpha(c1,.18),
      TAG_COL:c1, TAG_BDR:alpha(c1,.55),
      HEADING:'#F5F2EC', BODY:'rgba(245,242,236,.68)',
      ACCENT:c2, ACCENT_ALPHA:alpha(c2,.25),
      META_BDR:'rgba(255,255,255,.18)', NUM_COL:'rgba(255,255,255,.04)',
      CARD_ACCENT:alpha(c1,.1),
    };
  } else if(mode==='light'){
    return {
      BG:'#F5F2EC', BG2:'#EDEAE2',
      TX:'#111110', TX2:'rgba(17,17,16,.65)', TX3:'rgba(17,17,16,.35)',
      CARD:'rgba(17,17,16,.04)', CARD_BDR:'rgba(17,17,16,.1)',
      TAG_COL:c1, TAG_BDR:alpha(c1,.5),
      HEADING:'#111110', BODY:'rgba(17,17,16,.65)',
      ACCENT:c2, ACCENT_ALPHA:alpha(c2,.2),
      META_BDR:'rgba(17,17,16,.12)', NUM_COL:'rgba(17,17,16,.05)',
      CARD_ACCENT:alpha(c1,.1),
    };
  } else {
    // dark (default for content-heavy slides)
    return {
      BG:'#111110', BG2:'#1e1e1c',
      TX:'#F5F2EC', TX2:'rgba(245,242,236,.65)', TX3:'rgba(245,242,236,.35)',
      CARD:'rgba(255,255,255,.04)', CARD_BDR:'rgba(255,255,255,.08)',
      TAG_COL:c1, TAG_BDR:alpha(c1,.5),
      HEADING:'#F5F2EC', BODY:'rgba(245,242,236,.65)',
      ACCENT:c2, ACCENT_ALPHA:alpha(c2,.25),
      META_BDR:'rgba(255,255,255,.15)', NUM_COL:'rgba(255,255,255,.04)',
      CARD_ACCENT:alpha(c1,.08),
    };
  }
}"""

new_theme = """function getThemeVars(slideId){
  const c1=STATE.color1,c2=STATE.color2,ct=STATE.colorTxt;

  // ══ MONOCHROME DECK SYSTEM ══
  // 70% neutral/stone base + 30% brand color as accent only
  // Cover & Thank You: brand-accent (stone bg with brand hero element)
  // All other slides: clean stone/neutral

  const HERO_SLIDES=['s-cover','s-thankyou'];

  let mode=STATE.slideTheme;
  if(mode==='brand'){
    mode=HERO_SLIDES.includes(slideId)?'brand-accent':'mono';
  }

  // ── Monochrome Stone (default for all content slides) ──
  if(mode==='mono'||mode==='brand'||mode==='light'){
    return {
      BG:'#f5f5f4', BG2:'#e7e5e4',
      TX:'#0a0a0a', TX2:'rgba(10,10,10,.55)', TX3:'rgba(10,10,10,.32)',
      CARD:'rgba(10,10,10,.03)', CARD_BDR:'rgba(163,163,163,.2)',
      TAG_COL:c1, TAG_BDR:alpha(c1,.4),
      HEADING:'#0a0a0a', BODY:'rgba(10,10,10,.55)',
      ACCENT:c1, ACCENT_ALPHA:alpha(c1,.15),
      META_BDR:'rgba(10,10,10,.1)', NUM_COL:'rgba(10,10,10,.05)',
      CARD_ACCENT:alpha(c1,.06),
    };
  }

  // ── Brand Accent (cover/thankyou: stone bg + bold brand accent elements) ──
  if(mode==='brand-accent'){
    return {
      BG:'#f5f5f4', BG2:'#e7e5e4',
      TX:'#0a0a0a', TX2:'rgba(10,10,10,.55)', TX3:'rgba(10,10,10,.32)',
      CARD:alpha(c1,.05), CARD_BDR:alpha(c1,.15),
      TAG_COL:c1, TAG_BDR:alpha(c1,.5),
      HEADING:'#0a0a0a', BODY:'rgba(10,10,10,.55)',
      ACCENT:c1, ACCENT_ALPHA:alpha(c1,.2),
      META_BDR:'rgba(10,10,10,.1)', NUM_COL:'rgba(10,10,10,.04)',
      CARD_ACCENT:alpha(c1,.08),
    };
  }

  // ── Dark (if user explicitly picks dark in settings) ──
  if(mode==='dark'){
    return {
      BG:'#1a1a1a', BG2:'#262626',
      TX:'#e5e5e5', TX2:'rgba(229,229,229,.6)', TX3:'rgba(229,229,229,.35)',
      CARD:'rgba(255,255,255,.04)', CARD_BDR:'rgba(255,255,255,.08)',
      TAG_COL:c1, TAG_BDR:alpha(c1,.45),
      HEADING:'#e5e5e5', BODY:'rgba(229,229,229,.6)',
      ACCENT:c1, ACCENT_ALPHA:alpha(c1,.2),
      META_BDR:'rgba(255,255,255,.12)', NUM_COL:'rgba(255,255,255,.04)',
      CARD_ACCENT:alpha(c1,.08),
    };
  }

  // fallback
  return {
    BG:'#f5f5f4', BG2:'#e7e5e4',
    TX:'#0a0a0a', TX2:'rgba(10,10,10,.55)', TX3:'rgba(10,10,10,.32)',
    CARD:'rgba(10,10,10,.03)', CARD_BDR:'rgba(163,163,163,.2)',
    TAG_COL:c1, TAG_BDR:alpha(c1,.4),
    HEADING:'#0a0a0a', BODY:'rgba(10,10,10,.55)',
    ACCENT:c1, ACCENT_ALPHA:alpha(c1,.15),
    META_BDR:'rgba(10,10,10,.1)', NUM_COL:'rgba(10,10,10,.05)',
    CARD_ACCENT:alpha(c1,.06),
  };
}"""

if old_theme in src:
    src = src.replace(old_theme, new_theme)
    changes += 1
    print("✅ 1. Rewrote getThemeVars() → monochrome deck system")
else:
    print("❌ 1. getThemeVars() not found — CRITICAL")

# ─── 2. Fix cover slide 'spread' variant background ───
# Replace the full brand gradient with stone bg + brand accent strip
old_cover_spread = """<div class="sl-bg" style="background:linear-gradient(135deg,${c1} 0%,${c2} 100%);position:absolute;inset:0;"></div>
    <div class="geo-ring" style="top:-200px;right:-200px;width:800px;height:800px;border-width:120px;border-color:rgba(255,255,255,.1);"></div>
    <div class="geo-ring" style="bottom:-100px;right:320px;width:300px;height:300px;border-width:50px;border-color:rgba(255,255,255,.07);"></div>
    <div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 480px;align-items:center;padding:0 80px 0 100px;">
      <div style="display:flex;flex-direction:column;justify-content:center;">
        <div style="display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,.18);border-radius:40px;padding:10px 28px;width:fit-content;margin-bottom:36px;">
          <div style="width:10px;height:10px;border-radius:50%;background:#fff;animation:pd 1.8s ease-in-out infinite;"></div>
          <span style="font-family:var(--fd);font-size:20px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;">${e(tx('cover_badge',L))}</span>
        </div>
        <div style="font-family:var(--fd);font-size:96px;font-weight:800;line-height:.9;letter-spacing:-.05em;color:#fff;margin-bottom:20px;">${e(STATE.aiCoverH||tx('cover_h',L))}</div>
        <div style="font-size:28px;color:rgba(255,255,255,.75);line-height:1.5;max-width:640px;margin-bottom:48px;">${e(tx('cover_sub',L))} <strong style="color:#fff;font-weight:800;">${e(C)}</strong>.</div>
        <div style="display:flex;gap:0;border-top:2px solid rgba(255,255,255,.25);padding-top:32px;">
          <div style="flex:1;padding-right:32px;border-right:1px solid rgba(255,255,255,.2);">
            <div style="font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.55);margin-bottom:6px;">${tx('prepared',L)}</div>
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:#fff;">${e(C)}</div>
          </div>
          <div style="flex:1;padding:0 32px;border-right:1px solid rgba(255,255,255,.2);">
            <div style="font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.55);margin-bottom:6px;">${tx('industry',L)}</div>
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:#fff;">${e(IND)}</div>
          </div>
          <div style="flex:1;padding-left:32px;">
            <div style="font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.55);margin-bottom:6px;">${tx('kickoff',L)}</div>
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:#fff;">${e(selDate?fmtDate(selDate):'—')}</div>
          </div>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;height:100%;">
        ${hasImg ? `<img src="${getMascotImageForSlide(sid)}" style="height:880px;max-width:520px;object-fit:contain;filter:drop-shadow(0 40px 80px rgba(0,0,0,.35));" alt="mascot"/>` :
          `<div style="font-size:580px;line-height:1;filter:drop-shadow(0 40px 80px rgba(0,0,0,.3));margin-top:60px;">${bigMascotEmoji}</div>`}
      </div>
    </div>
    <div class="sl-num" style="color:rgba(255,255,255,.08);">01</div>`;}"""

new_cover_spread = """<div class="sl-bg" style="background:#f5f5f4;position:absolute;inset:0;"></div>
    <div style="position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(circle at 25% 25%, rgba(10,10,10,.06) 0.7px, transparent 1px),radial-gradient(circle at 75% 75%, rgba(10,10,10,.04) 0.7px, transparent 1px);background-size:16px 16px;"></div>
    <div style="position:absolute;top:0;left:0;width:100%;height:6px;background:${c1};"></div>
    <div class="geo-ring" style="top:-200px;right:-200px;width:800px;height:800px;border-width:100px;border-color:rgba(10,10,10,.04);"></div>
    <div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 480px;align-items:center;padding:0 80px 0 100px;">
      <div style="display:flex;flex-direction:column;justify-content:center;">
        <div style="display:inline-flex;align-items:center;gap:12px;background:rgba(10,10,10,.05);border:1px solid rgba(163,163,163,.2);border-radius:9999px;padding:10px 28px;width:fit-content;margin-bottom:36px;">
          <div style="width:8px;height:8px;border-radius:50%;background:${c1};"></div>
          <span style="font-family:var(--fd);font-size:16px;font-weight:600;letter-spacing:.35em;text-transform:uppercase;color:#0a0a0a;">${e(tx('cover_badge',L))}</span>
        </div>
        <div style="font-family:var(--fd);font-size:88px;font-weight:600;line-height:.92;letter-spacing:-.04em;color:#0a0a0a;margin-bottom:24px;">${e(STATE.aiCoverH||tx('cover_h',L))}</div>
        <div style="font-size:26px;color:rgba(10,10,10,.5);line-height:1.5;max-width:640px;margin-bottom:48px;">${e(tx('cover_sub',L))} <strong style="color:#0a0a0a;font-weight:600;">${e(C)}</strong>.</div>
        <div style="display:flex;gap:0;border-top:1px solid rgba(10,10,10,.1);padding-top:32px;">
          <div style="flex:1;padding-right:32px;border-right:1px solid rgba(10,10,10,.08);">
            <div style="font-size:11px;letter-spacing:.35em;text-transform:uppercase;color:rgba(10,10,10,.35);margin-bottom:6px;">${tx('prepared',L)}</div>
            <div style="font-family:var(--fd);font-size:20px;font-weight:600;color:#0a0a0a;">${e(C)}</div>
          </div>
          <div style="flex:1;padding:0 32px;border-right:1px solid rgba(10,10,10,.08);">
            <div style="font-size:11px;letter-spacing:.35em;text-transform:uppercase;color:rgba(10,10,10,.35);margin-bottom:6px;">${tx('industry',L)}</div>
            <div style="font-family:var(--fd);font-size:20px;font-weight:600;color:#0a0a0a;">${e(IND)}</div>
          </div>
          <div style="flex:1;padding-left:32px;">
            <div style="font-size:11px;letter-spacing:.35em;text-transform:uppercase;color:rgba(10,10,10,.35);margin-bottom:6px;">${tx('kickoff',L)}</div>
            <div style="font-family:var(--fd);font-size:20px;font-weight:600;color:${c1};">${e(selDate?fmtDate(selDate):'—')}</div>
          </div>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;height:100%;">
        ${hasImg ? `<img src="${getMascotImageForSlide(sid)}" style="height:880px;max-width:520px;object-fit:contain;filter:drop-shadow(0 20px 60px rgba(0,0,0,.15));" alt="mascot"/>` :
          `<div style="font-size:580px;line-height:1;filter:drop-shadow(0 20px 40px rgba(0,0,0,.1));margin-top:60px;">${bigMascotEmoji}</div>`}
      </div>
    </div>
    <div class="sl-num" style="color:rgba(10,10,10,.05);">01</div>`;}"""

if old_cover_spread in src:
    src = src.replace(old_cover_spread, new_cover_spread)
    changes += 1
    print("✅ 2. Cover slide (spread) → monochrome + brand accent strip")
else:
    print("⚠️ 2. Cover spread not found")

# ─── 3. Fix slide watermark logo for light bg ───
# Since all slides are now light bg, the logo should be normal (black)
old_logo = """div.insertAdjacentHTML('beforeend','<div style="position:absolute;top:38px;right:64px;z-index:99;pointer-events:none;user-select:none;"><img src="logo.png" alt="notso.ai" style="height:28px;'+(_lgl?'':'filter:brightness(0) invert(1);')+'"></div>');"""
new_logo = """div.insertAdjacentHTML('beforeend','<div style="position:absolute;top:38px;right:64px;z-index:99;pointer-events:none;user-select:none;"><img src="logo.png" alt="notso.ai" style="height:28px;"></div>');"""
if old_logo in src:
    src = src.replace(old_logo, new_logo)
    changes += 1
    print("✅ 3. Slide logo → always black (light bg)")
else:
    print("⚠️ 3. Slide logo not found")

# ─── 4. Update slide CSS: geo-ring, sl-num, body fonts to match setup ───
# Make geo-rings more subtle
old_geo = ".geo-ring{position:absolute;border-radius:50%;border-style:solid;pointer-events:none;}"
new_geo = ".geo-ring{position:absolute;border-radius:50%;border-style:solid;pointer-events:none;opacity:.6;}"
if old_geo in src:
    src = src.replace(old_geo, new_geo)
    changes += 1
    print("✅ 4. Geo-rings → more subtle")
else:
    print("⚠️ 4. Geo-ring CSS not found")

# ─── 5. Update slide dot grid background for monochrome slides ───
# Add a consistent dot grid to the slide canvas
old_canvas = ".slide-canvas{width:1920px;height:1080px;position:relative;overflow:hidden;}"
new_canvas = """.slide-canvas{width:1920px;height:1080px;position:relative;overflow:hidden;}
.slide-canvas::after{content:'';position:absolute;inset:0;pointer-events:none;z-index:1;background-image:radial-gradient(circle, rgba(10,10,10,.04) 0.6px, transparent 0.6px);background-size:20px 20px;opacity:.5;}"""
if old_canvas in src:
    src = src.replace(old_canvas, new_canvas)
    changes += 1
    print("✅ 5. Added dot grid to slide canvas")
else:
    print("⚠️ 5. Slide canvas CSS not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

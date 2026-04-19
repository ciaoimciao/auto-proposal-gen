#!/usr/bin/env python3
"""Redesign setup page to match HeroOrbitDeck monochrome style."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── COMPLETE CSS REPLACEMENT for setup section ───

OLD_CSS_START = """/* ═══════════════════════════════════════
   SETUP — LIGHT UI
═══════════════════════════════════════ */"""

# Find the end of setup CSS (before the deck view section)
OLD_CSS_END = """.sf{animation:fadeInUp .6s ease .3s both;}"""

# Find the block
start_i = src.find(OLD_CSS_START)
end_i = src.find(OLD_CSS_END)
if start_i == -1 or end_i == -1:
    print("❌ Could not locate setup CSS block")
    exit(1)

end_i += len(OLD_CSS_END)

NEW_CSS = """/* ═══════════════════════════════════════
   SETUP — MONOCHROME DECK UI
═══════════════════════════════════════ */
#setup-view{
  min-height:100vh;position:relative;isolation:isolate;
  background-color:#f5f5f4;color:#0a0a0a;
  font-family:'DM Sans',sans-serif;
}
/* ── dot grid bg ── */
#setup-view::before{
  content:'';position:absolute;inset:0;z-index:-2;
  background-image:
    radial-gradient(circle at 25% 25%, rgba(17,17,17,.10) 0.7px, transparent 1px),
    radial-gradient(circle at 75% 75%, rgba(17,17,17,.07) 0.7px, transparent 1px);
  background-size:14px 14px;opacity:.8;pointer-events:none;
}
/* ── top radial glow ── */
#setup-view::after{
  content:'';position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(ellipse 80% 60% at 10% -10%, rgba(15,15,15,.10), transparent 60%),
    radial-gradient(ellipse 90% 70% at 90% -20%, rgba(15,15,15,.06), transparent 70%),
    radial-gradient(60% 50% at 50% 8%, rgba(17,17,17,.09), transparent 70%);
  filter:blur(18px);
}

/* ── floating nav ── */
.sn{
  display:flex;align-items:center;justify-content:space-between;
  padding:.6rem 1.6rem;
  background:rgba(245,245,244,.82);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
  border-radius:9999px;border:1px solid rgba(163,163,163,.22);
  box-shadow:0 2px 16px rgba(0,0,0,.04);
  position:fixed;top:18px;left:50%;transform:translateX(-50%);
  z-index:100;width:auto;max-width:640px;
  gap:1rem;
}
.sn-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:1.15rem;letter-spacing:-.04em;color:#0a0a0a;}
.sn-logo span{color:#0a0a0a;}
.sn-chip{
  font-size:.6rem;font-weight:600;
  text-transform:uppercase;letter-spacing:.35em;
  background:transparent;color:#525252;
  padding:4px 14px;border-radius:9999px;
  border:1px solid rgba(163,163,163,.3);
}

/* ── hero header ── */
.sh{
  padding:7.5rem 2rem 2rem;max-width:1100px;margin:0 auto;
  display:flex;flex-direction:column;align-items:flex-start;text-align:left;gap:2.5rem;
}
.sh-eyebrow{
  font-size:.6rem;font-weight:600;letter-spacing:.4em;text-transform:uppercase;
  color:#525252;margin-bottom:0;
  display:inline-flex;align-items:center;gap:8px;
  padding:6px 18px;background:rgba(163,163,163,.12);
  border:1px solid rgba(163,163,163,.22);border-radius:9999px;
}
.sh-eyebrow::before{
  content:'';display:inline-block;width:6px;height:6px;border-radius:50%;
  background:#0a0a0a;animation:hero3-pulse-dot 2.5s ease-in-out infinite;
}
@keyframes hero3-pulse-dot{0%,100%{opacity:.3}50%{opacity:1}}
.sh-title{
  font-family:'Syne',sans-serif;font-weight:600;
  font-size:clamp(2.2rem,5.5vw,3.8rem);line-height:1.08;
  letter-spacing:-.035em;margin-bottom:0;color:#0a0a0a;
}
.sh-title em{color:#0a0a0a;font-style:normal;font-weight:600;}
.sh-sub{
  font-size:1.05rem;color:#525252;line-height:1.75;margin-bottom:0;
  max-width:640px;
}
.sh-cta{
  display:inline-flex;align-items:center;gap:8px;
  background:#0a0a0a;color:#fff;
  font-family:'Syne',sans-serif;font-weight:600;font-size:.82rem;
  padding:.65rem 1.6rem;border-radius:9999px;
  cursor:pointer;border:none;transition:all .25s ease;
  letter-spacing:.02em;
}
.sh-cta:hover{transform:translateY(-1px);box-shadow:0 8px 28px rgba(0,0,0,.18);background:#1a1a1a;}

/* ── feature stat cards ── */
.sh-stats{
  display:grid;grid-template-columns:repeat(4,1fr);gap:.65rem;
  width:100%;max-width:1100px;
}
.sh-stat{
  background:rgba(245,245,244,.7);backdrop-filter:blur(6px);
  border:1px solid rgba(163,163,163,.22);border-radius:20px;
  padding:1.1rem 1rem;display:flex;flex-direction:column;align-items:flex-start;
  gap:10px;text-align:left;
  transition:transform .3s,box-shadow .3s;position:relative;overflow:hidden;
}
.sh-stat::after{
  content:'';position:absolute;inset:0;opacity:0;transition:opacity .4s;pointer-events:none;
  background:radial-gradient(180px circle at 50% 20%, rgba(17,17,17,.06), transparent 70%);
}
.sh-stat:hover{transform:translateY(-3px);box-shadow:0 12px 32px rgba(0,0,0,.08);}
.sh-stat:hover::after{opacity:1;}
.sh-stat-ico{font-size:1.2rem;}
.sh-stat-val{font-family:'Syne',sans-serif;font-weight:600;font-size:.88rem;letter-spacing:-.02em;color:#0a0a0a;text-transform:uppercase;letter-spacing:.04em;}
.sh-stat-lbl{font-size:.72rem;color:#525252;line-height:1.5;}

/* ── form container ── */
.sf{max-width:780px;margin:0 auto;padding:1rem 2rem 5rem;}

/* ── sections ── */
.sec{
  margin-bottom:2.5rem;
  background:rgba(245,245,244,.6);backdrop-filter:blur(4px);
  border:1px solid rgba(163,163,163,.18);border-radius:24px;
  padding:2rem;
}
.sec-hdr{
  display:flex;align-items:flex-start;gap:12px;margin-bottom:1.5rem;
  padding-bottom:.85rem;border-bottom:1px solid rgba(163,163,163,.18);
}
.sec-num{
  width:28px;height:28px;border-radius:50%;background:#0a0a0a;color:#fff;
  font-family:'Syne',sans-serif;font-size:.7rem;font-weight:700;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.sec-ttl{
  font-family:'Syne',sans-serif;font-weight:600;font-size:1rem;
  letter-spacing:-.01em;color:#0a0a0a;text-transform:uppercase;letter-spacing:.06em;
}
.sec-sub{font-size:.78rem;color:#737373;margin-top:2px;}

/* ── form fields ── */
.fg{margin-bottom:.9rem;}
.fl{
  display:block;font-size:.6rem;font-weight:600;
  letter-spacing:.35em;text-transform:uppercase;
  color:#737373;margin-bottom:.4rem;
}
.fi{
  width:100%;background:rgba(255,255,255,.6);backdrop-filter:blur(4px);
  border:1px solid rgba(163,163,163,.25);border-radius:12px;
  padding:.65rem 1rem;color:#0a0a0a;
  font-family:'Inter','DM Sans',sans-serif;font-size:.88rem;
  transition:border-color .2s,box-shadow .2s;outline:none;
}
.fi:focus{border-color:#0a0a0a;box-shadow:0 0 0 3px rgba(10,10,10,.06);}
.fi::placeholder{color:#a3a3a3;}
textarea.fi{resize:vertical;min-height:72px;}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:.85rem;}

/* ── calendar (monochrome) ── */
.cal-wrap{position:relative;}
.cal-trig{
  width:100%;background:rgba(255,255,255,.6);backdrop-filter:blur(4px);
  border:1px solid rgba(163,163,163,.25);border-radius:12px;
  padding:.65rem 1rem;color:#0a0a0a;
  font-family:'DM Sans',sans-serif;font-size:.88rem;
  cursor:pointer;text-align:left;display:flex;align-items:center;justify-content:space-between;
  transition:border-color .2s;
}
.cal-trig:hover,.cal-trig.open{border-color:#0a0a0a;}
.cal-pop{
  position:absolute;top:calc(100% + 6px);left:0;z-index:400;
  background:rgba(255,255,255,.92);backdrop-filter:blur(16px);
  border:1px solid rgba(163,163,163,.22);border-radius:16px;
  padding:1rem;width:280px;box-shadow:0 12px 40px rgba(0,0,0,.1);
}
.cal-pop.hidden{display:none;}
.cal-hdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:.75rem;}
.cal-mon{font-family:'Syne',sans-serif;font-size:.85rem;font-weight:700;color:#0a0a0a;}
.cal-nav{background:none;border:1px solid rgba(163,163,163,.3);cursor:pointer;color:#737373;font-size:1rem;padding:1px 7px;border-radius:8px;transition:all .15s;}
.cal-nav:hover{border-color:#0a0a0a;color:#0a0a0a;}
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;}
.cal-dow{font-size:.6rem;text-align:center;color:#a3a3a3;padding-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.1em;}
.cal-day{aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:.78rem;border-radius:8px;cursor:pointer;color:#404040;transition:all .15s;}
.cal-day:hover:not(.empty):not(.disabled){background:rgba(10,10,10,.06);color:#0a0a0a;}
.cal-day.today{border:1.5px solid #0a0a0a;color:#0a0a0a;font-weight:600;}
.cal-day.selected{background:#0a0a0a!important;color:#fff!important;font-weight:700;}
.cal-day.empty,.cal-day.disabled{cursor:default;opacity:.22;pointer-events:none;}
.cal-foot{margin-top:.65rem;padding-top:.65rem;border-top:1px solid rgba(163,163,163,.18);display:flex;align-items:center;justify-content:space-between;}
.cal-clr{background:none;border:none;color:#737373;font-size:.74rem;cursor:pointer;font-family:'DM Sans',sans-serif;}
.cal-ok{background:#0a0a0a;border:none;border-radius:9999px;padding:5px 16px;font-size:.72rem;font-weight:600;font-family:'Syne',sans-serif;color:#fff;cursor:pointer;letter-spacing:.05em;}

/* ── roadmap preview ── */
.rm-prev{margin-top:.65rem;background:rgba(10,10,10,.03);border:1px solid rgba(163,163,163,.2);border-radius:14px;padding:.65rem .9rem;display:none;}
.rm-prev.show{display:block;}
.rm-prev-ttl{font-size:.6rem;text-transform:uppercase;letter-spacing:.35em;color:#525252;font-weight:600;margin-bottom:.4rem;}
.rm-pi{font-size:.78rem;color:#525252;display:flex;gap:8px;line-height:1.65;}
.rm-pi-d{color:#0a0a0a;min-width:82px;font-weight:600;}

/* ── AI section ── */
.api-hint{font-size:.7rem;color:#737373;margin-top:.3rem;}
.ai-row{display:flex;gap:.6rem;align-items:center;flex-wrap:wrap;margin-top:.5rem;}
.ai-btn{
  display:flex;align-items:center;gap:5px;
  padding:6px 18px;background:#0a0a0a;color:#fff;
  border:none;border-radius:9999px;
  font-size:.72rem;font-weight:600;font-family:'Syne',sans-serif;
  cursor:pointer;transition:all .2s;
  letter-spacing:.03em;text-transform:uppercase;
}
.ai-btn:hover{opacity:.85;transform:translateY(-1px);}
.ai-btn.loading{opacity:.4;pointer-events:none;}
.ai-btn.orange{background:#404040;}
.ai-st{font-size:.74rem;color:#737373;}

/* ── context boxes ── */
.ctx-box{
  margin-top:.75rem;padding:1rem 1.1rem;
  background:rgba(255,255,255,.4);backdrop-filter:blur(4px);
  border-radius:16px;border:1px solid rgba(163,163,163,.2);
}
.ctx-lbl{font-size:.6rem;font-weight:600;text-transform:uppercase;letter-spacing:.35em;color:#737373;margin-bottom:.6rem;}

/* ── generate button ── */
.btn-gen{
  width:100%;padding:1rem 2rem;
  background:#0a0a0a;color:#fff;border:none;border-radius:9999px;
  font-family:'Syne',sans-serif;font-size:1rem;font-weight:600;
  cursor:pointer;transition:all .25s ease;margin-top:1.5rem;
  letter-spacing:.03em;
}
.btn-gen:hover{transform:translateY(-2px);box-shadow:0 12px 36px rgba(0,0,0,.2);background:#1a1a1a;}

/* ── Animations (HeroOrbitDeck-inspired) ── */
@keyframes hero3-intro{
  0%{opacity:0;transform:translate3d(0,64px,0) scale(.98);filter:blur(12px);}
  60%{filter:blur(0);}
  100%{opacity:1;transform:translate3d(0,0,0) scale(1);filter:blur(0);}
}
@keyframes hero3-card{
  0%{opacity:0;transform:translate3d(0,32px,0) scale(.95);}
  100%{opacity:1;transform:translate3d(0,0,0) scale(1);}
}
@keyframes fadeInUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.sh{animation:hero3-intro 1s cubic-bezier(.22,.68,0,1) forwards;}
.sh-stats{animation:hero3-card .7s cubic-bezier(.22,.68,0,1) .2s both;}
.sf{animation:hero3-card .7s cubic-bezier(.22,.68,0,1) .35s both;}"""

src = src[:start_i] + NEW_CSS + src[end_i:]
changes += 1
print(f"✅ 1. Replaced entire setup CSS block")

# ─── Fix responsive breakpoint ───
old_responsive = """.sh{grid-template-columns:1fr;gap:28px;padding:2.5rem 1.5rem 2rem;}
  .sf{padding:0 1.5rem 3rem;}
  .fr{grid-template-columns:1fr;}
  .sn{padding:.85rem 1.5rem;}"""

new_responsive = """.sh{padding:6rem 1.5rem 2rem;gap:2rem;}
  .sh-stats{grid-template-columns:1fr 1fr;}
  .sf{padding:0 1.5rem 3rem;}
  .sec{padding:1.25rem;}
  .fr{grid-template-columns:1fr;}
  .sn{padding:.5rem 1.2rem;width:auto;max-width:calc(100% - 40px);}"""

if old_responsive in src:
    src = src.replace(old_responsive, new_responsive)
    changes += 1
    print("✅ 2. Updated responsive breakpoint")
else:
    print("⚠️ 2. Responsive breakpoint not found")

# ─── Update HTML: chip styling ───
old_chip = '<div class="sn-chip">Proposal Generator v6</div>'
new_chip = '<div class="sn-chip">Proposal Generator</div>'
if old_chip in src:
    src = src.replace(old_chip, new_chip)
    changes += 1
    print("✅ 3. Updated chip text")
else:
    print("⚠️ 3. Chip not found")

# ─── Update hero title ───
old_title = '<h1 class="sh-title">Build your<br/><em>proposal deck</em><br/>in minutes.</h1>'
new_title = '<h1 class="sh-title">Command deck for proposals that demand precision.</h1>'
if old_title in src:
    src = src.replace(old_title, new_title)
    changes += 1
    print("✅ 4. Updated hero title")
else:
    print("⚠️ 4. Title not found")

# ─── Update subtitle ───
old_sub = '<p class="sh-sub">Enter client details below. After generating, use the right-hand panel to adjust colours, font, language, slides, and upload mascot images — all live.</p>'
new_sub = '<p class="sh-sub">Enter client intelligence below. The deck combines live toggles, brand theming, and AI-generated copy for a distinct proposal every time.</p>'
if old_sub in src:
    src = src.replace(old_sub, new_sub)
    changes += 1
    print("✅ 5. Updated subtitle")
else:
    print("⚠️ 5. Subtitle not found")

# ─── Update eyebrow ───
old_eye = '<div class="sh-eyebrow">Internal Tool</div>'
new_eye = '<div class="sh-eyebrow">Notso.ai Proposal Deck</div>'
if old_eye in src:
    src = src.replace(old_eye, new_eye)
    changes += 1
    print("✅ 6. Updated eyebrow")
else:
    print("⚠️ 6. Eyebrow not found")

# ─── Update CTA ───
old_cta = """Start →</button>"""
new_cta = """Begin setup ↓</button>"""
if old_cta in src:
    src = src.replace(old_cta, new_cta, 1)
    changes += 1
    print("✅ 7. Updated CTA text")
else:
    print("⚠️ 7. CTA not found")

# ─── Remove emojis from stat cards, replace with monochrome labels ───
old_stats = """<div class="sh-stats">
      <div class="sh-stat"><div class="sh-stat-ico">🎨</div><div><div class="sh-stat-val">Brand-colored</div><div class="sh-stat-lbl">Slides use your client's primary color as background</div></div></div>
      <div class="sh-stat"><div class="sh-stat-ico">🖼️</div><div><div class="sh-stat-val">Mascot upload</div><div class="sh-stat-lbl">Drop in mascot images — auto-placed on the right slides</div></div></div>
      <div class="sh-stat"><div class="sh-stat-ico">☀️🌙</div><div><div class="sh-stat-val">Panel theme</div><div class="sh-stat-lbl">Toggle settings panel light or dark</div></div></div>
      <div class="sh-stat"><div class="sh-stat-ico">🌍</div><div><div class="sh-stat-val">Full translation</div><div class="sh-stat-lbl">Every word on every slide, 7 languages</div></div></div>
    </div>"""

new_stats = """<div class="sh-stats">
      <div class="sh-stat"><div class="sh-stat-ico" style="font-size:.72rem;font-weight:600;letter-spacing:.3em;opacity:.45;">01</div><div><div class="sh-stat-val">Brand-colored</div><div class="sh-stat-lbl">Slides adapt to your client's primary color palette</div></div></div>
      <div class="sh-stat"><div class="sh-stat-ico" style="font-size:.72rem;font-weight:600;letter-spacing:.3em;opacity:.45;">02</div><div><div class="sh-stat-val">Mascot upload</div><div class="sh-stat-lbl">Drop in mascot images — auto-placed on the right slides</div></div></div>
      <div class="sh-stat"><div class="sh-stat-ico" style="font-size:.72rem;font-weight:600;letter-spacing:.3em;opacity:.45;">03</div><div><div class="sh-stat-val">Panel theme</div><div class="sh-stat-lbl">Toggle settings panel light or dark in realtime</div></div></div>
      <div class="sh-stat"><div class="sh-stat-ico" style="font-size:.72rem;font-weight:600;letter-spacing:.3em;opacity:.45;">04</div><div><div class="sh-stat-val">Translation</div><div class="sh-stat-lbl">Every word on every slide, 7 languages supported</div></div></div>
    </div>"""

if old_stats in src:
    src = src.replace(old_stats, new_stats)
    changes += 1
    print("✅ 8. Updated stat cards to monochrome")
else:
    print("⚠️ 8. Stats not found")

# ─── Fix inline styles that use old colors ───
# Golden box
old_golden = 'style="border-color:rgba(201,100,66,.25);background:rgba(201,100,66,.04);margin-top:.9rem;"'
new_golden = 'style="border-color:rgba(10,10,10,.12);background:rgba(10,10,10,.02);margin-top:.9rem;"'
if old_golden in src:
    src = src.replace(old_golden, new_golden)
    changes += 1
    print("✅ 9. Fixed golden box border")
else:
    print("⚠️ 9. Golden box not found")

old_golden_lbl = 'style="color:var(--or);"'
new_golden_lbl = 'style="color:#0a0a0a;"'
# Only replace the first occurrence (in the ctx-lbl)
idx = src.find(old_golden_lbl)
if idx != -1:
    src = src[:idx] + new_golden_lbl + src[idx+len(old_golden_lbl):]
    changes += 1
    print("✅ 10. Fixed golden label color")
else:
    print("⚠️ 10. Golden label not found")

# Quote highlight
old_quote = 'style="color:#c96442;font-weight:700;"'
new_quote = 'style="color:#0a0a0a;font-weight:700;"'
if old_quote in src:
    src = src.replace(old_quote, new_quote, 1)
    changes += 1
    print("✅ 11. Fixed quote highlight")
else:
    print("⚠️ 11. Quote not found")

# Tools subtitle
old_tools = 'style="color:#83827d;font-weight:400;"'
new_tools = 'style="color:#737373;font-weight:400;"'
if old_tools in src:
    src = src.replace(old_tools, new_tools, 1)
    changes += 1
    print("✅ 12. Fixed tools subtitle color")
else:
    print("⚠️ 12. Tools subtitle not found")

# API link
old_api = 'style="color:#c96442;"'
new_api = 'style="color:#0a0a0a;text-decoration:underline;"'
if old_api in src:
    src = src.replace(old_api, new_api, 1)
    changes += 1
    print("✅ 13. Fixed API link color")
else:
    print("⚠️ 13. API link not found")

# Calendar display placeholder
old_cal_disp = 'style="color:#b4b2a7;"'
new_cal_disp = 'style="color:#a3a3a3;"'
if old_cal_disp in src:
    src = src.replace(old_cal_disp, new_cal_disp, 1)
    changes += 1
    print("✅ 14. Fixed calendar display color")
else:
    print("⚠️ 14. Calendar display not found")

# AI tags inline styles
old_tags_bg = "background:#f5f4ee;border-radius:8px;border:1.5px solid #dad9d4"
new_tags_bg = "background:rgba(245,245,244,.6);border-radius:14px;border:1px solid rgba(163,163,163,.18)"
if old_tags_bg in src:
    src = src.replace(old_tags_bg, new_tags_bg)
    changes += 1
    print("✅ 15. Fixed AI tags container")
else:
    print("⚠️ 15. AI tags container not found")

old_tag_label = 'font-size:.66rem;color:#83827d'
new_tag_label = 'font-size:.6rem;color:#737373;letter-spacing:.1em;text-transform:uppercase'
if old_tag_label in src:
    src = src.replace(old_tag_label, new_tag_label)
    changes += 1
    print("✅ 16. Fixed tag label")
else:
    print("⚠️ 16. Tag label not found")

old_tag_pill = "background:#ede9de;border:1px solid #dad9d4;color:#535146"
new_tag_pill = "background:rgba(10,10,10,.05);border:1px solid rgba(163,163,163,.22);color:#525252"
if old_tag_pill in src:
    src = src.replace(old_tag_pill, new_tag_pill, 6)
    changes += 1
    print("✅ 17. Fixed tag pills (all instances)")
else:
    print("⚠️ 17. Tag pills not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} change groups applied.")

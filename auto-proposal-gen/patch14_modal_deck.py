#!/usr/bin/env python3
"""Fix missing modal CSS + restyle deck view to monochrome."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Add back modal CSS (was accidentally removed) ───
# Insert before the Animations section
anchor = "/* ── Animations (HeroOrbitDeck-inspired) ── */"
modal_css = """/* ── Modal (monochrome) ── */
.modal-bg{position:fixed;inset:0;background:rgba(10,10,10,.45);z-index:600;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(6px);}
.modal-bg.hidden{display:none!important;}
.modal{background:rgba(255,255,255,.95);backdrop-filter:blur(16px);border-radius:24px;padding:2rem;width:100%;max-width:500px;box-shadow:0 24px 64px rgba(0,0,0,.12);border:1px solid rgba(163,163,163,.2);}
.modal-ttl{font-family:'Syne',sans-serif;font-weight:600;font-size:1.1rem;margin-bottom:.25rem;color:#0a0a0a;letter-spacing:-.01em;}
.modal-sub{font-size:.78rem;color:#737373;margin-bottom:1rem;}
.modal-close{float:right;background:none;border:1px solid rgba(163,163,163,.25);font-size:.9rem;cursor:pointer;color:#737373;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:all .15s;}
.modal-close:hover{background:#0a0a0a;color:#fff;border-color:#0a0a0a;}
.modal-out{background:rgba(10,10,10,.03);border:1px solid rgba(163,163,163,.18);border-radius:14px;padding:1rem;font-size:.85rem;line-height:1.65;color:#525252;min-height:80px;}
.modal-btns{display:flex;gap:.65rem;margin-top:1rem;}
.modal-btn{flex:1;padding:.6rem 1rem;border-radius:9999px;font-family:'Syne',sans-serif;font-weight:600;font-size:.8rem;cursor:pointer;border:none;transition:all .15s;letter-spacing:.02em;}
.modal-btn.p{background:#0a0a0a;color:#fff;}
.modal-btn.p:hover{background:#1a1a1a;transform:translateY(-1px);}
.modal-btn.s{background:transparent;border:1px solid rgba(163,163,163,.3);color:#525252;}
.modal-btn.s:hover{border-color:#0a0a0a;color:#0a0a0a;}

"""

if anchor in src:
    src = src.replace(anchor, modal_css + anchor)
    changes += 1
    print("✅ 1. Added modal CSS (monochrome)")
else:
    print("❌ 1. Anchor not found")

# ─── 2. Restyle deck view background ───
old = "#deck-view{display:none;flex-direction:row;height:100vh;overflow:hidden;background:#111110;}"
new = "#deck-view{display:none;flex-direction:row;height:100vh;overflow:hidden;background:#f5f5f4;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 2. Deck view background → #f5f5f4")
else:
    print("⚠️ 2. Deck bg not found")

# ─── 3. Restyle deck topbar ───
old = ".dtb{display:flex;align-items:center;justify-content:space-between;padding:.6rem 1.25rem;border-bottom:1px solid rgba(255,255,255,.07);background:rgba(17,17,16,.96);backdrop-filter:blur(12px);flex-shrink:0;gap:.5rem;flex-wrap:wrap;}"
new = ".dtb{display:flex;align-items:center;justify-content:space-between;padding:.6rem 1.25rem;border-bottom:1px solid rgba(163,163,163,.18);background:rgba(245,245,244,.88);backdrop-filter:blur(16px);flex-shrink:0;gap:.5rem;flex-wrap:wrap;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 3. Deck topbar → monochrome light")
else:
    print("⚠️ 3. Deck topbar not found")

# ─── 4. Topbar logo ───
old = ".dtb-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:.95rem;letter-spacing:-.03em;color:#F5F2EC;}"
new = ".dtb-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:.95rem;letter-spacing:-.03em;color:#0a0a0a;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 4. Topbar logo → dark")
else:
    print("⚠️ 4. Topbar logo not found")

# ─── 5. Topbar logo span ───
old = ".dtb-logo span{color:var(--or);}"
new = ".dtb-logo span{color:#0a0a0a;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 5. Topbar logo span → dark")
else:
    print("⚠️ 5. Logo span not found")

# ─── 6. Slide counter ───
old = ".sctr{font-size:.76rem;color:#7A7870;font-variant-numeric:tabular-nums;min-width:40px;}"
new = ".sctr{font-size:.72rem;color:#737373;font-variant-numeric:tabular-nums;min-width:40px;letter-spacing:.05em;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 6. Slide counter → monochrome")
else:
    print("⚠️ 6. Slide counter not found")

# ─── 7. Nav buttons ───
old = ".nb{padding:.32rem .85rem;border-radius:8px;border:1px solid rgba(255,255,255,.12);background:transparent;color:#F5F2EC;font-family:'DM Sans',sans-serif;font-size:.78rem;cursor:pointer;transition:all .15s;white-space:nowrap;}"
new = ".nb{padding:.32rem .85rem;border-radius:9999px;border:1px solid rgba(163,163,163,.25);background:transparent;color:#0a0a0a;font-family:'DM Sans',sans-serif;font-size:.74rem;cursor:pointer;transition:all .15s;white-space:nowrap;letter-spacing:.02em;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 7. Nav buttons → rounded pill")
else:
    print("⚠️ 7. Nav buttons not found")

# ─── 8. Nav button hover ───
old = ".nb:hover:not(:disabled){background:rgba(255,255,255,.08);}"
new = ".nb:hover:not(:disabled){background:rgba(10,10,10,.05);}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 8. Nav hover → light")
else:
    print("⚠️ 8. Nav hover not found")

# ─── 9. Nav primary button ───
old = ".nb.p{background:var(--or);border-color:var(--or);}"
new = ".nb.p{background:#0a0a0a;border-color:#0a0a0a;color:#fff;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 9. Nav primary → black")
else:
    print("⚠️ 9. Nav primary not found")

# ─── 10. Nav primary hover ───
old = ".nb.p:hover:not(:disabled){background:#e85a2c;}"
new = ".nb.p:hover:not(:disabled){background:#1a1a1a;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 10. Nav primary hover → dark")
else:
    print("⚠️ 10. Nav primary hover not found")

# ─── 11. Nav active ───
old = ".nb.act{background:rgba(255,107,61,.15);border-color:rgba(255,107,61,.4);color:var(--or);}"
new = ".nb.act{background:rgba(10,10,10,.08);border-color:rgba(10,10,10,.25);color:#0a0a0a;font-weight:600;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 11. Nav active → monochrome")
else:
    print("⚠️ 11. Nav active not found")

# ─── 12. Nav back ───
old = ".nb.back{color:#7A7870;border-color:rgba(255,255,255,.1);}"
new = ".nb.back{color:#737373;border-color:rgba(163,163,163,.2);}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 12. Nav back → monochrome")
else:
    print("⚠️ 12. Nav back not found")

old = ".nb.back:hover{color:#F5F2EC;}"
new = ".nb.back:hover{color:#0a0a0a;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 12b. Nav back hover")
else:
    print("⚠️ 12b. Nav back hover not found")

# ─── 13. Dots bar ───
old = ".dot{width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,.2);transition:all .2s;cursor:pointer;}"
new = ".dot{width:5px;height:5px;border-radius:50%;background:rgba(10,10,10,.15);transition:all .2s;cursor:pointer;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 13. Dots → monochrome")
else:
    print("⚠️ 13. Dots not found")

old = ".dot.active{background:var(--or);width:16px;border-radius:3px;}"
new = ".dot.active{background:#0a0a0a;width:16px;border-radius:3px;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 13b. Active dot → black")
else:
    print("⚠️ 13b. Active dot not found")

# ─── 14. Edit bar ───
old = ".edit-bar{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);background:var(--or);color:#fff;font-size:.76rem;font-family:'Syne',sans-serif;font-weight:700;padding:6px 20px;border-radius:28px;pointer-events:none;z-index:999;opacity:0;transition:opacity .3s;white-space:nowrap;}"
new = ".edit-bar{position:fixed;bottom:14px;left:50%;transform:translateX(-50%);background:#0a0a0a;color:#fff;font-size:.72rem;font-family:'Syne',sans-serif;font-weight:600;padding:6px 22px;border-radius:9999px;pointer-events:none;z-index:999;opacity:0;transition:opacity .3s;white-space:nowrap;letter-spacing:.03em;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 14. Edit bar → monochrome")
else:
    print("⚠️ 14. Edit bar not found")

# ─── 15. Filmstrip ───
old = ".filmstrip{display:flex;gap:10px;padding:8px 16px;background:#1a1a18;border-top:1px solid rgba(255,255,255,.12);overflow-x:auto;flex-shrink:0;scrollbar-width:thin;scrollbar-color:rgba(255,255,255,.15) transparent;align-items:center;min-height:82px;}"
new = ".filmstrip{display:flex;gap:10px;padding:8px 16px;background:rgba(245,245,244,.92);border-top:1px solid rgba(163,163,163,.18);overflow-x:auto;flex-shrink:0;scrollbar-width:thin;scrollbar-color:rgba(10,10,10,.12) transparent;align-items:center;min-height:82px;}"
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 15. Filmstrip → light")
else:
    print("⚠️ 15. Filmstrip not found")

# ─── 16. Settings panel dark → monochrome dark ───
# The settings panel has its own dark/light system - update dark panel colors
# to use our monochrome palette instead of orange accent
replacements_sp = [
    # Dark panel background
    (".sp.dark{background:#1a1a18;border-left:1px solid rgba(255,255,255,.07);}",
     ".sp.dark{background:#1a1a1a;border-left:1px solid rgba(255,255,255,.08);}"),
    # Dark panel font hover
    (".sp.dark .sp-font:hover{border-color:rgba(255,107,61,.35);}",
     ".sp.dark .sp-font:hover{border-color:rgba(255,255,255,.3);}"),
    # Dark panel font selected
    (".sp.dark .sp-font.sel{border-color:var(--or);background:rgba(255,107,61,.08);}",
     ".sp.dark .sp-font.sel{border-color:#fff;background:rgba(255,255,255,.1);}"),
    # Dark layout active
    (".sp.dark .sp-layout-btn.active{border-color:var(--or);color:var(--or);background:rgba(255,107,61,.1);}",
     ".sp.dark .sp-layout-btn.active{border-color:#fff;color:#fff;background:rgba(255,255,255,.1);}"),
    # Dark lang hover
    (".sp.dark .sp-lang:hover{color:#F5F2EC;border-color:rgba(255,255,255,.25);}",
     ".sp.dark .sp-lang:hover{color:#fff;border-color:rgba(255,255,255,.3);}"),
    # Dark lang active
    (".sp.dark .sp-lang.active{background:rgba(255,107,61,.15);border-color:rgba(255,107,61,.4);color:var(--or);}",
     ".sp.dark .sp-lang.active{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.3);color:#fff;}"),
    # Dark slide hover
    (".sp.dark .sp-slide-item:hover{border-color:rgba(255,107,61,.3);}",
     ".sp.dark .sp-slide-item:hover{border-color:rgba(255,255,255,.25);}"),
    # Dark slide num
    (".sp.dark .sp-slide-num{color:var(--or);}",
     ".sp.dark .sp-slide-num{color:#a3a3a3;}"),
    # Dark upload hover
    (".sp.dark .sp-upload-zone:hover{border-color:var(--or);background:rgba(255,107,61,.05);}",
     ".sp.dark .sp-upload-zone:hover{border-color:rgba(255,255,255,.3);background:rgba(255,255,255,.05);}"),
    # Light panel font hover
    (".sp.light .sp-font:hover{border-color:rgba(255,107,61,.4);}",
     ".sp.light .sp-font:hover{border-color:#0a0a0a;}"),
    # Light panel font selected
    (".sp.light .sp-font.sel{border-color:var(--or);background:rgba(255,107,61,.07);}",
     ".sp.light .sp-font.sel{border-color:#0a0a0a;background:rgba(10,10,10,.05);}"),
    # Light layout hover
    (".sp.light .sp-layout-btn:hover{border-color:var(--or);color:var(--or);}",
     ".sp.light .sp-layout-btn:hover{border-color:#0a0a0a;color:#0a0a0a;}"),
    # Light layout active
    (".sp.light .sp-layout-btn.active{background:var(--or);border-color:var(--or);color:#fff;}",
     ".sp.light .sp-layout-btn.active{background:#0a0a0a;border-color:#0a0a0a;color:#fff;}"),
    # Light lang hover
    (".sp.light .sp-lang:hover{border-color:var(--or);color:var(--or);}",
     ".sp.light .sp-lang:hover{border-color:#0a0a0a;color:#0a0a0a;}"),
    # Light lang active
    (".sp.light .sp-lang.active{background:var(--or);border-color:var(--or);color:#fff;}",
     ".sp.light .sp-lang.active{background:#0a0a0a;border-color:#0a0a0a;color:#fff;}"),
    # Light slide hover
    (".sp.light .sp-slide-item:hover{border-color:var(--or);}",
     ".sp.light .sp-slide-item:hover{border-color:#0a0a0a;}"),
    # Light slide num
    (".sp.light .sp-slide-num{color:var(--or);}",
     ".sp.light .sp-slide-num{color:#525252;}"),
    # Light preset hover
    (".sp.light .sp-preset-btns button:hover{border-color:var(--or);color:var(--or);}",
     ".sp.light .sp-preset-btns button:hover{border-color:#0a0a0a;color:#0a0a0a;}"),
    # Light upload hover
    (".sp.light .sp-upload-zone:hover{border-color:var(--or);background:rgba(255,107,61,.04);}",
     ".sp.light .sp-upload-zone:hover{border-color:#0a0a0a;background:rgba(10,10,10,.03);}"),
    # sp-lbl-cnt (active slide count)
    (".sp-lbl-cnt{font-size:.85rem;color:var(--or);font-family:'Syne',sans-serif;font-weight:700;}",
     ".sp-lbl-cnt{font-size:.85rem;color:#0a0a0a;font-family:'Syne',sans-serif;font-weight:700;}"),
]

for i, (old_sp, new_sp) in enumerate(replacements_sp, 1):
    if old_sp in src:
        src = src.replace(old_sp, new_sp)
        changes += 1
        print(f"✅ 16.{i}. SP panel fix applied")
    else:
        print(f"⚠️ 16.{i}. SP pattern not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

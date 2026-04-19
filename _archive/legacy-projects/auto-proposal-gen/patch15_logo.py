#!/usr/bin/env python3
"""Replace all text-based notso.ai logos with logo.png image."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Setup page navbar logo ───
old = '<div class="sn-logo">notso<span>.</span>ai</div>'
new = '<div class="sn-logo"><img src="logo.png" alt="notso.ai" style="height:24px;"></div>'
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 1. Setup navbar logo → image")
else:
    print("⚠️ 1. Setup navbar logo not found")

# ─── 2. Deck view topbar logo ───
old = '<div class="dtb-logo">notso<span>.</span>ai</div>'
new = '<div class="dtb-logo"><img src="logo.png" alt="notso.ai" style="height:20px;filter:invert(1);"></div>'
# Note: deck topbar is now light bg, logo.png is black text, so no invert needed
# Actually the deck bg is now #f5f5f4 (light) so black logo is fine, no invert
new = '<div class="dtb-logo"><img src="logo.png" alt="notso.ai" style="height:20px;"></div>'
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 2. Deck topbar logo → image")
else:
    print("⚠️ 2. Deck topbar logo not found")

# ─── 3. Slide watermark logo (top-right corner on all slides) ───
# Replace the text-based logo with an img tag
# The original uses span elements with colors based on slide bg
old_slide_logo = """div.insertAdjacentHTML('beforeend','<div style="position:absolute;top:38px;right:64px;z-index:99;display:flex;align-items:center;gap:4px;font-family:Syne,sans-serif;font-weight:800;font-size:26px;letter-spacing:-.03em;pointer-events:none;user-select:none;"><span style="color:'+_lgc+';">notso</span><span style="color:'+_lgd+';">.</span><span style="color:'+_lgc+';">ai</span></div>');"""

# For slides: use the PNG with filter:invert for dark bg slides, normal for light bg slides
# _lgl is true for light-bg slides, false for dark-bg slides
# On light bg: black logo is fine (no filter)
# On dark bg: need filter:brightness(0) invert(1) to make it white
new_slide_logo = """div.insertAdjacentHTML('beforeend','<div style="position:absolute;top:38px;right:64px;z-index:99;pointer-events:none;user-select:none;"><img src="logo.png" alt="notso.ai" style="height:28px;'+(_lgl?'':'filter:brightness(0) invert(1);')+'"></div>');"""

if old_slide_logo in src:
    src = src.replace(old_slide_logo, new_slide_logo)
    changes += 1
    print("✅ 3. Slide watermark logo → image")
else:
    print("⚠️ 3. Slide watermark logo not found")

# ─── 4. Update CSS: sn-logo no longer needs text styling ───
old_css = ".sn-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:1.15rem;letter-spacing:-.04em;color:#0a0a0a;}\n.sn-logo span{color:#0a0a0a;}"
new_css = ".sn-logo{display:flex;align-items:center;}\n.sn-logo img{height:24px;}"
if old_css in src:
    src = src.replace(old_css, new_css)
    changes += 1
    print("✅ 4. Setup logo CSS → image style")
else:
    print("⚠️ 4. Setup logo CSS not found")

# ─── 5. Update CSS: dtb-logo ───
old_css2 = ".dtb-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:.95rem;letter-spacing:-.03em;color:#0a0a0a;}\n.dtb-logo span{color:#0a0a0a;}"
new_css2 = ".dtb-logo{display:flex;align-items:center;}\n.dtb-logo img{height:20px;}"
if old_css2 in src:
    src = src.replace(old_css2, new_css2)
    changes += 1
    print("✅ 5. Deck logo CSS → image style")
else:
    print("⚠️ 5. Deck logo CSS not found")

# ─── 6. Also remove the _lgc/_lgd color variables since they're no longer needed for the logo text ───
# Keep them because they might be used elsewhere — actually let's check
# _lgl is only used for the logo, so we can simplify but let's keep it safe

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

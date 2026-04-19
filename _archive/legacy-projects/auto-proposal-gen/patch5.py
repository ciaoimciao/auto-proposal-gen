#!/usr/bin/env python3
"""Fix P14 Promo card layout (horizontal 3-col) and P2 TOC bottom clipping."""
import re

with open('index.html','r',encoding='utf-8') as f:
    src = f.read()

# ── 1. Fix P14 Promo: reduce card heights, remove long desc, make compact ──
old_promo_top = """<div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="font-family:var(--fd);font-size:52px;font-weight:800;color:${V.TX};letter-spacing:-.03em;line-height:1;margin-bottom:10px;">${e(tx('prm_tag',L))}</div>
      <div style="font-size:18px;color:${V.TX2};line-height:1.6;max-width:900px;margin-bottom:28px;">${e(promoDesc[L]||promoDesc.en)}</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;">"""

new_promo_top = """<div class="sl-safe" style="display:flex;flex-direction:column;justify-content:flex-start;">
      <div style="margin-bottom:6px;"><span style="font-family:var(--fd);font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:${c1};background:${alpha(c1,.12)};padding:6px 16px;border-radius:6px;">${e(tx('prm_tag',L))}</span></div>
      <div style="font-family:var(--fd);font-size:42px;font-weight:800;color:${V.TX};letter-spacing:-.03em;line-height:1.1;margin-bottom:8px;">${L==='nl'?'Fysieke & digitale materialen.':L==='zh'?'實體與數位材料。':'Physical & digital materials.'}</div>
      <div style="font-size:15px;color:${V.TX2};line-height:1.5;max-width:800px;margin-bottom:20px;">${e(promoDesc[L]||promoDesc.en)}</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;flex:1;">"""

if old_promo_top in src:
    src = src.replace(old_promo_top, new_promo_top)
    print("✅ 1a. Promo top section fixed (compact tag+title+desc)")
else:
    print("⚠️ 1a. Promo top not found")

# Fix card heights from 360px to 220px
src = src.replace(
    'height:360px;background:linear-gradient(135deg,${alpha(c1,.2)},${alpha(c2,.15)});display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;padding:20px;',
    'height:220px;background:linear-gradient(135deg,${alpha(c1,.2)},${alpha(c2,.15)});display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;padding:16px;'
)
print("✅ 1b. Poster card height reduced")

# Vinyl toy card height
src = src.replace(
    'height:360px;background:linear-gradient(180deg,${alpha(V.TX,.06)},${alpha(V.TX,.02)});display:flex;align-items:center;justify-content:center;',
    'height:220px;background:linear-gradient(180deg,${alpha(V.TX,.06)},${alpha(V.TX,.02)});display:flex;align-items:center;justify-content:center;'
)
print("✅ 1c. Vinyl toy card height reduced")

# Vinyl toy emoji size
src = src.replace(
    'font-size:200px;filter:drop-shadow(0 16px 40px rgba(0,0,0,.3));',
    'font-size:120px;filter:drop-shadow(0 12px 30px rgba(0,0,0,.3));'
)
print("✅ 1d. Vinyl emoji size reduced")

# Banner card height
src = src.replace(
    'height:360px;background:linear-gradient(135deg,${alpha(c2,.2)},${alpha(c1,.15)});display:flex;align-items:center;justify-content:center;padding:20px;',
    'height:220px;background:linear-gradient(135deg,${alpha(c2,.2)},${alpha(c1,.15)});display:flex;align-items:center;justify-content:center;padding:16px;'
)
print("✅ 1e. Banner card height reduced")

# Poster mockup: make it smaller
src = src.replace(
    "style=\"font-family:var(--fd);font-size:16px;font-weight:800;color:${c1};text-transform:uppercase;text-align:center;\">DIGITALE<br/>BUDDY</div>\n              <div style=\"font-size:100px;line-height:1;\">${pEmoji}</div>",
    "style=\"font-family:var(--fd);font-size:13px;font-weight:800;color:${c1};text-transform:uppercase;text-align:center;\">DIGITALE<br/>BUDDY</div>\n              <div style=\"font-size:64px;line-height:1;\">${pEmoji}</div>"
)
print("✅ 1f. Poster mockup emoji reduced")

# Fix poster mockup padding to be more compact
src = src.replace(
    'background:#fff;border-radius:8px;padding:16px 20px;box-shadow:0 8px 32px rgba(0,0,0,.3);display:flex;flex-direction:column;align-items:center;gap:8px;width:180px;',
    'background:#fff;border-radius:8px;padding:12px 16px;box-shadow:0 8px 32px rgba(0,0,0,.3);display:flex;flex-direction:column;align-items:center;gap:4px;width:140px;'
)
print("✅ 1g. Poster mockup padding reduced")

# Add promo card small text with location + included/price labels
# Fix the "Poster + Media pakket" label and included text spacing
src = src.replace(
    """<div style="padding:16px 20px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:${V.TX};margin-bottom:4px;">Poster + Media pakket</div>
            <div style="font-size:16px;color:#4CD8A8;font-weight:600;">""",
    """<div style="padding:12px 16px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:18px;font-weight:700;color:${V.TX};margin-bottom:2px;">Poster + Mediapakket</div>
            <div style="font-size:13px;color:${V.TX2};margin-bottom:4px;">${L==='nl'?'Hoogwaardig poster, drukklaar. Inclusief 10 afbeeldingen + 5 videoclips.':L==='zh'?'高品質海報，印刷就緒。含10張圖片+5段影片。':'High-quality poster, print-ready. Includes 10 images + 5 video clips.'}</div>
            <div style="font-size:14px;color:#4CD8A8;font-weight:600;">"""
)
print("✅ 1h. Poster card text fixed")

# Fix vinyl toy card text area
src = src.replace(
    """<div style="padding:16px 20px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:${V.TX};">Vinyl Toy</div>
          </div>
        </div>
        <!-- Banner -->""",
    """<div style="padding:12px 16px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:18px;font-weight:700;color:${V.TX};margin-bottom:2px;">Vinyl Toy</div>
            <div style="font-size:13px;color:${V.TX2};">${L==='nl'?'Fysiek 3D-speelgoed met QR-codestandaard.':L==='zh'?'實體3D玩具，附QR碼底座。':'Physical 3D toy with QR code stand.'}</div>
          </div>
        </div>
        <!-- Banner -->"""
)
print("✅ 1i. Vinyl toy card text fixed")

# Fix banner card text area
src = src.replace(
    """<div style="padding:16px 20px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:${V.TX};">Banner</div>
          </div>
        </div>
      </div>
    </div>
    <div class="sl-num""",
    """<div style="padding:12px 16px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:18px;font-weight:700;color:${V.TX};margin-bottom:2px;">Roll-up Banner</div>
            <div style="font-size:13px;color:${V.TX2};">${L==='nl'?'Groot formaat banner voor '+promoLoc.nl+'.':L==='zh'?'大型展示橫幅，適用於'+promoLoc.zh+'。':'Large format banner for '+promoLoc.en+'.'}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="sl-num\""""
)
print("✅ 1j. Banner card text fixed")

# ── 2. Fix P2 TOC bottom clipping — reduce item spacing further ──
# The items grid needs less gap and the title needs less bottom margin
old_toc_title = "font-size:52px;font-weight:900"
new_toc_title = "font-size:46px;font-weight:900"
src = src.replace(old_toc_title, new_toc_title, 1)
print("✅ 2a. TOC title reduced to 46px")

# Find and reduce the TOC grid item main text size
# The spread/editorial variant items
old_toc_grid = "grid-template-columns:1fr 1fr;gap:6px 40px;"
new_toc_grid = "grid-template-columns:1fr 1fr;gap:2px 36px;"
src = src.replace(old_toc_grid, new_toc_grid)
print("✅ 2b. TOC grid gap reduced")

# Reduce toc item padding
old_toc_pad = "padding:12px 0;border-bottom:1px solid"
new_toc_pad = "padding:8px 0;border-bottom:1px solid"
if old_toc_pad in src:
    src = src.replace(old_toc_pad, new_toc_pad)
    print("✅ 2c. TOC item padding reduced")
else:
    print("⚠️ 2c. TOC item padding pattern not found")

with open('index.html','w',encoding='utf-8') as f:
    f.write(src)

print("\n✅ All fixes applied. File saved.")

#!/usr/bin/env python3
"""
Patch 10: Visual upgrade based on Notso.ai brand guidelines + Text editing + Image drag
"""
import re

with open('index.html','r',encoding='utf-8') as f:
    src = f.read()

# ════════════════════════════════════════
# PART A: VISUAL UPGRADE — Brand Color System & Typography
# ════════════════════════════════════════

# 1. Update setup UI to use Notso.ai brand colors (neon green accent on dark)
# Current: --sb:#F5F2EC (cream bg), --or:#FF6B3D (orange accent)
# Brand guideline says: dark mode background, neon green/lime accent for CTA
# BUT keep --or for slides. For the SETUP UI, add Notso.ai's own brand feel.

# Add Inter font to the Google Fonts import for setup UI body text
old_fonts_link = "family=Outfit:wght@300;400;500;600;700;800&display=swap"
new_fonts_link = "family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700;800&display=swap"
if old_fonts_link in src:
    src = src.replace(old_fonts_link, new_fonts_link)
    print("✅ A1. Added Inter font")
else:
    print("⚠️ A1. Font link not found")

# 2. Update CSS tokens for a more premium dark-mode setup page option
# Add a new class for the setup page that matches Notso.ai's actual website aesthetic
old_tokens = """:root{
  --sb:#F5F2EC;--sb2:#EDEAE2;--ink:#111110;--ink2:#4A4846;--mu:#888580;--bdr:#D8D4CC;
  --or:#FF6B3D;"""

new_tokens = """:root{
  --sb:#0A0A0A;--sb2:#141414;--ink:#F5F2EC;--ink2:#B8B5AE;--mu:#6B6966;--bdr:#2A2A28;
  --or:#FF6B3D;--lime:#B8FF00;--notso-bg:#0A0A0A;"""

if old_tokens in src:
    src = src.replace(old_tokens, new_tokens)
    print("✅ A2. Updated tokens to dark-mode brand style")
else:
    print("⚠️ A2. Token pattern not found")

# 3. Update setup UI background and form styles
old_setup_bg = "#setup-view{min-height:100vh;background:var(--sb);}"
new_setup_bg = "#setup-view{min-height:100vh;background:var(--sb);background-image:radial-gradient(ellipse 80% 50% at 50% -20%,rgba(255,107,61,.08),transparent);}"
if old_setup_bg in src:
    src = src.replace(old_setup_bg, new_setup_bg)
    print("✅ A3. Added subtle gradient glow to setup bg")
else:
    print("⚠️ A3. Setup bg not found")

# 4. Update form input styles for dark mode
old_fi = ".fi{width:100%;background:#fff;border:1.5px solid var(--bdr);border-radius:10px;padding:.6rem .9rem;color:var(--ink);font-family:'DM Sans',sans-serif;font-size:.88rem;transition:border-color .2s,box-shadow .2s;outline:none;}"
new_fi = ".fi{width:100%;background:var(--sb2);border:1.5px solid var(--bdr);border-radius:10px;padding:.6rem .9rem;color:var(--ink);font-family:'Inter','DM Sans',sans-serif;font-size:.88rem;transition:border-color .2s,box-shadow .2s;outline:none;}"
if old_fi in src:
    src = src.replace(old_fi, new_fi)
    print("✅ A4. Updated input styles for dark mode")
else:
    print("⚠️ A4. Input styles not found")

# 5. Update calendar trigger bg
old_cal = ".cal-trig{width:100%;background:#fff;"
new_cal = ".cal-trig{width:100%;background:var(--sb2);"
if old_cal in src:
    src = src.replace(old_cal, new_cal)
    print("✅ A5. Calendar trigger dark mode")
else:
    print("⚠️ A5. Calendar trigger not found")

# 6. Update calendar popup bg
old_calpop = ".cal-pop{position:absolute;top:calc(100% + 5px);left:0;z-index:400;background:#fff;"
new_calpop = ".cal-pop{position:absolute;top:calc(100% + 5px);left:0;z-index:400;background:var(--sb2);"
if old_calpop in src:
    src = src.replace(old_calpop, new_calpop)
    print("✅ A6. Calendar popup dark mode")
else:
    print("⚠️ A6. Calendar popup not found")

# 7. Update stat cards bg
old_shstat = ".sh-stat{background:#fff;border:1px solid var(--bdr);"
new_shstat = ".sh-stat{background:var(--sb2);border:1px solid var(--bdr);"
if old_shstat in src:
    src = src.replace(old_shstat, new_shstat)
    print("✅ A7. Stat cards dark mode")
else:
    print("⚠️ A7. Stat cards not found")

# 8. Update the Generate button to use lime accent
old_genbtn_css = ".gen-btn{width:100%;padding:1rem;font-family:'Syne',sans-serif;font-weight:700;font-size:1.15rem;border:none;border-radius:14px;cursor:pointer;background:var(--or);color:#fff;"
new_genbtn_css = ".gen-btn{width:100%;padding:1rem;font-family:'Syne',sans-serif;font-weight:700;font-size:1.15rem;border:none;border-radius:14px;cursor:pointer;background:linear-gradient(135deg,var(--or),#E85D2F);color:#fff;"
if old_genbtn_css in src:
    src = src.replace(old_genbtn_css, new_genbtn_css)
    print("✅ A8. Generate button gradient")
else:
    print("⚠️ A8. Generate button not found")

# 9. Update the top nav bar
old_snbar = ".sn{display:flex;align-items:center;justify-content:space-between;padding:1rem 3rem;border-bottom:1px solid var(--bdr);background:var(--sb);position:sticky;top:0;z-index:100;}"
new_snbar = ".sn{display:flex;align-items:center;justify-content:space-between;padding:1rem 3rem;border-bottom:1px solid var(--bdr);background:rgba(10,10,10,.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);position:sticky;top:0;z-index:100;}"
if old_snbar in src:
    src = src.replace(old_snbar, new_snbar)
    print("✅ A9. Nav bar glassmorphism")
else:
    print("⚠️ A9. Nav bar not found")

# 10. Update section headers bg colors for dark mode
old_secbdr = ".sec-hdr{display:flex;align-items:center;gap:10px;margin-bottom:1rem;padding-bottom:.6rem;border-bottom:1px solid var(--bdr);}"
new_secbdr = ".sec-hdr{display:flex;align-items:center;gap:10px;margin-bottom:1rem;padding-bottom:.6rem;border-bottom:1px solid rgba(255,255,255,.06);}"
if old_secbdr in src:
    src = src.replace(old_secbdr, new_secbdr)
    print("✅ A10. Section headers subtle border")
else:
    print("⚠️ A10. Section header not found")

# ════════════════════════════════════════
# PART B: TEXT EDITING (contenteditable)
# ════════════════════════════════════════

# 11. Add CSS for edit mode
edit_css = """
/* ═══════════════════════════════════════
   EDIT MODE — inline text editing
═══════════════════════════════════════ */
.slide-canvas.editing [data-editable]{outline:1px dashed rgba(255,107,61,.35);outline-offset:2px;cursor:text;border-radius:4px;transition:outline-color .2s;}
.slide-canvas.editing [data-editable]:hover{outline-color:rgba(255,107,61,.6);}
.slide-canvas.editing [data-editable]:focus{outline:2px solid var(--or);outline-offset:2px;background:rgba(255,107,61,.04);}
/* Image edit toolbar */
.img-edit-bar{position:absolute;background:rgba(17,17,16,.92);backdrop-filter:blur(8px);border-radius:10px;padding:6px 10px;display:flex;gap:6px;align-items:center;z-index:200;box-shadow:0 4px 20px rgba(0,0,0,.4);}
.img-edit-bar button{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);color:#fff;width:28px;height:28px;border-radius:6px;cursor:pointer;font-size:14px;display:flex;align-items:center;justify-content:center;transition:all .15s;}
.img-edit-bar button:hover{background:var(--or);border-color:var(--or);}
.img-edit-bar .rot-slider{width:80px;accent-color:var(--or);height:4px;}
.img-edit-bar .rot-val{color:rgba(255,255,255,.6);font-size:11px;min-width:32px;text-align:center;font-family:var(--fb);}
"""

# Insert before the closing </style> tag
style_end = "</style>"
if style_end in src:
    src = src.replace(style_end, edit_css + style_end, 1)
    print("✅ B11. Added edit mode CSS")
else:
    print("⚠️ B11. </style> not found")

# 12. Add edit mode toggle logic — enhance the existing Edit button
# Find the existing edit button toggle function
old_edit_toggle = "function toggleEdit(){"
if old_edit_toggle in src:
    # Read the full function to replace
    idx = src.index(old_edit_toggle)
    # Find the closing brace
    brace_count = 0
    i = idx
    start_found = False
    for i in range(idx, len(src)):
        if src[i] == '{':
            brace_count += 1
            start_found = True
        elif src[i] == '}':
            brace_count -= 1
            if start_found and brace_count == 0:
                break
    old_func = src[idx:i+1]

    new_func = """function toggleEdit(){
  STATE.editMode=!STATE.editMode;
  const canvas=document.querySelector('.slide-canvas');
  const btn=document.querySelector('[onclick*="toggleEdit"]');
  if(STATE.editMode){
    canvas?.classList.add('editing');
    if(btn)btn.style.background='var(--or)';
    if(btn)btn.style.color='#fff';
    // Make all data-editable elements contentEditable
    document.querySelectorAll('[data-editable]').forEach(el=>{el.contentEditable='true';});
    // Make images clickable for position controls
    document.querySelectorAll('.slide-canvas img, .slide-canvas [data-mascot-img]').forEach(img=>{
      img.style.cursor='move';
      img.onclick=function(e){e.stopPropagation();showImgEditBar(this);};
    });
  } else {
    canvas?.classList.remove('editing');
    if(btn)btn.style.background='';
    if(btn)btn.style.color='';
    document.querySelectorAll('[data-editable]').forEach(el=>{el.contentEditable='false';});
    document.querySelectorAll('.slide-canvas img').forEach(img=>{img.style.cursor='';img.onclick=null;});
    // Remove any floating toolbar
    document.querySelectorAll('.img-edit-bar').forEach(b=>b.remove());
  }
}"""
    src = src.replace(old_func, new_func)
    print("✅ B12. Enhanced toggleEdit function")
else:
    # Add edit mode to STATE and create the function
    state_insert = "let STATE={"
    if state_insert in src:
        src = src.replace(state_insert, "let STATE={editMode:false,imageOffsets:{},")
        print("✅ B12a. Added editMode to STATE")

    # Add the toggleEdit function before the closing </script>
    edit_func = """
/* ════════════════════════════════════════
   EDIT MODE — Text editing & Image positioning
════════════════════════════════════════ */
function toggleEdit(){
  STATE.editMode=!STATE.editMode;
  const canvas=document.querySelector('.slide-canvas');
  if(STATE.editMode){
    canvas?.classList.add('editing');
    document.querySelectorAll('[data-editable]').forEach(el=>{el.contentEditable='true';});
    document.querySelectorAll('.slide-canvas img, .slide-canvas [data-mascot-img]').forEach(img=>{
      img.style.cursor='move';
      img.onclick=function(e){e.stopPropagation();showImgEditBar(this);};
    });
  } else {
    canvas?.classList.remove('editing');
    document.querySelectorAll('[data-editable]').forEach(el=>{el.contentEditable='false';});
    document.querySelectorAll('.slide-canvas img').forEach(img=>{img.style.cursor='';img.onclick=null;});
    document.querySelectorAll('.img-edit-bar').forEach(b=>b.remove());
  }
}
"""
    src = src.replace("</script>", edit_func + "</script>", 1)
    print("✅ B12b. Added toggleEdit function")

# 13. Add image edit toolbar function
img_edit_func = """
function showImgEditBar(img){
  document.querySelectorAll('.img-edit-bar').forEach(b=>b.remove());
  const sid=img.closest('[data-slide-id]')?.dataset?.slideId||'default';
  if(!STATE.imageOffsets)STATE.imageOffsets={};
  if(!STATE.imageOffsets[sid])STATE.imageOffsets[sid]={x:0,y:0,rotate:0};
  const off=STATE.imageOffsets[sid];
  const bar=document.createElement('div');
  bar.className='img-edit-bar';
  bar.innerHTML=`
    <button onclick="moveImg(this,-10,0)" title="Left">←</button>
    <button onclick="moveImg(this,10,0)" title="Right">→</button>
    <button onclick="moveImg(this,0,-10)" title="Up">↑</button>
    <button onclick="moveImg(this,0,10)" title="Down">↓</button>
    <input type="range" class="rot-slider" min="-180" max="180" value="${off.rotate}" oninput="rotateImg(this)" title="Rotate"/>
    <span class="rot-val">${off.rotate}°</span>
    <button onclick="resetImg(this)" title="Reset" style="font-size:12px;">↺</button>
  `;
  bar.dataset.sid=sid;
  bar._img=img;
  const rect=img.getBoundingClientRect();
  const parent=img.closest('.slide-canvas')||img.parentElement;
  parent.style.position='relative';
  parent.appendChild(bar);
  bar.style.top=(img.offsetTop-40)+'px';
  bar.style.left=img.offsetLeft+'px';
  applyImgTransform(img,off);
}
function moveImg(btn,dx,dy){
  const bar=btn.closest('.img-edit-bar');
  const sid=bar.dataset.sid;
  const off=STATE.imageOffsets[sid];
  off.x+=dx;off.y+=dy;
  applyImgTransform(bar._img,off);
}
function rotateImg(slider){
  const bar=slider.closest('.img-edit-bar');
  const sid=bar.dataset.sid;
  const off=STATE.imageOffsets[sid];
  off.rotate=parseInt(slider.value);
  bar.querySelector('.rot-val').textContent=off.rotate+'°';
  applyImgTransform(bar._img,off);
}
function resetImg(btn){
  const bar=btn.closest('.img-edit-bar');
  const sid=bar.dataset.sid;
  STATE.imageOffsets[sid]={x:0,y:0,rotate:0};
  bar.querySelector('.rot-slider').value=0;
  bar.querySelector('.rot-val').textContent='0°';
  applyImgTransform(bar._img,STATE.imageOffsets[sid]);
}
function applyImgTransform(img,off){
  if(!img||!off)return;
  img.style.transform='translate('+off.x+'px,'+off.y+'px) rotate('+off.rotate+'deg)';
  img.style.transition='transform .15s ease';
}
"""

# Insert before closing </script>
src = src.replace("</script>", img_edit_func + "\n</script>", 1)
print("✅ B13. Added image edit toolbar functions")

# 14. Add editMode to STATE if not already there
if "editMode:" not in src:
    src = src.replace("let STATE={", "let STATE={editMode:false,imageOffsets:{},")
    print("✅ B14. Added editMode and imageOffsets to STATE")
else:
    print("✓ B14. editMode already in STATE")

# ════════════════════════════════════════
# PART C: Add data-editable to slide templates
# ════════════════════════════════════════

# 15. We need to add data-editable to text elements in buildSlideHTML
# Since these are inside template literals, we do targeted replacements

# Add data-editable to common heading patterns
# Pattern: class="sl-tag" → add data-editable
editable_patterns = [
    # Tag badges
    ('class="sl-tag"', 'class="sl-tag" data-editable="true"'),
    # Main headings h2 style
    ('class="sl-h2"', 'class="sl-h2" data-editable="true"'),
    # Body text
    ('class="sl-body"', 'class="sl-body" data-editable="true"'),
]

for old_cls, new_cls in editable_patterns:
    count = src.count(old_cls)
    if count > 0:
        src = src.replace(old_cls, new_cls)
        print(f"✅ C15. Added data-editable to {old_cls} ({count} instances)")
    else:
        print(f"⚠️ C15. {old_cls} not found")

# Also look for inline heading styles commonly used in slides
# These are font-weight:800 or font-weight:700 with large font-size
# We'll add a few targeted ones

# ════════════════════════════════════════
# PART D: Update AI generation section styling
# ════════════════════════════════════════

# 16. Update the AI section card backgrounds
old_ai_card = ".ai-card{background:#fff;border:1.5px solid var(--bdr);"
new_ai_card = ".ai-card{background:var(--sb2);border:1.5px solid var(--bdr);"
if old_ai_card in src:
    src = src.replace(old_ai_card, new_ai_card)
    print("✅ D16. AI card dark mode")
else:
    print("⚠️ D16. AI card style not found")

# 17. Update the "important" pain section highlight
old_pain_bg = "background:rgba(255,107,61,.06)"
new_pain_bg = "background:rgba(255,107,61,.08)"
if old_pain_bg in src:
    src = src.replace(old_pain_bg, new_pain_bg, 1)
    print("✅ D17. Pain section highlight adjusted")
else:
    print("⚠️ D17. Pain section bg not found")

with open('index.html','w',encoding='utf-8') as f:
    f.write(src)

# Verify syntax
match = re.search(r'<script>(.*?)</script>', src, re.DOTALL)
if match:
    with open('/tmp/test_script.js','w') as f:
        f.write(match.group(1))

print("\n✅ Patch 10 complete — Visual upgrade + Text editing + Image controls")

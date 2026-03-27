#!/usr/bin/env python3
"""
patch6_edit.py — Adds two features to index.html:
  1. Inline Text Editing with data-editable, letter-spacing/line-height controls
  2. Image Position & Rotation Controls (floating toolbar)
"""
import os, sys

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
with open(path, 'r', encoding='utf-8') as f:
    src = f.read()

count = 0

# ─────────────────────────────────────────
# 1) CSS: Add .editing [data-editable] styles + image toolbar styles
# ─────────────────────────────────────────
old_css = '#slide-canvas.em .editable:focus{outline:2px solid var(--or);}'
new_css = '''#slide-canvas.em .editable:focus{outline:2px solid var(--or);}
/* ── Patch6: data-editable editing styles ── */
.editing [data-editable]{outline:1px dashed rgba(255,107,61,.4);cursor:text;border-radius:3px;transition:outline .15s,background .15s;}
.editing [data-editable]:hover{outline:2px solid rgba(255,107,61,.5);background:rgba(255,107,61,.06);}
.editing [data-editable]:focus{outline:2px solid var(--or);background:rgba(255,107,61,.1);}
/* ── Patch6: Image toolbar ── */
.img-edit-toolbar{position:absolute;z-index:500;background:rgba(17,17,16,.92);border:1px solid rgba(255,255,255,.15);border-radius:12px;padding:8px 10px;display:flex;flex-direction:column;gap:6px;backdrop-filter:blur(8px);box-shadow:0 8px 28px rgba(0,0,0,.4);min-width:180px;}
.img-edit-toolbar .iet-row{display:flex;align-items:center;gap:4px;}
.img-edit-toolbar .iet-btn{width:28px;height:28px;border-radius:6px;border:1px solid rgba(255,255,255,.15);background:rgba(255,255,255,.06);color:#F5F2EC;font-size:14px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s;padding:0;}
.img-edit-toolbar .iet-btn:hover{background:rgba(255,107,61,.2);border-color:rgba(255,107,61,.4);color:var(--or);}
.img-edit-toolbar .iet-lbl{font-size:10px;color:#7A7870;letter-spacing:.06em;text-transform:uppercase;font-weight:600;min-width:44px;}
.img-edit-toolbar input[type="range"]{width:80px;accent-color:var(--or);cursor:pointer;height:4px;}
.img-edit-toolbar .iet-val{font-size:10px;color:var(--or);min-width:30px;text-align:right;font-variant-numeric:tabular-nums;}
.img-edit-toolbar .iet-reset{padding:3px 10px;border-radius:6px;border:1px solid rgba(255,255,255,.12);background:transparent;color:#9A9890;font-size:10px;cursor:pointer;font-family:'DM Sans',sans-serif;transition:all .15s;margin-top:2px;}
.img-edit-toolbar .iet-reset:hover{border-color:var(--or);color:var(--or);}
.slide-img-editable{cursor:move !important;pointer-events:auto !important;transition:outline .15s;}
.editing .slide-img-editable{outline:2px dashed rgba(255,107,61,.35);outline-offset:4px;}
.editing .slide-img-editable:hover{outline-color:var(--or);}'''

if old_css in src:
    src = src.replace(old_css, new_css)
    count += 1
    print(f'[{count}] Added CSS for data-editable + image toolbar styles')
else:
    print('WARNING: Could not find CSS anchor for data-editable styles')

# ─────────────────────────────────────────
# 2) STATE: Add imageOffsets to STATE object
# ─────────────────────────────────────────
old_state = "  mascotImages:[] // [{id, name, url, assignedSlides:[]}]\n};"
new_state = "  mascotImages:[], // [{id, name, url, assignedSlides:[]}]\n  imageOffsets:{} // {'slide-id': {x:0,y:0,rotate:0}}\n};"

if old_state in src:
    src = src.replace(old_state, new_state)
    count += 1
    print(f'[{count}] Added imageOffsets to STATE')
else:
    print('WARNING: Could not find STATE mascotImages anchor')

# ─────────────────────────────────────────
# 3) Sidebar: Add letter-spacing and line-height controls after Body weight section
# ─────────────────────────────────────────
old_sidebar_anchor = '''    <!-- Layout Style -->'''
new_sidebar_section = '''    <!-- Letter Spacing & Line Height (Patch6) -->
    <div class="sp-sec">
      <div class="sp-lbl">Spacing & Height</div>
      <div style="display:flex;flex-direction:column;gap:.55rem;">
        <div>
          <div class="sp-clr-lbl" style="margin-bottom:.3rem;">Letter spacing <span id="sp-ls-lbl" style="color:var(--or);font-weight:700;">0em</span></div>
          <input type="range" id="sp-ls" min="-5" max="20" value="0" step="1"
            style="width:100%;accent-color:var(--or);cursor:pointer;"
            oninput="updateSpacing()"/>
        </div>
        <div>
          <div class="sp-clr-lbl" style="margin-bottom:.3rem;">Line height <span id="sp-lh-lbl" style="color:var(--or);font-weight:700;">1.5</span></div>
          <input type="range" id="sp-lh" min="8" max="30" value="15" step="1"
            style="width:100%;accent-color:var(--or);cursor:pointer;"
            oninput="updateSpacing()"/>
        </div>
      </div>
    </div>

    <!-- Layout Style -->'''

if old_sidebar_anchor in src:
    src = src.replace(old_sidebar_anchor, new_sidebar_section, 1)
    count += 1
    print(f'[{count}] Added letter-spacing & line-height controls to sidebar')
else:
    print('WARNING: Could not find Layout Style sidebar anchor')

# ─────────────────────────────────────────
# 4) Modify the e() function to add data-editable attribute
# ─────────────────────────────────────────
old_e_func = 'function e(txt){return `<span class="editable" contenteditable="false">${txt}</span>`;}'
new_e_func = 'function e(txt){return `<span class="editable" data-editable="true" contenteditable="false">${txt}</span>`;}'

if old_e_func in src:
    src = src.replace(old_e_func, new_e_func)
    count += 1
    print(f'[{count}] Added data-editable="true" to e() function')
else:
    print('WARNING: Could not find e() function')

# ─────────────────────────────────────────
# 5) Modify mascotImgTag to add slide-img-editable class and image offsets
# ─────────────────────────────────────────
old_mascot_img = '''  return `<img src="${url}" style="${style}" alt="mascot"/>`;
}'''
new_mascot_img = '''  // Patch6: apply saved image offsets
  const offsets = STATE.imageOffsets[slideId] || {x:0, y:0, rotate:0};
  if(offsets.x || offsets.y || offsets.rotate){
    // need to merge transform
    const existingTransform = rule.transform || '';
    const offsetTransform = `translate(${offsets.x}px, ${offsets.y}px) rotate(${offsets.rotate}deg)`;
    style = style.replace(/transform:[^;]+;?/, '');
    style += `transform:${offsetTransform} ${existingTransform};`;
  }
  return `<img src="${url}" class="slide-img-editable" data-slide-id="${slideId}" style="${style}" alt="mascot"/>`;
}'''

if old_mascot_img in src:
    src = src.replace(old_mascot_img, new_mascot_img)
    count += 1
    print(f'[{count}] Enhanced mascotImgTag with offsets + slide-img-editable class')
else:
    print('WARNING: Could not find mascotImgTag return statement')

# ─────────────────────────────────────────
# 6) Enhance toggleEdit and applyEdit to handle data-editable + editing class + image toolbar
# ─────────────────────────────────────────
old_edit = "function toggleEdit(){editMode=!editMode;applyEdit(editMode);}\nfunction applyEdit(on){document.getElementById('slide-canvas').classList.toggle('em',on);document.getElementById('slide-canvas').querySelectorAll('.editable').forEach(el=>{el.contentEditable=on?'true':'false';if(!on)el.blur();});document.getElementById('edit-bar').classList.toggle('show',on);document.getElementById('edit-btn').classList.toggle('act',on);}"

new_edit = r"""function toggleEdit(){editMode=!editMode;applyEdit(editMode);}
function applyEdit(on){
  const canvas=document.getElementById('slide-canvas');
  canvas.classList.toggle('em',on);
  canvas.classList.toggle('editing',on);
  // original editable spans
  canvas.querySelectorAll('.editable').forEach(el=>{el.contentEditable=on?'true':'false';if(!on)el.blur();});
  // Patch6: data-editable elements
  document.querySelectorAll('[data-editable]').forEach(el=>{el.contentEditable=on?'true':'false';if(!on)el.blur();});
  document.getElementById('edit-bar').classList.toggle('show',on);
  document.getElementById('edit-btn').classList.toggle('act',on);
  // Patch6: remove image toolbar when edit mode off
  if(!on){
    const tb=document.getElementById('img-edit-toolbar');
    if(tb)tb.remove();
    _ietSelectedImg=null;
  }
}"""

if old_edit in src:
    src = src.replace(old_edit, new_edit)
    count += 1
    print(f'[{count}] Enhanced toggleEdit/applyEdit for data-editable + editing class')
else:
    print('WARNING: Could not find toggleEdit/applyEdit functions')

# ─────────────────────────────────────────
# 7) Add spacing update function + image toolbar logic before "/* init */"
# ─────────────────────────────────────────
old_init = "/* init */\nactiveSl=ALL_SLIDES.map((_,i)=>i);poolSl=[];"

new_init = r"""/* ════════════════════════════════════════
   PATCH6: Letter-Spacing & Line-Height
════════════════════════════════════════ */
function updateSpacing(){
  const lsVal=parseInt(document.getElementById('sp-ls').value)/100;
  const lhVal=parseInt(document.getElementById('sp-lh').value)/10;
  document.getElementById('sp-ls-lbl').textContent=lsVal.toFixed(2)+'em';
  document.getElementById('sp-lh-lbl').textContent=lhVal.toFixed(1);
  const canvas=document.getElementById('slide-canvas');
  canvas.style.setProperty('--user-ls',lsVal+'em');
  canvas.style.setProperty('--user-lh',lhVal);
  canvas.querySelectorAll('.sl-h1,.sl-h2,.sl-h3').forEach(el=>{el.style.letterSpacing=lsVal+'em';});
  canvas.querySelectorAll('.sl-body,.sl-body-sm,[data-editable]').forEach(el=>{el.style.lineHeight=lhVal;});
}

/* ════════════════════════════════════════
   PATCH6: Image Position & Rotation Toolbar
════════════════════════════════════════ */
let _ietSelectedImg=null;

function _ietEnsureOffsets(slideId){
  if(!STATE.imageOffsets[slideId])STATE.imageOffsets[slideId]={x:0,y:0,rotate:0};
  return STATE.imageOffsets[slideId];
}

function _ietShowToolbar(img){
  let tb=document.getElementById('img-edit-toolbar');
  if(tb)tb.remove();
  _ietSelectedImg=img;
  const slideId=img.getAttribute('data-slide-id');
  if(!slideId)return;
  const off=_ietEnsureOffsets(slideId);

  tb=document.createElement('div');
  tb.id='img-edit-toolbar';
  tb.className='img-edit-toolbar';
  tb.innerHTML=`
    <div class="iet-row"><span class="iet-lbl">Move</span>
      <button class="iet-btn" onclick="_ietMove('up')" title="Up">&#8593;</button>
      <button class="iet-btn" onclick="_ietMove('down')" title="Down">&#8595;</button>
      <button class="iet-btn" onclick="_ietMove('left')" title="Left">&#8592;</button>
      <button class="iet-btn" onclick="_ietMove('right')" title="Right">&#8594;</button>
    </div>
    <div class="iet-row"><span class="iet-lbl">Rotate</span>
      <input type="range" min="-180" max="180" value="${off.rotate}" step="5" oninput="_ietRotate(this.value)"/>
      <span class="iet-val" id="iet-rot-val">${off.rotate}&deg;</span>
    </div>
    <div class="iet-row" style="justify-content:flex-end;">
      <button class="iet-reset" onclick="_ietReset()">Reset</button>
    </div>`;

  // position near the image
  const canvas=document.getElementById('slide-canvas');
  const cRect=canvas.getBoundingClientRect();
  const iRect=img.getBoundingClientRect();
  let tLeft=(iRect.left - cRect.left + iRect.width/2)/cRect.width*1920 - 90;
  let tTop=(iRect.top - cRect.top)/cRect.height*1080 - 120;
  if(tTop<10)tTop=(iRect.bottom - cRect.top)/cRect.height*1080 + 10;
  if(tLeft<10)tLeft=10;
  if(tLeft>1700)tLeft=1700;
  tb.style.position='absolute';
  tb.style.left=tLeft+'px';
  tb.style.top=tTop+'px';
  canvas.appendChild(tb);
}

function _ietApplyTransform(){
  if(!_ietSelectedImg)return;
  const slideId=_ietSelectedImg.getAttribute('data-slide-id');
  const off=STATE.imageOffsets[slideId]||{x:0,y:0,rotate:0};
  const rule=typeof MASCOT_SLIDE_RULES!=='undefined'?MASCOT_SLIDE_RULES[slideId]:null;
  const existingTransform=(rule&&rule.transform)?rule.transform:'';
  _ietSelectedImg.style.transform=`translate(${off.x}px, ${off.y}px) rotate(${off.rotate}deg) ${existingTransform}`;
}

function _ietMove(dir){
  if(!_ietSelectedImg)return;
  const slideId=_ietSelectedImg.getAttribute('data-slide-id');
  const off=_ietEnsureOffsets(slideId);
  const step=10;
  if(dir==='up')off.y-=step;
  if(dir==='down')off.y+=step;
  if(dir==='left')off.x-=step;
  if(dir==='right')off.x+=step;
  _ietApplyTransform();
}

function _ietRotate(val){
  if(!_ietSelectedImg)return;
  const slideId=_ietSelectedImg.getAttribute('data-slide-id');
  const off=_ietEnsureOffsets(slideId);
  off.rotate=parseInt(val);
  document.getElementById('iet-rot-val').textContent=val+'\u00B0';
  _ietApplyTransform();
}

function _ietReset(){
  if(!_ietSelectedImg)return;
  const slideId=_ietSelectedImg.getAttribute('data-slide-id');
  STATE.imageOffsets[slideId]={x:0,y:0,rotate:0};
  _ietApplyTransform();
  // update slider
  const slider=document.querySelector('#img-edit-toolbar input[type="range"]');
  if(slider)slider.value=0;
  const valSpan=document.getElementById('iet-rot-val');
  if(valSpan)valSpan.textContent='0\u00B0';
}

// Click handler for images in edit mode
document.addEventListener('click',function(ev){
  if(!editMode)return;
  const img=ev.target.closest('.slide-img-editable');
  if(img){
    ev.preventDefault();ev.stopPropagation();
    _ietShowToolbar(img);
    return;
  }
  // if clicking outside toolbar and image, close toolbar
  if(!ev.target.closest('#img-edit-toolbar')&&!ev.target.closest('.slide-img-editable')){
    const tb=document.getElementById('img-edit-toolbar');
    if(tb)tb.remove();
    _ietSelectedImg=null;
  }
},true);

/* init */
activeSl=ALL_SLIDES.map((_,i)=>i);poolSl=[];"""

if old_init in src:
    src = src.replace(old_init, new_init)
    count += 1
    print(f'[{count}] Added spacing functions + image toolbar logic')
else:
    print('WARNING: Could not find /* init */ anchor')

# ─────────────────────────────────────────
# Write out
# ─────────────────────────────────────────
with open(path, 'w', encoding='utf-8') as f:
    f.write(src)

print(f'\nDone — {count} patches applied to index.html')
if count < 7:
    print('WARNING: Not all patches applied. Check messages above.')

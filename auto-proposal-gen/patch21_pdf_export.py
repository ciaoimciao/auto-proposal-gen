#!/usr/bin/env python3
"""Add PDF export functionality using html2canvas + jsPDF."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Add CDN scripts for html2canvas + jsPDF ───
old_head = '</style>\n</head>'
new_head = """</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.2/jspdf.umd.min.js"></script>
</head>"""

if old_head in src:
    src = src.replace(old_head, new_head)
    changes += 1
    print("✅ 1. Added html2canvas + jsPDF CDN scripts")
else:
    print("⚠️ 1. </head> pattern not found")

# ─── 2. Add Export PDF button in toolbar ───
old_toolbar = """<button class="nb p" id="btn-next" onclick="nextSlide()">Next →</button>"""
new_toolbar = """<button class="nb p" id="btn-next" onclick="nextSlide()">Next →</button>
        <button class="nb act" id="btn-pdf" onclick="exportPDF()" style="margin-left:8px;background:var(--or);color:#fff;border-color:var(--or);">📄 Export PDF</button>"""

if old_toolbar in src:
    src = src.replace(old_toolbar, new_toolbar)
    changes += 1
    print("✅ 2. Added Export PDF button")
else:
    print("⚠️ 2. Toolbar button pattern not found")

# ─── 3. Add CSS for PDF progress overlay ───
old_style_end = '.img-edit-bar .rot-val{color:rgba(255,255,255,.6);font-size:11px;min-width:32px;text-align:center;font-family:var(--fb);}\n</style>'
new_style_end = """.img-edit-bar .rot-val{color:rgba(255,255,255,.6);font-size:11px;min-width:32px;text-align:center;font-family:var(--fb);}
/* PDF export overlay */
.pdf-overlay{position:fixed;inset:0;background:rgba(10,10,10,.85);backdrop-filter:blur(8px);z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1rem;}
.pdf-overlay .pdf-title{font-family:var(--fh);font-size:1.4rem;color:#F5F2EC;font-weight:700;}
.pdf-overlay .pdf-progress{width:320px;height:6px;border-radius:3px;background:rgba(255,255,255,.1);overflow:hidden;}
.pdf-overlay .pdf-bar{height:100%;background:var(--or);border-radius:3px;transition:width .3s ease;}
.pdf-overlay .pdf-status{font-size:.8rem;color:#B8B5AE;font-family:var(--fb);}
</style>"""

if old_style_end in src:
    src = src.replace(old_style_end, new_style_end)
    changes += 1
    print("✅ 3. Added PDF overlay CSS")
else:
    print("⚠️ 3. Style end pattern not found")

# ─── 4. Add exportPDF() function before the init block ───
old_init = "\n/* init — default to 8 core pages */"
new_init = """
/* ═══════════════════════════════════
   PDF EXPORT
═══════════════════════════════════ */
async function exportPDF(){
  const {jsPDF}=window.jspdf;
  if(!jsPDF){alert('jsPDF not loaded — check internet connection.');return;}
  const canvas=document.getElementById('slide-canvas');
  const scaler=document.getElementById('slide-scaler');
  const totalSlides=activeSl.length;
  if(!totalSlides){alert('No slides to export.');return;}

  // Save current state
  const savedIdx=curSlide;
  const savedScale=scaler.style.transform;
  const savedEm=canvas.classList.contains('em');
  if(savedEm)canvas.classList.remove('em');

  // Remove edit bars
  document.querySelectorAll('.img-edit-bar,.img-edit-toolbar').forEach(b=>b.remove());

  // Show progress overlay
  const overlay=document.createElement('div');
  overlay.className='pdf-overlay';
  overlay.innerHTML=`
    <div class="pdf-title">Exporting PDF...</div>
    <div class="pdf-progress"><div class="pdf-bar" style="width:0%"></div></div>
    <div class="pdf-status">Preparing slide 1 of ${totalSlides}</div>
  `;
  document.body.appendChild(overlay);
  const bar=overlay.querySelector('.pdf-bar');
  const status=overlay.querySelector('.pdf-status');

  // Create PDF — landscape 1920x1080 (16:9)
  const pdf=new jsPDF({orientation:'landscape',unit:'px',format:[1920,1080],compress:true});

  // Render at full scale
  scaler.style.transform='scale(1)';
  scaler.style.transformOrigin='top left';

  for(let i=0;i<totalSlides;i++){
    status.textContent='Rendering slide '+(i+1)+' of '+totalSlides+'...';
    bar.style.width=Math.round(((i+0.5)/totalSlides)*100)+'%';

    // Navigate to slide
    curSlide=i;
    renderCurrentSlide();
    buildDots();

    // Wait for images and rendering
    await new Promise(r=>setTimeout(r,400));

    // Wait for all images in the canvas to load
    const imgs=canvas.querySelectorAll('img');
    await Promise.all([...imgs].map(im=>{
      if(im.complete)return Promise.resolve();
      return new Promise(r=>{im.onload=r;im.onerror=r;});
    }));

    try{
      const c=await html2canvas(canvas,{
        scale:1,
        useCORS:true,
        allowTaint:true,
        backgroundColor:null,
        width:1920,
        height:1080,
        logging:false,
        removeContainer:true,
      });
      if(i>0)pdf.addPage([1920,1080],'landscape');
      pdf.addImage(c.toDataURL('image/jpeg',0.92),'JPEG',0,0,1920,1080);
    }catch(e){
      console.error('PDF render error on slide '+(i+1),e);
    }

    bar.style.width=Math.round(((i+1)/totalSlides)*100)+'%';
  }

  // Generate filename
  const mn=document.getElementById('in-mascot')?.value||'proposal';
  const cn=document.getElementById('in-client')?.value||'';
  const safeName=(cn?cn.replace(/[^a-zA-Z0-9\\u4e00-\\u9fff]/g,'_')+'_':'')+'Notso_Proposal';
  const date=new Date().toISOString().slice(0,10);

  status.textContent='Saving PDF...';
  bar.style.width='100%';

  pdf.save(safeName+'_'+date+'.pdf');

  // Restore state
  scaler.style.transform=savedScale;
  curSlide=savedIdx;
  renderCurrentSlide();
  buildDots();
  if(savedEm)canvas.classList.add('em');

  // Remove overlay
  setTimeout(()=>overlay.remove(),600);
}

/* init — default to 8 core pages */"""

if old_init in src:
    src = src.replace(old_init, new_init)
    changes += 1
    print("✅ 4. Added exportPDF() function")
else:
    print("⚠️ 4. Init block pattern not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

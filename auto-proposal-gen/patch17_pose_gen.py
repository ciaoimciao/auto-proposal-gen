#!/usr/bin/env python3
"""Add Mascot Pose Generator to Settings Panel."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Add CSS for pose generator ───
css_anchor = ".sp-upload-zone input[type=\"file\"]{position:absolute;inset:0;opacity:0;cursor:pointer;}"
pose_css = """.sp-upload-zone input[type="file"]{position:absolute;inset:0;opacity:0;cursor:pointer;}

/* ── Pose Generator ── */
.sp-pose-ref{display:flex;align-items:center;gap:10px;margin-bottom:.6rem;padding:6px;border-radius:10px;}
.sp-pose-ref img{width:48px;height:48px;border-radius:8px;object-fit:cover;}
.sp-pose-ref-info{font-size:.65rem;line-height:1.4;}
.sp-pose-presets{display:flex;flex-wrap:wrap;gap:4px;margin-bottom:.6rem;}
.sp-pose-presets button{
  padding:3px 10px;border-radius:9999px;font-size:.65rem;font-weight:600;
  cursor:pointer;transition:all .15s;font-family:'DM Sans',sans-serif;
  letter-spacing:.02em;
}
.sp-pose-prompt{
  width:100%;border-radius:8px;padding:6px 8px;font-size:.72rem;
  font-family:'DM Sans',sans-serif;resize:none;min-height:48px;
  transition:border-color .2s;outline:none;
}
.sp-pose-gen-btn{
  width:100%;padding:6px;border:none;border-radius:9999px;
  font-family:'Syne',sans-serif;font-size:.72rem;font-weight:600;
  cursor:pointer;transition:all .2s;margin-top:.5rem;
  letter-spacing:.03em;display:flex;align-items:center;justify-content:center;gap:6px;
}
.sp-pose-gen-btn:disabled{opacity:.4;cursor:not-allowed;}
.sp-pose-results{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:.6rem;}
.sp-pose-result{border-radius:10px;overflow:hidden;position:relative;cursor:pointer;transition:transform .15s;}
.sp-pose-result:hover{transform:scale(1.02);}
.sp-pose-result img{width:100%;aspect-ratio:1;object-fit:cover;display:block;}
.sp-pose-result-add{
  position:absolute;bottom:4px;right:4px;padding:2px 8px;border-radius:9999px;
  font-size:.55rem;font-weight:600;cursor:pointer;border:none;
  transition:all .15s;letter-spacing:.03em;
}
.sp-pose-status{font-size:.65rem;margin-top:.4rem;text-align:center;}
.sp-pose-input{
  width:100%;border-radius:8px;padding:5px 8px;font-size:.68rem;
  font-family:'DM Sans',sans-serif;outline:none;transition:border-color .2s;
  margin-bottom:.5rem;
}
/* loading spinner */
@keyframes sp-spin{to{transform:rotate(360deg)}}
.sp-spinner{width:16px;height:16px;border:2px solid rgba(0,0,0,.1);border-top-color:#0a0a0a;border-radius:50%;animation:sp-spin .6s linear infinite;display:inline-block;}"""

# Dark theme
pose_dark = """
/* Pose gen dark */
.sp.dark .sp-pose-ref{background:rgba(255,255,255,.04);}
.sp.dark .sp-pose-ref-info{color:#9A9890;}
.sp.dark .sp-pose-presets button{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:#9A9890;}
.sp.dark .sp-pose-presets button:hover{border-color:rgba(255,255,255,.3);color:#F5F2EC;}
.sp.dark .sp-pose-presets button.active{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.3);color:#fff;}
.sp.dark .sp-pose-prompt{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);color:#F5F2EC;}
.sp.dark .sp-pose-prompt:focus{border-color:rgba(255,255,255,.25);}
.sp.dark .sp-pose-gen-btn{background:#e5e5e5;color:#0a0a0a;}
.sp.dark .sp-pose-gen-btn:hover:not(:disabled){background:#fff;}
.sp.dark .sp-pose-result{border:1px solid rgba(255,255,255,.08);}
.sp.dark .sp-pose-result-add{background:rgba(255,255,255,.9);color:#0a0a0a;}
.sp.dark .sp-pose-result-add:hover{background:#fff;}
.sp.dark .sp-pose-status{color:#7A7870;}
.sp.dark .sp-pose-input{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);color:#F5F2EC;}
.sp.dark .sp-pose-input:focus{border-color:rgba(255,255,255,.25);}
.sp.dark .sp-spinner{border-color:rgba(255,255,255,.15);border-top-color:#fff;}"""

# Light theme
pose_light = """
/* Pose gen light */
.sp.light .sp-pose-ref{background:#F5F2EC;}
.sp.light .sp-pose-ref-info{color:#888580;}
.sp.light .sp-pose-presets button{background:#F5F2EC;border:1px solid #D8D4CC;color:#4A4846;}
.sp.light .sp-pose-presets button:hover{border-color:#0a0a0a;color:#0a0a0a;}
.sp.light .sp-pose-presets button.active{background:#0a0a0a;border-color:#0a0a0a;color:#fff;}
.sp.light .sp-pose-prompt{background:#F5F2EC;border:1px solid #D8D4CC;color:#111110;}
.sp.light .sp-pose-prompt:focus{border-color:#0a0a0a;}
.sp.light .sp-pose-gen-btn{background:#0a0a0a;color:#fff;}
.sp.light .sp-pose-gen-btn:hover:not(:disabled){background:#1a1a1a;}
.sp.light .sp-pose-result{border:1px solid #D8D4CC;}
.sp.light .sp-pose-result-add{background:#0a0a0a;color:#fff;}
.sp.light .sp-pose-result-add:hover{background:#1a1a1a;}
.sp.light .sp-pose-status{color:#888580;}
.sp.light .sp-pose-input{background:#F5F2EC;border:1px solid #D8D4CC;color:#111110;}
.sp.light .sp-pose-input:focus{border-color:#0a0a0a;}"""

if css_anchor in src:
    src = src.replace(css_anchor, pose_css)
    changes += 1
    print("✅ 1. Added pose generator CSS")
else:
    print("⚠️ 1. CSS anchor not found")

# Insert dark theme CSS after existing dark section
dark_anchor = ".sp.dark .sp-upload-lbl{color:#7A7870;}"
if dark_anchor in src:
    src = src.replace(dark_anchor, dark_anchor + pose_dark)
    changes += 1
    print("✅ 1b. Added dark theme CSS")
else:
    print("⚠️ 1b. Dark anchor not found")

# Insert light theme CSS after existing light section
light_anchor = ".sp.light .sp-upload-lbl{color:#888580;}"
if light_anchor in src:
    src = src.replace(light_anchor, light_anchor + pose_light)
    changes += 1
    print("✅ 1c. Added light theme CSS")
else:
    print("⚠️ 1c. Light anchor not found")

# ─── 2. Add HTML section to Settings Panel ───
html_anchor = """    <!-- Slides -->
    <div class="sp-sec">
      <div class="sp-lbl">Slides"""

pose_html = """    <!-- Pose Generator -->
    <div class="sp-sec" id="sp-pose-sec">
      <div class="sp-lbl">Pose Generator</div>
      <div style="margin-bottom:.5rem;">
        <input class="sp-pose-input" id="sp-rep-token" type="password" placeholder="Replicate API token (r8_...)" />
        <input class="sp-pose-input" id="sp-worker-url" placeholder="Worker URL (https://...workers.dev)" />
      </div>
      <div id="sp-pose-ref-area"></div>
      <div class="sp-pose-presets" id="sp-pose-presets">
        <button onclick="setPosePreset('wave')">Wave</button>
        <button onclick="setPosePreset('point')">Point</button>
        <button onclick="setPosePreset('think')">Think</button>
        <button onclick="setPosePreset('thumbsup')">Thumbs Up</button>
        <button onclick="setPosePreset('present')">Present</button>
        <button onclick="setPosePreset('sit')">Sit</button>
      </div>
      <textarea class="sp-pose-prompt" id="sp-pose-prompt" placeholder="Describe the pose or action..."></textarea>
      <button class="sp-pose-gen-btn" id="sp-pose-gen-btn" onclick="generatePose()">Generate Pose</button>
      <div class="sp-pose-status" id="sp-pose-status"></div>
      <div class="sp-pose-results" id="sp-pose-results"></div>
    </div>

    <!-- Slides -->
    <div class="sp-sec">
      <div class="sp-lbl">Slides"""

if html_anchor in src:
    src = src.replace(html_anchor, pose_html)
    changes += 1
    print("✅ 2. Added pose generator HTML section")
else:
    print("⚠️ 2. HTML anchor not found")

# ─── 3. Add JavaScript ───
js_anchor = "function buildSpImages(){"

pose_js = """// ═══════════════════════════════════════
// POSE GENERATOR (Replicate API)
// ═══════════════════════════════════════
const POSE_PRESETS={
  wave:'3D animated mascot character waving hello with one hand raised high, friendly cheerful pose, full body, white background, same character identity, consistent style',
  point:'3D animated mascot character pointing forward at viewer with index finger, confident pose, full body, white background, same character identity, consistent style',
  think:'3D animated mascot character with hand on chin thinking deeply, curious thoughtful pose, full body, white background, same character identity, consistent style',
  thumbsup:'3D animated mascot character giving enthusiastic thumbs up with big smile, happy cheerful pose, full body, white background, same character identity, consistent style',
  present:'3D animated mascot character gesturing to the side with open palm presenting something, professional pose, full body, white background, same character identity, consistent style',
  sit:'3D animated mascot character sitting casually cross-legged, relaxed friendly pose, full body, white background, same character identity, consistent style',
};

function setPosePreset(key){
  document.getElementById('sp-pose-prompt').value=POSE_PRESETS[key]||'';
  document.querySelectorAll('.sp-pose-presets button').forEach(b=>b.classList.remove('active'));
  event.target.classList.add('active');
}

function updatePoseRefArea(){
  const area=document.getElementById('sp-pose-ref-area');
  if(!area)return;
  if(STATE.mascotImages.length===0){
    area.innerHTML='<div style="font-size:.65rem;color:#888;margin-bottom:.5rem;">Upload a mascot image first (above) to use as reference</div>';
    return;
  }
  const img=STATE.mascotImages[0];
  area.innerHTML=`<div class="sp-pose-ref">
    <img src="${img.url}" alt="ref"/>
    <div class="sp-pose-ref-info"><strong>Reference:</strong> ${img.file.name}<br/>This character will be used for pose generation</div>
  </div>`;
}

async function blobUrlToBase64(blobUrl){
  const res=await fetch(blobUrl);
  const blob=await res.blob();
  return new Promise((resolve,reject)=>{
    const reader=new FileReader();
    reader.onloadend=()=>resolve(reader.result);
    reader.onerror=reject;
    reader.readAsDataURL(blob);
  });
}

async function generatePose(){
  const token=document.getElementById('sp-rep-token').value.trim();
  const workerUrl=document.getElementById('sp-worker-url').value.trim();
  const prompt=document.getElementById('sp-pose-prompt').value.trim();
  const statusEl=document.getElementById('sp-pose-status');
  const btn=document.getElementById('sp-pose-gen-btn');

  if(!token){statusEl.textContent='Enter your Replicate API token';return;}
  if(!workerUrl){statusEl.textContent='Enter your Cloudflare Worker URL';return;}
  if(!prompt){statusEl.textContent='Describe the pose first';return;}
  if(STATE.mascotImages.length===0){statusEl.textContent='Upload a mascot image first';return;}

  btn.disabled=true;
  btn.innerHTML='<span class="sp-spinner"></span> Generating...';
  statusEl.textContent='Converting reference image...';

  try{
    // Convert reference image to base64
    const refBase64=await blobUrlToBase64(STATE.mascotImages[0].url);

    statusEl.textContent='Sending to Replicate...';

    // Create prediction via Cloudflare Worker
    const createRes=await fetch(workerUrl.replace(/\/$/,'')+'/predict',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        replicateToken:token,
        version:'ea16514e940159c0a1e1da109905d1a5e3648f23e0648e1044699f5d388db1d9',
        input:{
          image:refBase64,
          prompt:prompt,
          negative_prompt:'blurry, low quality, distorted, deformed, ugly, realistic photo, human face',
          num_outputs:2,
          guidance_scale:7.5,
          ip_adapter_scale:0.75,
          num_inference_steps:30,
        }
      })
    });

    if(!createRes.ok){
      const err=await createRes.json();
      throw new Error(err.error||'Failed to create prediction');
    }

    const prediction=await createRes.json();
    let predId=prediction.id;

    // Poll for results
    statusEl.textContent='Generating... this takes 15-30 seconds';
    let result=prediction;
    let attempts=0;
    const maxAttempts=60; // 2 minutes max

    while(result.status!=='succeeded'&&result.status!=='failed'&&attempts<maxAttempts){
      await new Promise(r=>setTimeout(r,2000));
      attempts++;
      statusEl.textContent=`Generating... ${attempts*2}s`;

      const pollRes=await fetch(workerUrl.replace(/\/$/,'')+'/predict/'+predId+'?token='+encodeURIComponent(token));
      result=await pollRes.json();
    }

    if(result.status==='failed'){
      throw new Error(result.error||'Generation failed');
    }
    if(result.status!=='succeeded'){
      throw new Error('Timed out — try again');
    }

    // Display results
    const outputs=result.output||[];
    statusEl.textContent=`Done! ${outputs.length} image(s) generated`;
    renderPoseResults(outputs);

  }catch(err){
    statusEl.textContent='Error: '+err.message;
    console.error('Pose generation error:',err);
  }finally{
    btn.disabled=false;
    btn.innerHTML='Generate Pose';
  }
}

function renderPoseResults(imageUrls){
  const container=document.getElementById('sp-pose-results');
  container.innerHTML=imageUrls.map((url,i)=>`
    <div class="sp-pose-result">
      <img src="${url}" alt="Generated pose ${i+1}" loading="lazy"/>
      <button class="sp-pose-result-add" onclick="addPoseToSlides('${url}',${i})">+ Add</button>
    </div>
  `).join('');
}

async function addPoseToSlides(imageUrl,index){
  try{
    // Download image and create local blob URL
    const res=await fetch(imageUrl);
    const blob=await res.blob();
    const file=new File([blob],'pose-'+Date.now()+'.png',{type:'image/png'});
    const localUrl=URL.createObjectURL(blob);

    // Add to STATE.mascotImages using existing system
    const autoSlides=MASCOT_SLIDE_RULES.map(r=>r.slideId);
    const usedSlides=STATE.mascotImages.flatMap(m=>m.assignedSlides);
    const availSlides=autoSlides.filter(s=>!usedSlides.includes(s));
    const assign=availSlides.slice(0,2);

    STATE.mascotImages.push({
      id:'pose-'+Date.now()+'-'+index,
      url:localUrl,
      file:file,
      assignedSlides:assign,
    });

    buildSpImages();
    rebuildSlides();
    document.getElementById('sp-pose-status').textContent='Added to slides!';
  }catch(err){
    document.getElementById('sp-pose-status').textContent='Failed to add: '+err.message;
  }
}

// Update ref area when mascot images change
const _origBuildSpImages=typeof buildSpImages==='function'?buildSpImages:null;

""" + "function buildSpImages(){"

if js_anchor in src:
    src = src.replace(js_anchor, pose_js, 1)
    changes += 1
    print("✅ 3. Added pose generator JavaScript")
else:
    print("⚠️ 3. JS anchor not found")

# ─── 4. Hook updatePoseRefArea into buildSpImages ───
# Find the end of buildSpImages to add our hook
build_sp_end = "document.getElementById('sp-img-cnt').textContent=STATE.mascotImages.length;"
if build_sp_end in src:
    src = src.replace(build_sp_end, build_sp_end + "\n  updatePoseRefArea();")
    changes += 1
    print("✅ 4. Hooked updatePoseRefArea into buildSpImages")
else:
    print("⚠️ 4. buildSpImages hook point not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

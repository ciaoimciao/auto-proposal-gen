import re

with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'r') as f:
    content = f.read()

changes = 0

# ═══════════════════════════════════════════════
# 1. SMALLER PAGE NUMBERS — 180px → 48px
# ═══════════════════════════════════════════════
old_slnum = '.sl-num{position:absolute;bottom:60px;right:80px;font-family:var(--fd);font-size:180px;font-weight:800;letter-spacing:-.08em;line-height:1;user-select:none;pointer-events:none;}'
new_slnum = '.sl-num{position:absolute;bottom:32px;right:48px;font-family:var(--fd);font-size:42px;font-weight:700;letter-spacing:-.02em;line-height:1;user-select:none;pointer-events:none;opacity:.3;}'
if old_slnum in content:
    content = content.replace(old_slnum, new_slnum, 1)
    changes += 1
    print("✅ 1. Page numbers shrunk to 42px")
else:
    print("❌ 1. sl-num CSS not found")

# ═══════════════════════════════════════════════
# 2. ADD FILMSTRIP PREVIEW STRIP
# ═══════════════════════════════════════════════

# 2a. Add CSS for filmstrip (before </style>)
filmstrip_css = """
/* ══ FILMSTRIP PREVIEW STRIP ══ */
.filmstrip{display:flex;gap:8px;padding:10px 16px;background:#1a1a18;border-top:1px solid rgba(255,255,255,.08);overflow-x:auto;flex-shrink:0;scrollbar-width:thin;scrollbar-color:rgba(255,255,255,.15) transparent;align-items:center;}
.filmstrip::-webkit-scrollbar{height:4px;}
.filmstrip::-webkit-scrollbar-track{background:transparent;}
.filmstrip::-webkit-scrollbar-thumb{background:rgba(255,255,255,.15);border-radius:2px;}
.fs-thumb{flex-shrink:0;width:128px;height:72px;border-radius:6px;overflow:hidden;cursor:pointer;border:2px solid transparent;transition:border-color .2s,box-shadow .2s;position:relative;background:#222;}
.fs-thumb.active{border-color:var(--or);box-shadow:0 0 0 2px rgba(255,107,61,.3);}
.fs-thumb:hover:not(.active){border-color:rgba(255,255,255,.25);}
.fs-thumb-inner{width:1920px;height:1080px;transform:scale(0.0667);transform-origin:top left;pointer-events:none;position:absolute;top:0;left:0;}
.fs-num{position:absolute;bottom:2px;right:4px;font-family:var(--fd);font-size:10px;font-weight:700;color:rgba(255,255,255,.6);z-index:2;text-shadow:0 1px 3px rgba(0,0,0,.5);}
/* ══ TOC VARIANT STYLES ══ */
.toc-agenda{display:grid;grid-template-columns:1fr 1fr;gap:0 80px;margin-top:24px;}
.toc-agenda-item{display:flex;align-items:flex-start;gap:16px;padding:28px 0;border-bottom:1px solid rgba(255,255,255,.08);position:relative;}
.toc-agenda-num{font-family:var(--fd);font-size:38px;font-weight:800;line-height:1;min-width:56px;}
.toc-agenda-dot{width:10px;height:10px;border-radius:50%;margin-top:12px;flex-shrink:0;}
.toc-agenda-txt{display:flex;flex-direction:column;gap:4px;}
.toc-agenda-ttl{font-family:var(--fd);font-size:26px;font-weight:700;line-height:1.2;}
.toc-agenda-desc{font-size:18px;opacity:.5;line-height:1.4;}
.toc-arrow{display:grid;grid-template-columns:1fr 1fr;gap:20px 60px;margin-top:20px;}
.toc-arrow-item{display:flex;align-items:center;gap:16px;padding:24px 0;border-bottom:1px solid;}
.toc-arrow-ico{font-size:28px;flex-shrink:0;}
.toc-arrow-ttl{font-family:var(--fd);font-size:26px;font-weight:700;line-height:1.2;}
.toc-arrow-desc{font-size:16px;opacity:.5;line-height:1.5;margin-top:4px;}
/* ══ P7 PERSONALITY EXPRESSION GRID ══ */
.expr-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
.expr-cell{border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:16px 10px;transition:transform .15s;}
.expr-cell-ico{font-size:72px;line-height:1;}
.expr-cell-lbl{font-size:14px;font-weight:600;text-align:center;line-height:1.2;}
/* ══ P10 KNOWLEDGE BASE 3-COL ══ */
.kb3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:28px;}
.kb3-col{background:rgba(255,255,255,.85);border-radius:18px;padding:28px 24px;display:flex;flex-direction:column;gap:0;}
.kb3-hdr{display:inline-block;font-family:var(--fd);font-size:20px;font-weight:700;padding:6px 18px;border-radius:8px;margin-bottom:16px;line-height:1.3;}
.kb3-list{list-style:none;display:flex;flex-direction:column;gap:8px;padding:0;}
.kb3-list li{display:flex;align-items:flex-start;gap:8px;font-size:16px;line-height:1.4;}
.kb3-list li::before{content:'•';flex-shrink:0;font-weight:700;margin-top:0;}
.kb3-sec{font-family:var(--fd);font-size:17px;font-weight:700;padding:5px 14px;border-radius:6px;display:inline-block;margin:18px 0 10px;}
"""
style_end = '</style>'
if style_end in content:
    content = content.replace(style_end, filmstrip_css + style_end, 1)
    changes += 1
    print("✅ 2a. Filmstrip + TOC + expression grid + KB3 CSS added")
else:
    print("❌ 2a. </style> not found")

# 2b. Add filmstrip HTML div after slide-stage closing div
old_stage = '    <div class="edit-bar" id="edit-bar">'
new_stage = '    <div class="filmstrip" id="filmstrip"></div>\n    <div class="edit-bar" id="edit-bar">'
if old_stage in content:
    content = content.replace(old_stage, new_stage, 1)
    changes += 1
    print("✅ 2b. Filmstrip HTML div added")
else:
    print("❌ 2b. edit-bar div not found")

# 2c. Add filmstrip JS logic — inject into rebuildSlides
old_rebuild_end = "  if(editMode)applyEdit(true);\n  buildSpSlides();\n}"
new_rebuild_end = """  if(editMode)applyEdit(true);
  buildSpSlides();
  buildFilmstrip();
}
function buildFilmstrip(){
  const fs=document.getElementById('filmstrip');if(!fs)return;
  fs.innerHTML='';
  activeSl.forEach((si,idx)=>{
    const s=ALL_SLIDES[si];
    const thumb=document.createElement('div');
    thumb.className='fs-thumb'+(idx===curSlide?' active':'');
    thumb.onclick=()=>goTo(idx);
    const inner=document.createElement('div');
    inner.className='fs-thumb-inner';
    inner.innerHTML=buildSlideHTML(s.id);
    const num=document.createElement('div');
    num.className='fs-num';
    num.textContent=String(idx+1).padStart(2,'0');
    thumb.appendChild(inner);
    thumb.appendChild(num);
    fs.appendChild(thumb);
  });
}"""
if old_rebuild_end in content:
    content = content.replace(old_rebuild_end, new_rebuild_end, 1)
    changes += 1
    print("✅ 2c. Filmstrip JS logic added to rebuildSlides")
else:
    print("❌ 2c. rebuildSlides end not found")

# 2d. Update goTo to also update filmstrip active state
old_goto = "function goTo(i){if(i<0||i>=activeSl.length)return;document.querySelectorAll('#slide-canvas .slide').forEach(s=>s.classList.remove('active'));const el=document.querySelectorAll('#slide-canvas .slide')[i];if(el)el.classList.add('active');curSlide=i;updDots();updateNav();}"
new_goto = "function goTo(i){if(i<0||i>=activeSl.length)return;document.querySelectorAll('#slide-canvas .slide').forEach(s=>s.classList.remove('active'));const el=document.querySelectorAll('#slide-canvas .slide')[i];if(el)el.classList.add('active');curSlide=i;updDots();updateNav();document.querySelectorAll('.fs-thumb').forEach((t,j)=>{t.classList.toggle('active',j===i);});const at=document.querySelector('.fs-thumb.active');if(at)at.scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'});}"
if old_goto in content:
    content = content.replace(old_goto, new_goto, 1)
    changes += 1
    print("✅ 2d. goTo updated with filmstrip sync")
else:
    print("❌ 2d. goTo function not found")

# ═══════════════════════════════════════════════
# 3. setLayout should rebuild slides (for cover/TOC variant switching)
# ═══════════════════════════════════════════════
old_setlayout_end = "    b.classList.toggle('active',isActive);\n  });\n}"
# Find the one inside setLayout specifically
setlayout_block = "function setLayout(name){"
if setlayout_block in content:
    idx = content.index(setlayout_block)
    # Find the closing brace of setLayout
    search_area = content[idx:idx+500]
    old_end = "    b.classList.toggle('active',isActive);\n  });\n}"
    if old_end in search_area:
        pos = content.index(old_end, idx)
        new_end = "    b.classList.toggle('active',isActive);\n  });\n  rebuildSlides();\n}"
        content = content[:pos] + new_end + content[pos+len(old_end):]
        changes += 1
        print("✅ 3. setLayout now calls rebuildSlides")
    else:
        print("❌ 3. setLayout end pattern not found")
else:
    print("❌ 3. setLayout function not found")

# ═══════════════════════════════════════════════
# 4. TOC SLIDE — 2 variants based on layout
# ═══════════════════════════════════════════════
toc_pattern = r"(  case 's-toc':.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">02</div>`;)"
toc_match = re.search(toc_pattern, content, re.DOTALL)
if toc_match:
    old_toc = toc_match.group(1)
    print(f"✅ Found s-toc block ({len(old_toc)} chars)")
else:
    print("❌ s-toc block not found")
    old_toc = None

new_toc = r"""  case 's-toc': {
    const tocLayout=STATE.layout||'spread';
    const tocItems=activeSl.filter((_,i)=>i>0).map((si,pos)=>{const s=ALL_SLIDES[si];return {num:'0'+(pos+1),e:s.e,title:s.title};});

    if(tocLayout==='impact'){
      // VARIANT B: AGENDA style — numbered items with dots and vertical line feel
      return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="font-family:var(--fd);font-size:72px;font-weight:800;letter-spacing:-.04em;color:${V.TX};margin-bottom:12px;">AGENDA</div>
      <div class="toc-agenda">
        ${tocItems.map(t=>`
        <div class="toc-agenda-item" style="border-color:${alpha(V.TX,.1)};">
          <div class="toc-agenda-num" style="color:${c1};">${t.num}</div>
          <div class="toc-agenda-dot" style="background:${c1};"></div>
          <div class="toc-agenda-txt">
            <div class="toc-agenda-ttl" style="color:${V.TX};">${e(t.title)}</div>
            <div class="toc-agenda-desc" style="color:${V.TX3};">${t.e}</div>
          </div>
        </div>`).join('')}
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">02</div>`;
    }

    // VARIANT A (spread/editorial): Table Of Content with arrow icons
    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="top:-80px;right:-80px;width:400px;height:400px;border-width:64px;border-color:${alpha(c2,.08)};"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="font-family:var(--fd);font-size:78px;font-weight:800;letter-spacing:-.04em;color:${V.TX};line-height:.95;margin-bottom:8px;">${e(tx('toc_h',L))}</div>
      <div style="font-size:20px;color:${V.TX3};margin-bottom:12px;">${e(C)} — ${e(IND)}</div>
      <div class="toc-arrow">
        ${tocItems.map(t=>`
        <div class="toc-arrow-item" style="border-color:${alpha(V.TX,.08)};">
          <div class="toc-arrow-ico" style="color:${c1};">→</div>
          <div>
            <div class="toc-arrow-ttl" style="color:${V.TX};">${e(t.title)}</div>
            <div class="toc-arrow-desc" style="color:${V.TX3};">${t.e} ${t.title}</div>
          </div>
        </div>`).join('')}
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">02</div>`;}"""

if old_toc:
    content = content.replace(old_toc, new_toc, 1)
    changes += 1
    print("✅ 4. TOC slide updated with 2 variants")
else:
    print("❌ 4. Could not replace s-toc")

# ═══════════════════════════════════════════════
# 5. P7 (s-emotion) — Personality & Empathy with expression grid
# ═══════════════════════════════════════════════
emo_pattern = r"(  case 's-emotion': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">07</div>`;\})"
emo_match = re.search(emo_pattern, content, re.DOTALL)
if emo_match:
    old_emo = emo_match.group(1)
    print(f"✅ Found s-emotion block ({len(old_emo)} chars)")
else:
    print("❌ s-emotion block not found")
    old_emo = None

new_emo = r"""  case 's-emotion': {
    const mData3=MASCOTS.find(x=>x.id===STATE.mascotStyle)||MASCOTS[2];
    const imgEmo=getMascotImageForSlide(sid);
    const hasImgEmo=!!imgEmo;
    // 9 expression variants for the grid
    const exprEmojis=[
      {ico:'😊',lbl:{en:'Happy',nl:'Blij',zh:'開心'}},
      {ico:'😤',lbl:{en:'Frustrated',nl:'Gefrustreerd',zh:'沮喪'}},
      {ico:'🤔',lbl:{en:'Curious',nl:'Nieuwsgierig',zh:'好奇'}},
      {ico:'🎉',lbl:{en:'Celebrating',nl:'Vierend',zh:'慶祝'}},
      {ico:'😔',lbl:{en:'Apologetic',nl:'Verontschuldigend',zh:'道歉'}},
      {ico:'💡',lbl:{en:'Helpful',nl:'Behulpzaam',zh:'樂於助人'}},
      {ico:'😅',lbl:{en:'Nervous',nl:'Nerveus',zh:'緊張'}},
      {ico:'🤗',lbl:{en:'Welcoming',nl:'Verwelkomend',zh:'歡迎'}},
      {ico:'😌',lbl:{en:'Calm',nl:'Kalm',zh:'平靜'}},
    ];
    const exprColors=['#F7C94E','#FF6B3D','#4CD8A8','#7B7BFF','#9CA3AF','#FF6B3D','#F59E0B','#EC4899','#10B981'];
    const stepLabel={en:'Step 3:',nl:'Stap 3:',zh:'步驟3：',de:'Schritt 3:',fr:'Étape 3 :',ja:'ステップ3：',es:'Paso 3:'};
    const titlePers={en:'Personality &',nl:'Persoonlijkheid &',zh:'人格特質與',de:'Persönlichkeit &',fr:'Personnalité &',ja:'パーソナリティ＆',es:'Personalidad y'};
    const titleEmpathy={en:'Empathy',nl:'Empathie',zh:'共情',de:'Empathie',fr:'Empathie',ja:'共感',es:'Empatía'};
    const bullets=[
      {en:'Not just a search box — a digital colleague with personality and empathy.',
       nl:`${MN} is geen zoekbalk, maar een digitale collega met karakter en empathie.`},
      {en:`In a workshop session, we define ${MN}'s personality traits together.`,
       nl:`Samen ontwikkelen: In een workshop-sessie bepalen we ${MN}'s persoonlijkheid. Is ${MN.charAt(0)==='L'||MN.charAt(0)==='M'?'zij':'hij'} formeel en rustig, of juist vlot en coachend?`},
      {en:`Thanks to our Empathy Engine, ${MN} recognizes user emotions.`,
       nl:`Empathie: Dankzij onze Empathy Engine herkent ${MN} de emotie van de gebruiker.`},
      {en:`${MN} responds with understanding and patience in every situation.`,
       nl:`We vertalen jullie merkwaarden naar een consistente dialoogstijl.`},
    ];
    return `
    <div class="sl-bg-light"></div>
    <div class="sl-safe" style="display:grid;grid-template-columns:1fr 420px;gap:48px;align-items:center;height:100%;">
      <div style="display:flex;flex-direction:column;justify-content:center;">
        <div style="font-family:var(--fd);font-size:28px;font-weight:600;color:#999;letter-spacing:.02em;margin-bottom:4px;">${e(stepLabel[L]||stepLabel.en)}</div>
        <div style="font-family:var(--fd);font-size:52px;font-weight:800;color:#111;line-height:1.05;letter-spacing:-.03em;margin-bottom:8px;">${e(titlePers[L]||titlePers.en)}</div>
        <div style="font-family:var(--fd);font-size:52px;font-weight:800;color:${c1};line-height:1.05;letter-spacing:-.03em;margin-bottom:32px;">${e(titleEmpathy[L]||titleEmpathy.en)}</div>
        <div style="display:flex;flex-direction:column;gap:20px;">
          ${bullets.map(b=>`
          <div style="display:flex;align-items:flex-start;gap:14px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#111;margin-top:9px;flex-shrink:0;"></div>
            <div style="font-size:20px;color:#333;line-height:1.6;"><strong style="font-weight:700;">${e((b[L]||b.en).split(':')[0]+(b[L]||b.en).includes(':')?':':'')}</strong>${e((b[L]||b.en).includes(':')?((b[L]||b.en).split(':').slice(1).join(':')):(b[L]||b.en))}</div>
          </div>`).join('')}
        </div>
      </div>
      <div>
        <div class="expr-grid">
          ${exprEmojis.map((ex,i)=>`
          <div class="expr-cell" style="background:${alpha(exprColors[i],.1)};border:1px solid ${alpha(exprColors[i],.15)};">
            ${hasImgEmo
              ? `<img src="${imgEmo}" style="width:84px;height:84px;object-fit:cover;border-radius:12px;filter:hue-rotate(${i*40}deg) saturate(${0.6+i*0.1});"/>`
              : `<div class="expr-cell-ico">${ex.ico}</div>`}
            <div class="expr-cell-lbl" style="color:${exprColors[i]};">${ex.lbl[L]||ex.lbl.en}</div>
          </div>`).join('')}
        </div>
      </div>
    </div>
    <div class="sl-num" style="color:rgba(0,0,0,.06);">07</div>`;}"""

if old_emo:
    content = content.replace(old_emo, new_emo, 1)
    changes += 1
    print("✅ 5. P7 Personality & Empathy redesigned with expression grid")
else:
    print("❌ 5. Could not replace s-emotion")

# Also update the slide title in ALL_SLIDES
old_emotion_slide = "{id:'s-emotion',title:'Emotion States',e:'😊',quick:false}"
new_emotion_slide = "{id:'s-emotion',title:'Personality & Empathy',e:'😊',quick:false}"
if old_emotion_slide in content:
    content = content.replace(old_emotion_slide, new_emotion_slide, 1)
    changes += 1
    print("✅ 5b. s-emotion title updated")

# Also add s-emotion to light bg slides in rebuildSlides logo logic
old_lgl = "var _lgl=['s-mopt','s-mdesign'].includes(s.id);"
new_lgl = "var _lgl=['s-mopt','s-mdesign','s-emotion'].includes(s.id);"
if old_lgl in content:
    content = content.replace(old_lgl, new_lgl, 1)
    changes += 1
    print("✅ 5c. s-emotion added to light slide logo list")

# ═══════════════════════════════════════════════
# 6. P10 (s-kb) — Knowledge Base 3-column redesign
# ═══════════════════════════════════════════════
kb_pattern = r"(  case 's-kb': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">10</div>`;\})"
kb_match = re.search(kb_pattern, content, re.DOTALL)
if kb_match:
    old_kb = kb_match.group(1)
    print(f"✅ Found s-kb block ({len(old_kb)} chars)")
else:
    print("❌ s-kb block not found")
    old_kb = None

new_kb = r"""  case 's-kb': {
    // Dynamic knowledge base categories based on industry
    const ind=(STATE.industry||'').toLowerCase();
    let kbCats;
    if(ind.includes('retail')||ind.includes('supermar')||ind.includes('jumbo')){
      kbCats=[
        {hdr:{en:'Onboarding',nl:'Onboarding',zh:'入職'},
         items:{en:['Welcome to the company','First workday overview','Important documents to submit','Meet your team leader','Dress code explanation'],
                nl:['Welkom bij '+C,'Eerste werkdag uitleg','Belangrijke documenten aanleveren','Kennismaking teamleider','Uitleg bedrijfskleding']},
         docs:{en:['Welcome letter','Employment contract','General instruction booklet','App & systems guide','Dress code checklist'],
               nl:['Welkomstbrief','Arbeidsovereenkomst','Instructieboekje (algemeen)','Uitleg apps en systemen','Bedrijfskleding checklist']}},
        {hdr:{en:'Q&A',nl:'Q&A',zh:'問答'},
         items:{en:['App instructions via link','Salary deduction explanation','Company policies','Frequently asked questions'],
                nl:['Instructies via link','Loonheffingskorting uitleg','Bedrijfsregels vinden','Veelgestelde vragen']},
         docs:{en:['Staff app manual','FAQ document','Company regulations','Tax form','Link pages list'],
               nl:['Handleiding personeelsapp','FAQ document','Reglementen','Loonheffingskorting formulier','Linklijst met uitlegpagina\'s']}},
        {hdr:{en:'Offboarding',nl:'Vertrek & afronding',zh:'離職'},
         items:{en:['Resignation process','Offboarding documents','Final settlement info','Exit interview prep'],
                nl:['Opzeggen uitleg','Offboarding documenten','Eindafrekening informatie','Exitgesprek voorbereiden']},
         docs:{en:['Resignation form','Offboarding checklist','Settlement confirmation','Equipment return list','Final settlement info'],
               nl:['Opzegformulier','Offboarding checklist','Bevestiging uitdiensttreding','Inleverlijst bedrijfsmiddelen','Info over eindafrekening']}}
      ];
    } else if(ind.includes('office')||ind.includes('wtc')||ind.includes('commercial')){
      kbCats=[
        {hdr:{en:'Visitor Guide',nl:'Bezoekersgids',zh:'訪客指南'},
         items:{en:['Building access','Reception procedures','Meeting room locations','WiFi access','Emergency protocols'],
                nl:['Gebouwtoegang','Receptie procedures','Vergaderzalen locaties','WiFi toegang','Noodprotocollen']},
         docs:{en:['Access card manual','Floor plan','Emergency guide','WiFi instructions','Visitor policy'],
               nl:['Toegangspas handleiding','Plattegrond','Noodgids','WiFi instructies','Bezoekersbeleid']}},
        {hdr:{en:'Parking',nl:'Parkeerregels',zh:'停車規範'},
         items:{en:['Parking registration','Reserved spaces','EV charging','Bicycle parking','Guest parking'],
                nl:['Parkeerregistratie','Gereserveerde plekken','EV laden','Fietsenstalling','Gastenparkeren']},
         docs:{en:['Parking guide','Registration form','EV charging map','Rate overview','Garage rules'],
               nl:['Parkeergids','Registratieformulier','EV laadpuntenkaart','Tarievenoverzicht','Garagereglement']}},
        {hdr:{en:'Space Booking',nl:'Ruimte reserveren',zh:'空間預約'},
         items:{en:['Room booking system','Catering orders','AV equipment','Flex desk policy','Event spaces'],
                nl:['Zalenreservering','Catering bestellen','AV apparatuur','Flex desk beleid','Evenementruimtes']},
         docs:{en:['Booking manual','Catering menu','AV guide','Flex policy','Event request form'],
               nl:['Reserveringshandleiding','Catering menu','AV gids','Flexbeleid','Evenement aanvraagformulier']}}
      ];
    } else if(ind.includes('dent')||ind.includes('clinic')||ind.includes('medical')||ind.includes('health')){
      kbCats=[
        {hdr:{en:'New Patients',nl:'Nieuwe patiënten',zh:'新病患'},
         items:{en:['Registration process','Insurance verification','First appointment prep','Medical history form','Clinic policies'],
                nl:['Registratieproces','Verzekering verificatie','Eerste afspraak voorbereiden','Medische voorgeschiedenis','Kliniekbeleid']},
         docs:{en:['Registration form','Insurance guide','Patient welcome letter','Medical history form','Policy document'],
               nl:['Registratieformulier','Verzekeringsgids','Welkomstbrief patiënt','Anamnese formulier','Beleidsdocument']}},
        {hdr:{en:'Return Visits',nl:'Vervolgbezoeken',zh:'複診病患'},
         items:{en:['Appointment scheduling','Treatment plans','Prescription renewals','Lab results access','Billing inquiries'],
                nl:['Afspraken inplannen','Behandelplannen','Receptverlenging','Labresultaten','Factuurvragen']},
         docs:{en:['Appointment guide','Treatment overview','Prescription form','Lab portal guide','Billing FAQ'],
               nl:['Afsprakengids','Behandeloverzicht','Receptformulier','Labportaal gids','Factuur FAQ']}},
        {hdr:{en:'Aftercare',nl:'Nazorg',zh:'術後護理'},
         items:{en:['Post-treatment care','Follow-up scheduling','Emergency contacts','Recovery guidelines','Feedback survey'],
                nl:['Post-behandeling zorg','Vervolgafspraak plannen','Noodcontacten','Herstelinstructies','Feedback enquête']},
         docs:{en:['Care instructions','Follow-up form','Emergency card','Recovery guide','Satisfaction survey'],
               nl:['Zorginstructies','Vervolgformulier','Noodkaart','Herstelgids','Tevredenheidsenquête']}}
      ];
    } else {
      // Generic / education fallback
      kbCats=[
        {hdr:{en:'Getting Started',nl:'Aan de slag',zh:'入門指南'},
         items:{en:['Platform overview','Account setup','Key features tour','FAQ access','Support channels'],
                nl:['Platform overzicht','Account instellen','Belangrijkste functies','FAQ toegang','Supportkanalen']},
         docs:{en:['Welcome guide','Setup manual','Feature guide','FAQ document','Support directory'],
               nl:['Welkomstgids','Installatiehandleiding','Functiegids','FAQ document','Support directory']}},
        {hdr:{en:'Daily Use',nl:'Dagelijks gebruik',zh:'日常使用'},
         items:{en:['Common workflows','Tips & tricks','Keyboard shortcuts','Troubleshooting','Updates log'],
                nl:['Veelgebruikte workflows','Tips & tricks','Sneltoetsen','Problemen oplossen','Updates log']},
         docs:{en:['Workflow guide','Tips sheet','Shortcut card','Troubleshoot doc','Changelog'],
               nl:['Workflow gids','Tips sheet','Sneltoetsen kaart','Probleemoplossing','Changelog']}},
        {hdr:{en:'Advanced',nl:'Geavanceerd',zh:'進階'},
         items:{en:['API access','Custom integrations','Admin settings','Analytics dashboard','Security policies'],
                nl:['API toegang','Aangepaste integraties','Admin instellingen','Analytics dashboard','Beveiligingsbeleid']},
         docs:{en:['API documentation','Integration guide','Admin manual','Analytics guide','Security policy'],
               nl:['API documentatie','Integratie gids','Admin handleiding','Analytics gids','Beveiligingsbeleid']}}
      ];
    }
    const kbTitle={en:'KNOWLEDGE BASE',nl:'KENNISBANK',zh:'知識庫',de:'WISSENSBASIS',fr:'BASE DE CONNAISSANCES',ja:'ナレッジベース',es:'BASE DE CONOCIMIENTO'};
    const kbSub={en:'What information does the buddy need?',nl:'Wat voor kennis heeft de buddy nodig?',zh:'Buddy 需要什麼資訊？',de:'Welches Wissen braucht der Buddy?',fr:'De quelles informations le buddy a-t-il besoin ?',ja:'バディにはどんな情報が必要？',es:'¿Qué información necesita el buddy?'};
    const kbIntro={en:`The digital buddy uses the knowledge and documents provided by ${C}. We determine per item whether the chatbot explains the content directly or simply refers via a link.`,
                   nl:`De digitale buddy gebruikt de kennis en documenten die ${C} aanlevert. Wij bepalen per document of de chatbot het inhoudelijk uitlegt of simpelweg doorverwijst via een link.`};
    const docWord={en:'Documents',nl:'Documenten',zh:'文件',de:'Dokumente',fr:'Documents',ja:'ドキュメント',es:'Documentos'};
    return `
    <div class="sl-bg-light"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="font-family:var(--fd);font-size:58px;font-weight:800;letter-spacing:-.04em;color:#111;line-height:1;margin-bottom:6px;">${e(kbTitle[L]||kbTitle.en)}</div>
      <div style="font-family:var(--fd);font-size:32px;font-weight:700;color:#111;line-height:1.15;margin-bottom:12px;">${e(kbSub[L]||kbSub.en)}</div>
      <div style="font-size:16px;color:#666;line-height:1.6;max-width:1000px;margin-bottom:8px;">${e(kbIntro[L]||kbIntro.en)}</div>
      <div class="kb3">
        ${kbCats.map(cat=>`
        <div class="kb3-col">
          <div class="kb3-hdr" style="background:${alpha(c1,.2)};color:#111;">${e(cat.hdr[L]||cat.hdr.en)}</div>
          <ul class="kb3-list" style="color:#333;">
            ${(cat.items[L]||cat.items.en).map(it=>`<li>${e(it)}</li>`).join('')}
          </ul>
          <div class="kb3-sec" style="background:#222;color:#fff;">${e(docWord[L]||docWord.en)}</div>
          <ul class="kb3-list" style="color:#333;">
            ${(cat.docs[L]||cat.docs.en).map(d=>`<li>${e(d)}</li>`).join('')}
          </ul>
        </div>`).join('')}
      </div>
    </div>
    <div class="sl-num" style="color:rgba(0,0,0,.06);">10</div>`;}"""

if old_kb:
    content = content.replace(old_kb, new_kb, 1)
    changes += 1
    print("✅ 6. P10 Knowledge Base redesigned with 3-column layout")

# Also add s-kb to light slide list for logo
old_lgl2 = "var _lgl=['s-mopt','s-mdesign','s-emotion'].includes(s.id);"
new_lgl2 = "var _lgl=['s-mopt','s-mdesign','s-emotion','s-kb'].includes(s.id);"
if old_lgl2 in content:
    content = content.replace(old_lgl2, new_lgl2, 1)
    changes += 1
    print("✅ 6b. s-kb added to light slide logo list")

# ═══════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════
with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'w') as f:
    f.write(content)
print(f"\n✅ All done — {changes} changes applied. File saved.")

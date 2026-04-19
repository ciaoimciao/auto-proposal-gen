import re

with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'r') as f:
    content = f.read()

changes = 0

# ─────────────────────────────────────────────────────────────
# 1. FILMSTRIP — Fix positioning (dock below slide, no scroll)
# ─────────────────────────────────────────────────────────────
old_dv = "#deck-view{display:none;flex-direction:row;min-height:100vh;background:#111110;}"
new_dv = "#deck-view{display:none;flex-direction:row;height:100vh;overflow:hidden;background:#111110;}"
if old_dv in content:
    content = content.replace(old_dv, new_dv, 1)
    changes += 1
    print("✅ 1a. deck-view height fixed to 100vh")
else:
    print("❌ 1a. deck-view not found")

# Reduce slide-stage padding to give filmstrip more room
old_ss = ".slide-stage{flex:1;display:flex;align-items:flex-start;justify-content:center;padding:.75rem 1rem 1.5rem;overflow:hidden;}"
new_ss = ".slide-stage{flex:1;display:flex;align-items:center;justify-content:center;padding:.5rem 1rem .5rem;overflow:hidden;min-height:0;}"
if old_ss in content:
    content = content.replace(old_ss, new_ss, 1)
    changes += 1
    print("✅ 1b. slide-stage padding reduced, centered")
else:
    print("❌ 1b. slide-stage not found")

# Make filmstrip slightly taller and more visible
old_fs_css = ".filmstrip{display:flex;gap:8px;padding:10px 16px;background:#1a1a18;border-top:1px solid rgba(255,255,255,.08);overflow-x:auto;flex-shrink:0;scrollbar-width:thin;scrollbar-color:rgba(255,255,255,.15) transparent;align-items:center;}"
new_fs_css = ".filmstrip{display:flex;gap:10px;padding:8px 16px;background:#1a1a18;border-top:1px solid rgba(255,255,255,.12);overflow-x:auto;flex-shrink:0;scrollbar-width:thin;scrollbar-color:rgba(255,255,255,.15) transparent;align-items:center;min-height:82px;}"
if old_fs_css in content:
    content = content.replace(old_fs_css, new_fs_css, 1)
    changes += 1
    print("✅ 1c. filmstrip CSS updated")
else:
    print("❌ 1c. filmstrip CSS not found")

# ─────────────────────────────────────────────────────────────
# 2. P11 — Data & Insights / De Analytics Portal
# ─────────────────────────────────────────────────────────────

# Update ALL_SLIDES title
old_an_title = "{id:'s-analytics',title:'Analytics',e:'📊',quick:true}"
new_an_title = "{id:'s-analytics',title:'Data & Insights',e:'📊',quick:true}"
if old_an_title in content:
    content = content.replace(old_an_title, new_an_title, 1)
    changes += 1
    print("✅ 2a. Analytics title updated to Data & Insights")

# Update TX data for analytics
old_an_tag = "an_tag:{en:'Analytics',nl:'Analyse',zh:'分析洞察'"
new_an_tag = "an_tag:{en:'Data & Insights',nl:'Data & Inzichten',zh:'數據洞察'"
if old_an_tag in content:
    content = content.replace(old_an_tag, new_an_tag, 1)
    changes += 1
    print("✅ 2b. an_tag TX updated")

old_an_h = "an_h:{en:'The results speak.',nl:'De resultaten spreken.',zh:'成果會說話'"
new_an_h = "an_h:{en:'De Analytics Portal.',nl:'De Analytics Portal.',zh:'分析儀表板'"
if old_an_h in content:
    content = content.replace(old_an_h, new_an_h, 1)
    changes += 1
    print("✅ 2c. an_h TX updated")

# Add dashboard upload rule to MASCOT_SLIDE_RULES
old_rules_end = "'s-roadmap':  {x:'left',  left:'0px',    bottom:'0px',                               height:'540px', maxW:'420px'},"
new_rules_end = ("'s-roadmap':  {x:'left',  left:'0px',    bottom:'0px',                               height:'540px', maxW:'420px'},\n"
                 "  's-analytics-dash': {x:'center', right:'60px', top:'140px', height:'620px', maxW:'900px'},")
if old_rules_end in content:
    content = content.replace(old_rules_end, new_rules_end, 1)
    changes += 1
    print("✅ 2d. Dashboard upload rule added")

# Replace the entire s-analytics case
an_pattern = r"(  case 's-analytics': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">11</div>`;\})"
an_match = re.search(an_pattern, content, re.DOTALL)
if an_match:
    old_an = an_match.group(1)
    new_an = r"""  case 's-analytics': {
    const anb=tx('an_badges',L)||[];
    const imgTagAn=mascotImgTag(sid,V);const hasImgAn=!!getMascotImageForSlide(sid);
    const dashUrl=STATE.dashboardImg||null;
    const anItems=[
      {ico:'📊',t:{en:'Weekly/monthly conversations',nl:'Wekelijkse/maandelijkse gesprekken',zh:'每週/每月對話次數'}},
      {ico:'🕒',t:{en:'Average conversation duration',nl:'Gemiddelde gespreksduur',zh:'平均對話時長'}},
      {ico:'⏰',t:{en:'Busiest moments (date/time)',nl:'Drukste momenten (datum/tijd)',zh:'最繁忙時段'}},
      {ico:'🧠',t:{en:'Popular topics (onboarding, Q&A, offboarding)',nl:'Populaire onderwerpen (onboarding, Q&A, vertrek)',zh:'熱門主題（入職、Q&A、離職）'}},
      {ico:'❓',t:{en:'Top 5 most asked questions',nl:'Top 5 meest gestelde vragen',zh:'前五大常見問題'}},
    ];
    const anDesc={en:'Via the online dashboard you can review your chatbot\'s monthly performance. See which questions are asked most, where employees drop off, and how active your Buddy is.',nl:'Via het online dashboard kun je elke maand de prestaties van je chatbot bekijken. Je ziet welke vragen het meest gesteld worden, waar medewerkers afhaken, en hoe actief je Buddy is.',zh:'透過線上儀表板，你可以每月查看聊天機器人的運行成果。你可以看到哪些問題最常被詢問、員工在哪個步驟放棄對話，以及夥伴的活躍程度。'};
    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="top:-80px;right:80px;width:320px;height:320px;border-width:52px;border-color:${alpha(c1,.08)};"></div>
    <div class="sl-safe" style="display:grid;grid-template-columns:480px 1fr;gap:48px;align-items:center;height:100%;">
      <div style="display:flex;flex-direction:column;justify-content:center;">
        <div class="sl-tag" style="${tagStyle}">${e(tx('an_tag',L))}</div>
        <div class="sl-h3" style="${h3Style}">${e(tx('an_h',L))}</div>
        <div style="font-size:20px;color:${V.TX2};line-height:1.6;margin-bottom:28px;">${e(anDesc[L]||anDesc.en)}</div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          ${anItems.map(a=>'<div style="display:flex;align-items:center;gap:12px;font-size:20px;"><span style="font-size:22px;">'+a.ico+'</span><span style="color:'+V.TX+';font-weight:500;">'+e(a.t[L]||a.t.en)+'</span></div>').join('')}
        </div>
        <div style="margin-top:24px;display:flex;gap:8px;flex-wrap:wrap;">
          ${anb.map(b=>'<span style="background:'+alpha(c1,.12)+';color:'+c1+';border:1px solid '+alpha(c1,.25)+';padding:4px 14px;border-radius:26px;font-size:16px;">'+b+'</span>').join('')}
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;">
        <div style="position:relative;width:100%;max-width:680px;">
          <!-- Laptop mockup frame -->
          <div style="background:#222;border-radius:14px 14px 0 0;padding:8px 8px 0;box-shadow:0 20px 60px rgba(0,0,0,.5);">
            <div style="display:flex;align-items:center;gap:5px;padding:5px 12px 8px;">
              <div style="width:7px;height:7px;border-radius:50%;background:#FF5F57;"></div>
              <div style="width:7px;height:7px;border-radius:50%;background:#FEBC2E;"></div>
              <div style="width:7px;height:7px;border-radius:50%;background:#28C840;"></div>
              <div style="flex:1;margin-left:12px;height:18px;background:rgba(255,255,255,.08);border-radius:4px;display:flex;align-items:center;padding:0 8px;"><span style="font-size:10px;color:rgba(255,255,255,.35);">analytics.notso.ai</span></div>
            </div>
            ${dashUrl ? '<img src="'+dashUrl+'" style="width:100%;border-radius:4px 4px 0 0;display:block;" alt="dashboard"/>' : '<div style="background:#1a1a2e;border-radius:4px 4px 0 0;padding:20px 24px;min-height:320px;"><div style="display:flex;gap:12px;margin-bottom:16px;"><div style="flex:1;background:rgba(255,255,255,.06);border-radius:10px;padding:14px;"><div style="font-size:10px;color:rgba(255,255,255,.4);margin-bottom:4px;">Conversations</div><div style="font-size:24px;font-weight:800;color:#fff;font-family:var(--fd);">1,247</div><div style="font-size:9px;color:#4CD8A8;margin-top:2px;">↑ +18%</div></div><div style="flex:1;background:rgba(255,255,255,.06);border-radius:10px;padding:14px;"><div style="font-size:10px;color:rgba(255,255,255,.4);margin-bottom:4px;">Resolved</div><div style="font-size:24px;font-weight:800;color:'+c1+';font-family:var(--fd);">87%</div><div style="font-size:9px;color:#4CD8A8;margin-top:2px;">↑ +5%</div></div><div style="flex:1;background:rgba(255,255,255,.06);border-radius:10px;padding:14px;"><div style="font-size:10px;color:rgba(255,255,255,.4);margin-bottom:4px;">Avg. Duration</div><div style="font-size:24px;font-weight:800;color:#fff;font-family:var(--fd);">2:34</div><div style="font-size:9px;color:rgba(255,255,255,.3);">minutes</div></div></div><div style="display:flex;gap:12px;"><div style="flex:2;background:rgba(255,255,255,.04);border-radius:10px;padding:14px;min-height:140px;"><div style="font-size:10px;color:rgba(255,255,255,.4);margin-bottom:8px;">Weekly Conversations</div><svg width="100%" height="80" viewBox="0 0 300 80" preserveAspectRatio="none"><polyline fill="none" stroke="'+c1+'" stroke-width="2" points="0,60 40,45 80,55 120,30 160,35 200,15 240,25 280,10 300,20"/><polyline fill="none" stroke="'+alpha(c2,.5)+'" stroke-width="2" stroke-dasharray="4,4" points="0,65 40,60 80,62 120,50 160,52 200,40 240,42 280,35 300,38"/></svg></div><div style="flex:1;background:rgba(255,255,255,.04);border-radius:10px;padding:14px;"><div style="font-size:10px;color:rgba(255,255,255,.4);margin-bottom:8px;">Top Topics</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:9px;color:rgba(255,255,255,.6);">Onboarding</span><div style="width:60%;height:4px;background:rgba(255,255,255,.1);border-radius:2px;overflow:hidden;"><div style="width:72%;height:100%;background:'+c1+';border-radius:2px;"></div></div></div><div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:9px;color:rgba(255,255,255,.6);">Q&A</span><div style="width:60%;height:4px;background:rgba(255,255,255,.1);border-radius:2px;overflow:hidden;"><div style="width:55%;height:100%;background:'+c2+';border-radius:2px;"></div></div></div><div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:9px;color:rgba(255,255,255,.6);">Vertrek</span><div style="width:60%;height:4px;background:rgba(255,255,255,.1);border-radius:2px;overflow:hidden;"><div style="width:30%;height:100%;background:#4CD8A8;border-radius:2px;"></div></div></div></div></div></div></div>'}
          </div>
          <div style="width:110%;margin-left:-5%;height:14px;background:#333;border-radius:0 0 8px 8px;"></div>
          <div style="width:40%;margin:0 auto;height:4px;background:#444;border-radius:0 0 4px 4px;"></div>
        </div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">11</div>`;}"""
    content = content.replace(old_an, new_an, 1)
    changes += 1
    print("✅ 2e. s-analytics redesigned as Data & Insights with mockup")
else:
    print("❌ 2e. s-analytics block not found")

# ─────────────────────────────────────────────────────────────
# 3. P12 ROADMAP — Two variants + seasonal auto-adjust
# ─────────────────────────────────────────────────────────────
rm_pattern = r"(  case 's-roadmap': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">12</div>`;\})"
rm_match = re.search(rm_pattern, content, re.DOTALL)
if rm_match:
    old_rm = rm_match.group(1)
    new_rm = r"""  case 's-roadmap': {
    const imgTagRm=mascotImgTag(sid,V);const hasImgRm=!!getMascotImageForSlide(sid);
    const rmColors=[c1,c2,'#4CD8A8','#F7C94E',c1,c2];
    const layoutRM=STATE.layout||'spread';
    // Seasonal events auto-adjust based on kickoff date
    const allSeasons=[
      {month:1,lbl:{en:"New Year campaign",nl:"Nieuwjaarscampagne",zh:"新年活動"}},
      {month:2,lbl:{en:"Valentine's update",nl:"Valentijnsdag update",zh:"情人節更新"}},
      {month:3,lbl:{en:"Easter special",nl:"Paas-special",zh:"復活節特別版"}},
      {month:5,lbl:{en:"Mother's Day",nl:"Moederdag",zh:"母親節"}},
      {month:6,lbl:{en:"Summer campaign",nl:"Zomercampagne",zh:"夏季活動"}},
      {month:8,lbl:{en:"Back to school",nl:"Back to school",zh:"開學季"}},
      {month:10,lbl:{en:"Halloween",nl:"Halloween",zh:"萬聖節"}},
      {month:11,lbl:{en:"Black Friday",nl:"Black Friday",zh:"黑色星期五"}},
      {month:12,lbl:{en:"Christmas & NYE",nl:"Kerst & Oud & Nieuw",zh:"聖誕節與跨年"}},
    ];
    const kickMonth=base?base.getMonth()+1:1;
    const futureSeasons=allSeasons.filter(s=>{
      if(s.month>=kickMonth+2) return true;
      if(s.month<kickMonth) return true; // next year
      return false;
    }).slice(0,4);
    const seasonLbl={en:'Seasonal Updates',nl:'Seizoensgebonden updates',zh:'季節性更新'};

    if(layoutRM==='impact'){
      // VERTICAL TIMELINE variant
      return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="bottom:-60px;left:-60px;width:340px;height:340px;border-width:56px;border-color:${alpha(c1,.09)};"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;">
      <div class="sl-tag" style="${tagStyle};margin-bottom:8px;">${e(tx('rm_tag',L))}</div>
      <div class="sl-h3" style="${h3Style}">${e(tx('rm_h',L))}</div>
      <div style="display:grid;grid-template-columns:1fr 280px;gap:36px;margin-top:20px;">
        <div style="position:relative;padding-left:40px;">
          <div style="position:absolute;left:14px;top:0;bottom:0;width:2px;background:${alpha(V.TX,.12)};"></div>
          ${RM_MS.map((m,i)=>{const d=addDays(base,m.off);const col=rmColors[i]||c1;return `
          <div style="position:relative;margin-bottom:16px;">
            <div style="position:absolute;left:-33px;top:6px;width:12px;height:12px;border-radius:50%;background:${col};border:3px solid ${V.BG};z-index:1;"></div>
            <div style="display:flex;align-items:baseline;gap:10px;margin-bottom:3px;">
              <span style="font-family:var(--fd);font-size:14px;font-weight:700;color:${col};min-width:70px;">${base?fmtDate(d):'Day '+m.off}</span>
              <span style="font-family:var(--fd);font-size:20px;font-weight:700;color:${V.TX};">${e(m.lbl[L]||m.lbl.en)}</span>
            </div>
            <div style="font-size:16px;color:${V.TX3};line-height:1.5;padding-left:80px;">${e(m.detail[L]||m.detail.en)}</div>
          </div>`}).join('')}
        </div>
        <div style="background:${alpha(V.TX,.04)};border:1px solid ${alpha(V.TX,.08)};border-radius:16px;padding:20px 22px;">
          <div style="font-family:var(--fd);font-size:16px;font-weight:700;color:${c1};letter-spacing:.08em;text-transform:uppercase;margin-bottom:14px;">📅 ${seasonLbl[L]||seasonLbl.en}</div>
          <div style="display:flex;flex-direction:column;gap:10px;">
            ${futureSeasons.map(s=>'<div style="display:flex;align-items:center;gap:10px;padding:8px 12px;background:'+alpha(V.TX,.05)+';border-radius:10px;"><span style="font-size:16px;color:'+V.TX+';font-weight:500;">'+e(s.lbl[L]||s.lbl.en)+'</span></div>').join('')}
          </div>
        </div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">12</div>`;}

    // SPREAD / DEFAULT — Horizontal timeline
    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="bottom:-60px;left:-60px;width:340px;height:340px;border-width:56px;border-color:${alpha(c1,.09)};"></div>
    ${hasImgRm ? imgTagRm : ''}
    <div class="sl-safe" style="${hasImgRm?'left:460px;':''}display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:24px;margin-bottom:16px;">
        <div class="sl-tag" style="${tagStyle};margin-bottom:0;">${e(tx('rm_tag',L))}</div>
      </div>
      <div class="sl-h3" style="${h3Style}">${e(tx('rm_h',L))}</div>
      <div class="hrm" style="grid-template-columns:repeat(${RM_MS.length},1fr);gap:0;">
        ${RM_MS.map((m,i)=>{const d=addDays(base,m.off);const col=rmColors[i]||c1;return `
          <div class="hrm-step">
            <div class="hrm-num" style="color:${alpha(V.TX,.25)};">0${i+1}</div>
            <div class="hrm-bar" style="background:${col};"></div>
            <div class="hrm-body" style="background:${alpha(V.TX,.05)};border:1px solid ${alpha(V.TX,.09)};">
              <div class="hrm-ttl" style="color:${V.TX};">${e(m.lbl[L]||m.lbl.en)}</div>
              <div class="hrm-txt" style="color:${V.TX3};">${e(m.detail[L]||m.detail.en)}</div>
              <div class="hrm-date" style="color:${col};">${base?fmtDate(d)+' · ':''}Day ${m.off}</div>
            </div>
          </div>`}).join('')}
      </div>
      <div style="margin-top:18px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
        <span style="font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:${V.TX3};">📅 ${seasonLbl[L]||seasonLbl.en}:</span>
        ${futureSeasons.map(s=>'<span style="background:'+alpha(V.TX,.05)+';border:1px solid '+alpha(V.TX,.08)+';padding:4px 14px;border-radius:20px;font-size:14px;color:'+V.TX2+';">'+e(s.lbl[L]||s.lbl.en)+'</span>').join('')}
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">12</div>`;}"""
    content = content.replace(old_rm, new_rm, 1)
    changes += 1
    print("✅ 3. Roadmap redesigned with 2 variants + seasonal auto-adjust")
else:
    print("❌ 3. s-roadmap block not found")

# ─────────────────────────────────────────────────────────────
# 4. P16 CLOSING SLIDE — Full redesign with contact block
# ─────────────────────────────────────────────────────────────
ty_pattern = r"(  case 's-thankyou': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">16</div>`;\})"
ty_match = re.search(ty_pattern, content, re.DOTALL)
if ty_match:
    old_ty = ty_match.group(1)
    new_ty = r"""  case 's-thankyou': {
    const imgTag=mascotImgTag(sid,V);const hasImg=!!getMascotImageForSlide(sid);
    const mData3=MASCOTS.find(x=>x.id===STATE.mascotStyle)||MASCOTS[2];
    const bigEmoji3=mData3.avatar||'🤖';
    // Auto-generate audience-specific closing
    const ind2=(STATE.industry||'').toLowerCase();
    let closingTarget={en:'the employees of the future',nl:'de medewerkers van de toekomst',zh:'未來的員工'};
    if(ind2.includes('retail')||ind2.includes('supermark'))closingTarget={en:'the supermarket employees of tomorrow',nl:'de supermarktmedewerkers van morgen',zh:'未來的超市員工'};
    else if(ind2.includes('finance')||ind2.includes('bank'))closingTarget={en:'the financial professionals of the future',nl:'de financieel professionals van de toekomst',zh:'未來的金融專業人才'};
    else if(ind2.includes('health')||ind2.includes('medic')||ind2.includes('dent')||ind2.includes('zorg'))closingTarget={en:'the caregivers of tomorrow',nl:'de zorgverleners van morgen',zh:'未來的醫護人員'};
    else if(ind2.includes('edu')||ind2.includes('school')||ind2.includes('universit'))closingTarget={en:'the students of tomorrow',nl:'de studenten van morgen',zh:'未來的學生'};
    else if(ind2.includes('legal')||ind2.includes('law')||ind2.includes('advocat'))closingTarget={en:'the legal professionals of tomorrow',nl:'de juridische professionals van morgen',zh:'未來的法律專業人才'};
    else if(ind2.includes('office')||ind2.includes('wtc')||ind2.includes('vastgoed'))closingTarget={en:'the office professionals of the future',nl:'de kantoorprofessionals van de toekomst',zh:'未來的辦公室專業人才'};
    const ctLbl={en:'Supporting',nl:'Ondersteuning voor',zh:'支援'};
    const mascotCTA={en:'bring '+MN+' to life',nl:MN+' tot leven brengen',zh:'讓'+MN+'活起來'};
    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="top:-140px;right:-140px;width:640px;height:640px;border-width:90px;border-color:${alpha(c2,.18)};"></div>
    <div class="geo-ring" style="bottom:-60px;right:200px;width:280px;height:280px;border-width:44px;border-color:${alpha(c1,.12)};"></div>
    <div style="position:absolute;inset:0;display:grid;grid-template-columns:${hasImg?'1fr 420px':'1fr 340px'};gap:40px;padding:64px 80px;">
      <div style="display:flex;flex-direction:column;justify-content:center;">
        <div class="sl-tag" style="${tagStyle}">${e(tx('ty_tag',L))}</div>
        <div style="font-family:var(--fd);font-size:72px;font-weight:800;line-height:.92;letter-spacing:-.04em;color:${V.TX};margin-bottom:16px;">${e(ctLbl[L]||ctLbl.en)}<br/><span style="color:${c1};">${e(closingTarget[L]||closingTarget.en)}</span></div>
        <div style="font-size:26px;color:${V.TX2};line-height:1.5;margin-bottom:20px;font-style:italic;">${e((mascotCTA[L]||mascotCTA.en).charAt(0).toUpperCase()+(mascotCTA[L]||mascotCTA.en).slice(1))}! 🚀</div>
        <div style="border-top:2px solid ${alpha(V.TX,.12)};padding-top:24px;display:grid;grid-template-columns:1fr 1fr;gap:12px 32px;">
          <div style="display:flex;align-items:center;gap:10px;font-size:20px;color:${V.TX2};">📞 <span style="color:${V.TX};">+31 6 34 197 668</span></div>
          <div style="display:flex;align-items:center;gap:10px;font-size:20px;color:${V.TX2};">✉️ <a href="mailto:hello@notso.ai" style="color:${c1};text-decoration:none;">hello@notso.ai</a></div>
          <div style="display:flex;align-items:center;gap:10px;font-size:20px;color:${V.TX2};">🌐 <a href="https://www.notso.ai" target="_blank" style="color:${c1};text-decoration:none;">www.notso.ai</a></div>
          <div style="display:flex;align-items:center;gap:10px;font-size:20px;color:${V.TX2};">🏢 <span style="color:${V.TX};">Berkenstraat 11, Duivendrecht</span></div>
        </div>
        <div style="margin-top:16px;padding-top:14px;border-top:1px solid ${alpha(V.TX,.06)};display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:${V.TX3};letter-spacing:.02em;">
          <span>Notso B.V.</span>
          <span>KvK: 95131124</span>
          <span>RSIN: 867013916</span>
          <span>VAT: NL867013316B01</span>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
        ${hasImg ? '<img src="'+getMascotImageForSlide(sid)+'" style="height:600px;max-width:400px;object-fit:contain;filter:drop-shadow(0 30px 60px '+alpha(V.BG,.5)+');" alt="mascot"/>' :
          '<div style="font-size:380px;line-height:1;filter:drop-shadow(0 30px 60px rgba(0,0,0,.3));">'+bigEmoji3+'</div>'}
        <div style="margin-top:16px;background:${c1};color:${STATE.colorTxt||'#fff'};font-family:var(--fd);font-size:18px;font-weight:700;padding:12px 32px;border-radius:40px;letter-spacing:.06em;text-transform:uppercase;">Book a call →</div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">16</div>`;}"""
    content = content.replace(old_ty, new_ty, 1)
    changes += 1
    print("✅ 4. Closing slide redesigned with contact block + mascot CTA")
else:
    print("❌ 4. s-thankyou block not found")

# ─────────────────────────────────────────────────────────────
# 5. ADD DASHBOARD IMAGE UPLOAD SUPPORT
# ─────────────────────────────────────────────────────────────
# Add STATE.dashboardImg initialization if not present
old_state_init = "STATE.mascotStyle=STATE.mascotStyle||'liza';"
if old_state_init in content:
    content = content.replace(old_state_init, old_state_init + "\nSTATE.dashboardImg=STATE.dashboardImg||null;", 1)
    changes += 1
    print("✅ 5. STATE.dashboardImg initialized")

# ─────────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────────
with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'w') as f:
    f.write(content)
print(f"\n✅ All done — {changes} changes applied. File saved.")

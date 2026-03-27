import re

with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'r') as f:
    content = f.read()

changes = 0

# ─────────────────────────────────────────────────────────────
# 1. P2 TOC — Fix text clipping (reduce sizes)
# ─────────────────────────────────────────────────────────────

# Fix spread/editorial TOC title from 78px to 52px
toc_pattern = r"(  case 's-toc': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">02</div>`;\})"
toc_match = re.search(toc_pattern, content, re.DOTALL)
if toc_match:
    old_toc = toc_match.group(1)
    new_toc = r"""  case 's-toc': {
    const tocLayout=STATE.layout||'spread';
    const tocItems=activeSl.filter((_,i)=>i>0).map((si,pos)=>{const s=ALL_SLIDES[si];return {num:'0'+(pos+1),e:s.e,title:s.title};});

    if(tocLayout==='impact'){
      return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="font-family:var(--fd);font-size:64px;font-weight:800;letter-spacing:-.04em;color:${V.TX};margin-bottom:10px;">AGENDA</div>
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
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:flex-start;padding-top:48px;">
      <div style="font-family:var(--fd);font-size:52px;font-weight:800;letter-spacing:-.04em;color:${V.TX};line-height:1;margin-bottom:6px;">${e(tx('toc_h',L))}</div>
      <div style="font-size:18px;color:${V.TX3};margin-bottom:10px;">${e(C)} — ${e(IND)}</div>
      <div class="toc-arrow" style="gap:8px 48px;">
        ${tocItems.map(t=>`
        <div class="toc-arrow-item" style="border-color:${alpha(V.TX,.08)};padding:12px 0;">
          <div class="toc-arrow-ico" style="color:${c1};font-size:22px;">→</div>
          <div>
            <div class="toc-arrow-ttl" style="color:${V.TX};font-size:22px;">${e(t.title)}</div>
            <div class="toc-arrow-desc" style="color:${V.TX3};font-size:14px;">${t.e} ${t.title}</div>
          </div>
        </div>`).join('')}
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">02</div>`;}"""
    content = content.replace(old_toc, new_toc, 1)
    changes += 1
    print("✅ 1. TOC clipping fixed — reduced font sizes")
else:
    print("❌ 1. s-toc block not found")

# Also reduce the CSS base sizes for toc-agenda
content = content.replace(
    ".toc-agenda-item{display:flex;align-items:flex-start;gap:16px;padding:28px 0;",
    ".toc-agenda-item{display:flex;align-items:flex-start;gap:14px;padding:18px 0;", 1)
content = content.replace(
    ".toc-agenda-num{font-family:var(--fd);font-size:38px;",
    ".toc-agenda-num{font-family:var(--fd);font-size:32px;", 1)
content = content.replace(
    ".toc-agenda-ttl{font-family:var(--fd);font-size:26px;",
    ".toc-agenda-ttl{font-family:var(--fd);font-size:22px;", 1)
content = content.replace(
    ".toc-agenda-desc{font-size:18px;",
    ".toc-agenda-desc{font-size:14px;", 1)
changes += 1
print("✅ 1b. TOC agenda CSS sizes reduced")

# ─────────────────────────────────────────────────────────────
# 2. P9 CHATFLOW — Flowchart-style redesign
# ─────────────────────────────────────────────────────────────

# Update ALL_SLIDES title
old_cf_title = "{id:'s-chatflow',title:'Chatflow',e:'🔀',quick:false}"
new_cf_title = "{id:'s-chatflow',title:'Chatflow Design',e:'🔀',quick:false}"
if old_cf_title in content:
    content = content.replace(old_cf_title, new_cf_title, 1)
    changes += 1
    print("✅ 2a. Chatflow title updated")

# Update TX data
old_cf_tag = "flow_tag:{en:'Architecture',nl:'Architectuur'"
new_cf_tag = "flow_tag:{en:'Chatflow',nl:'Chatflow'"
if old_cf_tag in content:
    content = content.replace(old_cf_tag, new_cf_tag, 1)
    changes += 1
    print("✅ 2b. flow_tag TX updated")

old_cf_h = "flow_h:{en:'Conversation flow.',nl:'Gespreksflow.'"
new_cf_h = "flow_h:{en:'Chatflow Design',nl:'Chatflow Design'"
if old_cf_h in content:
    content = content.replace(old_cf_h, new_cf_h, 1)
    changes += 1
    print("✅ 2c. flow_h TX updated")

# Replace the chatflow slide
cf_pattern = r"(  case 's-chatflow': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">09</div>`;\})"
cf_match = re.search(cf_pattern, content, re.DOTALL)
if cf_match:
    old_cf = cf_match.group(1)
    new_cf = r"""  case 's-chatflow': {
    const mData4=MASCOTS.find(x=>x.id===STATE.mascotStyle)||MASCOTS[2];
    const cfEmoji=mData4.avatar||'🤖';
    const ind3=(STATE.industry||'').toLowerCase();
    // Dynamic scenario based on industry
    let cfWelcome={en:'How are things going with your work?',nl:'Hoe gaat het met je werk?',zh:'工作順利嗎？'};
    let cfUserMsg={en:'I spent the whole weekend trying to figure out the process...',nl:'Ik ben het hele weekend bezig geweest met het uitzoeken van het proces...',zh:'我整個週末都在研究這個流程…'};
    let cfEmpathy={en:'I totally understand. Doing it manually is really tedious work.',nl:'Ik snap je helemaal. Handmatig uitzoeken is echt monnikenwerk.',zh:'我完全理解。手動處理真的是苦差事。'};
    let cfSplit={en:'Did you know you can automate this?',nl:'Wist je dat je dit kunt automatiseren?',zh:'你知道這可以自動化嗎？'};
    let cfUpsell={en:'With our automation module, all requests are processed at once.',nl:'Met onze automatiseringsmodule worden alle verzoeken in één keer verwerkt.',zh:'透過我們的自動化模組，所有請求可一次處理完畢。'};
    if(ind3.includes('retail')||ind3.includes('supermark')){
      cfWelcome={en:'How is the onboarding going?',nl:'Lukt het met de inwerking?',zh:'入職培訓進行得如何？'};
      cfUserMsg={en:'New employees keep calling me with the same uniform questions...',nl:'Nieuwe medewerkers blijven me bellen met dezelfde vragen over het uniform...',zh:'新員工一直打電話來問同樣的制服問題…'};
    }else if(ind3.includes('dent')||ind3.includes('health')||ind3.includes('zorg')){
      cfWelcome={en:'Can I help with appointment scheduling?',nl:'Kan ik helpen met afspraken inplannen?',zh:'我可以幫忙預約排程嗎？'};
      cfUserMsg={en:'Patients keep calling because they can\'t figure out the online booking...',nl:'Patiënten blijven bellen omdat ze niet uit de online boeking komen...',zh:'病患一直打電話來因為搞不清楚線上預約…'};
    }else if(ind3.includes('edu')||ind3.includes('universit')){
      cfWelcome={en:'Questions about your studies?',nl:'Vragen over je studie?',zh:'關於學業有問題嗎？'};
      cfUserMsg={en:'I don\'t know how to register for courses and the deadline is tomorrow...',nl:'Ik weet niet hoe ik me moet inschrijven en de deadline is morgen...',zh:'我不知道怎麼選課，截止日期是明天…'};
    }
    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;gap:0;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
        <div>
          <div style="font-size:18px;color:${V.TX3};font-family:var(--fd);font-weight:600;">Stap 4:</div>
          <div style="font-family:var(--fd);font-size:52px;font-weight:800;color:${V.TX};line-height:1;letter-spacing:-.03em;">${e(tx('flow_h',L))}</div>
        </div>
        <div style="max-width:480px;font-size:17px;color:${V.TX2};line-height:1.5;padding-top:14px;">${e(tx('flow_body',L))}</div>
      </div>
      <!-- Flowchart mockup -->
      <div style="background:${alpha(V.TX,.03)};border:1px solid ${alpha(V.TX,.08)};border-radius:20px;padding:32px 36px;position:relative;overflow:hidden;">
        <div style="position:absolute;top:16px;left:28px;font-family:var(--fd);font-size:16px;font-weight:800;color:${alpha(V.TX,.15)};letter-spacing:.1em;text-transform:uppercase;writing-mode:vertical-lr;">VOORBEELD CHATFLOW</div>
        <div style="display:grid;grid-template-columns:180px 200px 240px 280px 220px;gap:18px;align-items:center;margin-left:28px;">
          <!-- 1. Welcome -->
          <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
            <div style="width:52px;height:52px;border-radius:50%;background:${alpha(V.TX,.08)};display:flex;align-items:center;justify-content:center;font-size:28px;">${cfEmoji}</div>
            <div style="background:${alpha(V.TX,.06)};border:1px solid ${alpha(V.TX,.1)};border-radius:12px;padding:12px 14px;width:100%;text-align:center;">
              <div style="font-family:var(--fd);font-size:14px;font-weight:700;color:${V.TX};margin-bottom:4px;">Welkoms bericht</div>
              <div style="font-size:12px;color:${V.TX3};line-height:1.4;font-style:italic;">"${cfWelcome[L]||cfWelcome.en}"</div>
            </div>
          </div>
          <!-- 2. User input -->
          <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
            <div style="width:52px;height:52px;border-radius:50%;background:${alpha(c1,.15)};display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:${c1};font-family:var(--fd);">USER</div>
            <div style="background:${alpha(c1,.08)};border:1px solid ${alpha(c1,.2)};border-radius:12px;padding:12px 14px;width:100%;">
              <div style="font-family:var(--fd);font-size:14px;font-weight:700;color:${V.TX};margin-bottom:4px;">Gebruiker</div>
              <div style="font-size:12px;color:${V.TX2};line-height:1.4;">${cfUserMsg[L]||cfUserMsg.en}</div>
            </div>
          </div>
          <!-- 3. Brain processing -->
          <div style="display:flex;flex-direction:column;gap:6px;">
            <div style="background:${alpha(c2,.1)};border:1px solid ${alpha(c2,.2)};border-radius:10px;padding:8px 12px;display:flex;align-items:center;gap:8px;">
              <span style="font-size:16px;">✨</span>
              <div><div style="font-size:13px;font-weight:700;color:${V.TX};">Emotie selecteren</div><div style="font-size:11px;color:${c2};border:1px solid ${alpha(c2,.3)};border-radius:20px;padding:1px 8px;display:inline-block;margin-top:2px;">Meelevend</div></div>
            </div>
            <div style="background:${alpha(V.TX,.05)};border:1px solid ${alpha(V.TX,.1)};border-radius:10px;padding:8px 12px;display:flex;align-items:center;gap:8px;">
              <span style="font-size:16px;">🔍</span>
              <div style="font-size:13px;font-weight:700;color:${V.TX};">Kennis zoeken</div>
            </div>
            <div style="background:${alpha('#4CD8A8',.1)};border:1px solid ${alpha('#4CD8A8',.2)};border-radius:10px;padding:8px 12px;display:flex;align-items:center;gap:8px;">
              <span style="font-size:16px;">🛡️</span>
              <div style="font-size:13px;font-weight:700;color:${V.TX};">Control Agent</div>
            </div>
          </div>
          <!-- 4. Response -->
          <div style="display:flex;flex-direction:column;gap:6px;">
            <div style="font-family:var(--fd);font-size:16px;font-weight:700;color:${V.TX};margin-bottom:2px;">Antwoord</div>
            <div style="display:flex;gap:8px;align-items:flex-start;">
              <div style="width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;">${cfEmoji}</div>
              <div style="background:${alpha(V.TX,.06)};border-radius:10px;padding:10px 12px;font-size:12px;color:${V.TX};line-height:1.4;">${cfEmpathy[L]||cfEmpathy.en}</div>
            </div>
            <div style="background:${alpha(c2,.08)};border-radius:10px;padding:8px 12px;font-size:12px;color:${V.TX2};display:flex;align-items:center;gap:6px;">
              <span style="color:${c2};font-size:14px;">💡</span>${cfSplit[L]||cfSplit.en}
            </div>
            <div style="background:${alpha(c1,.08)};border-radius:10px;padding:8px 12px;font-size:12px;color:${V.TX2};display:flex;align-items:center;gap:6px;">
              <span style="color:${c1};font-size:14px;">📈</span>${cfUpsell[L]||cfUpsell.en}
            </div>
          </div>
          <!-- 5. Conversion -->
          <div style="display:flex;flex-direction:column;align-items:center;gap:8px;">
            <div style="width:52px;height:52px;border-radius:50%;background:${alpha(c1,.15)};display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:${c1};font-family:var(--fd);">USER</div>
            <div style="background:${alpha(V.TX,.06)};border:1px solid ${alpha(V.TX,.1)};border-radius:12px;padding:12px 14px;width:100%;">
              <div style="font-size:12px;color:${V.TX2};line-height:1.4;margin-bottom:6px;">Klinkt goed, wat kost dat?</div>
            </div>
            <div style="background:${alpha(c1,.1)};border:1px solid ${alpha(c1,.25)};border-radius:12px;padding:10px 14px;width:100%;text-align:center;">
              <div style="font-size:12px;color:${c1};font-weight:600;">🔗 Link naar module</div>
            </div>
          </div>
        </div>
        <!-- Flow arrows overlay -->
        <div style="position:absolute;top:50%;left:0;right:0;display:flex;justify-content:space-around;pointer-events:none;padding:0 120px;">
          <div style="color:${alpha(V.TX,.15)};font-size:28px;font-family:var(--fd);">→</div>
          <div style="color:${alpha(V.TX,.15)};font-size:28px;font-family:var(--fd);">→</div>
          <div style="color:${alpha(V.TX,.15)};font-size:28px;font-family:var(--fd);">→</div>
          <div style="color:${alpha(V.TX,.15)};font-size:28px;font-family:var(--fd);">→</div>
        </div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">09</div>`;}"""
    content = content.replace(old_cf, new_cf, 1)
    changes += 1
    print("✅ 2d. P9 Chatflow redesigned with flowchart layout")
else:
    print("❌ 2d. s-chatflow block not found")

# Add s-chatflow to light slide detection? No, keep dark bg

# ─────────────────────────────────────────────────────────────
# 3. P14 PROMO — Redesign with mockup cards + industry-adaptive text
# ─────────────────────────────────────────────────────────────

prm_pattern = r"(  case 's-promo': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">14</div>`;\})"
prm_match = re.search(prm_pattern, content, re.DOTALL)
if prm_match:
    old_prm = prm_match.group(1)
    new_prm = r"""  case 's-promo': {
    const mData5=MASCOTS.find(x=>x.id===STATE.mascotStyle)||MASCOTS[2];
    const pEmoji=mData5.avatar||'🤖';
    const ind4=(STATE.industry||'').toLowerCase();
    // Industry-adaptive location terms
    let promoLoc={en:'canteen or lobby',nl:'kantine of lobby',zh:'餐廳或大廳'};
    if(ind4.includes('retail')||ind4.includes('supermark'))promoLoc={en:'staff canteen or warehouse',nl:'kantine of loods',zh:'員工餐廳或倉庫'};
    else if(ind4.includes('dent')||ind4.includes('health')||ind4.includes('zorg'))promoLoc={en:'waiting room or reception',nl:'wachtkamer of receptie',zh:'候診室或接待處'};
    else if(ind4.includes('edu')||ind4.includes('universit'))promoLoc={en:'canteen or around campus',nl:'kantine of campus',zh:'餐廳或校園'};
    else if(ind4.includes('office')||ind4.includes('wtc')||ind4.includes('vastgoed'))promoLoc={en:'lobby or elevator area',nl:'lobby of bij de lift',zh:'大廳或電梯口'};
    else if(ind4.includes('legal')||ind4.includes('advocat'))promoLoc={en:'reception or meeting rooms',nl:'receptie of vergaderzalen',zh:'接待處或會議室'};
    const promoDesc={
      en:'We also design a poster featuring your chosen '+MN+' mascot — perfect for display in the '+promoLoc.en+'. Additionally, we provide a small media kit with visuals for internal communication and social media. Optionally, we can produce the mascot as a physical 3D designer toy or a large banner — this is not included in the standard package.',
      nl:'We ontwerpen ook een poster met jouw gekozen buddy '+MN+' — ideaal om op te hangen in de '+promoLoc.nl+'. Daarnaast leveren we een klein mediapakket met beelden voor interne communicatie of social media. Optioneel kunnen we de mascotte ook als fysieke 3D-designer toy of banner laten maken — dit valt buiten de standaardprijs.',
      zh:'我們也會設計一張印有您所選 '+MN+' 吉祥物的海報——非常適合展示在'+promoLoc.zh+'。此外，我們還會提供一個小型媒體包，內含可用於內部通訊與社群媒體的視覺素材。選配項目：可將吉祥物製作成實體 3D 設計師公仔或大型布條——不包含在標準方案內。'
    };
    const porLbl={en:'Price on request',nl:'Prijs op aanvraag',zh:'價格另議'};
    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="font-family:var(--fd);font-size:52px;font-weight:800;color:${V.TX};letter-spacing:-.03em;line-height:1;margin-bottom:10px;">${e(tx('prm_tag',L))}</div>
      <div style="font-size:18px;color:${V.TX2};line-height:1.6;max-width:900px;margin-bottom:28px;">${e(promoDesc[L]||promoDesc.en)}</div>
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;">
        <!-- Poster + Media Kit -->
        <div style="border-radius:18px;overflow:hidden;border:1px solid ${alpha(V.TX,.1)};">
          <div style="height:360px;background:linear-gradient(135deg,${alpha(c1,.2)},${alpha(c2,.15)});display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;padding:20px;">
            <div style="background:#fff;border-radius:8px;padding:16px 20px;box-shadow:0 8px 32px rgba(0,0,0,.3);display:flex;flex-direction:column;align-items:center;gap:8px;width:180px;">
              <div style="font-family:var(--fd);font-size:16px;font-weight:800;color:${c1};text-transform:uppercase;text-align:center;">DIGITALE<br/>BUDDY</div>
              <div style="font-size:100px;line-height:1;">${pEmoji}</div>
              <div style="background:${c1};color:#fff;font-family:var(--fd);font-size:12px;font-weight:700;padding:6px 14px;border-radius:20px;">Chat met me!</div>
            </div>
          </div>
          <div style="padding:16px 20px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:${V.TX};margin-bottom:4px;">Poster + Media pakket</div>
            <div style="font-size:16px;color:#4CD8A8;font-weight:600;">✓ ${L==='nl'?'Inbegrepen':L==='zh'?'已包含':'Included'}</div>
          </div>
        </div>
        <!-- Vinyl Toy -->
        <div style="border-radius:18px;overflow:hidden;border:1px solid ${alpha(V.TX,.1)};position:relative;">
          <div style="position:absolute;top:12px;right:12px;background:#fff;color:#111;font-family:var(--fd);font-size:14px;font-weight:700;padding:6px 16px;border-radius:8px;z-index:2;box-shadow:0 4px 16px rgba(0,0,0,.2);">${porLbl[L]||porLbl.en}</div>
          <div style="height:360px;background:linear-gradient(180deg,${alpha(V.TX,.06)},${alpha(V.TX,.02)});display:flex;align-items:center;justify-content:center;">
            <div style="font-size:200px;filter:drop-shadow(0 16px 40px rgba(0,0,0,.3));">${pEmoji}</div>
          </div>
          <div style="padding:16px 20px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:${V.TX};">Vinyl Toy</div>
          </div>
        </div>
        <!-- Banner -->
        <div style="border-radius:18px;overflow:hidden;border:1px solid ${alpha(V.TX,.1)};position:relative;">
          <div style="position:absolute;top:12px;right:12px;background:#fff;color:#111;font-family:var(--fd);font-size:14px;font-weight:700;padding:6px 16px;border-radius:8px;z-index:2;box-shadow:0 4px 16px rgba(0,0,0,.2);">${porLbl[L]||porLbl.en}</div>
          <div style="height:360px;background:linear-gradient(135deg,${alpha(c2,.2)},${alpha(c1,.15)});display:flex;align-items:center;justify-content:center;padding:20px;">
            <div style="background:linear-gradient(180deg,${c1},${alpha(c1,.8)});border-radius:12px;padding:20px 24px;display:flex;flex-direction:column;align-items:center;gap:8px;width:160px;box-shadow:0 8px 32px rgba(0,0,0,.3);">
              <div style="font-family:var(--fd);font-size:14px;font-weight:800;color:#fff;text-transform:uppercase;text-align:center;">DIGITALE BUDDY</div>
              <div style="font-size:80px;line-height:1;">${pEmoji}</div>
              <div style="font-size:12px;color:rgba(255,255,255,.9);text-align:center;font-weight:600;">Chat met me!</div>
            </div>
          </div>
          <div style="padding:16px 20px;background:${V.CARD};">
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:${V.TX};">Banner</div>
          </div>
        </div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">14</div>`;}"""
    content = content.replace(old_prm, new_prm, 1)
    changes += 1
    print("✅ 3. P14 Promo redesigned with 3 mockup cards + industry-adaptive text")
else:
    print("❌ 3. s-promo block not found")

# ─────────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────────
with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'w') as f:
    f.write(content)
print(f"\n✅ All done — {changes} changes applied. File saved.")

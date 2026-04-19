import re

with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'r') as f:
    content = f.read()

# ─────────────────────────────────────────────────────────────
# 1. ADD NOTSO.AI LOGO OVERLAY IN rebuildSlides
# ─────────────────────────────────────────────────────────────
old1 = "div.innerHTML=buildSlideHTML(s.id);canvas.appendChild(div);"
new1 = ("div.innerHTML=buildSlideHTML(s.id);\n"
        "    var _lgl=['s-mopt','s-mdesign'].includes(s.id);\n"
        "    var _lgc=_lgl?'#111111':'rgba(255,255,255,.9)';\n"
        "    var _lgd=_lgl?'#FF6B3D':'rgba(255,107,61,.95)';\n"
        "    div.insertAdjacentHTML('beforeend','<div style=\"position:absolute;top:38px;right:64px;z-index:99;display:flex;align-items:center;gap:4px;font-family:Syne,sans-serif;font-weight:800;font-size:26px;letter-spacing:-.03em;pointer-events:none;user-select:none;\"><span style=\"color:'+_lgc+';\">notso</span><span style=\"color:'+_lgd+';\">.</span><span style=\"color:'+_lgc+';\">ai</span></div>');\n"
        "    canvas.appendChild(div);")

if old1 in content:
    content = content.replace(old1, new1, 1)
    print("Logo overlay added to rebuildSlides")
else:
    print("Logo old string NOT FOUND")

# ─────────────────────────────────────────────────────────────
# 2. COVER SLIDE — 2 layout variants
# ─────────────────────────────────────────────────────────────
cover_pattern = r"(  case 's-cover': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">01</div>`;\})"
cover_match = re.search(cover_pattern, content, re.DOTALL)
if cover_match:
    old_cover = cover_match.group(1)
    print(f"Found s-cover block ({len(old_cover)} chars)")
else:
    print("s-cover block NOT FOUND via regex")
    old_cover = None

new_cover = r"""  case 's-cover': {
    const imgTag=mascotImgTag(sid,V);
    const hasImg=!!getMascotImageForSlide(sid);
    const mData2=MASCOTS.find(x=>x.id===STATE.mascotStyle)||MASCOTS[2];
    const bigMascotEmoji=mData2.avatar||'🤖';
    const clientUpper=(STATE.client||'Your Company').toUpperCase();
    const layoutMode=STATE.layout||'spread';

    // ── SPREAD variant (DIGITALE BUDDIES inspired) ──
    if(layoutMode==='spread'){
      return `
    <div class="sl-bg" style="background:linear-gradient(135deg,${c1} 0%,${c2} 100%);position:absolute;inset:0;"></div>
    <div class="geo-ring" style="top:-200px;right:-200px;width:800px;height:800px;border-width:120px;border-color:rgba(255,255,255,.1);"></div>
    <div class="geo-ring" style="bottom:-100px;right:320px;width:300px;height:300px;border-width:50px;border-color:rgba(255,255,255,.07);"></div>
    <div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 480px;align-items:center;padding:0 80px 0 100px;">
      <div style="display:flex;flex-direction:column;justify-content:center;">
        <div style="display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,.18);border-radius:40px;padding:10px 28px;width:fit-content;margin-bottom:36px;">
          <div style="width:10px;height:10px;border-radius:50%;background:#fff;animation:pd 1.8s ease-in-out infinite;"></div>
          <span style="font-family:var(--fd);font-size:20px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;">${e(tx('cover_badge',L))}</span>
        </div>
        <div style="font-family:var(--fd);font-size:96px;font-weight:800;line-height:.9;letter-spacing:-.05em;color:#fff;margin-bottom:20px;">${e(STATE.aiCoverH||tx('cover_h',L))}</div>
        <div style="font-size:28px;color:rgba(255,255,255,.75);line-height:1.5;max-width:640px;margin-bottom:48px;">${e(tx('cover_sub',L))} <strong style="color:#fff;font-weight:800;">${e(C)}</strong>.</div>
        <div style="display:flex;gap:0;border-top:2px solid rgba(255,255,255,.25);padding-top:32px;">
          <div style="flex:1;padding-right:32px;border-right:1px solid rgba(255,255,255,.2);">
            <div style="font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.55);margin-bottom:6px;">${tx('prepared',L)}</div>
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:#fff;">${e(C)}</div>
          </div>
          <div style="flex:1;padding:0 32px;border-right:1px solid rgba(255,255,255,.2);">
            <div style="font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.55);margin-bottom:6px;">${tx('industry',L)}</div>
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:#fff;">${e(IND)}</div>
          </div>
          <div style="flex:1;padding-left:32px;">
            <div style="font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.55);margin-bottom:6px;">${tx('kickoff',L)}</div>
            <div style="font-family:var(--fd);font-size:22px;font-weight:700;color:#fff;">${e(selDate?fmtDate(selDate):'—')}</div>
          </div>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:center;height:100%;">
        ${hasImg ? `<img src="${getMascotImageForSlide(sid)}" style="height:880px;max-width:520px;object-fit:contain;filter:drop-shadow(0 40px 80px rgba(0,0,0,.35));" alt="mascot"/>` :
          `<div style="font-size:580px;line-height:1;filter:drop-shadow(0 40px 80px rgba(0,0,0,.3));margin-top:60px;">${bigMascotEmoji}</div>`}
      </div>
    </div>
    <div class="sl-num" style="color:rgba(255,255,255,.08);">01</div>`;}

    // ── IMPACT variant ──
    if(layoutMode==='impact'){
      return `
    <div class="sl-bg" style="${bg}"></div>
    <div style="position:absolute;inset:0;overflow:hidden;pointer-events:none;">
      <div style="position:absolute;font-family:var(--fd);font-size:320px;font-weight:800;letter-spacing:-.06em;color:${alpha(V.TX,.04)};white-space:nowrap;top:50%;left:-60px;transform:translateY(-50%);line-height:1;text-transform:uppercase;">${clientUpper}</div>
    </div>
    <div class="geo-ring" style="top:-120px;right:-120px;width:620px;height:620px;border-width:88px;border-color:${alpha(c1,.2)};"></div>
    <div class="geo-ring" style="bottom:-60px;left:60px;width:280px;height:280px;border-width:44px;border-color:${alpha(c2,.14)};"></div>
    <div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 520px;align-items:center;padding:80px 100px;">
      <div style="display:flex;flex-direction:column;justify-content:center;">
        <div class="cvr-badge" style="background:${alpha(V.TX,.08)};border-color:${alpha(V.TX,.25)};width:fit-content;margin-bottom:44px;">
          <div class="cvr-dot" style="background:${c1};"></div>
          <span class="cvr-bt" style="color:${V.TX};">${e(tx('cover_badge',L))}</span>
        </div>
        <div style="font-family:var(--fd);font-size:110px;font-weight:800;line-height:.88;letter-spacing:-.05em;color:${V.TX};margin-bottom:28px;">${e(STATE.aiCoverH||tx('cover_h',L))}</div>
        <div style="font-size:30px;color:${V.TX2};line-height:1.5;margin-bottom:52px;">${e(tx('cover_sub',L))} <strong style="color:${V.TX};">${e(C)}</strong>.</div>
        <div style="display:flex;gap:40px;padding-top:36px;border-top:2px solid ${alpha(V.TX,.12)};">
          <div><div style="font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:${V.TX3};margin-bottom:6px;">${tx('by',L)}</div><div style="font-family:var(--fd);font-size:20px;font-weight:700;color:${V.TX};">Notso.ai</div></div>
          <div><div style="font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:${V.TX3};margin-bottom:6px;">${tx('industry',L)}</div><div style="font-family:var(--fd);font-size:20px;font-weight:700;color:${V.TX};">${e(IND)}</div></div>
          <div><div style="font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:${V.TX3};margin-bottom:6px;">${tx('kickoff',L)}</div><div style="font-family:var(--fd);font-size:20px;font-weight:700;color:${c1};">${e(selDate?fmtDate(selDate):'—')}</div></div>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;">
        <div style="width:440px;height:440px;border-radius:50%;background:linear-gradient(135deg,${alpha(c1,.25)},${alpha(c2,.15)});border:2px solid ${alpha(c1,.3)};display:flex;align-items:center;justify-content:center;position:relative;">
          ${hasImg ? `<img src="${getMascotImageForSlide(sid)}" style="height:400px;object-fit:contain;filter:drop-shadow(0 20px 40px ${alpha(V.BG,.5)});" alt="mascot"/>` :
            `<div style="font-size:320px;line-height:1;filter:drop-shadow(0 20px 40px rgba(0,0,0,.3));">${bigMascotEmoji}</div>`}
          <div style="position:absolute;bottom:-16px;left:50%;transform:translateX(-50%);background:${c1};color:#fff;font-family:var(--fd);font-size:18px;font-weight:700;padding:10px 28px;border-radius:40px;white-space:nowrap;letter-spacing:.06em;text-transform:uppercase;">${e(MN)}</div>
        </div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">01</div>`;}

    // ── DEFAULT (editorial / clean) ──
    return `
    <div class="sl-bg" style="${bg}"></div>
    ${!hasImg?`
    <div class="geo-ring" style="top:-120px;right:-120px;width:620px;height:620px;border-width:88px;border-color:${alpha(c2,.18)};"></div>
    <div class="geo-ring" style="top:-20px;right:360px;width:220px;height:220px;border-width:36px;border-color:${alpha(c1,.13)};"></div>
    <div class="geo-ring" style="bottom:-90px;left:60px;width:340px;height:340px;border-width:52px;border-color:${alpha(c2,.1)};"></div>
    `:''}
    <div class="sl-safe sl-vc" style="${hasImg?'max-width:860px;':'max-width:900px;'}">
      <div class="cvr-badge" style="background:${alpha(V.TX,.08)};border-color:${alpha(V.TX,.25)};">
        <div class="cvr-dot" style="background:${V.TX2};"></div>
        <span class="cvr-bt" style="color:${V.TX};">${e(tx('cover_badge',L))}</span>
      </div>
      <div class="sl-h1" style="${h1Style}">${e(STATE.aiCoverH||tx('cover_h',L))}</div>
      <div class="sl-body" style="${bodyStyle}">${e(tx('cover_sub',L))} <strong style="color:${V.TX};font-weight:800;">${e(C)}</strong>.</div>
      <div class="cvr-mr" style="${metaBdr}">
        <div><div class="cvr-ml" style="color:${V.TX3};">${tx('prepared',L)}</div><div class="cvr-mv" style="color:${V.TX};font-family:var(--fd);">${e(C)}</div></div>
        <div><div class="cvr-ml" style="color:${V.TX3};">${tx('industry',L)}</div><div class="cvr-mv" style="color:${V.TX};font-family:var(--fd);">${e(IND)}</div></div>
        <div><div class="cvr-ml" style="color:${V.TX3};">${tx('kickoff',L)}</div><div class="cvr-mv" style="color:${V.TX};font-family:var(--fd);">${e(selDate?fmtDate(selDate):'—')}</div></div>
        <div><div class="cvr-ml" style="color:${V.TX3};">${tx('by',L)}</div><div class="cvr-mv" style="color:${V.TX};font-family:var(--fd);">Notso.ai</div></div>
      </div>
    </div>
    ${hasImg ? imgTag : `<div style="position:absolute;right:80px;top:50%;transform:translateY(-50%);">
      <svg width="360" height="360" viewBox="0 0 360 360"><defs><radialGradient id="cg" cx="35%" cy="35%"><stop offset="0%" stop-color="${lightenHex(c2)}" stop-opacity=".9"/><stop offset="60%" stop-color="${c2}" stop-opacity=".6"/><stop offset="100%" stop-color="${V.BG}" stop-opacity="0"/></radialGradient></defs><circle cx="180" cy="180" r="150" fill="url(#cg)" opacity=".7"/><ellipse cx="140" cy="125" rx="44" ry="24" fill="${V.TX}" opacity=".14" transform="rotate(-25,140,125)"/></svg>
    </div>`}
    <div class="sl-num" style="${numStyle}">01</div>`;}"""

if old_cover:
    content = content.replace(old_cover, new_cover, 1)
    print("Cover slide updated with 2 variants")
else:
    print("Could not replace s-cover block")

# ─────────────────────────────────────────────────────────────
# 3. PRICING SLIDE — full redesign
# ─────────────────────────────────────────────────────────────
pricing_pattern = r"(  case 's-pricing': \{.*?<div class=\"sl-num\" style=\"\$\{numStyle\}\">13</div>`;\})"
pricing_match = re.search(pricing_pattern, content, re.DOTALL)
if pricing_match:
    old_pricing = pricing_match.group(1)
    print(f"Found s-pricing block ({len(old_pricing)} chars)")
else:
    print("s-pricing block NOT FOUND via regex")
    old_pricing = None

new_pricing = r"""  case 's-pricing': {
    const pp=tx('pr_plans',L)||tx('pr_plans','en');
    const addons=[
      {ico:'🎨',name:{en:'Extra character design',nl:'Extra karakterontwerp',zh:'額外角色設計',de:'Extra Charakterdesign',fr:'Design personnage sup.',ja:'追加キャラ',es:'Diseño extra'},price:'+€142'},
      {ico:'🗺️',name:{en:'Extra Journey',nl:'Extra Journey',zh:'額外旅程',de:'Extra Journey',fr:'Journey supplémentaire',ja:'追加Journey',es:'Journey extra'},price:'+€96'},
      {ico:'🤝',name:{en:'Partner licence',nl:'Partnerlicentie',zh:'合作夥伴授權',de:'Partnerlizenz',fr:'Licence partenaire',ja:'パートナーライセンス',es:'Licencia de socio'},price:'+€149'},
      {ico:'🏷️',name:{en:'Whitelabel licence',nl:'Whitelabel-licentie',zh:'白標授權',de:'White-Label-Lizenz',fr:'Licence marque blanche',ja:'ホワイトラベル',es:'Licencia whitelabel'},price:'+€349'},
    ];
    const perWord={en:'mo',nl:'mnd',zh:'月',de:'Mo',fr:'mois',ja:'月',es:'mes'};
    const pw=perWord[L]||'mo';
    const addonLbl={en:'Add-ons',nl:'Add-ons',zh:'附加選項',de:'Add-ons',fr:'Options',ja:'オプション',es:'Complementos'};
    const popularBadgeTxt=pp.popular||'Popular';
    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="top:-160px;right:-160px;width:700px;height:700px;border-width:100px;border-color:${alpha(c1,.09)};"></div>
    <div class="geo-ring" style="bottom:-80px;left:-80px;width:380px;height:380px;border-width:60px;border-color:${alpha(c2,.07)};"></div>
    <div class="sl-safe" style="display:flex;flex-direction:column;gap:0;">

      <div style="display:flex;align-items:baseline;gap:20px;margin-bottom:28px;">
        <div style="font-family:var(--fd);font-size:58px;font-weight:800;letter-spacing:-.04em;color:${V.TX};line-height:1;">${e(tx('pr_h',L))}</div>
        <div style="font-family:var(--fd);font-size:28px;font-weight:600;color:${c1};letter-spacing:.06em;text-transform:uppercase;opacity:.85;">${e(tx('pr_tag',L))}</div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1.08fr 1fr;gap:16px;flex:1;min-height:0;">

        <div style="background:${V.CARD};border:1px solid ${V.CARD_BDR};border-radius:20px;padding:28px 26px;display:flex;flex-direction:column;gap:0;">
          <div style="font-size:15px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:${V.TX3};margin-bottom:12px;">${e(pp.basic.name)}</div>
          <div style="display:flex;align-items:baseline;gap:6px;margin-bottom:10px;">
            <span style="font-family:var(--fd);font-size:62px;font-weight:800;letter-spacing:-.04em;color:${V.TX};line-height:1;">${e(pp.basic.price)}</span>
            <span style="font-size:18px;color:${V.TX3};font-weight:400;">/${pw}</span>
          </div>
          <div style="display:flex;gap:10px;margin-bottom:16px;">
            <div style="background:${alpha(V.TX,.07)};border-radius:40px;padding:4px 14px;font-size:14px;font-weight:600;color:${V.TX2};">1.000 users</div>
            <div style="background:${alpha(V.TX,.07)};border-radius:40px;padding:4px 14px;font-size:14px;font-weight:600;color:${V.TX2};">1 journey</div>
          </div>
          <div style="height:1px;background:${alpha(V.TX,.1)};margin-bottom:16px;"></div>
          <div style="display:flex;flex-direction:column;gap:9px;flex:1;">
            ${pp.basic.items.map(it=>`<div style="display:flex;align-items:flex-start;gap:10px;font-size:17px;color:${V.TX2};line-height:1.3;">
              <span style="color:${c1};font-size:18px;margin-top:1px;flex-shrink:0;">✓</span>${it}
            </div>`).join('')}
          </div>
        </div>

        <div style="background:${alpha(c1,.12)};border:2px solid ${alpha(c1,.4)};border-radius:20px;padding:28px 26px;display:flex;flex-direction:column;gap:0;position:relative;overflow:hidden;">
          <div style="position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,${c1},${c2});border-radius:20px 20px 0 0;"></div>
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;">
            <div style="font-size:15px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:${alpha(c1,.8)};">${e(pp.premium.name)}</div>
            <div style="background:${c1};color:${STATE.colorTxt||'#fff'};font-family:var(--fd);font-size:14px;font-weight:700;padding:4px 14px;border-radius:20px;letter-spacing:.06em;">★ ${popularBadgeTxt}</div>
          </div>
          <div style="display:flex;align-items:baseline;gap:6px;margin-bottom:10px;">
            <span style="font-family:var(--fd);font-size:62px;font-weight:800;letter-spacing:-.04em;color:${V.TX};line-height:1;">${e(pp.premium.price)}</span>
            <span style="font-size:18px;color:${V.TX3};font-weight:400;">/${pw}</span>
          </div>
          <div style="display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap;">
            <div style="background:${alpha(c1,.15)};border-radius:40px;padding:4px 14px;font-size:14px;font-weight:600;color:${c1};">2.000 users</div>
            <div style="background:${alpha(c1,.15)};border-radius:40px;padding:4px 14px;font-size:14px;font-weight:600;color:${c1};">2 journeys</div>
          </div>
          <div style="height:1px;background:${alpha(c1,.2)};margin-bottom:16px;"></div>
          <div style="display:flex;flex-direction:column;gap:9px;flex:1;">
            ${pp.premium.items.map(it=>`<div style="display:flex;align-items:flex-start;gap:10px;font-size:17px;color:${V.TX2};line-height:1.3;">
              <span style="color:${c1};font-size:18px;margin-top:1px;flex-shrink:0;">✓</span>${it}
            </div>`).join('')}
          </div>
        </div>

        <div style="background:${V.CARD};border:1px solid ${V.CARD_BDR};border-radius:20px;padding:28px 26px;display:flex;flex-direction:column;gap:0;">
          <div style="font-size:15px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:${V.TX3};margin-bottom:12px;">${e(pp.enterprise.name)}</div>
          <div style="display:flex;align-items:baseline;gap:6px;margin-bottom:10px;">
            <span style="font-family:var(--fd);font-size:52px;font-weight:800;letter-spacing:-.04em;color:${V.TX};line-height:1;">${e(pp.enterprise.price)}</span>
          </div>
          <div style="display:flex;gap:10px;margin-bottom:16px;">
            <div style="background:${alpha(c2,.12)};border-radius:40px;padding:4px 14px;font-size:14px;font-weight:600;color:${alpha(c2,.9)};">∞ users</div>
            <div style="background:${alpha(c2,.12)};border-radius:40px;padding:4px 14px;font-size:14px;font-weight:600;color:${alpha(c2,.9)};">∞ journeys</div>
          </div>
          <div style="height:1px;background:${alpha(V.TX,.1)};margin-bottom:16px;"></div>
          <div style="display:flex;flex-direction:column;gap:9px;flex:1;">
            ${pp.enterprise.items.map(it=>`<div style="display:flex;align-items:flex-start;gap:10px;font-size:17px;color:${V.TX2};line-height:1.3;">
              <span style="color:${c2};font-size:18px;margin-top:1px;flex-shrink:0;">✓</span>${it}
            </div>`).join('')}
          </div>
        </div>
      </div>

      <div style="margin-top:18px;">
        <div style="font-size:14px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:${V.TX3};margin-bottom:10px;">— ${addonLbl[L]||addonLbl.en}</div>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">
          ${addons.map(a=>`
          <div style="background:${alpha(V.TX,.04)};border:1px solid ${alpha(V.TX,.08)};border-radius:14px;padding:14px 16px;display:flex;align-items:center;gap:12px;">
            <span style="font-size:26px;">${a.ico}</span>
            <div style="flex:1;min-width:0;">
              <div style="font-size:15px;font-weight:600;color:${V.TX};line-height:1.3;">${a.name[L]||a.name.en}</div>
            </div>
            <div style="font-family:var(--fd);font-size:18px;font-weight:700;color:${c1};white-space:nowrap;">${a.price}</div>
          </div>`).join('')}
        </div>
      </div>

    </div>
    <div class="sl-num" style="${numStyle}">13</div>`;}"""

if old_pricing:
    content = content.replace(old_pricing, new_pricing, 1)
    print("Pricing slide redesigned")
else:
    print("Could not replace s-pricing block")

with open('/Users/albehero2323/Desktop/VibeCoding/auto-proposal-gen/index.html', 'w') as f:
    f.write(content)
print("File saved successfully")

#!/usr/bin/env python3
"""Redesign s-chat slide (page 4) to device mockup showcase layout."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Add CSS for device mockups ───
old_css = '/* Image slot assignment tags */'
new_css = """/* Device mockup frames */
.mockup-wrap{position:relative;display:flex;align-items:center;justify-content:center;width:100%;height:100%;}
.mockup-laptop{position:relative;width:680px;z-index:1;}
.mockup-laptop .ml-screen{position:relative;width:620px;height:388px;background:#1a1a1a;border-radius:8px 8px 0 0;border:3px solid #2a2a2a;overflow:hidden;margin:0 auto;}
.mockup-laptop .ml-screen img{width:100%;height:100%;object-fit:cover;object-position:top;}
.mockup-laptop .ml-screen .ml-placeholder{width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#1a1a2e,#16213e);color:rgba(255,255,255,.3);font-size:14px;font-family:var(--fb);}
.mockup-laptop .ml-base{width:680px;height:14px;background:linear-gradient(180deg,#c0c0c0,#a0a0a0);border-radius:0 0 8px 8px;position:relative;}
.mockup-laptop .ml-base::after{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:120px;height:4px;background:#888;border-radius:0 0 4px 4px;}
.mockup-laptop .ml-bottom{width:740px;height:6px;background:#888;border-radius:0 0 12px 12px;margin:0 auto;margin-top:-1px;}
.mockup-phone{position:absolute;right:-30px;bottom:20px;width:200px;z-index:2;filter:drop-shadow(-8px 8px 24px rgba(0,0,0,.25));}
.mockup-phone .mp-frame{position:relative;width:200px;height:410px;background:#1a1a1a;border-radius:28px;border:3px solid #333;padding:8px;box-sizing:border-box;}
.mockup-phone .mp-notch{position:absolute;top:8px;left:50%;transform:translateX(-50%);width:80px;height:22px;background:#1a1a1a;border-radius:0 0 14px 14px;z-index:3;}
.mockup-phone .mp-screen{width:100%;height:100%;border-radius:20px;overflow:hidden;background:#111;position:relative;}
.mockup-phone .mp-screen img{width:100%;height:100%;object-fit:cover;object-position:top;}
.mockup-phone .mp-screen .mp-placeholder{width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0f0c29,#302b63);color:rgba(255,255,255,.3);font-size:11px;font-family:var(--fb);}
.mockup-phone .mp-bar{position:absolute;bottom:6px;left:50%;transform:translateX(-50%);width:100px;height:4px;background:rgba(255,255,255,.2);border-radius:2px;}
/* Image slot assignment tags */"""

if old_css in src:
    src = src.replace(old_css, new_css)
    changes += 1
    print("✅ 1. Added device mockup CSS")
else:
    print("⚠️ 1. CSS anchor not found")

# ─── 2. Add mockup image slots to IMG_SLOTS ───
old_slots = "  {id:'s-chat',label:'Chat Demo'},"
new_slots = "  {id:'s-chat',label:'Chat Demo'},\n  {id:'s-mockup-laptop',label:'Laptop Screen'},\n  {id:'s-mockup-phone',label:'Phone Screen'},"

if old_slots in src:
    src = src.replace(old_slots, new_slots)
    changes += 1
    print("✅ 2. Added mockup slots to IMG_SLOTS")
else:
    print("⚠️ 2. IMG_SLOTS anchor not found")

# ─── 3. Update autoAssignSlides to include mockup slots ───
old_assign = "    ['s-chat','s-pain','s-analytics','s-features-2','s-features-3'],"
new_assign = "    ['s-chat','s-pain','s-analytics','s-features-2','s-features-3','s-mockup-laptop','s-mockup-phone'],"

if old_assign in src:
    src = src.replace(old_assign, new_assign)
    changes += 1
    print("✅ 3. Updated autoAssignSlides")
else:
    print("⚠️ 3. autoAssignSlides anchor not found")

# ─── 4. Replace s-chat slide case ───
old_chat = """  case 's-chat': {
    const imgTag=mascotImgTag(sid,V);const hasImg=!!getMascotImageForSlide(sid);
    return `
    <div class="sl-bg" style="${bg}"></div>
    ${hasImg ? imgTag : ''}
    <div class="sl-safe sl-2col-40" style="${hasImg?'':''}">
      <div class="sl-vc">
        <div class="sl-tag" data-editable="true" style="${tagStyle}">${e(tx('chat_tag',L))}</div>
        <div class="sl-h2" data-editable="true" style="${h2Style}">${e(tx('chat_h',L).replace('{M}',MN))}</div>
        <div class="sl-body" data-editable="true" style="${bodyStyle}margin-bottom:28px;">${e(tx('chat_body',L))}</div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;">
          ${(tx('an_badges',L)||[]).slice(0,3).map(b=>`<span style="background:${alpha(V.TX,.08)};color:${V.TX2};border:1px solid ${alpha(V.TX,.2)};padding:5px 16px;border-radius:26px;font-size:17px;">${b}</span>`).join('')}
        </div>
      </div>
      <div class="sl-vc">
        <div style="background:${alpha(V.TX,.04)};border:1px solid ${alpha(V.TX,.1)};border-radius:22px;overflow:hidden;">
          <div style="padding:24px 28px;background:${alpha(V.TX,.04)};border-bottom:1px solid ${alpha(V.TX,.08)};display:flex;align-items:center;gap:16px;">
            <div style="width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,${c1},${c2});display:flex;align-items:center;justify-content:center;font-size:${S.chatSm}px;font-weight:700;color:#fff;">${MN.charAt(0)}</div>
            <div><div style="font-size:${S.chat}px;font-weight:500;color:${V.TX};">${e(MN)} · ${e(C)}</div><div style="font-size:${S.chatSm}px;color:#4CD8A8;display:flex;align-items:center;gap:6px;"><div style="width:7px;height:7px;border-radius:50%;background:#4CD8A8;"></div> ${tx('chat_online',L)||'Online'}</div></div>
          </div>
          <div style="padding:28px;display:flex;flex-direction:column;gap:14px;">
            <div style="display:flex;gap:12px;max-width:78%;"><div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,${c1},${c2});display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;flex-shrink:0;margin-top:3px;">${MN.charAt(0)}</div><div style="padding:14px 18px;border-radius:14px;background:${alpha(V.TX,.08)};color:${V.TX};font-size:${S.chat}px;line-height:1.5;border-bottom-left-radius:4px;">${e(cu1)}</div></div>
            <div style="display:flex;gap:12px;max-width:78%;align-self:flex-end;flex-direction:row-reverse;"><div style="width:34px;height:34px;border-radius:50%;background:${alpha(V.TX,.12)};display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:${V.TX};flex-shrink:0;margin-top:3px;">U</div><div style="padding:14px 18px;border-radius:14px;background:${c1};color:${STATE.colorTxt};font-size:${S.chat}px;line-height:1.5;border-bottom-right-radius:4px;">${e(cu2)}</div></div>
            <div style="display:flex;gap:12px;max-width:78%;"><div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,${c1},${c2});display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;flex-shrink:0;margin-top:3px;">${MN.charAt(0)}</div><div style="padding:14px 18px;border-radius:14px;background:${alpha(V.TX,.08)};color:${V.TX};font-size:${S.chat}px;line-height:1.5;border-bottom-left-radius:4px;">${e(ca1)}</div></div>
            ${cu3?`<div style="display:flex;gap:12px;max-width:78%;align-self:flex-end;flex-direction:row-reverse;"><div style="width:34px;height:34px;border-radius:50%;background:${alpha(V.TX,.12)};display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:${V.TX};flex-shrink:0;margin-top:3px;">U</div><div style="padding:14px 18px;border-radius:14px;background:${c1};color:${STATE.colorTxt};font-size:${S.chat}px;line-height:1.5;border-bottom-right-radius:4px;">${e(cu3)}</div></div>`:''}
            ${ca2?`<div style="display:flex;gap:12px;max-width:78%;"><div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,${c1},${c2});display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;flex-shrink:0;margin-top:3px;">${MN.charAt(0)}</div><div style="padding:14px 18px;border-radius:14px;background:${alpha(V.TX,.08)};color:${V.TX};font-size:${S.chat}px;line-height:1.5;border-bottom-left-radius:4px;">${e(ca2)}</div></div>`:''}
          </div>
        </div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">08</div>`;}"""

new_chat = r"""  case 's-chat': {
    const imgTag=mascotImgTag(sid,V);const hasImg=!!getMascotImageForSlide(sid);
    // Get mockup screen images
    const laptopImg=getMascotImageForSlide('s-mockup-laptop');
    const phoneImg=getMascotImageForSlide('s-mockup-phone');
    // Key highlights
    const highlights=[
      tx('chat_hl1',L)||{en:'24/7 Instant Response',nl:'24/7 Direct Antwoord',zh:'24/7 即時回覆'}[L]||'24/7 Instant Response',
      tx('chat_hl2',L)||{en:'Multi-channel Integration',nl:'Multi-channel Integratie',zh:'多渠道整合'}[L]||'Multi-channel Integration',
      tx('chat_hl3',L)||{en:'Smart Escalation',nl:'Slimme Escalatie',zh:'智慧轉接'}[L]||'Smart Escalation',
      tx('chat_hl4',L)||{en:'Analytics Dashboard',nl:'Analytics Dashboard',zh:'數據分析儀表板'}[L]||'Analytics Dashboard',
    ];
    return `
    <div class="sl-bg" style="${bg}"></div>
    ${hasImg ? imgTag : ''}
    <div class="sl-safe" style="display:grid;grid-template-columns:1.1fr 0.9fr;gap:60px;align-items:center;height:100%;">
      <!-- Left: Device mockups -->
      <div style="position:relative;display:flex;align-items:center;justify-content:center;padding:20px 0;">
        <div class="mockup-wrap">
          <!-- Laptop -->
          <div class="mockup-laptop">
            <div class="ml-screen">
              ${laptopImg
                ?`<img src="${laptopImg}" class="slide-img-editable" data-slide-id="s-mockup-laptop" alt="laptop-screen"/>`
                :`<div class="ml-placeholder">Upload laptop screenshot<br>in Image Manager → "Laptop Screen"</div>`}
            </div>
            <div class="ml-base"></div>
            <div class="ml-bottom"></div>
          </div>
          <!-- Phone -->
          <div class="mockup-phone">
            <div class="mp-frame">
              <div class="mp-notch"></div>
              <div class="mp-screen">
                ${phoneImg
                  ?`<img src="${phoneImg}" class="slide-img-editable" data-slide-id="s-mockup-phone" alt="phone-screen"/>`
                  :`<div class="mp-placeholder">Upload phone screenshot<br>→ "Phone Screen"</div>`}
              </div>
              <div class="mp-bar"></div>
            </div>
          </div>
        </div>
      </div>
      <!-- Right: Text content -->
      <div style="display:flex;flex-direction:column;gap:20px;">
        <div class="sl-tag" data-editable="true" style="${tagStyle}">${e(tx('chat_tag',L))}</div>
        <div data-editable="true" style="font-family:var(--fd);font-size:${S.h2}px;font-weight:800;color:${V.TX};line-height:1.1;letter-spacing:-.02em;">
          ${e(tx('chat_h',L).replace('{M}',MN))}
        </div>
        <div data-editable="true" style="font-size:${S.body}px;color:${V.TX2};line-height:1.6;max-width:420px;">
          ${e(tx('chat_body',L))}
        </div>
        <div style="display:flex;flex-direction:column;gap:12px;margin-top:8px;">
          ${highlights.map((h,i)=>`
          <div style="display:flex;align-items:center;gap:14px;">
            <div style="width:36px;height:36px;border-radius:10px;background:${alpha(c1,.12)};display:flex;align-items:center;justify-content:center;">
              <div style="width:8px;height:8px;border-radius:50%;background:${c1};"></div>
            </div>
            <span data-editable="true" style="font-size:${S.body}px;font-weight:600;color:${V.TX};font-family:var(--fd);">${e(h)}</span>
          </div>`).join('')}
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:8px;">
          ${(tx('an_badges',L)||[]).slice(0,3).map(b=>`<span style="background:${alpha(V.TX,.08)};color:${V.TX2};border:1px solid ${alpha(V.TX,.2)};padding:6px 18px;border-radius:26px;font-size:${S.bodySm}px;">${b}</span>`).join('')}
        </div>
      </div>
    </div>
    <div class="sl-num" style="${numStyle}">04</div>`;
  }"""

if old_chat in src:
    src = src.replace(old_chat, new_chat)
    changes += 1
    print("✅ 4. Replaced s-chat slide with device mockup layout")
else:
    print("⚠️ 4. s-chat case not found — trying to locate...")
    # Try to find and report what's different
    idx = src.find("case 's-chat':")
    if idx >= 0:
        snippet = src[idx:idx+200]
        print(f"   Found case at position {idx}:")
        print(f"   {snippet[:150]}...")
    else:
        print("   case 's-chat' not found anywhere!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

#!/usr/bin/env python3
"""
Patch: Lead Text system + Thank You page mascot fix
1. Add lead_text fields to genAll() JSON output — one per slide
2. Store lead texts in STATE
3. Update each slide's h3 to use AI lead text (fall back to static)
4. Fix thank you page: put book-a-call button ABOVE mascot
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ═══════════════════════════════════════
# 1. Add lead_text fields to genAll() JSON prompt
# ═══════════════════════════════════════
old_json_output = '''{
  "cover_headline": "MAX 15 WORDS. Formula: '{mascot} – {role}: {benefit}.' Example: 'Liza – The Digital AI Buddy: Your 24/7 Super FRESH Assistant.'",
  "cover_sub": "MAX 20 WORDS. What ${mascotName} does for ${clientName}.",

  "pain_intro": "MAX 30 WORDS total, 2 sentences. Example: 'Management and HR are overwhelmed by repetitive administrative employee questions. There is no modern digital touchpoint aligned with their brand vision.'",
  "pain_cards": [
    {"title": "MAX 5 WORDS. Example: 'Repetitive Admin Overload'", "text": "MAX 15 WORDS. One sentence. Example: 'Volunteer treasurers struggle to keep up with complex changing subsidy regulations.'"},
    {"title": "MAX 5 WORDS", "text": "MAX 15 WORDS"},
    {"title": "MAX 5 WORDS", "text": "MAX 15 WORDS"},
    {"title": "MAX 5 WORDS", "text": "MAX 15 WORDS"}
  ],

  "feature_body": "MAX 20 WORDS. ${mascotName}'s role at ${clientName}.",
  "feature_items": [
    "MAX 15 WORDS each. Formula: 'Capability Name: outcome.' Example: 'Automated Onboarding: Welcomes new hires, guides store selection, assists with ID submission.'",
    "MAX 15 WORDS",
    "MAX 15 WORDS",
    "MAX 15 WORDS",
    "MAX 15 WORDS"
  ],

  "chat_messages": [
    {"role": "mascot", "text": "MAX 15 WORDS. Warm greeting."},
    {"role": "user", "text": "MAX 15 WORDS. Real question from their daily work."},
    {"role": "mascot", "text": "MAX 25 WORDS. Empathy first, then specific answer with next action."},
    {"role": "user", "text": "MAX 10 WORDS. Follow-up."},
    {"role": "mascot", "text": "MAX 20 WORDS. Shows depth of knowledge."}
  ],

  "roi_headline": "MAX 10 WORDS. Example: 'What Changes When ${mascotName} Joins the Team'",
  "roi_metrics": [
    {"number": "-60% or 3x or 24/7", "label": "MAX 8 WORDS", "detail": "MAX 15 WORDS"},
    {"number": "metric", "label": "MAX 8 WORDS", "detail": "MAX 15 WORDS"},
    {"number": "metric", "label": "MAX 8 WORDS", "detail": "MAX 15 WORDS"}
  ],
  "roi_before": "MAX 3 bullet points, each MAX 12 WORDS",
  "roi_after": "MAX 3 bullet points, each MAX 12 WORDS",

  "ty_headline": "MAX 12 WORDS. Question that echoes the transformation.",
  "ty_body": "MAX 20 WORDS. Personal, warm closing.",
  "ty_cta": "MAX 8 WORDS. Example: 'Book a 30-min demo'"
}'''

new_json_output = '''{
  "lead_texts": {
    "pain": "MAX 2 SENTENCES. The slide's conclusion — reader gets the point WITHOUT seeing the data below. Must contain a specific number or finding. Example: '每年超過 84% 的學務人員面臨倦怠，重複性行政工作是首要原因。' or 'HR managers spend 12+ hours/week answering the same onboarding questions — that is 30% of their productive time.'",
    "market": "MAX 2 SENTENCES. Why this market matters NOW with a specific number. Example: 'AI 教育市場預計 2028 年達 $25.7B，年複合成長率 36%。但現有方案都缺少品牌人格化。' or 'The AI customer service market hits $12B by 2027 — yet no solution offers empathetic 3D brand agents.'",
    "features": "MAX 2 SENTENCES. What ${mascotName} specifically does for ${clientName}. Example: '${mascotName} replaces 4 disconnected tools with one empathetic brand agent — onboarding, FAQ, scheduling, and emotional check-ins in a single interface.'",
    "chat": "MAX 2 SENTENCES. What this demo shows. Example: 'Real conversation: a new hire asks about shift scheduling at 11pm. ${mascotName} responds with empathy and the exact store-specific answer.'",
    "roi": "MAX 2 SENTENCES. The bottom-line impact with numbers. Example: 'Similar implementations reduced HR workload by 70% and cut onboarding time from 3 days to 4 hours.' Use research data if available.",
    "pricing": "MAX 2 SENTENCES. Value framing. Example: 'Starting at EUR 399/month — less than 10% of one FTE. 12-month commitment, live in 4 weeks.'",
    "thankyou": "MAX 2 SENTENCES. Warm, forward-looking close. Example: 'Imagine ${clientName} where every new employee feels welcomed from day one — ${mascotName} makes that real.'"
  },

  "cover_headline": "MAX 15 WORDS. Formula: '{mascot} – {role}: {benefit}.' Example: 'Liza – The Digital AI Buddy: Your 24/7 Super FRESH Assistant.'",
  "cover_sub": "MAX 20 WORDS. What ${mascotName} does for ${clientName}.",

  "pain_intro": "MAX 30 WORDS total, 2 sentences. Summarize the core pain in the client's own industry language.",
  "pain_cards": [
    {"title": "MAX 5 WORDS. Example: 'Repetitive Admin Overload'", "text": "MAX 15 WORDS. One sentence. Example: 'Volunteer treasurers struggle to keep up with complex changing subsidy regulations.'"},
    {"title": "MAX 5 WORDS", "text": "MAX 15 WORDS"},
    {"title": "MAX 5 WORDS", "text": "MAX 15 WORDS"},
    {"title": "MAX 5 WORDS", "text": "MAX 15 WORDS"}
  ],

  "feature_body": "MAX 20 WORDS. ${mascotName}'s role at ${clientName}.",
  "feature_items": [
    "MAX 15 WORDS each. Formula: 'Capability Name: outcome.' Example: 'Automated Onboarding: Welcomes new hires, guides store selection, assists with ID submission.'",
    "MAX 15 WORDS",
    "MAX 15 WORDS",
    "MAX 15 WORDS",
    "MAX 15 WORDS"
  ],

  "chat_messages": [
    {"role": "mascot", "text": "MAX 15 WORDS. Warm greeting."},
    {"role": "user", "text": "MAX 15 WORDS. Real question from their daily work."},
    {"role": "mascot", "text": "MAX 25 WORDS. Empathy first, then specific answer with next action."},
    {"role": "user", "text": "MAX 10 WORDS. Follow-up."},
    {"role": "mascot", "text": "MAX 20 WORDS. Shows depth of knowledge."}
  ],

  "roi_headline": "MAX 10 WORDS. Example: 'What Changes When ${mascotName} Joins the Team'",
  "roi_metrics": [
    {"number": "-60% or 3x or 24/7", "label": "MAX 8 WORDS", "detail": "MAX 15 WORDS"},
    {"number": "metric", "label": "MAX 8 WORDS", "detail": "MAX 15 WORDS"},
    {"number": "metric", "label": "MAX 8 WORDS", "detail": "MAX 15 WORDS"}
  ],
  "roi_before": "MAX 3 bullet points, each MAX 12 WORDS",
  "roi_after": "MAX 3 bullet points, each MAX 12 WORDS",

  "ty_headline": "MAX 12 WORDS. Question that echoes the transformation.",
  "ty_body": "MAX 20 WORDS. Personal, warm closing.",
  "ty_cta": "MAX 8 WORDS. Example: 'Book a 30-min demo'"
}'''

if old_json_output in html:
    html = html.replace(old_json_output, new_json_output)
    changes += 1
    print("✅ 1. Added lead_texts to genAll() JSON prompt")
else:
    print("❌ 1. JSON output pattern not found")

# ═══════════════════════════════════════
# 2. Store lead_texts in STATE after parsing
# ═══════════════════════════════════════
old_state_apply = """    STATE.aiPain=d.pain_intro||'';
    STATE.aiPainCards=d.pain_cards||null;
    STATE.aiFeatureBody=d.feature_body||'';
    STATE.aiFeatureItems=d.feature_items||null;
    STATE.aiCoverH=d.cover_headline||'';
    STATE.aiCoverSub=d.cover_sub||'';
    STATE.aiTyBody=d.ty_body||'';
    STATE.aiTyHeadline=d.ty_headline||'';
    STATE.aiTyCta=d.ty_cta||'';"""

new_state_apply = """    STATE.aiPain=d.pain_intro||'';
    STATE.aiPainCards=d.pain_cards||null;
    STATE.aiFeatureBody=d.feature_body||'';
    STATE.aiFeatureItems=d.feature_items||null;
    STATE.aiCoverH=d.cover_headline||'';
    STATE.aiCoverSub=d.cover_sub||'';
    STATE.aiTyBody=d.ty_body||'';
    STATE.aiTyHeadline=d.ty_headline||'';
    STATE.aiTyCta=d.ty_cta||'';
    // Lead texts — conclusion sentences for each slide
    STATE.aiLeadTexts=d.lead_texts||{};"""

if old_state_apply in html:
    html = html.replace(old_state_apply, new_state_apply)
    changes += 1
    print("✅ 2. STATE.aiLeadTexts stored after AI response")
else:
    print("❌ 2. STATE apply pattern not found")

# ═══════════════════════════════════════
# 3. Update s-pain slide h3 to use lead text
# ═══════════════════════════════════════
old_pain_h3 = '''<div class="sl-h3" style="${h3Style}">${e(tx('pain_h',L))} <span style="font-style:italic;">${e(C)}</span>.</div>
          <div class="sl-body" data-editable="true" style="${bodyStyle}margin-bottom:28px;">${e(PAIN)}</div>'''

new_pain_h3 = '''<div class="sl-h3" data-editable="true" style="${h3Style}">${e(STATE.aiLeadTexts?.pain || (tx('pain_h',L)+' '+C+'.'))}</div>'''

if old_pain_h3 in html:
    html = html.replace(old_pain_h3, new_pain_h3)
    changes += 1
    print("✅ 3. s-pain: h3 now uses lead text (replaces static title + pain_intro)")
else:
    print("❌ 3. s-pain h3 pattern not found")

# ═══════════════════════════════════════
# 4. Update s-market slide h3 to use lead text
# ═══════════════════════════════════════
old_market_h3 = """<div class="sl-h3" style="${h3Style}">${e({en:'Why Now. Why This Market.',nl:'Waarom nu. Waarom deze markt.',zh:'為什麼是現在。為什麼是這個市場。',ja:'なぜ今。なぜこの市場。',de:'Warum jetzt. Warum dieser Markt.',fr:'Pourquoi maintenant.',es:'Por qué ahora.'}[L]||'Why Now. Why This Market.')}</div>"""

new_market_h3 = """<div class="sl-h3" data-editable="true" style="${h3Style}">${e(STATE.aiLeadTexts?.market || {en:'Why Now. Why This Market.',nl:'Waarom nu. Waarom deze markt.',zh:'為什麼是現在。為什麼是這個市場。',ja:'なぜ今。なぜこの市場。',de:'Warum jetzt. Warum dieser Markt.',fr:'Pourquoi maintenant.',es:'Por qué ahora.'}[L] || 'Why Now. Why This Market.')}</div>"""

if old_market_h3 in html:
    html = html.replace(old_market_h3, new_market_h3)
    changes += 1
    print("✅ 4. s-market: h3 now uses lead text")
else:
    print("❌ 4. s-market h3 pattern not found")

# ═══════════════════════════════════════
# 5. Update s-roi slide h3 to use lead text
# ═══════════════════════════════════════
old_roi_h3 = """<div class="sl-h3" style="${h3Style}">${e({en:'Real Numbers. Real Impact.',nl:'Echte cijfers. Echte impact.',zh:'真實數據。真實影響。',ja:'リアルな数字。リアルなインパクト。',de:'Echte Zahlen. Echte Wirkung.',fr:'Vrais chiffres. Vrai impact.',es:'Números reales. Impacto real.'}[L]||'Real Numbers. Real Impact.')}</div>"""

new_roi_h3 = """<div class="sl-h3" data-editable="true" style="${h3Style}">${e(STATE.aiLeadTexts?.roi || {en:'Real Numbers. Real Impact.',nl:'Echte cijfers. Echte impact.',zh:'真實數據。真實影響。',ja:'リアルな数字。リアルなインパクト。',de:'Echte Zahlen. Echte Wirkung.',fr:'Vrais chiffres. Vrai impact.',es:'Números reales. Impacto real.'}[L] || 'Real Numbers. Real Impact.')}</div>"""

if old_roi_h3 in html:
    html = html.replace(old_roi_h3, new_roi_h3)
    changes += 1
    print("✅ 5. s-roi: h3 now uses lead text")
else:
    print("❌ 5. s-roi h3 pattern not found")

# ═══════════════════════════════════════
# 6. Update s-features slide — add lead text above feature grid
# ═══════════════════════════════════════
old_feat_h = """<div style="font-family:var(--fd);font-size:${S.h2}px;font-weight:800;color:#fff;line-height:1;" data-editable="true">${e(tx('feat_h',L))}</div>"""

new_feat_h = """<div style="font-family:var(--fd);font-size:${S.h2}px;font-weight:800;color:#fff;line-height:1;" data-editable="true">${e(STATE.aiLeadTexts?.features || tx('feat_h',L))}</div>"""

if old_feat_h in html:
    html = html.replace(old_feat_h, new_feat_h)
    changes += 1
    print("✅ 6. s-features: h2 now uses lead text")
else:
    print("❌ 6. s-features h2 pattern not found")

# ═══════════════════════════════════════
# 7. Update s-chat slide — look for chat title
# ═══════════════════════════════════════
# Find the chat slide title
import re
chat_h_pattern = r"case 's-chat'.*?sl-h3.*?\$\{e\(tx\('chat_h',L\)\)\}"
match = re.search(chat_h_pattern, html, re.DOTALL)
if match:
    old_chat_h = "${e(tx('chat_h',L))}"
    # We need to be more targeted — replace only within s-chat context
    # Let's find the specific line
    pass

# Instead find the chat_h reference more precisely
old_chat_title = ">${e(tx('chat_h',L))}</div>"
# This might appear in multiple places, let's count
count = html.count(old_chat_title)
if count > 0:
    # Replace only within template literal context
    new_chat_title = ">${e(STATE.aiLeadTexts?.chat || tx('chat_h',L))}</div>"
    html = html.replace(old_chat_title, new_chat_title)
    changes += 1
    print(f"✅ 7. s-chat: h3 now uses lead text ({count} occurrences)")
else:
    print("❌ 7. s-chat h3 pattern not found")

# ═══════════════════════════════════════
# 8. Update s-pricing slide
# ═══════════════════════════════════════
old_pricing_h = ">${e(tx('pr_h',L))}</div>"
count_pr = html.count(old_pricing_h)
if count_pr > 0:
    new_pricing_h = ">${e(STATE.aiLeadTexts?.pricing || tx('pr_h',L))}</div>"
    html = html.replace(old_pricing_h, new_pricing_h)
    changes += 1
    print(f"✅ 8. s-pricing: h3 now uses lead text ({count_pr} occurrences)")
else:
    print("❌ 8. s-pricing h3 pattern not found")

# ═══════════════════════════════════════
# 9. Update s-thankyou — use lead text for headline
# ═══════════════════════════════════════
old_ty_headline = """<div style="font-family:var(--fd);font-size:${S.h1}px;font-weight:800;line-height:.92;letter-spacing:-.04em;color:${V.TX};margin-bottom:16px;" data-editable="true">${e(ctLbl[L]||ctLbl.en)}<br/><span style="color:${c1};">${e(closingTarget[L]||closingTarget.en)}</span></div>
        <div style="font-size:${S.body}px;color:${V.TX2};line-height:1.5;margin-bottom:20px;font-style:italic;" data-editable="true">${e((mascotCTA[L]||mascotCTA.en).charAt(0).toUpperCase()+(mascotCTA[L]||mascotCTA.en).slice(1))}! 🚀</div>"""

new_ty_headline = """<div style="font-family:var(--fd);font-size:${STATE.aiLeadTexts?.thankyou ? S.h2 : S.h1}px;font-weight:800;line-height:${STATE.aiLeadTexts?.thankyou ? '1.15' : '.92'};letter-spacing:-.04em;color:${V.TX};margin-bottom:16px;" data-editable="true">${STATE.aiLeadTexts?.thankyou ? e(STATE.aiLeadTexts.thankyou) : (e(ctLbl[L]||ctLbl.en)+'<br/><span style="color:'+c1+';">'+e(closingTarget[L]||closingTarget.en)+'</span>')}</div>"""

if old_ty_headline in html:
    html = html.replace(old_ty_headline, new_ty_headline)
    changes += 1
    print("✅ 9. s-thankyou: headline now uses lead text")
else:
    print("❌ 9. s-thankyou headline pattern not found")

# ═══════════════════════════════════════
# 10. Fix thank you page — move book-a-call button above mascot
# ═══════════════════════════════════════
old_ty_right = """      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;">
        ${hasImg ? imgTag :
          '<div style="font-size:380px;line-height:1;filter:drop-shadow(0 30px 60px rgba(0,0,0,.3));">'+bigEmoji3+'</div>'}
        <div style="margin-top:16px;background:${c1};color:${STATE.colorTxt||'#fff'};font-family:var(--fd);font-size:${S.body}px;font-weight:700;padding:14px 36px;border-radius:40px;letter-spacing:.06em;text-transform:uppercase;">${tx("ty_book_call",L)} →</div>
      </div>"""

new_ty_right = """      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;">
        <div style="position:relative;z-index:2;margin-bottom:24px;background:${c1};color:${STATE.colorTxt||'#fff'};font-family:var(--fd);font-size:${S.body}px;font-weight:700;padding:16px 42px;border-radius:40px;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 8px 32px ${alpha(c1,.35)};">${e(STATE.aiTyCta || tx("ty_book_call",L))} →</div>
        ${hasImg ? '<div style="position:relative;z-index:1;">'+imgTag+'</div>' :
          '<div style="font-size:320px;line-height:1;filter:drop-shadow(0 30px 60px rgba(0,0,0,.3));">'+bigEmoji3+'</div>'}
      </div>"""

if old_ty_right in html:
    html = html.replace(old_ty_right, new_ty_right)
    changes += 1
    print("✅ 10. s-thankyou: book-a-call button moved above mascot with z-index fix")
else:
    print("❌ 10. s-thankyou right column pattern not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Patch applied: {changes} changes")
print("""
Summary:
  Lead Text system:
  - genAll() now outputs lead_texts.{pain,market,features,chat,roi,pricing,thankyou}
  - Each lead text is a 1-2 sentence CONCLUSION (not a label)
  - Must contain specific data/numbers — reader understands the point without looking at charts
  - Falls back to original static titles if AI doesn't provide lead text

  Thank You page fix:
  - Book-a-call button moved ABOVE mascot image
  - Button has z-index:2, mascot has z-index:1
  - Button uses AI-generated CTA text when available
""")

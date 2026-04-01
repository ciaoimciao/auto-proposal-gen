#!/usr/bin/env python3
"""
Patch 20: Core 8-page deck system overhaul
1. Add new input fields (Use Case, quantitative data, conversation scenario)
2. Update getCtx() to include new fields
3. Rewrite AI prompt for 8-page focused generation with web search
4. Update genAll() to produce ROI data + better content
"""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ═══════════════════════════════════════
# 1. ADD NEW INPUT FIELDS — Use Case dropdown + quantitative data
# ═══════════════════════════════════════

# Insert Use Case dropdown after Industry field
old_industry = '''<div class="fg"><label class="fl">Industry &amp; Department</label><input class="fi" id="in-industry" placeholder="e.g. Retail — HR &amp; Onboarding"/></div>
      </div>
      <div class="fr">
        <div class="fg"><label class="fl">Decision-maker Name &amp; Role</label><input class="fi" id="in-role" placeholder="e.g. Bas Bobeldijk — Store Manager"/></div>'''

new_industry = '''<div class="fg"><label class="fl">Industry &amp; Department</label><input class="fi" id="in-industry" placeholder="e.g. Retail — HR &amp; Onboarding"/></div>
      </div>
      <div class="fr">
        <div class="fg">
          <label class="fl">Use Case <span style="color:#0a0a0a;font-weight:700;">What will the AI agent do?</span></label>
          <select class="fi" id="in-usecase" style="appearance:auto;cursor:pointer;">
            <option value="">— Select use case —</option>
            <option value="student-services">🎓 Student Services (enrollment, FAQ, campus life)</option>
            <option value="employee-onboarding">👔 Employee Onboarding &amp; Training</option>
            <option value="customer-service">🎧 Customer Service &amp; Support</option>
            <option value="internal-kb">📚 Internal Knowledge Base</option>
            <option value="sales-assistant">🛒 Sales &amp; Product Assistant</option>
            <option value="patient-support">🏥 Patient / Healthcare Support</option>
            <option value="other">✏️ Other (describe in pain points)</option>
          </select>
        </div>
        <div class="fg"><label class="fl">Decision-maker Name &amp; Role</label><input class="fi" id="in-role" placeholder="e.g. Bas Bobeldijk — Store Manager"/></div>'''

if old_industry in src:
    src = src.replace(old_industry, new_industry)
    changes += 1
    print("✅ 1. Added Use Case dropdown")
else:
    print("⚠️ 1. Industry field block not found")

# Add quantitative data fields after the "Extra context" box opener
old_extra = '''<div class="ctx-lbl">&#128188; Extra context (optional but makes the deck sharper)</div>
        <div class="fr">
          <div class="fg" style="margin-bottom:.5rem;">
            <label class="fl">End users / target audience</label>
            <input class="fi" id="in-audience" placeholder="e.g. Nieuwe medewerkers, 16-25 jaar, winkelvloer"/>
          </div>
          <div class="fg" style="margin-bottom:.5rem;">
            <label class="fl">Scale / size</label>
            <input class="fi" id="in-scale" placeholder="e.g. 700+ filialen, 100.000 medewerkers NL"/>
          </div>
        </div>'''

new_extra = '''<div class="ctx-lbl">&#128188; Extra context (optional but makes the deck sharper)</div>
        <div class="fr">
          <div class="fg" style="margin-bottom:.5rem;">
            <label class="fl">End users / target audience</label>
            <input class="fi" id="in-audience" placeholder="e.g. Nieuwe medewerkers, 16-25 jaar, winkelvloer"/>
          </div>
          <div class="fg" style="margin-bottom:.5rem;">
            <label class="fl">Scale / size</label>
            <input class="fi" id="in-scale" placeholder="e.g. 700+ filialen, 100.000 medewerkers NL"/>
          </div>
        </div>
        <div class="fr">
          <div class="fg" style="margin-bottom:.5rem;">
            <label class="fl">Monthly inquiry volume <span style="color:#737373;font-weight:400;">(approx.)</span></label>
            <input class="fi" id="in-volume" type="text" placeholder="e.g. 3,000 calls/month, 500 emails/week"/>
          </div>
          <div class="fg" style="margin-bottom:.5rem;">
            <label class="fl">Support team size</label>
            <input class="fi" id="in-teamsize" type="text" placeholder="e.g. 5 staff handling inquiries"/>
          </div>
        </div>
        <div class="fg" style="margin-bottom:.5rem;">
          <label class="fl">Chat scenario hint <span style="color:#737373;font-weight:400;">(for Chat Mock-up slide)</span></label>
          <input class="fi" id="in-chatscene" placeholder="e.g. Student asking about credit transfer process / New hire asking about shift schedule"/>
        </div>'''

if old_extra in src:
    src = src.replace(old_extra, new_extra)
    changes += 1
    print("✅ 2. Added quantitative data + chat scenario fields")
else:
    print("⚠️ 2. Extra context block not found")


# ═══════════════════════════════════════
# 2. UPDATE getCtx() to include new fields
# ═══════════════════════════════════════

old_getctx = '''function getCtx(){
  return{
    c:document.getElementById('in-client').value.trim()||'the client',
    ind:document.getElementById('in-industry').value.trim()||'their industry',
    pain:document.getElementById('in-pain').value.trim()||'repetitive queries',
    role:document.getElementById('in-role').value.trim()||'decision-maker',
    tools:document.getElementById('in-tools').value.trim()||'standard FAQ page',
    url:document.getElementById('in-url').value.trim()||'',
    audience:document.getElementById('in-audience')?.value.trim()||'',
    scale:document.getElementById('in-scale')?.value.trim()||'',
    anecdote:document.getElementById('in-anecdote')?.value.trim()||'',
    goal:document.getElementById('in-goal')?.value.trim()||'',
  };
}'''

new_getctx = '''function getCtx(){
  return{
    c:document.getElementById('in-client').value.trim()||'the client',
    ind:document.getElementById('in-industry').value.trim()||'their industry',
    usecase:document.getElementById('in-usecase')?.value||'',
    pain:document.getElementById('in-pain').value.trim()||'repetitive queries',
    role:document.getElementById('in-role').value.trim()||'decision-maker',
    tools:document.getElementById('in-tools').value.trim()||'standard FAQ page',
    url:document.getElementById('in-url').value.trim()||'',
    audience:document.getElementById('in-audience')?.value.trim()||'',
    scale:document.getElementById('in-scale')?.value.trim()||'',
    volume:document.getElementById('in-volume')?.value.trim()||'',
    teamsize:document.getElementById('in-teamsize')?.value.trim()||'',
    chatscene:document.getElementById('in-chatscene')?.value.trim()||'',
    anecdote:document.getElementById('in-anecdote')?.value.trim()||'',
    goal:document.getElementById('in-goal')?.value.trim()||'',
  };
}'''

if old_getctx in src:
    src = src.replace(old_getctx, new_getctx)
    changes += 1
    print("✅ 3. Updated getCtx() with new fields")
else:
    print("⚠️ 3. getCtx() not found")


# ═══════════════════════════════════════
# 3. REWRITE genAll() — new AI prompt for 8-page system
# ═══════════════════════════════════════

old_genall_start = '''  const prompt=`You are a senior B2B marketing strategist and conversion copywriter for Notso.ai — a company that builds empathetic 3D animated AI brand agents. Your copy wins deals.

MISSION: Write proposal slide content so specific, so resonant, that the client thinks "they really understand our world." Generic copy loses. Specificity wins.

ABOUT NOTSO.AI:
Notso.ai creates Visual Agents — 3D animated AI brand mascots with personality, empathy, and visual identity. Not chatbots. We are "The Experience Layer of AI" — we sit on top of existing AI stacks (Salesforce, Zendesk) and make them delightful.

KEY DIFFERENTIATORS (use in feature descriptions):
- Empathy Engine: real-time emotion detection triggers specific animations (happy, confused, apologetic)
- Agentic RAG: trained on client's own docs (PDFs, FAQs), zero hallucination, brand-safe
- 3D Animation Engine: proprietary, lightweight, fast-loading animated characters
- We are NOT photorealistic avatars. We are stylized, brandable, expressive characters.

PROVEN RESULTS (reference when relevant):
- Jumbo (retail): 70% reduction in HR workload after deploying mascot Liza
- Brand mascots increase consumer trust by 35%
- Mascot campaigns boost online engagement metrics by up to 40%
- Mascots are recognized 7x more than logos or human agents

COMPETITIVE EDGE (use to frame features):
- vs Traditional chatbots: powerful but lack brand personality, feel cold
- vs Design agencies: great mascots but no AI brain for real-time conversation
- Notso.ai = AI automation efficiency + brand character emotional appeal

OBJECTION PREEMPTION (weave into copy subtly):
- Traditional custom 3D interactive dev costs €350,000+. Our Premium annual = ~€7,550.
- We don't replace existing systems — we upgrade them as an Experience Layer.

VOICE RULES:
- Speak like a smart colleague, not a vendor
- Use the client's OWN words wherever they are given
- Short, punchy sentences. Zero jargon. Zero filler.
- Pain must be felt — visceral, specific, real situations
- Headlines are bold claims or provocations, never descriptions
- NEVER say "chatbot" — say "Brand Agent" or "Visual Agent"
- Conversations, not interrogations. Built for delight, not realism.

TONE EXAMPLES (this is the bar):
Cover: "Jumbo's New Hire Calls End Today." (not "AI chatbot solution for retail")
Pain intro: "Every week, 3 new hires call the team leader for the same password reset. Meanwhile, the manager is stuck on a checkout — again."
Feature: "Answers shift questions before they're asked." (not "automated FAQ responses")

CLIENT PROFILE:
Company: ${clientName}
Website: ${c.url||'N/A'}
Industry: ${c.ind}
Decision-maker: ${c.role}
Their pain (use these exact words): ${c.pain}
Tools being replaced: ${c.tools}
End users: ${c.audience}
Scale: ${c.scale}
Real story they told: ${c.anecdote}
What success looks like: ${c.goal}
${webResearch}

OUTPUT LANGUAGE: ${langInstr}

Return ONLY a valid JSON object. No markdown. No explanation. No emoji in field values. Every field must be client-specific — never generic:
{
  "cover_headline": "6-8 word bold claim specific to ${clientName}. Examples: 'Jumbo\\'s New Hire Calls End Today.' or 'Every Conversation, An Experience.' — make it feel like a movie tagline",
  "cover_sub": "one precise sentence: what ${mascotName} does and for whom, mentioning the core pain",
  "pain_intro": "2 punchy sentences from their lived reality — use their exact words if given. Make the reader nod.",
  "pain_cards": [
    {"title": "3-4 word tension title", "text": "one vivid, specific sentence about this pain in their world"},
    {"title": "3-4 word tension title", "text": "one vivid, specific sentence"},
    {"title": "3-4 word tension title", "text": "one vivid, specific sentence"},
    {"title": "3-4 word tension title", "text": "one vivid, specific sentence"}
  ],
  "feature_body": "one sentence: how ${mascotName} directly solves ${clientName}'s core pain — be specific",
  "feature_items": [
    "concrete outcome for ${clientName}. Reference Empathy Engine, Knowledge Base, or Analytics when relevant. Frame as what changes for the user, not what the tech does.",
    "concrete feature",
    "concrete feature",
    "concrete feature",
    "concrete feature"
  ],
  "chat_mascot1": "warm, specific greeting from ${mascotName} that shows it knows ${clientName}'s world",
  "chat_user1": "user asking something they actually would ask — specific to their daily pain",
  "chat_mascot2": "empathetic, helpful response that solves the immediate question and hints at the bigger solution — max 20 words",
  "ty_body": "personal, warm, specific closing line — thank ${clientName} by name, reference the change ${mascotName} will bring"
}`;'''

new_genall_start = '''  // Build use case context string
  const useCaseMap={
    'student-services':'Student Services — AI agent answers enrollment, course selection, campus life, admin procedure questions for students',
    'employee-onboarding':'Employee Onboarding & Training — AI agent guides new hires through SOPs, policies, scheduling, and company knowledge',
    'customer-service':'Customer Service & Support — AI agent handles customer inquiries, complaints, product questions, and ticket routing',
    'internal-kb':'Internal Knowledge Base — AI agent helps employees find internal documents, policies, and procedures',
    'sales-assistant':'Sales & Product Assistant — AI agent helps customers browse products, compare options, and make purchase decisions',
    'patient-support':'Patient / Healthcare Support — AI agent answers patient questions about appointments, procedures, medications, and hospital services',
    'other':'Custom use case — see pain points for details',
  };
  const useCaseDesc=useCaseMap[c.usecase]||'General AI brand agent';

  const prompt=`You are a senior B2B pitch strategist for Notso.ai. You write cold proposals that make clients want to take a meeting. Your secret: you research the client so well they think you already had a conversation.

CRITICAL RULE: This is a COLD PITCH — we have NOT spoken to the client yet. Everything must be based on:
1. The input data the sales rep provides (below)
2. Website research findings (below, if available)
3. Industry knowledge and reasonable inference
NEVER fabricate quotes from the client. Instead, describe situations they likely face based on research.
NEVER invent specific numbers unless backed by research or industry data. When using industry averages, label them as such.

ABOUT NOTSO.AI:
Notso.ai creates Visual Agents — 3D animated AI brand mascots with personality, empathy, and visual identity. We are "The Experience Layer of AI" — we sit on top of existing AI stacks and make them delightful.
Key tech: Empathy Engine (emotion detection), Agentic RAG (trained on client docs, zero hallucination), 3D Animation Engine (lightweight, fast-loading).

VOICE RULES:
- Write like a smart colleague presenting insights, not a salesperson
- Short, punchy sentences. Zero jargon. Zero filler.
- Pain must feel real — specific situations, not abstract problems
- Headlines are bold claims or provocations, never descriptions
- NEVER say "chatbot" — say "Brand Agent" or "Visual Agent"
- Use the client's industry language — not tech jargon

CLIENT PROFILE:
Company: \${clientName}
Website: \${c.url||'N/A'}
Industry: \${c.ind}
Use Case: \${useCaseDesc}
Decision-maker: \${c.role}
Pain points provided: \${c.pain}
Tools being replaced: \${c.tools}
End users: \${c.audience}
Scale: \${c.scale}
Monthly inquiry volume: \${c.volume||'not provided — estimate from industry averages'}
Support team size: \${c.teamsize||'not provided — estimate from scale'}
Chat scenario hint: \${c.chatscene||'generate based on use case'}
Real story/anecdote: \${c.anecdote}
Success definition: \${c.goal}
\${webResearch}

OUTPUT LANGUAGE: \${langInstr}
If the language is Chinese/Japanese, adapt ALL content including data labels and descriptions. Do NOT mix English into Chinese/Japanese output.

Return ONLY a valid JSON object. No markdown. No explanation. No emoji in field values.

IMPORTANT: Every field must reference \${clientName} specifically. If the sales rep left fields blank, use website research + industry knowledge to fill gaps — but be honest about it (say "based on industry data" not fake quotes).

{
  "cover_headline": "6-10 word bold statement specific to \${clientName}. If you found their actual scale from research (e.g. number of students/employees/locations), USE that real number. If not, use a scenario-based headline without numbers. Examples: 'CMU's 7,300 Students Deserve Answers at Midnight' or 'Every Unanswered Question Costs More Than You Think'",
  "cover_sub": "one precise sentence positioning \${mascotName} for \${clientName}'s specific situation",

  "pain_intro": "2-3 sentences describing the situation \${clientName} likely faces. Use industry-specific details from research. Do NOT fake direct quotes — instead write observational statements like 'During peak enrollment, administrative staff at universities like \${clientName} typically handle...'",
  "pain_cards": [
    {"title": "3-5 word tension title", "text": "One specific, vivid sentence about this pain. Reference real systems/processes/tools the client uses if found in website research. Include a data point if available (industry average is fine, label it)."},
    {"title": "tension title", "text": "specific pain sentence with data if possible"},
    {"title": "tension title", "text": "specific pain sentence with data if possible"},
    {"title": "tension title", "text": "specific pain sentence with data if possible"}
  ],

  "feature_body": "one sentence: how \${mascotName} specifically solves \${clientName}'s core use case (\${useCaseDesc})",
  "feature_items": [
    "4-5 features, each written as a concrete outcome for \${clientName}. Customize to the use case: student-services → course FAQ, enrollment help, multilingual; employee-onboarding → SOP training, progress tracking; customer-service → ticket deflection, 24/7 response; etc. Frame as what changes for the END USER, not what the tech does.",
    "second feature outcome",
    "third feature outcome",
    "fourth feature outcome",
    "fifth feature outcome"
  ],

  "chat_messages": [
    {"role": "mascot", "text": "warm, contextual greeting from \${mascotName} — short, shows it understands the user's world (max 15 words)"},
    {"role": "user", "text": "user asks something they would ACTUALLY ask — use real scenarios from the client's context (e.g. actual course names, actual departments, actual processes found on their website)"},
    {"role": "mascot", "text": "helpful, specific response that SOLVES the question with real info if available from web research. Include a concrete action (link, form, next step). Max 40 words."},
    {"role": "user", "text": "natural follow-up question"},
    {"role": "mascot", "text": "empathetic follow-up that demonstrates depth of knowledge. Max 30 words."}
  ],

  "roi_headline": "bold ROI statement for \${clientName} — e.g. 'What Changes When \${mascotName} Joins the Team'",
  "roi_metrics": [
    {"number": "a percentage or multiplier (e.g. -70%, 3x, 24/7)", "label": "what this metric means for \${clientName} (e.g. 'reduction in admin calls')", "detail": "one sentence explanation with industry data source if applicable"},
    {"number": "metric", "label": "label", "detail": "explanation"},
    {"number": "metric", "label": "label", "detail": "explanation"}
  ],
  "roi_before": "2-3 bullet points describing the CURRENT situation (Before) — specific to \${clientName}",
  "roi_after": "2-3 bullet points describing the FUTURE with \${mascotName} (After) — specific and measurable",

  "ty_headline": "closing statement that creates urgency without being pushy — reference timing, upcoming semester/season, or business cycle relevant to \${clientName}",
  "ty_body": "personal, specific closing — reference the concrete change \${mascotName} will bring to \${clientName}. Include a clear CTA.",
  "ty_cta": "specific next step (e.g. 'Schedule a 30-min demo' or 'See \${mascotName} in action')"
}`;'''

if old_genall_start in src:
    src = src.replace(old_genall_start, new_genall_start)
    changes += 1
    print("✅ 4. Rewrote AI prompt for 8-page system")
else:
    print("⚠️ 4. AI prompt not found — trying to locate...")
    # debug: check if the start exists
    if "MISSION: Write proposal slide content" in src:
        print("   Found MISSION but full match failed — check whitespace")
    else:
        print("   MISSION text not found at all")


# ═══════════════════════════════════════
# 4. UPDATE STATE ASSIGNMENT after AI response
# ═══════════════════════════════════════

old_state_assign = '''    if(d.pain_intro)document.getElementById('in-pain').value=d.pain_intro;
    STATE.aiPain=d.pain_intro||'';
    STATE.aiPainCards=d.pain_cards||null;
    STATE.aiFeatureBody=d.feature_body||'';
    STATE.aiFeatureItems=d.feature_items||null;
    STATE.aiCoverH=d.cover_headline||'';
    STATE.aiCoverSub=d.cover_sub||'';
    STATE.aiTyBody=d.ty_body||'';
    STATE.aiChat='MASCOT: '+(d.chat_mascot1||'')+'\nUSER: '+(d.chat_user1||'')+'\nMASCOT: '+(d.chat_mascot2||'');
    st.textContent='Done! Click Generate Deck to apply.';'''

new_state_assign = '''    if(d.pain_intro)document.getElementById('in-pain').value=d.pain_intro;
    STATE.aiPain=d.pain_intro||'';
    STATE.aiPainCards=d.pain_cards||null;
    STATE.aiFeatureBody=d.feature_body||'';
    STATE.aiFeatureItems=d.feature_items||null;
    STATE.aiCoverH=d.cover_headline||'';
    STATE.aiCoverSub=d.cover_sub||'';
    STATE.aiTyBody=d.ty_body||'';
    STATE.aiTyHeadline=d.ty_headline||'';
    STATE.aiTyCta=d.ty_cta||'';
    // Chat: support new multi-message format
    if(d.chat_messages&&Array.isArray(d.chat_messages)){
      STATE.aiChat=d.chat_messages.map(m=>(m.role==='mascot'?'MASCOT':'USER')+': '+m.text).join('\\n');
      STATE.aiChatMessages=d.chat_messages;
    }else{
      STATE.aiChat='MASCOT: '+(d.chat_mascot1||'')+'\\nUSER: '+(d.chat_user1||'')+'\\nMASCOT: '+(d.chat_mascot2||'');
      STATE.aiChatMessages=null;
    }
    // ROI data
    STATE.aiRoiHeadline=d.roi_headline||'';
    STATE.aiRoiMetrics=d.roi_metrics||null;
    STATE.aiRoiBefore=d.roi_before||'';
    STATE.aiRoiAfter=d.roi_after||'';
    st.textContent='Done! Click Generate Deck to apply.';'''

if old_state_assign in src:
    src = src.replace(old_state_assign, new_state_assign)
    changes += 1
    print("✅ 5. Updated STATE assignment for new AI fields")
else:
    print("⚠️ 5. STATE assignment block not found")


# ═══════════════════════════════════════
# 5. UPDATE Analytics slide (s-analytics) to use ROI data
# ═══════════════════════════════════════

# Replace the hardcoded dashboard numbers with AI-generated ROI metrics
old_analytics_tag = '''        <div class="sl-tag" data-editable="true" style="${tagStyle}">${e(tx('an_tag',L))}</div>
        <div class="sl-h3" style="${h3Style}">${e(tx('an_h',L))}</div>
        <div style="font-size:20px;color:${V.TX2};line-height:1.6;margin-bottom:28px;">${e(anDesc[L]||anDesc.en)}</div>'''

new_analytics_tag = '''        <div class="sl-tag" data-editable="true" style="${tagStyle}">${e(tx('an_tag',L))}</div>
        <div class="sl-h3" style="${h3Style}">${e(STATE.aiRoiHeadline||tx('an_h',L))}</div>
        <div style="font-size:20px;color:${V.TX2};line-height:1.6;margin-bottom:28px;">${e(STATE.aiRoiBefore?'Before: '+STATE.aiRoiBefore:(anDesc[L]||anDesc.en))}</div>'''

if old_analytics_tag in src:
    src = src.replace(old_analytics_tag, new_analytics_tag)
    changes += 1
    print("✅ 6. Updated Analytics slide to use ROI headline")
else:
    print("⚠️ 6. Analytics tag block not found")


# ═══════════════════════════════════════
# 6. UPDATE Thank You slide to use new fields
# ═══════════════════════════════════════

# Find and update the thank you slide's body content to use ty_headline and ty_cta
old_ty_body_ref = '''STATE.aiTyBody||'''
new_ty_body_ref = '''STATE.aiTyBody||'''
# This is tricky because it's inside template literals. Let's just check the thank you slide.
# We'll add the CTA rendering in a separate smaller patch if needed.


# ═══════════════════════════════════════
# 7. UPDATE default active slides — set 8 core pages as default
# ═══════════════════════════════════════

# Find where activeSl is initialized
old_default = "let activeSl=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];"
new_default = "let activeSl=[0,2,3,7,10,11,12,15]; // 8 core: Cover, Pain, Features, Chat, Analytics(ROI), Roadmap, Pricing, ThankYou"

if old_default in src:
    src = src.replace(old_default, new_default)
    changes += 1
    print("✅ 7. Set 8 core pages as default active slides")
else:
    # Try alternative format
    alt = "let activeSl=["
    if alt in src:
        print("⚠️ 7. activeSl found but different format — skipping auto-change")
    else:
        print("⚠️ 7. activeSl not found")


# ═══════════════════════════════════════
# WRITE
# ═══════════════════════════════════════

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes}/7 changes applied.")

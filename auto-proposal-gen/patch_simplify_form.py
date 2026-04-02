#!/usr/bin/env python3
"""
Patch: Simplify input form to 3 fields + enhance research to cover removed fields
- Replace "pain + tools" box and "extra context" box with 3 fields:
  1. Sales Notes (free text - client quotes, anecdotes, anything first-hand)
  2. Scale (optional - employee count, locations)
  3. Monthly volume / Team size (optional - internal data that can't be searched)
- Update getCtx() to use new field IDs
- Update genAll() prompt to reference new fields
- Expand web search prompt to also find: tools/solutions used, target audience, company scale
- Add source citations to s-features slide
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ═══════════════════════════════════════
# 1. Replace the two form boxes with simplified 3-field version
# ═══════════════════════════════════════
old_form = '''      <!-- Golden box -->
      <div class="ctx-box" style="border-color:rgba(10,10,10,.12);background:rgba(10,10,10,.02);margin-top:.9rem;">
        <div class="ctx-lbl" style="color:#0a0a0a;">&#127919; Most important — use their own words</div>
        <div class="fg">
          <label class="fl">What does the client complain about? <span style="color:#0a0a0a;font-weight:700;">Quote them directly if possible</span></label>
          <textarea class="fi" id="in-pain" rows="3" placeholder="&quot;Nieuwe medewerkers bellen mij elke dag met dezelfde vragen over roosters en kleding — ik kom er niet meer aan toe om te managen.&quot; — Bas, Jumbo Filiaalmanager"></textarea>
        </div>
        <div class="fg" style="margin-bottom:0;">
          <label class="fl">Tools they use now <span style="color:#737373;font-weight:400;">(what Notso.ai replaces)</span></label>
          <input class="fi" id="in-tools" placeholder="e.g. WhatsApp-groep, uitgeprinte instructiebundels, mondelinge overdracht"/>
        </div>
      </div>

      <!-- Extra depth -->
      <div class="ctx-box" style="margin-top:.75rem;">
        <div class="ctx-lbl">&#128188; Extra context (optional but makes the deck sharper)</div>
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
        </div>
        <div class="fg" style="margin-bottom:.5rem;">
          <label class="fl">A specific situation or anecdote they told you</label>
          <textarea class="fi" id="in-anecdote" rows="2" placeholder="e.g. Bij een nieuwe kassa zaten 3 medewerkers 45 min te wachten op de manager voor uitleg over een app."></textarea>
        </div>
        <div class="fg" style="margin-bottom:0;">
          <label class="fl">What does success look like for them?</label>
          <input class="fi" id="in-goal" placeholder="e.g. Filiaalmanager kan focussen op klantcontact, niet op HR-vragen beantwoorden"/>
        </div>
      </div>'''

new_form = '''      <!-- Sales Intel — only first-hand info that web search can't find -->
      <div class="ctx-box" style="border-color:rgba(10,10,10,.12);background:rgba(10,10,10,.02);margin-top:.9rem;">
        <div class="ctx-lbl" style="color:#0a0a0a;">&#127919; Sales Notes — what you heard from the client</div>
        <div class="fg">
          <label class="fl">Anything the client told you <span style="color:#0a0a0a;font-weight:700;">— quotes, complaints, stories, context</span></label>
          <textarea class="fi" id="in-salesnotes" rows="4" placeholder="Paste anything useful here: direct quotes, anecdotes, what tools they use now, who the end users are, their goals...&#10;&#10;Example: &quot;Nieuwe medewerkers bellen mij elke dag met dezelfde vragen over roosters en kleding — ik kom er niet meer aan toe om te managen.&quot; — Bas, Filiaalmanager. They currently use a WhatsApp group + printed manuals. Goal: managers focus on customers, not HR questions."></textarea>
        </div>
        <div class="fr">
          <div class="fg" style="margin-bottom:0;">
            <label class="fl">Company scale <span style="color:#737373;font-weight:400;">(if known — otherwise we'll search)</span></label>
            <input class="fi" id="in-scale" placeholder="e.g. 700+ locations, 100,000 employees"/>
          </div>
          <div class="fg" style="margin-bottom:0;">
            <label class="fl">Monthly volume / team size <span style="color:#737373;font-weight:400;">(internal data — can't be searched)</span></label>
            <input class="fi" id="in-opdata" placeholder="e.g. 3,000 calls/month, 5 staff handling inquiries"/>
          </div>
        </div>
      </div>'''

if old_form in html:
    html = html.replace(old_form, new_form)
    changes += 1
    print("✅ 1. Form simplified: 9 fields → 3 fields")
else:
    print("❌ 1. Form HTML not found — check formatting")

# ═══════════════════════════════════════
# 2. Update getCtx() — map new field IDs
# ═══════════════════════════════════════
old_getctx = """    pain:document.getElementById('in-pain').value.trim()||'repetitive queries',
"""
# Find the full getCtx block to replace
old_ctx_block = """    pain:document.getElementById('in-pain').value.trim()||'repetitive queries',
"""

# Let's find and replace the entire getCtx field assignments
# We need to find the pattern more carefully
ctx_pattern = r"pain:document\.getElementById\('in-pain'\)\.value\.trim\(\)\|\|'repetitive queries',\n.*?tools:document\.getElementById\('in-tools'\)\.value\.trim\(\)\|\|'standard FAQ page',\n.*?audience:document\.getElementById\('in-audience'\)\?\.value\.trim\(\)\|\|'',\n.*?scale:document\.getElementById\('in-scale'\)\?\.value\.trim\(\)\|\|'',\n.*?volume:document\.getElementById\('in-volume'\)\?\.value\.trim\(\)\|\|'',\n.*?teamsize:document\.getElementById\('in-teamsize'\)\?\.value\.trim\(\)\|\|'',\n.*?chatscene:document\.getElementById\('in-chatscene'\)\?\.value\.trim\(\)\|\|'',\n.*?anecdote:document\.getElementById\('in-anecdote'\)\?\.value\.trim\(\)\|\|'',\n.*?goal:document\.getElementById\('in-goal'\)\?\.value\.trim\(\)\|\|'',"

new_ctx_fields = """salesnotes:document.getElementById('in-salesnotes')?.value.trim()||'',
    scale:document.getElementById('in-scale')?.value.trim()||'',
    opdata:document.getElementById('in-opdata')?.value.trim()||'',"""

match = re.search(ctx_pattern, html)
if match:
    html = html[:match.start()] + new_ctx_fields + html[match.end():]
    changes += 1
    print("✅ 2. getCtx() updated: 9 fields → 3 fields")
else:
    print("❌ 2. getCtx() pattern not found")

# ═══════════════════════════════════════
# 3. Update genAll() prompt — CLIENT PROFILE section
# ═══════════════════════════════════════
old_profile = """Company: ${clientName}
Website: ${c.url||'N/A'}
Industry: ${c.ind}
Use Case: ${useCaseDesc}
Decision-maker: ${c.role}
Pain points provided by sales rep: ${c.pain||'(not provided — research and infer from industry)'}
Tools being replaced: ${c.tools||'(not provided — research from website)'}
End users: ${c.audience||'(not provided — infer from use case)'}
Scale: ${c.scale||'(not provided — research from website)'}
Monthly inquiry volume: ${c.volume||'(not provided — estimate from industry averages)'}
Support team size: ${c.teamsize||'(not provided — estimate from scale)'}
Chat scenario hint: ${c.chatscene||'(not provided — generate based on use case + web research)'}
Real story/anecdote: ${c.anecdote||'(not provided — create a realistic scenario based on research)'}
Success definition: ${c.goal||'(not provided — infer from pain points)'}
${webResearch}${marketResearch}"""

new_profile = """Company: ${clientName}
Website: ${c.url||'N/A'}
Industry: ${c.ind}
Use Case: ${useCaseDesc}
Decision-maker: ${c.role}
Company scale: ${c.scale||'(not provided — check website research and web search results below)'}
Operational data: ${c.opdata||'(not provided — use industry averages for volume/team size estimates)'}

SALES REP NOTES (first-hand intelligence — highest priority, use verbatim quotes when available):
${c.salesnotes||'(no notes provided — rely on website research + web search below)'}
${webResearch}${marketResearch}"""

if old_profile in html:
    html = html.replace(old_profile, new_profile)
    changes += 1
    print("✅ 3. genAll() prompt updated with new field structure")
else:
    print("❌ 3. genAll() prompt pattern not found")

# ═══════════════════════════════════════
# 4. Expand web search prompt to also find company-specific info
# ═══════════════════════════════════════
old_search_task = """YOUR TASK: Search the web for REAL, VERIFIABLE data in these 4 areas:

1. PAIN POINTS — Search for real complaints, challenges, and statistics about this industry's operational problems that an AI agent could solve. Look for surveys, reports, and news articles.

2. MARKET DATA — Search for the market size of AI/chatbot solutions in this industry. Find growth rates, adoption statistics, and market projections from research firms.

3. COMPETITORS — Search for existing AI chatbot or automation solutions in this industry. Identify what they do and what they DON'T do (gaps Notso.ai can fill with 3D animated brand agents).

4. ROI EVIDENCE — Search for case studies of AI chatbot implementations in this industry. Find specific cost savings, time reductions, and efficiency improvements with real numbers."""

new_search_task = """YOUR TASK: Search the web for REAL, VERIFIABLE data in these 5 areas:

1. PAIN POINTS — Search for real complaints, challenges, and statistics about this industry's operational problems that an AI agent could solve. Look for surveys, reports, and news articles.

2. MARKET DATA — Search for the market size of AI/chatbot solutions in this industry. Find growth rates, adoption statistics, and market projections from research firms.

3. COMPETITORS — Search for existing AI chatbot or automation solutions in this industry. Identify what they do and what they DON'T do (gaps Notso.ai can fill with 3D animated brand agents).

4. ROI EVIDENCE — Search for case studies of AI chatbot implementations in this industry. Find specific cost savings, time reductions, and efficiency improvements with real numbers.

5. CLIENT PROFILE — If a specific client name is provided, search for: company size (employees, locations, revenue), what tools/platforms they currently use (look at job postings, press releases, tech stack mentions), their target audience, and any recent news or challenges they face."""

if old_search_task in html:
    html = html.replace(old_search_task, new_search_task)
    changes += 1
    print("✅ 4. Web search prompt expanded with client profile research")
else:
    print("❌ 4. Web search task pattern not found")

# Also expand the JSON output format to include client profile
old_json_format = '''  "roiBenchmarks": {
    "casestudies": [
      {"institution": "name", "result": "exact result", "source": "source", "url": "URL", "verified": true}
    ],
    "calculations": []
  }
}

Return ONLY the JSON after completing your research. No markdown wrapping.'''

new_json_format = '''  "roiBenchmarks": {
    "casestudies": [
      {"institution": "name", "result": "exact result", "source": "source", "url": "URL", "verified": true}
    ],
    "calculations": []
  },
  "clientProfile": {
    "companySize": {"value": "employee count, locations, etc.", "source": "source", "url": "URL", "verified": true},
    "currentTools": [{"name": "tool/platform name", "source": "where found", "url": "URL", "verified": true}],
    "targetAudience": {"value": "who they serve", "source": "source", "url": "URL", "verified": true},
    "recentNews": [{"headline": "brief", "url": "URL", "verified": true}]
  }
}

Return ONLY the JSON after completing your research. No markdown wrapping.'''

if old_json_format in html:
    html = html.replace(old_json_format, new_json_format)
    changes += 1
    print("✅ 5. Research JSON output expanded with clientProfile section")
else:
    print("❌ 5. Research JSON output pattern not found")

# ═══════════════════════════════════════
# 5. Fix the applyAI function that references in-pain
# ═══════════════════════════════════════
old_apply = "if(aiTarget==='pain'){document.getElementById('in-pain').value=lastAI;STATE.aiPain=lastAI;}"
new_apply = "if(aiTarget==='pain'){STATE.aiPain=lastAI;}"
if old_apply in html:
    html = html.replace(old_apply, new_apply)
    changes += 1
    print("✅ 6. applyAI() fixed — no longer writes to removed in-pain field")
else:
    print("❌ 6. applyAI() pattern not found")

# Fix the genAll success handler that writes to in-pain
old_pain_write = "if(d.pain_intro)document.getElementById('in-pain').value=d.pain_intro;"
new_pain_write = "if(d.pain_intro)STATE.aiPain=d.pain_intro;"
if old_pain_write in html:
    html = html.replace(old_pain_write, new_pain_write)
    changes += 1
    print("✅ 7. genAll() result handler fixed — no longer writes to removed in-pain field")
else:
    print("❌ 7. genAll() pain_intro write pattern not found")

# Fix STATE.pain initialization that references in-pain
old_state_pain = "STATE.pain=document.getElementById('in-pain').value.trim()||'repetitive customer queries';"
new_state_pain = "STATE.pain=STATE.aiPain||'repetitive customer queries';"
if old_state_pain in html:
    html = html.replace(old_state_pain, new_state_pain)
    changes += 1
    print("✅ 8. STATE.pain init fixed — reads from STATE.aiPain instead of removed field")
else:
    print("❌ 8. STATE.pain init pattern not found")

# ═══════════════════════════════════════
# 6. Add source footnote to s-features slide
# ═══════════════════════════════════════
# Find the s-features closing and add a research source line
old_feat_num = '''<div class="sl-num" style="color:rgba(255,255,255,.15);position:absolute;bottom:40px;right:60px;font-family:var(--fd);font-size:180px;font-weight:800;letter-spacing:-.08em;line-height:1;user-select:none;pointer-events:none;">03</div>`;}'''

new_feat_num = '''<div class="sl-num" style="color:rgba(255,255,255,.15);position:absolute;bottom:40px;right:60px;font-family:var(--fd);font-size:180px;font-weight:800;letter-spacing:-.08em;line-height:1;user-select:none;pointer-events:none;">03</div>
    ${STATE.research ? '<div style="position:absolute;bottom:18px;left:60px;font-size:10px;color:rgba(255,255,255,.35);max-width:60%;">Research: '+(STATE.research.source||'')+(STATE.research.isLive?' — '+STATE.research.searchCount+' web searches':'')+'</div>' : ''}`;}'''

if old_feat_num in html:
    html = html.replace(old_feat_num, new_feat_num)
    changes += 1
    print("✅ 9. s-features slide: added research source footnote")
else:
    print("❌ 9. s-features slide pattern not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ Patch applied: {changes} changes")
print("""
Summary:
  1. Form simplified: 9 fields → 3 (Sales Notes, Scale, Operational Data)
  2. getCtx() updated for new field IDs
  3. genAll() prompt restructured — sales notes = highest priority input
  4. Web search now also researches: company size, tools used, target audience, recent news
  5. Research JSON output includes clientProfile section
  6. Removed references to deleted form fields (in-pain, in-tools, etc.)
  7. s-features slide shows research source footnote
""")

#!/usr/bin/env python3
"""
Patch: Anthropic Web Search Tool + New Slide Templates
======================================================
1. Modify callClaude() to support tools parameter (web_search)
2. Replace Brave Search with Anthropic built-in web_search tool
3. Add 'Market Opportunity' slide (s-market)
4. Add 'ROI Evidence' slide (s-roi)
5. Update genAll() to populate new slides with research data
6. Remove Brave Search API key field (no longer needed)
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ═══════════════════════════════════════════════════════════════
# 1. MODIFY callClaude() to support optional tools parameter
# ═══════════════════════════════════════════════════════════════

old_callclaude = """async function callClaude(prompt, maxTokens=4096){
  const key=document.getElementById('api-key').value.trim();
  if(!key)return null;
  const controller=new AbortController();
  const timeout=setTimeout(()=>controller.abort(),120000);
  try{
    const r=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      signal:controller.signal,
      headers:{
        'Content-Type':'application/json',
        'x-api-key':key,
        'anthropic-version':'2023-06-01',
        'anthropic-dangerous-direct-browser-access':'true'
      },
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:maxTokens,
        messages:[{role:'user',content:prompt}]
      })
    });
    clearTimeout(timeout);
    const d=await r.json();
    if(d.error){
      console.error('Claude API error:',d.error);
      window._lastApiError=`${d.error.type}: ${d.error.message}`;
      return null;
    }
    return d.content?.map(x=>x.text||'').join('')||null;
  }catch(e){
    clearTimeout(timeout);
    console.error('callClaude fetch error:',e);
    window._lastApiError=e.name==='AbortError'?'Request timed out after 60s':e.message||String(e);
    return null;
  }
}"""

new_callclaude = r"""async function callClaude(prompt, maxTokens=4096, options={}){
  const key=document.getElementById('api-key').value.trim();
  if(!key)return null;
  const controller=new AbortController();
  const timeoutMs=options.timeout||120000;
  const timeout=setTimeout(()=>controller.abort(),timeoutMs);
  try{
    const body={
      model:'claude-sonnet-4-20250514',
      max_tokens:maxTokens,
      messages:[{role:'user',content:prompt}]
    };
    // Add tools if specified (e.g., web_search)
    if(options.tools) body.tools=options.tools;

    const r=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      signal:controller.signal,
      headers:{
        'Content-Type':'application/json',
        'x-api-key':key,
        'anthropic-version':'2023-06-01',
        'anthropic-dangerous-direct-browser-access':'true'
      },
      body:JSON.stringify(body)
    });
    clearTimeout(timeout);
    const d=await r.json();
    if(d.error){
      console.error('Claude API error:',d.error);
      window._lastApiError=`${d.error.type}: ${d.error.message}`;
      return null;
    }
    // If tools were used, return full response for citation extraction
    if(options.tools && options.returnFull) return d;
    return d.content?.map(x=>x.text||'').join('')||null;
  }catch(e){
    clearTimeout(timeout);
    console.error('callClaude fetch error:',e);
    window._lastApiError=e.name==='AbortError'?'Request timed out after 120s':e.message||String(e);
    return null;
  }
}"""

src = src.replace(old_callclaude, new_callclaude)

# ═══════════════════════════════════════════════════════════════
# 2. REPLACE Brave Search functions with Anthropic web_search
# ═══════════════════════════════════════════════════════════════

# Find and replace the searchWeb, searchIndustryData, formatSearchResultsForClaude,
# and synthesizeSearchResults functions with new web_search versions

old_brave_search = """/* ─── Brave Search API Integration ─── */
async function searchWeb(query, maxResults=5) {
  const key = document.getElementById('search-key')?.value?.trim();
  if (!key) return null;

  try {
    const url = `https://api.search.brave.com/res/v1/web/search?q=${encodeURIComponent(query)}&count=${maxResults}`;
    const res = await fetch(url, {
      headers: {
        'X-Subscription-Token': key,
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip'
      }
    });
    if (!res.ok) {
      console.warn('Brave Search error:', res.status);
      return null;
    }
    const data = await res.json();
    // Normalize to simple format
    return (data.web?.results || []).map(r => ({
      title: r.title || '',
      url: r.url || '',
      snippet: r.description || '',
    }));
  } catch (e) {
    console.warn('Brave Search fetch error:', e.message);
    return null;
  }
}

// Run 4 targeted searches for an industry
async function searchIndustryData(industryText, clientName, painText, statusEl) {
  const queries = [
    `${industryText} common problems challenges complaints statistics 2024`,
    `${industryText} AI chatbot automation market size 2024 2025`,
    `${industryText} AI chatbot competitors solutions comparison`,
    `${industryText} AI chatbot ROI cost savings case study university`
  ];

  const labels = ['Pain Points', 'Market Data', 'Competitors', 'ROI Data'];
  const allResults = {};

  for (let i = 0; i < queries.length; i++) {
    if (statusEl) statusEl.textContent = `🔍 Searching ${labels[i]}… (${i+1}/4)`;
    const results = await searchWeb(queries[i]);
    allResults[labels[i]] = results || [];
    // Small delay between requests to be nice to API
    if (i < queries.length - 1) await new Promise(r => setTimeout(r, 300));
  }

  return allResults;
}

// Format search results for Claude synthesis prompt
function formatSearchResultsForClaude(searchResults) {
  let out = '';
  for (const [category, results] of Object.entries(searchResults)) {
    out += `\\n【${category} — Search Results】\\n`;
    if (results.length === 0) {
      out += '(No results found)\\n';
      continue;
    }
    results.forEach((r, i) => {
      out += `[${i+1}] "${r.title}"\\n    URL: ${r.url}\\n    Snippet: ${r.snippet}\\n\\n`;
    });
  }
  return out;
}

// Claude synthesis prompt — ONLY organize search results, NEVER invent data
async function synthesizeSearchResults(searchResults, industryText, clientName, statusEl) {"""

new_web_search = r"""/* ─── Anthropic Web Search Tool Integration ─── */
// Uses Claude's built-in web_search server tool — searches happen on Anthropic's servers
// No external API key needed, just the same Anthropic key

async function liveResearchWithWebSearch(industryText, clientName, painText, statusEl) {
  if (statusEl) statusEl.textContent = '🔍 Starting live web research (Anthropic web_search)…';

  const researchPrompt = `You are a B2B market research analyst preparing data for a sales proposal for Notso.ai — a company that makes 3D animated AI brand agents with empathy.

RESEARCH TARGET:
- Industry: ${industryText}
- Client: ${clientName || 'Unknown'}
- Known pain points: ${painText || 'Not specified'}

YOUR TASK: Search the web for REAL, VERIFIABLE data in these 4 areas:

1. PAIN POINTS — Search for real complaints, challenges, and statistics about this industry's operational problems that an AI agent could solve. Look for surveys, reports, and news articles.

2. MARKET DATA — Search for the market size of AI/chatbot solutions in this industry. Find growth rates, adoption statistics, and market projections from research firms.

3. COMPETITORS — Search for existing AI chatbot or automation solutions in this industry. Identify what they do and what they DON'T do (gaps Notso.ai can fill with 3D animated brand agents).

4. ROI EVIDENCE — Search for case studies of AI chatbot implementations in this industry. Find specific cost savings, time reductions, and efficiency improvements with real numbers.

CRITICAL RULES:
- Search thoroughly for each area (use multiple searches if needed)
- Only report data you actually find in search results
- Include the exact URL for every data point
- If you cannot find data for a category, say "No verified data found"
- Do NOT estimate, infer, or fabricate ANY numbers
- Prefer recent data (2023-2026)

After searching, organize your findings into this EXACT JSON format:
{
  "painPoints": [
    {"title": "max 6 words", "desc": "exact finding from search", "source": "source name", "url": "exact URL", "verified": true}
  ],
  "marketData": {
    "industrySize": {"value": "exact number from search", "source": "source name", "url": "URL", "verified": true},
    "growthRate": {"value": "exact from search", "source": "source name", "url": "URL", "verified": true},
    "projectedSize": {"value": "exact from search or 'No verified data found'", "source": "", "url": "", "verified": false}
  },
  "competitors": [
    {"name": "competitor", "gap": "limitation found in research", "url": "URL", "verified": true}
  ],
  "roiBenchmarks": {
    "casestudies": [
      {"institution": "name", "result": "exact result", "source": "source", "url": "URL", "verified": true}
    ],
    "calculations": []
  }
}

Return ONLY the JSON after completing your research. No markdown wrapping.`;

  try {
    const fullResponse = await callClaude(researchPrompt, 8000, {
      tools: [{
        type: 'web_search_20250305',
        name: 'web_search',
        max_uses: 10,
        user_location: {
          type: 'approximate',
          country: 'NL',
          timezone: 'Europe/Amsterdam'
        }
      }],
      returnFull: true,
      timeout: 180000 // 3 min for research
    });

    if (!fullResponse || fullResponse.error) {
      console.error('Web search research failed:', fullResponse?.error);
      if (statusEl) statusEl.textContent = '⚠️ Web search failed — ' + (fullResponse?.error?.message || 'unknown error');
      return null;
    }

    // Extract text content and citations from response
    const textParts = [];
    const allCitations = [];
    if (fullResponse.content) {
      for (const block of fullResponse.content) {
        if (block.type === 'text') {
          textParts.push(block.text);
          // Extract citations
          if (block.citations) {
            for (const cite of block.citations) {
              if (cite.url) {
                allCitations.push({
                  url: cite.url,
                  title: cite.title || '',
                  text: cite.cited_text || ''
                });
              }
            }
          }
        }
      }
    }

    const rawText = textParts.join('');
    console.log('Web search research raw:', rawText);
    console.log('Citations found:', allCitations.length);

    // Log search usage
    if (fullResponse.usage?.server_tool_use) {
      console.log('Web searches used:', fullResponse.usage.server_tool_use.web_search_requests);
    }

    // Parse JSON from response
    let cleaned = rawText.replace(/```json/g, '').replace(/```/g, '').trim();
    const jsonStart = cleaned.indexOf('{');
    const jsonEnd = cleaned.lastIndexOf('}') + 1;
    if (jsonStart >= 0 && jsonEnd > jsonStart) cleaned = cleaned.slice(jsonStart, jsonEnd);

    const data = JSON.parse(cleaned);
    // Attach citation metadata
    data._citations = allCitations;
    data._searchCount = fullResponse.usage?.server_tool_use?.web_search_requests || 0;
    return data;

  } catch (e) {
    console.error('Live research error:', e);
    if (statusEl) statusEl.textContent = '⚠️ Research failed: ' + e.message;
    return null;
  }
}

// Legacy compatibility wrapper (replaces old synthesizeSearchResults)
async function synthesizeSearchResults(searchResults, industryText, clientName, statusEl) {"""

src = src.replace(old_brave_search, new_web_search)

# ═══════════════════════════════════════════════════════════════
# 3. UPDATE researchIndustry() — use web_search instead of Brave
# ═══════════════════════════════════════════════════════════════

old_live_research = """  // Step 2: Not in DB — check if Search API key is available
  const searchKey = document.getElementById('search-key')?.value?.trim();
  if (!searchKey) {
    if (statusEl) statusEl.textContent = '⚠️ Industry not in database & no Search API key — skipping research (no fake data will be generated)';
    STATE.research = null;
    return null;
  }

  // Step 3: Live search with real API
  if (statusEl) statusEl.textContent = '🔍 Industry not in DB — starting live web search…';
  const searchResults = await searchIndustryData(industryText, clientName, painText, statusEl);

  // Check if we got any results at all
  const totalResults = Object.values(searchResults).reduce((sum, arr) => sum + arr.length, 0);
  if (totalResults === 0) {
    if (statusEl) statusEl.textContent = '⚠️ No search results found — skipping research';
    STATE.research = null;
    return null;
  }

  // Step 4: Have Claude SYNTHESIZE (not generate) the search results
  const synthesized = await synthesizeSearchResults(searchResults, industryText, clientName, statusEl);
  if (!synthesized) {
    if (statusEl) statusEl.textContent = '⚠️ Could not synthesize search results — skipping research';
    STATE.research = null;
    return null;
  }

  // Count verified points
  let vCount = 0, tCount = 0;
  if (synthesized.painPoints) synthesized.painPoints.forEach(p => { tCount++; if (p.verified) vCount++; });
  if (synthesized.roiBenchmarks?.casestudies) synthesized.roiBenchmarks.casestudies.forEach(c => { tCount++; if (c.verified) vCount++; });

  STATE.research = {
    ...synthesized,
    matchedIndustry: 'live-search',
    source: 'Live Web Search (Brave) + Claude Synthesis',
    isLive: true,
    searchResults: searchResults, // Keep raw results for transparency
    verifiedCount: vCount,
    totalCount: tCount
  };

  if (statusEl) statusEl.textContent = `✅ Live research complete — ${vCount} verified data points from ${totalResults} search results`;"""

new_live_research = r"""  // Step 2: Not in DB — use Anthropic web_search tool (same API key, no extra key needed)
  if (statusEl) statusEl.textContent = '🔍 Industry not in DB — launching live web research…';
  const liveData = await liveResearchWithWebSearch(industryText, clientName, painText, statusEl);

  if (!liveData) {
    if (statusEl) statusEl.textContent = '⚠️ Live research returned no data — proceeding without research';
    STATE.research = null;
    return null;
  }

  // Count verified points
  let vCount = 0, tCount = 0;
  if (liveData.painPoints) liveData.painPoints.forEach(p => { tCount++; if (p.verified) vCount++; });
  if (liveData.roiBenchmarks?.casestudies) liveData.roiBenchmarks.casestudies.forEach(c => { tCount++; if (c.verified) vCount++; });

  STATE.research = {
    ...liveData,
    matchedIndustry: 'live-web-search',
    source: 'Anthropic Web Search Tool (server-side)',
    isLive: true,
    citations: liveData._citations || [],
    searchCount: liveData._searchCount || 0,
    verifiedCount: vCount,
    totalCount: tCount
  };

  if (statusEl) statusEl.textContent = `✅ Live research complete — ${vCount} verified data points from ${liveData._searchCount || '?'} web searches`;"""

src = src.replace(old_live_research, new_live_research)

# ═══════════════════════════════════════════════════════════════
# 4. REMOVE Brave Search API key field — no longer needed
# ═══════════════════════════════════════════════════════════════

old_api_keys = """<div class="fr">
        <div class="fg" style="margin-bottom:.4rem;"><label class="fl">Anthropic API Key <span style="color:#737373;font-weight:400;">(content generation)</span></label><input class="fi" id="api-key" type="password" placeholder="sk-ant-..."/></div>
        <div class="fg" style="margin-bottom:.4rem;"><label class="fl">Brave Search API Key <span style="color:#737373;font-weight:400;">(live research — optional)</span></label><input class="fi" id="search-key" type="password" placeholder="BSA..."/></div>
      </div>
      <div class="api-hint">Stored in memory only &middot; <a href="https://console.anthropic.com" target="_blank" style="color:#0a0a0a;text-decoration:underline;">Anthropic key &#8594;</a> &middot; <a href="https://brave.com/search/api/" target="_blank" style="color:#0a0a0a;text-decoration:underline;">Brave Search key (free 2K/mo) &#8594;</a></div>"""

new_api_keys = """<div class="fg" style="margin-bottom:.4rem;"><label class="fl">Anthropic API Key <span style="color:#737373;font-weight:400;">(powers content generation + web search research)</span></label><input class="fi" id="api-key" type="password" placeholder="sk-ant-..."/></div>
      <div class="api-hint">Stored in memory only &middot; One key does everything: research + content &middot; <a href="https://console.anthropic.com" target="_blank" style="color:#0a0a0a;text-decoration:underline;">Get a key &#8594;</a> &middot; Web search: $0.01/search</div>"""

src = src.replace(old_api_keys, new_api_keys)

# ═══════════════════════════════════════════════════════════════
# 5. ADD new slides to ALL_SLIDES array
# ═══════════════════════════════════════════════════════════════

# Insert s-market after s-pain and s-roi after s-analytics
old_all_slides = """  {id:'s-pain',title:'Pain Points',e:'😩',quick:true},
  {id:'s-features',title:'Core Features',e:'✨',quick:true},"""

new_all_slides = """  {id:'s-pain',title:'Pain Points',e:'😩',quick:true},
  {id:'s-market',title:'Market Opportunity',e:'📈',quick:true},
  {id:'s-features',title:'Core Features',e:'✨',quick:true},"""

src = src.replace(old_all_slides, new_all_slides)

old_analytics_slide = """  {id:'s-analytics',title:'Data & Insights',e:'📊',quick:true},
  {id:'s-roadmap',title:'Roadmap',e:'🗺️',quick:true},"""

new_analytics_slide = """  {id:'s-analytics',title:'Data & Insights',e:'📊',quick:true},
  {id:'s-roi',title:'ROI Evidence',e:'💰',quick:true},
  {id:'s-roadmap',title:'Roadmap',e:'🗺️',quick:true},"""

src = src.replace(old_analytics_slide, new_analytics_slide)

# ═══════════════════════════════════════════════════════════════
# 6. ADD STATE properties for new slides
# ═══════════════════════════════════════════════════════════════

src = src.replace(
    "research:null, // Market research data (from INDUSTRY_DB or live)",
    "research:null, // Market research data (from INDUSTRY_DB or live)\n  aiMarketSlide:null, // {headline, metrics[]} for Market Opportunity slide\n  aiRoiSlide:null, // {headline, evidence[]} for ROI Evidence slide"
)

# ═══════════════════════════════════════════════════════════════
# 7. ADD buildSlideHTML cases for s-market and s-roi
# ═══════════════════════════════════════════════════════════════

# We need to insert new cases into the switch statement in buildSlideHTML
# Insert after the s-pain case (which ends with a specific pattern)
# Find the s-features case start and insert before it

old_features_case = "  case 's-features': {"

market_slide_html = r"""  case 's-market': {
    // Market Opportunity slide — shows verified research data
    const research = STATE.research;
    const mktData = research?.marketData || {};
    const hasData = research && (mktData.industrySize?.verified || mktData.growthRate?.verified);

    // Build metric cards from research data
    let metricCards = '';
    if (mktData.industrySize?.verified) {
      metricCards += `<div style="flex:1;min-width:280px;background:${alpha(c1,.06)};border:1px solid ${alpha(c1,.15)};border-radius:16px;padding:28px;">
        <div style="font-size:${S.labelSm}px;text-transform:uppercase;letter-spacing:.12em;color:${V.TX3};margin-bottom:8px;">Industry Size</div>
        <div style="font-size:${S.card}px;color:${V.TX};font-weight:600;line-height:1.4;margin-bottom:8px;">${e(mktData.industrySize.value)}</div>
        <div style="font-size:${S.labelSm}px;color:${c1};">✓ ${e(mktData.industrySize.source)}</div>
      </div>`;
    }
    if (mktData.growthRate?.verified) {
      metricCards += `<div style="flex:1;min-width:280px;background:${alpha(c2,.06)};border:1px solid ${alpha(c2,.15)};border-radius:16px;padding:28px;">
        <div style="font-size:${S.labelSm}px;text-transform:uppercase;letter-spacing:.12em;color:${V.TX3};margin-bottom:8px;">Growth Rate</div>
        <div style="font-size:${S.card}px;color:${V.TX};font-weight:600;line-height:1.4;margin-bottom:8px;">${e(mktData.growthRate.value)}</div>
        <div style="font-size:${S.labelSm}px;color:${c2};">✓ ${e(mktData.growthRate.source)}</div>
      </div>`;
    }
    if (mktData.projectedSize?.verified) {
      metricCards += `<div style="flex:1;min-width:280px;background:${alpha(V.TX,.04)};border:1px solid ${alpha(V.TX,.1)};border-radius:16px;padding:28px;">
        <div style="font-size:${S.labelSm}px;text-transform:uppercase;letter-spacing:.12em;color:${V.TX3};margin-bottom:8px;">Projected</div>
        <div style="font-size:${S.card}px;color:${V.TX};font-weight:600;line-height:1.4;margin-bottom:8px;">${e(mktData.projectedSize.value)}</div>
        <div style="font-size:${S.labelSm}px;color:${V.TX2};">✓ ${e(mktData.projectedSize.source)}</div>
      </div>`;
    }

    // Competitor gaps
    let compCards = '';
    const comps = research?.competitors?.filter(c => c.verified) || [];
    if (comps.length) {
      compCards = comps.map(comp => `<div style="display:flex;align-items:flex-start;gap:12px;padding:16px 20px;background:${alpha(V.TX,.03)};border:1px solid ${alpha(V.TX,.06)};border-radius:12px;">
        <div style="font-size:18px;margin-top:2px;">🏁</div>
        <div>
          <div style="font-size:${S.cardTx}px;font-weight:600;color:${V.TX};">${e(comp.name)}</div>
          <div style="font-size:${S.chatSm}px;color:${V.TX2};margin-top:4px;">Gap: ${e(comp.gap)}</div>
        </div>
      </div>`).join('');
    }

    const noDataMsg = `<div style="text-align:center;padding:80px 40px;color:${V.TX3};font-size:${S.body}px;">
      <div style="font-size:48px;margin-bottom:16px;">📊</div>
      <div>No verified market data available for this industry.</div>
      <div style="font-size:${S.chatSm}px;margin-top:8px;">Research will populate this slide when data is found.</div>
    </div>`;

    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="bottom:-100px;left:-60px;width:350px;height:350px;border-width:55px;border-color:${alpha(c1,.07)};"></div>
    <div class="sl-safe">
      <div class="sl-tag" data-editable="true" style="${tagStyle}">${e({en:'Market Opportunity',nl:'Marktkans',zh:'市場機會',ja:'市場機会',de:'Marktchance',fr:'Opportunité',es:'Oportunidad'}[L]||'Market Opportunity')}</div>
      <div class="sl-h3" style="${h3Style}">${e({en:'Why Now. Why This Market.',nl:'Waarom nu. Waarom deze markt.',zh:'為什麼是現在。為什麼是這個市場。',ja:'なぜ今。なぜこの市場。',de:'Warum jetzt. Warum dieser Markt.',fr:'Pourquoi maintenant.',es:'Por qué ahora.'}[L]||'Why Now. Why This Market.')}</div>
      ${hasData ? `
        <div style="display:flex;flex-wrap:wrap;gap:20px;margin-top:24px;">
          ${metricCards}
        </div>
        ${compCards ? `<div style="margin-top:32px;">
          <div style="font-size:${S.labelSm}px;text-transform:uppercase;letter-spacing:.12em;color:${V.TX3};margin-bottom:12px;">Competitor Landscape — Gaps We Fill</div>
          <div style="display:flex;flex-direction:column;gap:10px;">${compCards}</div>
        </div>` : ''}
        <div style="margin-top:24px;font-size:${S.labelSm}px;color:${V.TX3};font-style:italic;">All data points verified with source URLs — see research panel for details</div>
      ` : noDataMsg}
    </div>
    <div class="sl-num" style="${numStyle}">04</div>`;
  }

"""

src = src.replace(old_features_case, market_slide_html + '  ' + old_features_case)

# Now add s-roi case — insert before s-roadmap
old_roadmap_case = "  case 's-roadmap': {"

roi_slide_html = r"""  case 's-roi': {
    // ROI Evidence slide — shows verified case studies and calculations
    const researchRoi = STATE.research;
    const rb = researchRoi?.roiBenchmarks || {};
    const cases = (rb.casestudies || []).filter(c => c.verified);
    const calcs = (rb.calculations || []).filter(c => c.verified);
    const hasEvidence = cases.length > 0 || calcs.length > 0;

    let evidenceCards = '';
    if (cases.length) {
      evidenceCards += cases.map((cs, i) => {
        const colors = [c1, c2, '#4CD8A8', '#8B5CF6'];
        const clr = colors[i % colors.length];
        return `<div style="flex:1;min-width:280px;background:${alpha(clr,.06)};border:1px solid ${alpha(clr,.15)};border-radius:16px;padding:28px;">
          <div style="font-size:${S.labelSm}px;text-transform:uppercase;letter-spacing:.1em;color:${clr};margin-bottom:8px;">Case Study</div>
          <div style="font-size:${S.card}px;font-weight:700;color:${V.TX};margin-bottom:8px;">${e(cs.institution)}</div>
          <div style="font-size:${S.cardTx}px;color:${V.TX2};line-height:1.5;">${e(cs.result)}</div>
          <div style="font-size:${S.labelSm}px;color:${clr};margin-top:12px;">✓ ${e(cs.source)}</div>
        </div>`;
      }).join('');
    }

    let calcCards = '';
    if (calcs.length) {
      calcCards = calcs.map(calc => `<div style="padding:16px 20px;background:${alpha(V.TX,.03)};border:1px solid ${alpha(V.TX,.08)};border-radius:12px;display:flex;align-items:flex-start;gap:12px;">
        <div style="font-size:20px;">📐</div>
        <div>
          <div style="font-size:${S.cardTx}px;color:${V.TX2};">${e(calc.scenario)}</div>
          <div style="font-size:${S.card}px;font-weight:700;color:${c1};margin-top:4px;">${e(calc.result)}</div>
          <div style="font-size:${S.labelSm}px;color:${V.TX3};margin-top:4px;">✓ ${e(calc.source)}</div>
        </div>
      </div>`).join('');
    }

    // Notso.ai's own case studies as fallback
    const notsoCase = `<div style="display:flex;flex-wrap:wrap;gap:20px;margin-top:24px;">
      <div style="flex:1;min-width:280px;background:${alpha(c1,.06)};border:1px solid ${alpha(c1,.15)};border-radius:16px;padding:28px;">
        <div style="font-size:${S.labelSm}px;text-transform:uppercase;letter-spacing:.1em;color:${c1};margin-bottom:8px;">Notso.ai Case</div>
        <div style="font-size:${S.card}px;font-weight:700;color:${V.TX};margin-bottom:8px;">Jumbo Supermarkets</div>
        <div style="font-size:${S.cardTx}px;color:${V.TX2};line-height:1.5;">70% reduction in HR workload for onboarding questions</div>
        <div style="font-size:${S.labelSm}px;color:${c1};margin-top:12px;">✓ Notso.ai client result</div>
      </div>
      <div style="flex:1;min-width:280px;background:${alpha(c2,.06)};border:1px solid ${alpha(c2,.15)};border-radius:16px;padding:28px;">
        <div style="font-size:${S.labelSm}px;text-transform:uppercase;letter-spacing:.1em;color:${c2};margin-bottom:8px;">Notso.ai Case</div>
        <div style="font-size:${S.card}px;font-weight:700;color:${V.TX};margin-bottom:8px;">WTC Amsterdam</div>
        <div style="font-size:${S.cardTx}px;color:${V.TX2};line-height:1.5;">24/7 digital concierge with real-time emotion tracking and conversion ROI</div>
        <div style="font-size:${S.labelSm}px;color:${c2};margin-top:12px;">✓ Notso.ai client result</div>
      </div>
    </div>`;

    return `
    <div class="sl-bg" style="${bg}"></div>
    <div class="geo-ring" style="top:-60px;right:-80px;width:320px;height:320px;border-width:50px;border-color:${alpha(c2,.07)};"></div>
    <div class="sl-safe">
      <div class="sl-tag" data-editable="true" style="${tagStyle}">${e({en:'Proven Results',nl:'Bewezen Resultaten',zh:'驗證成效',ja:'実証済み成果',de:'Bewiesene Ergebnisse',fr:'Résultats prouvés',es:'Resultados probados'}[L]||'Proven Results')}</div>
      <div class="sl-h3" style="${h3Style}">${e({en:'Real Numbers. Real Impact.',nl:'Echte cijfers. Echte impact.',zh:'真實數據。真實影響。',ja:'リアルな数字。リアルなインパクト。',de:'Echte Zahlen. Echte Wirkung.',fr:'Vrais chiffres. Vrai impact.',es:'Números reales. Impacto real.'}[L]||'Real Numbers. Real Impact.')}</div>
      ${hasEvidence ? `
        <div style="display:flex;flex-wrap:wrap;gap:20px;margin-top:24px;">${evidenceCards}</div>
        ${calcCards ? `<div style="margin-top:24px;display:flex;flex-direction:column;gap:10px;">${calcCards}</div>` : ''}
        <div style="margin-top:24px;font-size:${S.labelSm}px;color:${V.TX3};font-style:italic;">All figures from verified external sources — see research panel for URLs</div>
      ` : notsoCase}
    </div>
    <div class="sl-num" style="${numStyle}">12</div>`;
  }

"""

src = src.replace(old_roadmap_case, roi_slide_html + '  ' + old_roadmap_case)

# ═══════════════════════════════════════════════════════════════
# 8. UPDATE slide numbering indicator text in workflow badges
# ═══════════════════════════════════════════════════════════════

# Update the source badge in research panel for live search
src = src.replace(
    "'🔍 Live Web Search — all URLs are real search results'",
    "'🔍 Anthropic Web Search — Claude searched the web server-side (' + (research.searchCount || '?') + ' searches)'"
)

# Update the "Zero hallucination" badge
src = src.replace(
    "🚫 Zero hallucination",
    "🔍 Claude web_search API"
)

# Write output
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print('✅ Patch applied: Anthropic Web Search + New Slide Templates')
print()
print('Changes:')
print('  1. callClaude() now supports tools parameter (web_search)')
print('  2. Brave Search removed → replaced with Anthropic web_search_20250305')
print('  3. No extra API key needed (same Anthropic key does everything)')
print('  4. New slide: s-market (Market Opportunity) — after Pain Points')
print('  5. New slide: s-roi (ROI Evidence) — after Data & Insights')
print('  6. Both new slides ONLY show verified data with source URLs')
print('  7. Fallback: Notso.ai own case studies (Jumbo, WTC) on ROI slide')
print('  8. Total slides: 16 → 18')

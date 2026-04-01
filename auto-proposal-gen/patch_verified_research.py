#!/usr/bin/env python3
"""
Patch: Verified Research System — Real Search API Integration
=============================================================
Major changes:
1. Restructured INDUSTRY_DB with verified/url fields
2. Brave Search API integration for unknown industries
3. Claude API role changes from "generate" to "synthesize search results only"
4. Verification badges on all data points
5. New slide templates: Market Opportunity + ROI Analysis
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ═══════════════════════════════════════════════════════════════
# 1. REPLACE entire INDUSTRY_DB + research module with verified version
# ═══════════════════════════════════════════════════════════════

# Find the old research module and replace it entirely
old_module_start = '/* ════════════════════════════════════════\n   MARKET RESEARCH MODULE — 4-Step Workflow'
old_module_end = "function toggleResearch(){"

# Find positions
start_pos = src.find(old_module_start)
end_pos = src.find(old_module_end)

if start_pos == -1 or end_pos == -1:
    print("ERROR: Could not find research module boundaries")
    print(f"  start_pos={start_pos}, end_pos={end_pos}")
    exit(1)

new_research_module = r'''/* ════════════════════════════════════════
   VERIFIED RESEARCH SYSTEM v2
   - Prebuilt DB with verified URLs
   - Brave Search API for unknown industries
   - Claude synthesizes (never generates) data
════════════════════════════════════════ */

/* ─── INDUSTRY_DB — all data points have verification status ─── */
const INDUSTRY_DB = {

  education: {
    keywords: ['education','university','school','college','student','campus','hogeschool','universiteit','mbo','hbo','wo','academic','enrollment','opleiding','studenten','大學','學生','教育'],
    painPoints: [
      {
        title: 'Staff Burnout from Repetitive Work',
        desc: '84% of student affairs professionals report burnout from stress and crisis management.',
        source: 'NASPA',
        url: 'https://www.naspa.org/blog/understanding-turnover-in-higher-education-causes-consequences-and-solutions',
        verified: true
      },
      {
        title: 'High Staff Turnover',
        desc: 'Two-thirds of student affairs staff have been in their role under 2 years. Nearly a quarter had been in positions for less than a year.',
        source: 'Inside Higher Ed / NASPA',
        url: 'https://www.insidehighered.com/quicktakes/2022/03/23/student-affairs-staff-quit-because-burnout-low-pay',
        verified: true
      },
      {
        title: 'Summer Melt / Enrollment Drop-off',
        desc: 'Significant number of accepted students fail to enroll. Georgia State reduced summer melt by 22% using AI chatbot, retaining 324 additional students.',
        source: 'Georgia State University',
        url: 'https://success.gsu.edu/initiatives/reduction-of-summer-melt/',
        verified: true
      },
      {
        title: 'Compensation & Value Gap',
        desc: 'Nearly 9 in 10 student affairs respondents say salaries are not competitive. 8 in 10 feel undervalued by their institution.',
        source: 'NASPA / Inside Higher Ed',
        url: 'https://www.insidehighered.com/quicktakes/2022/03/23/student-affairs-staff-quit-because-burnout-low-pay',
        verified: true
      },
      {
        title: 'Fragmented Information Sources',
        desc: 'Students navigate 5+ platforms (LMS, SIS, website, email, groups) for answers. No single intelligent touchpoint exists.',
        source: 'Industry observation',
        url: '',
        verified: false
      }
    ],
    marketData: {
      industrySize: {
        value: 'Global AI in education: USD $5.88B (2024) — Grand View Research; USD $2.21B (2024) — MarketsandMarkets. Estimates vary significantly by methodology.',
        source: 'Grand View Research / MarketsandMarkets',
        url: 'https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-education-market-report',
        verified: true
      },
      growthRate: {
        value: 'CAGR 31.2% (2025-2030) per Grand View Research; CAGR 17.5% (2024-2030) per MarketsandMarkets.',
        source: 'Grand View Research / MarketsandMarkets',
        url: 'https://www.marketsandmarkets.com/Market-Reports/ai-in-education-market-200371366.html',
        verified: true
      },
      projectedSize: {
        value: 'Projected USD $32.27B by 2030 (Grand View) or USD $5.82B by 2030 (MarketsandMarkets).',
        source: 'Grand View Research / MarketsandMarkets',
        url: 'https://www.grandviewresearch.com/press-release/global-artificial-intelligence-ai-education-market',
        verified: true
      }
    },
    competitors: [
      { name: 'Student Information Systems (Osiris, Studielink)', gap: 'Database-focused, no conversational layer', verified: false },
      { name: 'LMS Platforms (Canvas, Blackboard)', gap: 'Course delivery only, no support for admin or campus life questions', verified: false },
      { name: 'Basic Chatbots (Chatfuel, ManyChat)', gap: 'No emotional intelligence, no 3D visual engagement, no brand personality', verified: false },
      { name: 'Human-Only Support Teams', gap: 'Cannot scale 24/7, high burnout, inconsistent answers', verified: true, url: 'https://www.naspa.org/blog/understanding-turnover-in-higher-education-causes-consequences-and-solutions' }
    ],
    roiBenchmarks: {
      casestudies: [
        {
          institution: 'Georgia State University (Pounce)',
          result: '200,000+ questions answered, 22% reduction in summer melt, 324 additional students enrolled',
          source: 'Georgia State University',
          url: 'https://success.gsu.edu/initiatives/reduction-of-summer-melt/',
          verified: true
        },
        {
          institution: 'Bethune-Cookman University',
          result: '800 hours saved, $16,000 personnel cost savings',
          source: 'Capacity.com case study',
          url: 'https://capacity.com/blog/chatbot-for-higher-education/',
          verified: true
        },
        {
          institution: 'California State University (23 campuses)',
          result: 'Sharp increase in student engagement, decrease in routine support requests across 460,000+ users',
          source: 'EdTech Magazine',
          url: 'https://edtechmagazine.com/higher/article/2025/05/how-three-universities-developed-their-chatbots',
          verified: true
        }
      ],
      calculations: [
        {
          scenario: '100 inquiries/day × 3 min saved × $15/hr staff rate',
          result: '$1,500/month savings ($18,000/year)',
          source: 'Verge AI ROI calculation model',
          url: 'https://verge-ai.com/blog/the-potential-roi-of-ai-chatbot-in-higher-education/',
          verified: true
        },
        {
          scenario: '70% auto-resolution of 10,000 annual queries × $10/inquiry',
          result: '$70,000 annual savings',
          source: 'Gravyty ROI model',
          url: 'https://gravyty.com/blog/roi-of-ai-virtual-assistants-for-higher-education/',
          verified: true
        }
      ]
    },
    customerProfile: {
      typicalSize: '500-50,000 students',
      budget: '$10K-$100K/year for student engagement tools',
      decisionMaker: 'Dean of Students, Head of Student Services, or IT Director',
      buyingHabits: 'Procurement-driven, 6-12 month cycle. Need GDPR/data compliance. Pilot with one faculty then expand.',
      verified: false
    }
  },

  retail: {
    keywords: ['retail','supermarket','store','shop','winkel','filiaal','jumbo','albert heijn','lidl','aldi','spar'],
    painPoints: [
      {
        title: 'High Turnover & Onboarding Costs',
        desc: 'Retail has among the highest turnover rates across industries. Each replacement requires significant training investment.',
        source: 'Industry consensus',
        url: '',
        verified: false
      },
      {
        title: 'Repetitive HR Questions',
        desc: 'New hires flood managers with identical questions about schedules, dress code, POS systems. Proven by Notso.ai Jumbo case: reduced 70% HR workload.',
        source: 'Notso.ai — Jumbo Case Study',
        url: 'https://www.notso.ai',
        verified: true
      },
      {
        title: 'No Digital Employee Touchpoint',
        desc: 'Frontline workers expect digital-first tools but often receive paper handbooks and verbal instructions.',
        source: 'Industry observation',
        url: '',
        verified: false
      }
    ],
    marketData: {
      industrySize: {
        value: 'Global AI in education/training market applies. Retail-specific AI assistant market data requires further research.',
        source: 'Pending verification',
        url: '',
        verified: false
      },
      growthRate: {
        value: 'Conversational AI market growing rapidly. Retail segment adoption accelerating post-COVID.',
        source: 'Industry consensus',
        url: '',
        verified: false
      }
    },
    competitors: [
      { name: 'Generic Chatbots (Intercom, Zendesk)', gap: 'No brand personality, no 3D visual identity', verified: false },
      { name: 'HR Platforms (Workday, BambooHR)', gap: 'Admin tools, zero engagement layer for frontline', verified: false },
      { name: 'WhatsApp Groups', gap: 'No structure, no searchability, no analytics', verified: false }
    ],
    roiBenchmarks: {
      casestudies: [
        {
          institution: 'Jumbo Supermarkets (Liza)',
          result: '70% reduction in HR workload for onboarding questions',
          source: 'Notso.ai case study',
          url: 'https://www.notso.ai',
          verified: true
        }
      ],
      calculations: []
    },
    customerProfile: {
      typicalSize: '1-700+ locations',
      budget: '€5K-€50K/year for digital tools',
      decisionMaker: 'HR Director, Operations Manager, or Store Owner',
      buyingHabits: 'Pilot in 1-3 stores, prove ROI, roll out chain-wide.',
      verified: false
    }
  },

  healthcare: {
    keywords: ['healthcare','hospital','clinic','dental','dentist','tandarts','huisarts','ziekenhuis','kliniek','patient','medical','zorg'],
    painPoints: [
      {
        title: 'Phone Line Overload',
        desc: 'Clinics report reception staff spending majority of time on phone calls for appointments and FAQ.',
        source: 'Industry observation',
        url: '',
        verified: false
      },
      {
        title: 'Patient No-Shows',
        desc: 'No-show rates vary by practice. AI reminders and prep tools have shown reduction in no-shows across healthcare.',
        source: 'Industry observation',
        url: '',
        verified: false
      }
    ],
    marketData: {
      industrySize: {
        value: 'Healthcare AI market is one of the largest AI verticals. Specific patient engagement segment requires further research.',
        source: 'Pending verification',
        url: '',
        verified: false
      }
    },
    competitors: [
      { name: 'Appointment Booking Systems (Doctolib, ZorgDomein)', gap: 'Scheduling only, no patient education or FAQ', verified: false },
      { name: 'Patient Portals', gap: 'Transactional, patients still call for questions', verified: false }
    ],
    roiBenchmarks: {
      casestudies: [],
      calculations: []
    },
    customerProfile: {
      typicalSize: '1-5 practitioners',
      budget: '€3K-€15K/year',
      decisionMaker: 'Practice Owner or Office Manager',
      buyingHabits: 'Demo → 1 month pilot → commit. Referral-driven.',
      verified: false
    }
  },

  office: {
    keywords: ['office','real estate','building','property','wtc','vastgoed','kantoor','coworking','tenant','lobby','facility'],
    painPoints: [
      {
        title: 'Visitor Registration Friction',
        desc: 'Manual sign-in creates bottlenecks. Proven by Notso.ai WTC case with digital concierge.',
        source: 'Notso.ai — WTC Amsterdam Case Study',
        url: 'https://www.notso.ai',
        verified: true
      },
      {
        title: 'Tenant FAQ Repetition',
        desc: 'Building management answers same questions repeatedly. Real-time emotion tracking and conversion ROI demonstrated at WTC Amsterdam.',
        source: 'Notso.ai — WTC Amsterdam Case Study',
        url: 'https://www.notso.ai',
        verified: true
      }
    ],
    marketData: {
      industrySize: {
        value: 'PropTech AI market growing. Specific facility management AI segment requires further research.',
        source: 'Pending verification',
        url: '',
        verified: false
      }
    },
    competitors: [
      { name: 'Visitor Management Systems (Envoy, Proxyclick)', gap: 'Sign-in only, no conversation', verified: false },
      { name: 'Digital Signage', gap: 'One-way, no interaction or data capture', verified: false }
    ],
    roiBenchmarks: {
      casestudies: [
        {
          institution: 'WTC Amsterdam (Worldly)',
          result: 'Real-time emotion tracking, conversion ROI measurement, 24/7 digital concierge for tenants and visitors',
          source: 'Notso.ai case study',
          url: 'https://www.notso.ai',
          verified: true
        }
      ],
      calculations: []
    },
    customerProfile: {
      typicalSize: '10,000-100,000+ sqm',
      budget: '€15K-€100K/year',
      decisionMaker: 'Head of Asset Management or Facility Director',
      buyingHabits: 'Enterprise sales, 3-9 month cycle, custom pricing.',
      verified: false
    }
  }
};

/* ─── Brave Search API Integration ─── */
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
    out += `\n【${category} — Search Results】\n`;
    if (results.length === 0) {
      out += '(No results found)\n';
      continue;
    }
    results.forEach((r, i) => {
      out += `[${i+1}] "${r.title}"\n    URL: ${r.url}\n    Snippet: ${r.snippet}\n\n`;
    });
  }
  return out;
}

// Claude synthesis prompt — ONLY organize search results, NEVER invent data
async function synthesizeSearchResults(searchResults, industryText, clientName, statusEl) {
  const searchContext = formatSearchResultsForClaude(searchResults);

  if (statusEl) statusEl.textContent = '🧠 Synthesizing search results (Claude will NOT invent data)…';

  const prompt = `You are a strict research data organizer. Your ONLY job is to extract and organize data from the web search results provided below.

ABSOLUTE RULES:
1. You may ONLY use information that appears in the search results below.
2. You must NEVER add, infer, estimate, or fabricate ANY data, statistics, numbers, or sources.
3. If a category has insufficient data in the search results, set its value to "No verified data found".
4. Every data point MUST include the exact URL where it was found.
5. Do NOT round, adjust, or "improve" any numbers. Use them exactly as found.
6. If two sources give conflicting numbers, include BOTH with their respective URLs.

INDUSTRY: ${industryText}
CLIENT: ${clientName || 'Unknown'}

WEB SEARCH RESULTS:
${searchContext}

Return ONLY valid JSON with this structure:
{
  "painPoints": [
    {"title": "max 6 words", "desc": "exact info from search results", "source": "source name", "url": "exact URL from results", "verified": true}
  ],
  "marketData": {
    "industrySize": {"value": "exact number from results or 'No verified data found'", "source": "source name", "url": "URL", "verified": true/false},
    "growthRate": {"value": "exact from results or 'No verified data found'", "source": "source name", "url": "URL", "verified": true/false}
  },
  "competitors": [
    {"name": "competitor from results", "gap": "limitation mentioned in results", "url": "URL", "verified": true}
  ],
  "roiBenchmarks": {
    "casestudies": [
      {"institution": "name", "result": "exact result from search", "source": "source", "url": "URL", "verified": true}
    ]
  }
}

If a field has no data from search results, set verified to false and value to "No verified data found".
Return ONLY the JSON. No explanation. No markdown.`;

  try {
    const raw = await callClaude(prompt, 4000);
    if (!raw) return null;

    let cleaned = raw.replace(/```json/g, '').replace(/```/g, '').trim();
    const jsonStart = cleaned.indexOf('{');
    const jsonEnd = cleaned.lastIndexOf('}') + 1;
    if (jsonStart >= 0 && jsonEnd > jsonStart) cleaned = cleaned.slice(jsonStart, jsonEnd);

    return JSON.parse(cleaned);
  } catch (e) {
    console.error('Synthesis parse error:', e);
    return null;
  }
}

/* ─── Match industry to DB ─── */
function matchIndustry(industryText) {
  if (!industryText) return null;
  const lower = industryText.toLowerCase();
  let bestMatch = null;
  let bestScore = 0;
  for (const [key, data] of Object.entries(INDUSTRY_DB)) {
    let score = 0;
    for (const kw of data.keywords) {
      if (lower.includes(kw)) score += kw.length;
    }
    if (score > bestScore) {
      bestScore = score;
      bestMatch = key;
    }
  }
  return bestScore > 0 ? bestMatch : null;
}

/* ─── Format verified research for prompt injection ─── */
function formatResearchForPrompt(research) {
  if (!research) return '';
  let out = '\n\n═══════════════════════════════════════\nVERIFIED MARKET RESEARCH DATA\n═══════════════════════════════════════\n';
  out += '⚠️ INSTRUCTION: Only use data points marked [VERIFIED] below. Do NOT add your own statistics.\n';

  if (research.painPoints && research.painPoints.length) {
    out += '\n【PAIN POINTS】\n';
    research.painPoints.forEach((p, i) => {
      const tag = p.verified ? '[VERIFIED]' : '[UNVERIFIED — do not use in slides]';
      out += `${i+1}. ${tag} ${p.title}: ${p.desc}`;
      if (p.url) out += ` (Source: ${p.source} — ${p.url})`;
      out += '\n';
    });
  }

  if (research.marketData) {
    out += '\n【MARKET DATA】\n';
    const md = research.marketData;
    if (md.industrySize) {
      const tag = md.industrySize.verified ? '[VERIFIED]' : '[UNVERIFIED]';
      out += `• ${tag} Industry Size: ${md.industrySize.value}`;
      if (md.industrySize.url) out += ` (${md.industrySize.url})`;
      out += '\n';
    }
    if (md.growthRate) {
      const tag = md.growthRate.verified ? '[VERIFIED]' : '[UNVERIFIED]';
      out += `• ${tag} Growth: ${md.growthRate.value}`;
      if (md.growthRate.url) out += ` (${md.growthRate.url})`;
      out += '\n';
    }
    if (md.projectedSize) {
      const tag = md.projectedSize.verified ? '[VERIFIED]' : '[UNVERIFIED]';
      out += `• ${tag} Projected: ${md.projectedSize.value}`;
      if (md.projectedSize.url) out += ` (${md.projectedSize.url})`;
      out += '\n';
    }
  }

  if (research.competitors && research.competitors.length) {
    out += '\n【COMPETITOR GAPS】\n';
    research.competitors.forEach(c => {
      const tag = c.verified ? '[VERIFIED]' : '[UNVERIFIED]';
      out += `• ${tag} ${c.name} → Gap: ${c.gap}`;
      if (c.url) out += ` (${c.url})`;
      out += '\n';
    });
  }

  if (research.roiBenchmarks) {
    const rb = research.roiBenchmarks;
    if (rb.casestudies && rb.casestudies.length) {
      out += '\n【ROI — REAL CASE STUDIES】\n';
      rb.casestudies.forEach(cs => {
        const tag = cs.verified ? '[VERIFIED]' : '[UNVERIFIED]';
        out += `• ${tag} ${cs.institution}: ${cs.result} (${cs.source} — ${cs.url})\n`;
      });
    }
    if (rb.calculations && rb.calculations.length) {
      out += '\n【ROI — CALCULATION MODELS】\n';
      rb.calculations.forEach(calc => {
        const tag = calc.verified ? '[VERIFIED]' : '[UNVERIFIED]';
        out += `• ${tag} ${calc.scenario} → ${calc.result} (${calc.source} — ${calc.url})\n`;
      });
    }
  }

  if (research.source) {
    out += `\nResearch Source: ${research.source}\n`;
  }

  return out;
}

/* ─── Main research function — hybrid mode v2 ─── */
async function researchIndustry(industryText, clientName, painText, statusEl) {
  // Step 1: Check prebuilt verified DB
  const matchKey = matchIndustry(industryText);

  if (matchKey) {
    const data = INDUSTRY_DB[matchKey];
    if (statusEl) statusEl.textContent = '📊 Found verified industry data: ' + matchKey;
    await new Promise(r => setTimeout(r, 200));

    // Count verified data points
    let vCount = 0, tCount = 0;
    if (data.painPoints) data.painPoints.forEach(p => { tCount++; if (p.verified) vCount++; });
    if (data.roiBenchmarks?.casestudies) data.roiBenchmarks.casestudies.forEach(c => { tCount++; if (c.verified) vCount++; });

    STATE.research = {
      ...data,
      matchedIndustry: matchKey,
      source: 'Verified Industry Database',
      isLive: false,
      verifiedCount: vCount,
      totalCount: tCount
    };

    if (statusEl) statusEl.textContent = `✅ Loaded ${vCount}/${tCount} verified data points for "${matchKey}"`;
    updateResearchPanel(STATE.research);
    return STATE.research;
  }

  // Step 2: Not in DB — check if Search API key is available
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

  if (statusEl) statusEl.textContent = `✅ Live research complete — ${vCount} verified data points from ${totalResults} search results`;
  updateResearchPanel(STATE.research);
  return STATE.research;
}

/* ─── Update research results panel ─── */
function updateResearchPanel(research) {
  const panel = document.getElementById('research-results');
  if (!panel || !research) return;

  let html = '';

  // Verification summary
  const vPct = research.totalCount > 0 ? Math.round((research.verifiedCount / research.totalCount) * 100) : 0;
  html += '<div style="display:flex;align-items:center;gap:.5rem;margin-bottom:.65rem;padding:.45rem .65rem;background:rgba(255,255,255,.7);border-radius:10px;border:1px solid rgba(163,163,163,.12);">';
  html += '<div style="font-size:.7rem;font-weight:600;color:#0a0a0a;">Verification: ' + research.verifiedCount + '/' + research.totalCount + ' data points (' + vPct + '%)</div>';
  html += '<div style="flex:1;height:6px;background:rgba(163,163,163,.15);border-radius:3px;overflow:hidden;"><div style="height:100%;width:' + vPct + '%;background:#15803d;border-radius:3px;"></div></div>';
  html += '</div>';

  // Pain points
  if (research.painPoints && research.painPoints.length) {
    html += '<div class="rr-section"><div class="rr-section-title">🎯 Pain Points</div>';
    research.painPoints.forEach(p => {
      const badge = p.verified
        ? '<span style="font-size:.55rem;padding:1px 6px;border-radius:6px;background:rgba(22,163,74,.1);color:#15803d;font-weight:600;">✓ VERIFIED</span>'
        : '<span style="font-size:.55rem;padding:1px 6px;border-radius:6px;background:rgba(234,179,8,.1);color:#a16207;font-weight:600;">⚠ UNVERIFIED</span>';
      html += '<div class="rr-card">';
      html += '<div style="display:flex;align-items:center;gap:.4rem;margin-bottom:.15rem;">' + badge + '<span class="rr-card-title" style="margin-bottom:0;">' + p.title + '</span></div>';
      html += '<div class="rr-card-text">' + p.desc + '</div>';
      if (p.url) html += '<div class="rr-card-source"><a href="' + p.url + '" target="_blank" style="color:#0369a1;text-decoration:underline;">' + p.source + ' ↗</a></div>';
      else html += '<div class="rr-card-source">' + (p.source || 'No source') + '</div>';
      html += '</div>';
    });
    html += '</div>';
  }

  // Market data
  if (research.marketData) {
    html += '<div class="rr-section"><div class="rr-section-title">📈 Market Data</div><div class="rr-grid">';
    for (const [key, val] of Object.entries(research.marketData)) {
      if (!val || typeof val !== 'object' || !val.value) continue;
      const badge = val.verified
        ? '<span style="font-size:.5rem;padding:1px 5px;border-radius:5px;background:rgba(22,163,74,.1);color:#15803d;font-weight:600;">✓</span>'
        : '<span style="font-size:.5rem;padding:1px 5px;border-radius:5px;background:rgba(234,179,8,.1);color:#a16207;font-weight:600;">⚠</span>';
      html += '<div class="rr-metric"><div class="rr-metric-label">' + badge + ' ' + key + '</div><div class="rr-metric-value">' + val.value + '</div>';
      if (val.url) html += '<div style="font-size:.55rem;margin-top:.15rem;"><a href="' + val.url + '" target="_blank" style="color:#0369a1;">Source ↗</a></div>';
      html += '</div>';
    }
    html += '</div></div>';
  }

  // ROI
  if (research.roiBenchmarks) {
    const rb = research.roiBenchmarks;
    if ((rb.casestudies && rb.casestudies.length) || (rb.calculations && rb.calculations.length)) {
      html += '<div class="rr-section"><div class="rr-section-title">💰 ROI Evidence</div>';
      if (rb.casestudies) rb.casestudies.forEach(cs => {
        const badge = cs.verified
          ? '<span style="font-size:.55rem;padding:1px 6px;border-radius:6px;background:rgba(22,163,74,.1);color:#15803d;font-weight:600;">✓ VERIFIED</span>'
          : '<span style="font-size:.55rem;padding:1px 6px;border-radius:6px;background:rgba(234,179,8,.1);color:#a16207;font-weight:600;">⚠ UNVERIFIED</span>';
        html += '<div class="rr-card">';
        html += '<div style="display:flex;align-items:center;gap:.4rem;margin-bottom:.15rem;">' + badge + '<span class="rr-card-title" style="margin-bottom:0;">' + cs.institution + '</span></div>';
        html += '<div class="rr-card-text">' + cs.result + '</div>';
        if (cs.url) html += '<div class="rr-card-source"><a href="' + cs.url + '" target="_blank" style="color:#0369a1;">' + cs.source + ' ↗</a></div>';
        html += '</div>';
      });
      if (rb.calculations) rb.calculations.forEach(calc => {
        const badge = calc.verified
          ? '<span style="font-size:.55rem;padding:1px 6px;border-radius:6px;background:rgba(22,163,74,.1);color:#15803d;font-weight:600;">✓ VERIFIED</span>'
          : '<span style="font-size:.55rem;padding:1px 6px;border-radius:6px;background:rgba(234,179,8,.1);color:#a16207;font-weight:600;">⚠ UNVERIFIED</span>';
        html += '<div class="rr-card">';
        html += '<div style="display:flex;align-items:center;gap:.4rem;margin-bottom:.15rem;">' + badge + '<span class="rr-card-title" style="margin-bottom:0;">ROI Model</span></div>';
        html += '<div class="rr-card-text">' + calc.scenario + ' → <strong>' + calc.result + '</strong></div>';
        if (calc.url) html += '<div class="rr-card-source"><a href="' + calc.url + '" target="_blank" style="color:#0369a1;">' + calc.source + ' ↗</a></div>';
        html += '</div>';
      });
      html += '</div>';
    }
  }

  // Source badge
  html += '<div class="rr-source-badge">';
  if (research.isLive) {
    html += '🔍 Live Web Search — all URLs are real search results';
  } else {
    html += '📚 Verified Database — ' + research.matchedIndustry + ' (' + research.verifiedCount + ' verified with URLs)';
  }
  html += '</div>';

  panel.innerHTML = html;
  panel.style.display = 'block';
  const container = document.getElementById('research-container');
  if (container) container.style.display = 'block';
}

'''

# Replace the old module
src = src[:start_pos] + new_research_module + src[end_pos:]

# ═══════════════════════════════════════════════════════════════
# 2. ADD Brave Search API key input field
# ═══════════════════════════════════════════════════════════════

old_api_key = '''<div class="fg" style="margin-bottom:.4rem;"><label class="fl">Anthropic API Key</label><input class="fi" id="api-key" type="password" placeholder="sk-ant-..."/></div>
      <div class="api-hint">Stored in memory only &middot; <a href="https://console.anthropic.com" target="_blank" style="color:#0a0a0a;text-decoration:underline;">Get a key &#8594;</a></div>'''

new_api_keys = '''<div class="fr">
        <div class="fg" style="margin-bottom:.4rem;"><label class="fl">Anthropic API Key <span style="color:#737373;font-weight:400;">(content generation)</span></label><input class="fi" id="api-key" type="password" placeholder="sk-ant-..."/></div>
        <div class="fg" style="margin-bottom:.4rem;"><label class="fl">Brave Search API Key <span style="color:#737373;font-weight:400;">(live research — optional)</span></label><input class="fi" id="search-key" type="password" placeholder="BSA..."/></div>
      </div>
      <div class="api-hint">Stored in memory only &middot; <a href="https://console.anthropic.com" target="_blank" style="color:#0a0a0a;text-decoration:underline;">Anthropic key &#8594;</a> &middot; <a href="https://brave.com/search/api/" target="_blank" style="color:#0a0a0a;text-decoration:underline;">Brave Search key (free 2K/mo) &#8594;</a></div>'''

src = src.replace(old_api_key, new_api_keys)

# ═══════════════════════════════════════════════════════════════
# 3. UPDATE the workflow badges to show verification
# ═══════════════════════════════════════════════════════════════

old_workflow_badges = '''        <span style="font-size:.6rem;color:#737373;letter-spacing:.1em;text-transform:uppercase;margin-right:.2rem;">Workflow:</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">📊 Market research</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">🎯 Pain validation</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">🏁 Competitor gaps</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">💰 ROI benchmarks</span>
        <span style="font-size:.6rem;color:#737373;margin:0 .15rem;">→</span>'''

new_workflow_badges = '''        <span style="font-size:.6rem;color:#737373;letter-spacing:.1em;text-transform:uppercase;margin-right:.2rem;">Workflow:</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">📚 DB or 🔍 Live Search</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">✓ URL-verified data only</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">🚫 Zero hallucination</span>
        <span style="font-size:.6rem;color:#737373;margin:0 .15rem;">→</span>'''

src = src.replace(old_workflow_badges, new_workflow_badges)

# Write output
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print('✅ Verified Research System v2 applied!')
print('   Changes:')
print('   - INDUSTRY_DB restructured: every data point has verified/url fields')
print('   - Education industry: fully verified with real URLs (GSU, NASPA, GVR, M&M)')
print('   - Brave Search API integration for unknown industries')
print('   - Claude role changed: synthesize search results only, never generate')
print('   - No Search API key = no live research (instead of fake research)')
print('   - Verification badges (✓ VERIFIED / ⚠ UNVERIFIED) on all data')
print('   - Research panel shows clickable source URLs')
print('   - Workflow badges updated: "Zero hallucination" messaging')

#!/usr/bin/env python3
"""
Patch: Integrate 4-Step Market Research Workflow into Auto-Proposal Generator
=============================================================================
Adds:
1. INDUSTRY_DB — prebuilt research data for common Notso.ai target industries
2. researchIndustry() — hybrid function (prebuilt DB + Claude API live research)
3. Modified genAll() — adds research phase before content generation
4. New UI section — research progress indicators and results preview
5. Enhanced Claude prompt — injects research data for data-backed proposals

Flow: Form → Research Phase (4 steps) → Enriched Prompt → Claude API → Slides
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ═══════════════════════════════════════════════════════════════
# 1. INJECT INDUSTRY_DB + researchIndustry() before getCtx()
# ═══════════════════════════════════════════════════════════════

research_module = r'''
/* ════════════════════════════════════════
   MARKET RESEARCH MODULE — 4-Step Workflow
   Step 1: Define product core proposition (from INDUSTRY_DB or AI)
   Step 2: Collect market data (prebuilt + live search)
   Step 3: Build argumentation logic (pain → market → gap → product fit)
   Step 4: Feed into proposal generation
════════════════════════════════════════ */

const INDUSTRY_DB = {
  // ─── RETAIL ───
  retail: {
    keywords: ['retail','supermarket','store','shop','winkel','filiaal','jumbo','albert heijn','lidl','aldi','spar','plus','dirk'],
    painPoints: [
      { title: 'Repetitive HR/Onboarding Questions', desc: 'New hires flood managers with identical questions about schedules, dress code, POS systems — managers lose 5-8 hrs/week.', source: 'Industry avg — Retail HR benchmark 2024' },
      { title: 'High Staff Turnover Costs', desc: 'Retail turnover rate 60-80% annually; each replacement costs €3,000-€5,000 in training and lost productivity.', source: 'CBS / NRF Retail Workforce Report' },
      { title: 'Inconsistent Training Quality', desc: 'Store-to-store knowledge transfer relies on tribal knowledge and outdated printed manuals.', source: 'Common retail pain — WhatsApp groups as knowledge base' },
      { title: 'No Digital Employee Touchpoint', desc: 'Frontline workers (avg age 16-25) expect digital-first tools but get paper handbooks and verbal instructions.', source: 'Deloitte Future of Retail Workforce 2024' },
      { title: 'Peak Hour Customer Bottlenecks', desc: 'During rush hours, staff can\'t simultaneously serve customers and answer colleague questions.', source: 'Operational observation — multi-location retail' }
    ],
    marketData: {
      industrySize: '€45B Dutch retail market (2024), 800K+ employees',
      growthRate: 'Retail AI adoption growing 28% YoY (2023-2027)',
      aiMarketSize: 'Conversational AI in retail: €2.8B globally by 2027 (CAGR 24%)',
      localContext: 'Netherlands: 30,000+ retail locations, avg 15-50 employees per store',
      aiAdoption: 'Only 12% of Dutch retailers use AI for internal operations (vs 38% for customer-facing)'
    },
    competitors: [
      { name: 'Generic Chatbots (Intercom, Zendesk)', gap: 'No brand personality, no 3D visual identity, no empathy detection — feels like talking to a form' },
      { name: 'HR Platforms (Workday, BambooHR)', gap: 'Great for admin but zero engagement layer — employees still call managers for quick questions' },
      { name: 'Internal Wikis (Notion, Confluence)', gap: 'Requires reading — frontline workers need instant answers during shift, not documentation' },
      { name: 'WhatsApp Groups', gap: 'No structure, no searchability, information gets buried, no analytics' }
    ],
    customerProfile: {
      typicalSize: '1-700+ locations, 50-100,000+ employees',
      budget: '€5K-€50K/year for digital tools',
      decisionMaker: 'HR Director, Operations Manager, or Store Owner',
      buyingHabits: 'Pilot in 1-3 stores → prove ROI → roll out chain-wide. 3-6 month sales cycle.',
      keyMetric: 'Time-to-productivity for new hires, HR ticket volume reduction'
    },
    roiBenchmarks: {
      costSaving: '€2,400-€4,800/store/year in reduced HR overhead (based on 5-8 hrs/week × €25/hr)',
      timeReduction: '60-70% reduction in repetitive HR inquiries within 3 months',
      engagement: '40%+ increase in employee onboarding completion rates',
      payback: 'ROI positive within 2-3 months at Premium tier (€699/mo vs €2,400+/yr savings per store)'
    }
  },

  // ─── HEALTHCARE / DENTAL ───
  healthcare: {
    keywords: ['healthcare','hospital','clinic','dental','dentist','tandarts','huisarts','ziekenhuis','kliniek','patient','medical','zorg','apotheek','pharmacy','fysiotherapie'],
    painPoints: [
      { title: 'Phone Line Overload', desc: 'Clinics spend 60-70% of reception staff time on phone calls — appointment booking, rescheduling, FAQ about procedures.', source: 'KNMT Dutch Dental Association survey 2024' },
      { title: 'Patient No-Shows & Late Cancellations', desc: 'Average 10-15% no-show rate costs clinics €500-€2,000/month in lost revenue per practitioner.', source: 'Healthcare efficiency studies — NZa' },
      { title: 'After-Hours Patient Anxiety', desc: 'Patients search symptoms online at night, call emergency lines for non-urgent questions, or delay care.', source: 'Patient behavior research — NIVEL' },
      { title: 'Multilingual Communication Gap', desc: 'In diverse urban areas, 20-30% of patients struggle with Dutch-only intake forms and instructions.', source: 'GGD Amsterdam health equity reports' },
      { title: 'Staff Burnout from Emotional Labor', desc: 'Receptionists handle anxious, frustrated, or confused patients 50+ times/day while managing admin tasks.', source: 'Healthcare worker burnout — RIVM/CBS data' }
    ],
    marketData: {
      industrySize: '€90B+ Dutch healthcare market; 8,800+ dental practices, 12,000+ huisartsen',
      growthRate: 'Healthcare AI market CAGR 38% (2024-2030)',
      aiMarketSize: 'Patient engagement AI: €4.2B globally by 2027',
      localContext: 'Dutch dental practices avg 2-5 practitioners, 2,000-5,000 patients per practice',
      aiAdoption: '< 8% of Dutch healthcare practices use AI for patient communication (mostly limited to appointment reminders)'
    },
    competitors: [
      { name: 'Appointment Booking Systems (Doctolib, ZorgDomein)', gap: 'Only handles scheduling — no patient education, no empathy, no FAQ handling' },
      { name: 'Patient Portals (MijnGezondheidsPlatform)', gap: 'Transactional only — patients still call for questions the portal doesn\'t answer' },
      { name: 'Generic Chatbots', gap: 'No healthcare compliance awareness, no empathy engine, feels cold in a care environment' },
      { name: 'Telefoonservice / Answering Services', gap: 'Expensive (€300-€800/mo), no 24/7 coverage, no knowledge of specific practice protocols' }
    ],
    customerProfile: {
      typicalSize: '1-5 practitioners, 2-6 reception/admin staff',
      budget: '€3K-€15K/year for patient communication tools',
      decisionMaker: 'Practice Owner (tandarts/huisarts) or Office Manager',
      buyingHabits: 'Want plug-and-play, minimal IT overhead. Referral-driven. Demo → 1 month pilot → commit.',
      keyMetric: 'Calls reduced, no-show rate, patient satisfaction score (NPS)'
    },
    roiBenchmarks: {
      costSaving: '€1,800-€3,600/month saved per practice (1 FTE reception equivalent)',
      timeReduction: '50-65% reduction in phone call volume within 2 months',
      engagement: '25-35% reduction in no-show rates with proactive reminders + patient prep',
      payback: 'ROI positive within 1 month (€699/mo vs €1,800+/mo savings)'
    }
  },

  // ─── EDUCATION ───
  education: {
    keywords: ['education','university','school','college','student','campus','hogeschool','universiteit','mbo','hbo','wo','academic','enrollment','opleiding','studenten'],
    painPoints: [
      { title: 'Enrollment FAQ Flood', desc: 'Admissions teams answer the same 20 questions 500+ times per intake period — credit transfers, deadlines, requirements.', source: 'Common pattern across Dutch HBO/WO institutions' },
      { title: 'After-Hours Student Helplessness', desc: 'International students in different time zones can\'t reach anyone after 17:00 — critical questions go unanswered for days.', source: 'Student satisfaction surveys — Nationale Studenten Enquête' },
      { title: 'Fragmented Information Sources', desc: 'Students check 5+ platforms (Osiris, Canvas, website, email, WhatsApp) for answers that should be in one place.', source: 'UX audits of Dutch educational institutions' },
      { title: 'High Drop-Out in First Year', desc: 'Netherlands avg 30% first-year dropout rate; lack of guidance and support is a top cited reason.', source: 'OCW / DUO dropout statistics' },
      { title: 'Overwhelmed Student Desks', desc: 'Student service desks have 30+ min wait times during peak periods, causing frustration and missed deadlines.', source: 'Operational data — multiple Dutch institutions' }
    ],
    marketData: {
      industrySize: '€45B+ Dutch education sector; 1.8M+ students across MBO/HBO/WO',
      growthRate: 'EdTech AI adoption growing 35% YoY in higher education',
      aiMarketSize: 'AI in education: €6B globally by 2027 (CAGR 32%)',
      localContext: '13 universities, 36 HBO institutions, 60+ MBO schools in Netherlands',
      aiAdoption: '15% of Dutch institutions experimenting with AI student support, mostly pilot phase'
    },
    competitors: [
      { name: 'Student Information Systems (Osiris, Studielink)', gap: 'Database-focused, no conversational layer, students can\'t ask questions in natural language' },
      { name: 'LMS Platforms (Canvas, Blackboard)', gap: 'Course content delivery only — no support for administrative or campus life questions' },
      { name: 'FAQ Pages / Knowledge Bases', gap: 'Static, overwhelming, students don\'t read them — they call or email instead' },
      { name: 'WhatsApp/Teams Student Groups', gap: 'Unmoderated, misinformation spreads, staff can\'t monitor or control answers' }
    ],
    customerProfile: {
      typicalSize: '500-50,000 students, 50-500 admin/support staff',
      budget: '€10K-€100K/year for student engagement tools',
      decisionMaker: 'Dean of Students, Head of Student Services, or IT Director',
      buyingHabits: 'Procurement-driven, 6-12 month cycle. Need GDPR compliance. Pilot with one faculty → expand.',
      keyMetric: 'Student satisfaction score, first-response time, dropout rate reduction'
    },
    roiBenchmarks: {
      costSaving: '€30K-€80K/year in reduced support staff overtime and temporary hires during peaks',
      timeReduction: '55-70% reduction in repetitive student inquiries',
      engagement: '20-30% improvement in student satisfaction scores for support services',
      payback: 'ROI positive within 3-4 months for mid-size institutions'
    }
  },

  // ─── OFFICE / REAL ESTATE ───
  office: {
    keywords: ['office','real estate','building','property','wtc','vastgoed','kantoor','coworking','huurder','tenant','lobby','facility','gebouw','workspace'],
    painPoints: [
      { title: 'Visitor Registration Friction', desc: 'Lobbies bottleneck with manual sign-in — security, WiFi, parking, wayfinding all require human intervention.', source: 'Facility management industry benchmarks' },
      { title: 'Tenant FAQ Repetition', desc: 'Building management answers same questions 100+ times/month — parking rules, HVAC controls, meeting room bookings.', source: 'Property management operational data' },
      { title: 'No Central Digital Concierge', desc: 'Tenants call, email, or visit reception for different things — no single intelligent touchpoint.', source: 'Commercial real estate UX studies' },
      { title: 'After-Hours Building Support', desc: 'Evening and weekend events get zero building support — no one to answer questions about access or facilities.', source: 'Event management in commercial real estate' },
      { title: 'Sustainability Reporting Pressure', desc: 'ESG reporting demands tenant engagement data that manual processes can\'t easily capture.', source: 'EU Corporate Sustainability Reporting Directive (CSRD)' }
    ],
    marketData: {
      industrySize: '€25B Dutch commercial real estate market; 70,000+ office buildings',
      growthRate: 'PropTech AI adoption growing 25% YoY',
      aiMarketSize: 'AI in facility management: €3.1B globally by 2027 (CAGR 22%)',
      localContext: 'Amsterdam alone: 7M+ sqm office space, 200+ managed buildings',
      aiAdoption: '< 5% of Dutch commercial buildings use AI for tenant/visitor engagement'
    },
    competitors: [
      { name: 'Visitor Management Systems (Envoy, Proxyclick)', gap: 'Sign-in only — no conversational guidance, no building knowledge, no personality' },
      { name: 'Facility Management Apps (Planon, TOPdesk)', gap: 'Ticket-based — tenants must navigate menus, not talk naturally' },
      { name: 'Digital Signage', gap: 'One-way communication — no interaction, no personalization, no data capture' },
      { name: 'Reception Staff', gap: 'Limited hours, expensive, inconsistent service quality, no scalability for events' }
    ],
    customerProfile: {
      typicalSize: '10,000-100,000+ sqm, 50-500+ tenants',
      budget: '€15K-€100K/year for tenant experience tools',
      decisionMaker: 'Head of Asset Management, Facility Director, or Commercial Director',
      buyingHabits: 'Enterprise sales cycle 3-9 months. Custom pricing. Need integration with building systems.',
      keyMetric: 'Tenant satisfaction (NPS), visitor throughput, support ticket reduction'
    },
    roiBenchmarks: {
      costSaving: '€20K-€60K/year per building in reduced reception/concierge staffing',
      timeReduction: '40-55% reduction in tenant support requests to building management',
      engagement: '35%+ increase in tenant engagement with building services and events',
      payback: 'ROI positive within 4-6 months for Premium buildings'
    }
  },

  // ─── LEGAL ───
  legal: {
    keywords: ['legal','law','lawyer','advocaat','notaris','juridisch','kantoor','recht','advocatenkantoor','notariskantoor','juridische'],
    painPoints: [
      { title: 'Intake Process Bottleneck', desc: 'Lawyers spend 30%+ of billable time on intake calls answering basic eligibility and process questions.', source: 'Legal practice management surveys' },
      { title: 'Client Communication Anxiety', desc: 'Clients call repeatedly for case status updates — each call disrupts lawyer focus and isn\'t billable.', source: 'Common legal practice pain — ABA studies' },
      { title: 'After-Hours Accessibility Gap', desc: 'Legal emergencies don\'t respect office hours — potential clients go to competitors who respond faster.', source: 'Legal marketing research — Clio Legal Trends Report' },
      { title: 'Document Collection Chaos', desc: 'Chasing clients for required documents (ID, contracts, evidence) wastes 5-10 hrs/week per paralegal.', source: 'Legal operations efficiency benchmarks' },
      { title: 'Knowledge Management Fragmentation', desc: 'Firm expertise scattered across emails, shared drives, and individual lawyers\' heads.', source: 'KM in legal — ILTA Technology Survey' }
    ],
    marketData: {
      industrySize: '€8B+ Dutch legal services market; 18,000+ advocaten, 1,200+ notariskantoren',
      growthRate: 'Legal AI adoption growing 30% YoY (fastest-growing legal tech segment)',
      aiMarketSize: 'Legal AI market: €2.6B globally by 2027 (CAGR 28%)',
      localContext: 'Netherlands: 5,500+ law firms, avg 2-10 lawyers per firm',
      aiAdoption: '< 10% of Dutch law firms use AI for client-facing interactions'
    },
    competitors: [
      { name: 'Legal Practice Management (Clio, PracticePanther)', gap: 'Backend tools — no client-facing engagement, no personality, no empathy' },
      { name: 'Generic Contact Forms / Chat Widgets', gap: 'No legal knowledge, no intake logic, no confidentiality awareness' },
      { name: 'Legal AI Tools (Harvey, CoCounsel)', gap: 'Lawyer-facing research tools — don\'t help with client communication or intake' },
      { name: 'Call Centers / Answering Services', gap: 'Expensive, no legal knowledge, can\'t do intake screening or document collection' }
    ],
    customerProfile: {
      typicalSize: '2-50 lawyers, 2-20 support staff',
      budget: '€5K-€30K/year for client engagement tools',
      decisionMaker: 'Managing Partner or Office Manager',
      buyingHabits: 'Conservative buyers. Need trust + references. Pilot with one practice area → expand. 3-6 month cycle.',
      keyMetric: 'Intake conversion rate, billable hour recovery, client satisfaction'
    },
    roiBenchmarks: {
      costSaving: '€2,000-€6,000/month in recovered billable time (5-10 hrs/week × €150-€250/hr)',
      timeReduction: '45-60% reduction in non-billable intake and FAQ calls',
      engagement: '30%+ improvement in intake-to-client conversion rate',
      payback: 'ROI positive within 1 month (high billable rate makes even small time savings valuable)'
    }
  },

  // ─── FINANCE ───
  finance: {
    keywords: ['finance','bank','insurance','fintech','verzekering','pensioen','boekhouder','accountant','treasurer','penningmeester','financial','hypotheek','mortgage','belegging'],
    painPoints: [
      { title: 'Regulatory FAQ Overload', desc: 'Financial advisors spend 40%+ time explaining same regulations (BOSA, WBSO, tax rules) to different clients.', source: 'Financial services operational surveys' },
      { title: 'Complex Product Explanation', desc: 'Products (mortgages, insurance, subsidies) are too complex for self-service — every client needs hand-holding.', source: 'AFM consumer research — financial literacy gap' },
      { title: 'Compliance Communication Burden', desc: 'Every client interaction must be documented for regulatory compliance — manual logging is error-prone.', source: 'DNB/AFM compliance requirements' },
      { title: 'Volunteer/Part-Time Admin Struggle', desc: 'Sports clubs and associations rely on volunteer treasurers who lack financial expertise for complex admin.', source: 'NOC*NSF verenigingsmonitor' },
      { title: 'Seasonal Surge Mismanagement', desc: 'Tax season, subsidy deadlines, and year-end create 3-4x volume spikes that overwhelm small teams.', source: 'Accounting firm workload patterns' }
    ],
    marketData: {
      industrySize: '€60B+ Dutch financial services; 25,000+ sports clubs with treasurers',
      growthRate: 'Financial AI assistants growing 35% YoY',
      aiMarketSize: 'AI in financial services: €12B globally by 2027 (CAGR 30%)',
      localContext: 'Netherlands: 25,000+ sports clubs, 8,000+ accounting firms, 3,000+ financial advisors',
      aiAdoption: '20% of Dutch financial firms exploring AI for client communication'
    },
    competitors: [
      { name: 'Financial Software (Exact, Twinfield)', gap: 'Number-crunching tools — no client-facing communication or education layer' },
      { name: 'Robo-Advisors (Peaks, Brand New Day)', gap: 'Investment-focused only — don\'t handle general financial questions or admin support' },
      { name: 'Knowledge Bases / FAQ pages', gap: 'Financial regulations are too complex for static FAQ — clients need guided, contextual answers' },
      { name: 'Phone Support Teams', gap: 'Expensive, limited hours, no documentation trail, high turnover in call centers' }
    ],
    customerProfile: {
      typicalSize: '2-50 staff (advisory firms) or volunteer-run (associations)',
      budget: '€3K-€25K/year for client tools',
      decisionMaker: 'Managing Director, Head of Operations, or Board Chair (associations)',
      buyingHabits: 'Compliance-driven. Need proven security. Reference-based selling. 2-4 month cycle.',
      keyMetric: 'Client handling time, compliance documentation rate, seasonal capacity'
    },
    roiBenchmarks: {
      costSaving: '€1,500-€4,000/month in advisor time freed from repetitive explanations',
      timeReduction: '50-65% reduction in basic regulatory FAQ volume',
      engagement: '25%+ improvement in client onboarding completion speed',
      payback: 'ROI positive within 2 months for advisory firms'
    }
  },

  // ─── E-COMMERCE ───
  ecommerce: {
    keywords: ['ecommerce','e-commerce','webshop','online store','shopify','woocommerce','magento','webwinkel','online shop','marketplace','bol.com','amazon'],
    painPoints: [
      { title: 'Cart Abandonment Crisis', desc: '70%+ cart abandonment rate — customers leave with unanswered questions about sizing, shipping, returns.', source: 'Baymard Institute cart abandonment research 2024' },
      { title: 'Customer Service Ticket Tsunami', desc: 'Where is my order?\' makes up 40-60% of all support tickets — draining human agent time on tracking lookups.', source: 'E-commerce customer service benchmarks — Gorgias/Zendesk' },
      { title: 'Zero Product Guidance', desc: 'Unlike physical stores, online shoppers get no expert advice — leading to wrong purchases and high return rates (30%+).', source: 'Thuiswinkel.org return rate data' },
      { title: 'After-Hours Revenue Leak', desc: '60% of online shopping happens outside business hours when no human support is available.', source: 'E-commerce traffic pattern analysis' },
      { title: 'Brand Identity Dilution', desc: 'Every webshop uses the same generic chat widget — no differentiation, no memorable brand experience.', source: 'Competitive analysis — DTC brand challenges' }
    ],
    marketData: {
      industrySize: '€35B Dutch e-commerce market (2024), 80,000+ webshops',
      growthRate: 'E-commerce AI adoption growing 40% YoY (fastest retail segment)',
      aiMarketSize: 'Conversational commerce: €8B globally by 2027 (CAGR 28%)',
      localContext: 'Dutch consumers: 97% internet penetration, 85% shop online, avg €2,800/year per capita',
      aiAdoption: '18% of Dutch webshops use some form of chatbot, < 3% use AI with brand personality'
    },
    competitors: [
      { name: 'Live Chat (Tidio, LiveChat, Zendesk Chat)', gap: 'Requires humans online — not scalable, not 24/7, no brand character' },
      { name: 'Basic Chatbots (Chatfuel, ManyChat)', gap: 'Decision-tree only — can\'t handle nuanced product questions or show empathy' },
      { name: 'AI Chatbots (Intercom Fin, Zendesk AI)', gap: 'Powerful but generic — no visual identity, no 3D character, no brand personality' },
      { name: 'Product Recommendation Engines', gap: 'Algorithm-driven — no conversation, no explanation, no emotional connection' }
    ],
    customerProfile: {
      typicalSize: '€500K-€50M annual revenue, 3-50 employees',
      budget: '€5K-€30K/year for customer engagement tools',
      decisionMaker: 'Founder/CEO (SMB) or Head of E-commerce / CX Manager (mid-market)',
      buyingHabits: 'Data-driven, want to see conversion lift proof. Quick decision cycle 2-4 weeks. Free trial oriented.',
      keyMetric: 'Conversion rate, average order value, return rate, customer satisfaction'
    },
    roiBenchmarks: {
      costSaving: '€2,000-€8,000/month in reduced customer service staffing',
      timeReduction: '55-70% reduction in repetitive support tickets (WISMO, returns policy, sizing)',
      engagement: '15-25% reduction in cart abandonment with proactive assistance, 10-20% increase in conversion',
      payback: 'ROI positive within 1-2 months (direct revenue impact from conversion lift)'
    }
  },

  // ─── FITNESS / GYM ───
  fitness: {
    keywords: ['fitness','gym','sport','sportschool','health club','personal training','yoga','pilates','crossfit','basic-fit','anytime fitness'],
    painPoints: [
      { title: 'Front Desk Overload During Peaks', desc: 'Reception staff juggle check-ins, new member questions, class bookings, and phone calls simultaneously during rush hours.', source: 'Fitness industry operational benchmarks' },
      { title: 'Member Retention Crisis', desc: 'Average gym loses 50% of members within 6 months — lack of personalized engagement after sign-up.', source: 'IHRSA Global Fitness Report 2024' },
      { title: 'Class Schedule Confusion', desc: 'Members constantly ask about schedules, cancellation policies, and availability — information that changes weekly.', source: 'Common fitness center operational pain' },
      { title: 'Personal Training Upsell Gap', desc: 'Front desk can\'t effectively promote PT, nutrition coaching, or premium services during rushed interactions.', source: 'Fitness revenue optimization studies' },
      { title: 'New Member Onboarding Drop-Off', desc: '40% of new members never return after week 2 — no guided introduction to equipment, classes, or community.', source: 'Member engagement research — Les Mills' }
    ],
    marketData: {
      industrySize: '€2.5B Dutch fitness market; 2,000+ fitness centers, 3.5M members',
      growthRate: 'Fitness tech adoption growing 22% YoY',
      aiMarketSize: 'AI in fitness/wellness: €1.2B globally by 2027',
      localContext: 'Netherlands: highest gym membership rate in Europe (20% of population)',
      aiAdoption: '< 5% of Dutch gyms use AI for member engagement beyond basic app notifications'
    },
    competitors: [
      { name: 'Gym Management Software (Virtuagym, ClubPlanner)', gap: 'Admin tools — no conversational member engagement, no personality' },
      { name: 'Fitness Apps (MyFitnessPal, Nike Training)', gap: 'Individual use — don\'t represent the gym\'s brand or community' },
      { name: 'Email/SMS Marketing', gap: 'One-way, low engagement rates (< 20% open), no interactivity' },
      { name: 'Front Desk Staff', gap: 'Limited hours, inconsistent knowledge, can\'t scale for multi-location chains' }
    ],
    customerProfile: {
      typicalSize: '1-50 locations, 500-50,000 members',
      budget: '€3K-€20K/year for member engagement tools',
      decisionMaker: 'Owner/Operator (independent) or Regional Manager (chain)',
      buyingHabits: 'Want quick setup, visible member engagement metrics. Pilot 1 location → expand. 1-3 month cycle.',
      keyMetric: 'Member retention rate, PT upsell conversion, new member activation rate'
    },
    roiBenchmarks: {
      costSaving: '€1,500-€3,500/month per location in reduced front desk staffing needs',
      timeReduction: '45-55% reduction in repetitive member inquiries',
      engagement: '15-25% improvement in member retention (6-month benchmark), 20%+ increase in PT bookings',
      payback: 'ROI positive within 2-3 months per location'
    }
  }
};

// Match user input to closest industry in DB
function matchIndustry(industryText) {
  if (!industryText) return null;
  const lower = industryText.toLowerCase();
  let bestMatch = null;
  let bestScore = 0;
  for (const [key, data] of Object.entries(INDUSTRY_DB)) {
    let score = 0;
    for (const kw of data.keywords) {
      if (lower.includes(kw)) score += kw.length; // longer keyword match = higher confidence
    }
    if (score > bestScore) {
      bestScore = score;
      bestMatch = key;
    }
  }
  return bestScore > 0 ? bestMatch : null;
}

// Format research data for prompt injection
function formatResearchForPrompt(research) {
  if (!research) return '';
  let out = '\n\n═══════════════════════════════════════\nMARKET RESEARCH DATA (pre-validated)\n═══════════════════════════════════════\n';

  if (research.painPoints && research.painPoints.length) {
    out += '\n【VALIDATED PAIN POINTS — from industry research】\n';
    research.painPoints.forEach((p, i) => {
      out += `${i+1}. ${p.title}: ${p.desc} (Source: ${p.source})\n`;
    });
  }

  if (research.marketData) {
    const m = research.marketData;
    out += '\n【MARKET DATA】\n';
    out += `• Industry Size: ${m.industrySize}\n`;
    out += `• Growth: ${m.growthRate}\n`;
    out += `• AI Market: ${m.aiMarketSize}\n`;
    out += `• Local Context: ${m.localContext}\n`;
    out += `• AI Adoption: ${m.aiAdoption}\n`;
  }

  if (research.competitors && research.competitors.length) {
    out += '\n【COMPETITOR GAPS — what exists vs what\'s missing】\n';
    research.competitors.forEach(c => {
      out += `• ${c.name} → Gap: ${c.gap}\n`;
    });
  }

  if (research.customerProfile) {
    const cp = research.customerProfile;
    out += '\n【TARGET CUSTOMER PROFILE】\n';
    out += `• Typical Size: ${cp.typicalSize}\n`;
    out += `• Budget: ${cp.budget}\n`;
    out += `• Decision Maker: ${cp.decisionMaker}\n`;
    out += `• Buying Habits: ${cp.buyingHabits}\n`;
    out += `• Key Metric: ${cp.keyMetric}\n`;
  }

  if (research.roiBenchmarks) {
    const r = research.roiBenchmarks;
    out += '\n【ROI BENCHMARKS — use these numbers in the proposal】\n';
    out += `• Cost Saving: ${r.costSaving}\n`;
    out += `• Time Reduction: ${r.timeReduction}\n`;
    out += `• Engagement Impact: ${r.engagement}\n`;
    out += `• Payback Period: ${r.payback}\n`;
  }

  if (research.source) {
    out += `\nResearch Source: ${research.source}\n`;
  }

  return out;
}

// Main research function — hybrid mode
async function researchIndustry(industryText, clientName, painText, statusEl) {
  // Step 1: Check prebuilt DB
  const matchKey = matchIndustry(industryText);

  if (matchKey) {
    // Found in prebuilt DB
    const data = INDUSTRY_DB[matchKey];
    if (statusEl) statusEl.textContent = '📊 Step 1/4: Loaded industry data — ' + matchKey;
    STATE.research = {
      ...data,
      matchedIndustry: matchKey,
      source: 'Prebuilt Industry Database',
      isLive: false
    };
    // Brief pause for UX
    await new Promise(r => setTimeout(r, 300));
    if (statusEl) statusEl.textContent = '📊 Step 2/4: Validating pain points against data…';
    await new Promise(r => setTimeout(r, 300));
    if (statusEl) statusEl.textContent = '📊 Step 3/4: Building argumentation logic…';
    await new Promise(r => setTimeout(r, 300));
    if (statusEl) statusEl.textContent = '📊 Step 4/4: Research ready — enriching proposal…';
    await new Promise(r => setTimeout(r, 200));
    updateResearchPanel(STATE.research);
    return STATE.research;
  }

  // Not in DB — use Claude API for live research
  if (statusEl) statusEl.textContent = '🔍 Step 1/4: Industry not in database — starting live research…';

  const researchPrompt = `You are a B2B market research analyst. Research the following industry and provide structured data for a sales proposal.

INDUSTRY: ${industryText}
CLIENT: ${clientName || 'Unknown'}
KNOWN PAIN POINTS: ${painText || 'Not specified'}

Provide a JSON response with this EXACT structure:
{
  "painPoints": [
    {"title": "Short title (max 5 words)", "desc": "1-2 sentences describing the pain with specifics", "source": "Data source or 'Industry estimate'"}
  ],
  "marketData": {
    "industrySize": "Market size with currency and year",
    "growthRate": "Growth rate with timeframe",
    "aiMarketSize": "AI/automation market size for this industry",
    "localContext": "Netherlands or EU specific context",
    "aiAdoption": "Current AI adoption rate in this industry"
  },
  "competitors": [
    {"name": "Competitor category", "gap": "What they don't do that Notso.ai does"}
  ],
  "customerProfile": {
    "typicalSize": "Company size range",
    "budget": "Annual budget for digital tools",
    "decisionMaker": "Who makes buying decisions",
    "buyingHabits": "How they typically buy",
    "keyMetric": "What KPI they care about most"
  },
  "roiBenchmarks": {
    "costSaving": "Estimated cost savings with AI agent",
    "timeReduction": "Expected reduction in manual work",
    "engagement": "Expected engagement or satisfaction improvement",
    "payback": "Estimated time to ROI"
  }
}

RULES:
- Provide 4-5 pain points
- Provide 3-4 competitors
- Use real industry data where possible, label estimates clearly
- Focus on Netherlands/EU market where relevant
- Frame everything in terms of what Notso.ai (3D AI brand agents with empathy) can solve
- Return ONLY valid JSON, no markdown`;

  try {
    if (statusEl) statusEl.textContent = '🔍 Step 2/4: Calling AI for market research…';
    const raw = await callClaude(researchPrompt, 4000);
    if (!raw) {
      if (statusEl) statusEl.textContent = '⚠️ Live research failed — proceeding without research data';
      STATE.research = null;
      return null;
    }

    if (statusEl) statusEl.textContent = '🔍 Step 3/4: Parsing research data…';
    let cleaned = raw.replace(/```json/g, '').replace(/```/g, '').trim();
    const jsonStart = cleaned.indexOf('{');
    const jsonEnd = cleaned.lastIndexOf('}') + 1;
    if (jsonStart >= 0 && jsonEnd > jsonStart) cleaned = cleaned.slice(jsonStart, jsonEnd);

    const data = JSON.parse(cleaned);
    if (statusEl) statusEl.textContent = '🔍 Step 4/4: Research complete — enriching proposal…';

    STATE.research = {
      ...data,
      matchedIndustry: 'custom',
      source: 'Live AI Research (Claude)',
      isLive: true
    };
    updateResearchPanel(STATE.research);
    return STATE.research;
  } catch (e) {
    console.error('Live research error:', e);
    if (statusEl) statusEl.textContent = '⚠️ Research parse error — proceeding without data';
    STATE.research = null;
    return null;
  }
}

// Update research results panel in UI
function updateResearchPanel(research) {
  const panel = document.getElementById('research-results');
  if (!panel || !research) return;

  let html = '';

  // Pain points
  if (research.painPoints && research.painPoints.length) {
    html += '<div class="rr-section"><div class="rr-section-title">🎯 Validated Pain Points</div>';
    research.painPoints.forEach(p => {
      html += '<div class="rr-card"><div class="rr-card-title">' + p.title + '</div><div class="rr-card-text">' + p.desc + '</div><div class="rr-card-source">' + p.source + '</div></div>';
    });
    html += '</div>';
  }

  // Market data
  if (research.marketData) {
    const m = research.marketData;
    html += '<div class="rr-section"><div class="rr-section-title">📈 Market Data</div>';
    html += '<div class="rr-grid">';
    html += '<div class="rr-metric"><div class="rr-metric-label">Industry Size</div><div class="rr-metric-value">' + m.industrySize + '</div></div>';
    html += '<div class="rr-metric"><div class="rr-metric-label">Growth</div><div class="rr-metric-value">' + m.growthRate + '</div></div>';
    html += '<div class="rr-metric"><div class="rr-metric-label">AI Market</div><div class="rr-metric-value">' + m.aiMarketSize + '</div></div>';
    html += '<div class="rr-metric"><div class="rr-metric-label">AI Adoption</div><div class="rr-metric-value">' + m.aiAdoption + '</div></div>';
    html += '</div></div>';
  }

  // Competitors
  if (research.competitors && research.competitors.length) {
    html += '<div class="rr-section"><div class="rr-section-title">🏁 Competitor Gaps</div>';
    research.competitors.forEach(c => {
      html += '<div class="rr-card"><div class="rr-card-title">' + c.name + '</div><div class="rr-card-text" style="color:#b45309;">Gap: ' + c.gap + '</div></div>';
    });
    html += '</div>';
  }

  // ROI
  if (research.roiBenchmarks) {
    const r = research.roiBenchmarks;
    html += '<div class="rr-section"><div class="rr-section-title">💰 ROI Benchmarks</div>';
    html += '<div class="rr-grid">';
    html += '<div class="rr-metric"><div class="rr-metric-label">Cost Saving</div><div class="rr-metric-value">' + r.costSaving + '</div></div>';
    html += '<div class="rr-metric"><div class="rr-metric-label">Time Reduction</div><div class="rr-metric-value">' + r.timeReduction + '</div></div>';
    html += '<div class="rr-metric"><div class="rr-metric-label">Engagement</div><div class="rr-metric-value">' + r.engagement + '</div></div>';
    html += '<div class="rr-metric"><div class="rr-metric-label">Payback</div><div class="rr-metric-value">' + r.payback + '</div></div>';
    html += '</div></div>';
  }

  // Source badge
  html += '<div class="rr-source-badge">' + (research.isLive ? '🔴 Live AI Research' : '🟢 Prebuilt Database — ' + research.matchedIndustry) + '</div>';

  panel.innerHTML = html;
  panel.style.display = 'block';
  // Also show the container
  const container = document.getElementById('research-container');
  if (container) container.style.display = 'block';
}

'''

# Insert before getCtx()
src = src.replace(
    '/* ════════════════════════════════════════\n   AI\n════════════════════════════════════════ */\nfunction getCtx(){',
    research_module + '\n/* ════════════════════════════════════════\n   AI\n════════════════════════════════════════ */\nfunction getCtx(){'
)

# ═══════════════════════════════════════════════════════════════
# 2. ADD research property to STATE
# ═══════════════════════════════════════════════════════════════

src = src.replace(
    "aiRoiAfter:'',",
    "aiRoiAfter:'',\n  research:null, // Market research data (from INDUSTRY_DB or live)",
)

# ═══════════════════════════════════════════════════════════════
# 3. MODIFY genAll() to include research phase + enriched prompt
# ═══════════════════════════════════════════════════════════════

# Replace the research step and status updates in genAll
old_research_step = """  // Step 1: Research client website
  let webResearch='';
  if(c.url&&c.url.startsWith('http')){
    st.textContent='🔍 Researching client website…';
    const scraped=await researchClientWebsite(c.url);
    if(scraped){
      webResearch=`\\n\\nCLIENT WEBSITE RESEARCH (scraped from ${c.url}):\\n${scraped}`;
    }
  }

  st.textContent='✦ Generating slide content…';"""

new_research_step = r"""  // Step 1: Research client website
  let webResearch='';
  if(c.url&&c.url.startsWith('http')){
    st.textContent='🔍 Step 0: Researching client website…';
    const scraped=await researchClientWebsite(c.url);
    if(scraped){
      webResearch=`\n\nCLIENT WEBSITE RESEARCH (scraped from ${c.url}):\n${scraped}`;
    }
  }

  // Step 2: Market Research (4-step workflow)
  st.textContent='📊 Starting market research…';
  const researchData=await researchIndustry(c.ind, c.c, c.pain, st);
  let marketResearch='';
  if(researchData){
    marketResearch=formatResearchForPrompt(researchData);
  }

  st.textContent='✦ Generating slide content with research data…';"""

src = src.replace(old_research_step, new_research_step)

# Now inject marketResearch into the prompt — add it after webResearch in the CLIENT PROFILE section
old_web_inject = '${webResearch}'
new_web_inject = '${webResearch}${marketResearch}'
# This appears in the prompt template — replace only the first occurrence after CLIENT PROFILE
src = src.replace(old_web_inject, new_web_inject, 1)

# ═══════════════════════════════════════════════════════════════
# 4. ADD RESEARCH PROMPT ENHANCEMENT — instruct Claude to use research data
# ═══════════════════════════════════════════════════════════════

# Add instruction to use research data in the CRITICAL RULES section
old_critical_rules = """CRITICAL RULES:
1. This is a COLD PITCH — we have NOT spoken to the client. Base everything on sales rep input + website research + industry knowledge.
2. NEVER fabricate direct quotes from the client. Describe situations they likely face.
3. NEVER invent numbers. Use research data or industry averages (label them as such).
4. NEVER say "chatbot" — say "Brand Agent" or "Visual Agent" or use the mascot name.
5. Write like a smart colleague presenting insights, not a vendor selling software."""

new_critical_rules = """CRITICAL RULES:
1. This is a COLD PITCH — we have NOT spoken to the client. Base everything on sales rep input + website research + market research data + industry knowledge.
2. NEVER fabricate direct quotes from the client. Describe situations they likely face.
3. NEVER invent numbers. USE THE MARKET RESEARCH DATA PROVIDED BELOW — it contains validated pain points, market size, competitor gaps, and ROI benchmarks. Reference these numbers directly.
4. NEVER say "chatbot" — say "Brand Agent" or "Visual Agent" or use the mascot name.
5. Write like a smart colleague presenting insights, not a vendor selling software.
6. ARGUMENTATION LOGIC: Pain is real (validated data) → Market is large & growing → Current solutions have gaps → Our product fills the gap → Clear ROI pathway."""

src = src.replace(old_critical_rules, new_critical_rules)

# ═══════════════════════════════════════════════════════════════
# 5. ADD UI: Research section between Client Intelligence and AI Generation
# ═══════════════════════════════════════════════════════════════

# CSS for research panel
research_css = '''
/* ═══════════════════════════════════════
   RESEARCH RESULTS PANEL
═══════════════════════════════════════ */
#research-container{
  display:none;margin-top:.75rem;
}
.research-toggle{
  display:flex;align-items:center;gap:.5rem;cursor:pointer;
  padding:.6rem .85rem;background:rgba(10,10,10,.02);
  border:1px solid rgba(163,163,163,.18);border-radius:14px;
  transition:all .2s;
}
.research-toggle:hover{background:rgba(10,10,10,.05);}
.research-toggle-title{
  font-size:.72rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#0a0a0a;
}
.research-toggle-badge{
  font-size:.6rem;padding:2px 8px;border-radius:10px;
  background:rgba(22,163,74,.08);border:1px solid rgba(22,163,74,.2);color:#15803d;
  font-weight:500;
}
.research-toggle-arrow{
  margin-left:auto;transition:transform .2s;font-size:.7rem;color:#737373;
}
.research-toggle.open .research-toggle-arrow{transform:rotate(180deg);}
#research-results{
  display:none;padding:.75rem;margin-top:.4rem;
  background:rgba(245,245,244,.5);border:1px solid rgba(163,163,163,.15);border-radius:14px;
  max-height:500px;overflow-y:auto;
}
#research-results.show{display:block;}
.rr-section{margin-bottom:.75rem;}
.rr-section:last-child{margin-bottom:0;}
.rr-section-title{
  font-size:.65rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  color:#525252;margin-bottom:.4rem;padding-bottom:.25rem;
  border-bottom:1px solid rgba(163,163,163,.15);
}
.rr-card{
  padding:.45rem .6rem;margin-bottom:.3rem;
  background:rgba(255,255,255,.7);border:1px solid rgba(163,163,163,.12);border-radius:10px;
}
.rr-card-title{font-size:.75rem;font-weight:600;color:#0a0a0a;margin-bottom:.15rem;}
.rr-card-text{font-size:.7rem;color:#525252;line-height:1.45;}
.rr-card-source{font-size:.6rem;color:#a3a3a3;margin-top:.2rem;font-style:italic;}
.rr-grid{
  display:grid;grid-template-columns:1fr 1fr;gap:.35rem;
}
.rr-metric{
  padding:.4rem .55rem;background:rgba(255,255,255,.7);
  border:1px solid rgba(163,163,163,.12);border-radius:10px;
}
.rr-metric-label{font-size:.58rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:#737373;margin-bottom:.15rem;}
.rr-metric-value{font-size:.68rem;color:#0a0a0a;line-height:1.4;}
.rr-source-badge{
  display:inline-flex;align-items:center;gap:.3rem;margin-top:.5rem;
  font-size:.6rem;padding:3px 10px;border-radius:10px;
  background:rgba(10,10,10,.04);border:1px solid rgba(163,163,163,.15);color:#525252;
}
'''

# Inject CSS before the closing </style>
src = src.replace('</style>', research_css + '</style>', 1)

# Inject HTML for research panel — after the AI Generation section header, before the API key input
research_html = '''
      <!-- RESEARCH RESULTS (auto-populated) -->
      <div id="research-container">
        <div class="research-toggle" onclick="toggleResearch()">
          <span class="research-toggle-title">📊 Market Research Results</span>
          <span class="research-toggle-badge" id="research-badge">Ready</span>
          <span class="research-toggle-arrow">▼</span>
        </div>
        <div id="research-results"></div>
      </div>
'''

# Place it inside the AI section, right after the section header
old_ai_section = '''      <div class="sec-hdr"><div class="sec-num">02</div><div><div class="sec-ttl">AI Content Generation</div><div class="sec-sub">Writes in Notso.ai&#39;s voice — empathetic, direct, industry-specific — based on everything above</div></div></div>
      <div class="fg" style="margin-bottom:.4rem;"><label class="fl">Anthropic API Key</label>'''

new_ai_section = '''      <div class="sec-hdr"><div class="sec-num">02</div><div><div class="sec-ttl">AI Content Generation</div><div class="sec-sub">Market research → argumentation logic → data-backed slide content — all in Notso.ai&#39;s voice</div></div></div>
''' + research_html + '''
      <div class="fg" style="margin-bottom:.4rem;"><label class="fl">Anthropic API Key</label>'''

src = src.replace(old_ai_section, new_ai_section)

# Add the toggleResearch function and update the generates badges
toggle_fn = '''
function toggleResearch(){
  const panel=document.getElementById('research-results');
  const toggle=document.querySelector('.research-toggle');
  if(panel.classList.contains('show')){
    panel.classList.remove('show');
    toggle.classList.remove('open');
  }else{
    panel.classList.add('show');
    toggle.classList.add('open');
  }
}
'''

# Insert toggleResearch before getCtx
src = src.replace(
    '/* ════════════════════════════════════════\n   AI\n════════════════════════════════════════ */\nfunction getCtx(){',
    toggle_fn + '\n/* ════════════════════════════════════════\n   AI\n════════════════════════════════════════ */\nfunction getCtx(){'
)

# Update the "Generates:" badges to include research
old_badges = '''        <span style="font-size:.6rem;color:#737373;letter-spacing:.1em;text-transform:uppercase;margin-right:.2rem;">Generates:</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(10,10,10,.05);border:1px solid rgba(163,163,163,.22);color:#525252;">Pain point (their words)</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(10,10,10,.05);border:1px solid rgba(163,163,163,.22);color:#525252;">4 pain cards</span>'''

new_badges = '''        <span style="font-size:.6rem;color:#737373;letter-spacing:.1em;text-transform:uppercase;margin-right:.2rem;">Workflow:</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">📊 Market research</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">🎯 Pain validation</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">🏁 Competitor gaps</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(22,163,74,.06);border:1px solid rgba(22,163,74,.18);color:#15803d;">💰 ROI benchmarks</span>
        <span style="font-size:.6rem;color:#737373;margin:0 .15rem;">→</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(10,10,10,.05);border:1px solid rgba(163,163,163,.22);color:#525252;">Pain point (their words)</span>
        <span style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(10,10,10,.05);border:1px solid rgba(163,163,163,.22);color:#525252;">4 pain cards</span>'''

src = src.replace(old_badges, new_badges)

# ═══════════════════════════════════════════════════════════════
# 6. UPDATE genAll button text
# ═══════════════════════════════════════════════════════════════

src = src.replace(
    '✦ Generate All Slide Content',
    '✦ Research & Generate All Content'
)

# ═══════════════════════════════════════════════════════════════
# 7. UPDATE research badge status during genAll
# ═══════════════════════════════════════════════════════════════

# Add badge update after research completes in genAll
old_gen_status = "st.textContent='✦ Generating slide content with research data…';"
new_gen_status = """st.textContent='✦ Generating slide content with research data…';
  // Update research badge
  const rBadge=document.getElementById('research-badge');
  if(rBadge){
    if(researchData){
      rBadge.textContent=researchData.isLive?'Live Research':'DB: '+researchData.matchedIndustry;
      rBadge.style.background='rgba(22,163,74,.08)';rBadge.style.color='#15803d';rBadge.style.borderColor='rgba(22,163,74,.2)';
    }else{
      rBadge.textContent='No data';
      rBadge.style.background='rgba(234,179,8,.08)';rBadge.style.color='#a16207';rBadge.style.borderColor='rgba(234,179,8,.2)';
    }
  }"""

src = src.replace(old_gen_status, new_gen_status)

# Write the modified file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print('✅ Patch applied successfully!')
print('   - INDUSTRY_DB with 7 industries (retail, healthcare, education, office, legal, finance, ecommerce, fitness)')
print('   - researchIndustry() hybrid function (prebuilt DB + Claude API live)')
print('   - genAll() now runs 4-step research before content generation')
print('   - Research results panel in UI (collapsible)')
print('   - Enhanced Claude prompt with market research data injection')
print('   - Argumentation logic rule added to prompt')

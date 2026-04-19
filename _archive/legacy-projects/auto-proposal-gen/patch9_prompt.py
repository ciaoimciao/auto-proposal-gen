#!/usr/bin/env python3
"""Enhance the AI prompt with real brand knowledge from the brand guidelines."""

with open('index.html','r',encoding='utf-8') as f:
    src = f.read()

old_prompt_start = "const prompt=`You are a senior B2B marketing strategist and conversion copywriter for Notso.ai — a company that builds empathetic 3D animated AI brand agents. Your copy wins deals."

old_prompt_voice = """VOICE RULES:
- Speak like a smart colleague, not a vendor
- Use the client's OWN words wherever they are given
- Short, punchy sentences. Zero jargon. Zero filler.
- Pain must be felt — visceral, specific, real situations
- Headlines are bold claims or provocations, never descriptions"""

new_prompt_voice = """ABOUT NOTSO.AI:
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
- Conversations, not interrogations. Built for delight, not realism."""

if old_prompt_voice in src:
    src = src.replace(old_prompt_voice, new_prompt_voice)
    print("✅ 1. Enhanced prompt with brand knowledge, differentiators, proven results, objection handling")
else:
    print("⚠️ 1. Voice rules pattern not found")

# Also enhance the cover_headline instruction
old_cover = '"cover_headline": "6-8 word bold claim or provocation specific to ${clientName}\'s world — make it memorable"'
new_cover = '"cover_headline": "6-8 word bold claim specific to ${clientName}. Examples: \'Jumbo\\\'s New Hire Calls End Today.\' or \'Every Conversation, An Experience.\' — make it feel like a movie tagline"'
if old_cover in src:
    src = src.replace(old_cover, new_cover)
    print("✅ 2. Enhanced cover_headline instruction")
else:
    print("⚠️ 2. cover_headline pattern not found")

# Enhance feature_items to reference real differentiators
old_feat = '"concrete feature framed as an outcome for ${clientName}\'s users, not a tech description"'
new_feat = '"concrete outcome for ${clientName}. Reference Empathy Engine, Knowledge Base, or Analytics when relevant. Frame as what changes for the user, not what the tech does."'
if old_feat in src:
    src = src.replace(old_feat, new_feat)
    print("✅ 3. Enhanced feature_items instruction")
else:
    print("⚠️ 3. feature_items pattern not found")

with open('index.html','w',encoding='utf-8') as f:
    f.write(src)

print("\n✅ AI prompt now includes full brand knowledge, proven results, and competitive positioning.")

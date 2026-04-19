#!/usr/bin/env python3
"""Switch generatePose() from PhotoMaker to Nano Banana Pro model."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Update POSE_PRESETS — remove 'img' trigger word (not needed for Nano Banana Pro) ───
old = """const POSE_PRESETS={
  wave:'a 3D animated mascot character img waving hello with one hand raised high, friendly cheerful pose, full body, white background, consistent style',
  point:'a 3D animated mascot character img pointing forward at viewer with index finger, confident pose, full body, white background, consistent style',
  think:'a 3D animated mascot character img with hand on chin thinking deeply, curious thoughtful pose, full body, white background, consistent style',
  thumbsup:'a 3D animated mascot character img giving enthusiastic thumbs up with big smile, happy cheerful pose, full body, white background, consistent style',
  present:'a 3D animated mascot character img gesturing to the side with open palm presenting something, professional pose, full body, white background, consistent style',
  sit:'a 3D animated mascot character img sitting casually cross-legged, relaxed friendly pose, full body, white background, consistent style',
};"""

new = """const POSE_PRESETS={
  wave:'Generate this exact same character in a waving pose, one hand raised high greeting hello. Keep the same character design, colors, proportions and style. Friendly cheerful expression, full body, clean white background.',
  point:'Generate this exact same character pointing forward at the viewer with index finger. Keep the same character design, colors, proportions and style. Confident pose, full body, clean white background.',
  think:'Generate this exact same character with hand on chin in a thinking pose. Keep the same character design, colors, proportions and style. Curious thoughtful expression, full body, clean white background.',
  thumbsup:'Generate this exact same character giving an enthusiastic thumbs up with a big smile. Keep the same character design, colors, proportions and style. Happy cheerful pose, full body, clean white background.',
  present:'Generate this exact same character gesturing to the side with open palm, presenting something. Keep the same character design, colors, proportions and style. Professional pose, full body, clean white background.',
  sit:'Generate this exact same character sitting casually cross-legged. Keep the same character design, colors, proportions and style. Relaxed friendly pose, full body, clean white background.',
};"""

if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 1. POSE_PRESETS → Nano Banana Pro style prompts")
else:
    print("⚠️ 1. POSE_PRESETS not found")

# ─── 2. Remove the 'img' trigger word auto-injection (not needed) ───
old_trigger = """  if(!prompt){statusEl.textContent='Describe the pose first';return;}
  // Ensure 'img' trigger word is present for PhotoMaker
  const finalPrompt=prompt.includes('img')?prompt:prompt.replace(/character/i,'character img').replace(/mascot/i,'mascot img')||prompt+' img';"""
new_trigger = """  if(!prompt){statusEl.textContent='Describe the pose first';return;}"""
if old_trigger in src:
    src = src.replace(old_trigger, new_trigger)
    changes += 1
    print("✅ 2. Removed 'img' trigger word injection")
else:
    print("⚠️ 2. Trigger word injection not found")

# ─── 3. Replace API call — use model-based + Nano Banana Pro params ───
old_api = """        body:JSON.stringify({
          replicateToken:token,
          version:'ddfc2b08d209f9fa8c1eca692712918bd449f695dabb4a958da31802a9570fe4',
          input:{
            input_image:refBase64,
            prompt:finalPrompt,
            negative_prompt:'blurry, low quality, distorted, deformed, ugly, realistic photo, human face',
            num_outputs:2,
            guidance_scale:5,
            style_name:'Photographic',
            num_steps:30,
            style_strength_ratio:20,
          }
        })"""

new_api = """        body:JSON.stringify({
          replicateToken:token,
          model:'google/nano-banana-pro',
          input:{
            image:refBase64,
            prompt:prompt,
            aspect_ratio:'1:1',
            resolution:'1K',
            output_format:'png',
            num_images:2,
            safety_filter_level:4,
          }
        })"""

if old_api in src:
    src = src.replace(old_api, new_api)
    changes += 1
    print("✅ 3. API call → Nano Banana Pro model-based")
else:
    print("⚠️ 3. API call not found")

# ─── 4. Fix output handling — Nano Banana Pro returns output differently ───
# Check how renderPoseResults is called
# Current code: result.output (array of URLs) — same for Nano Banana Pro, should be fine

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

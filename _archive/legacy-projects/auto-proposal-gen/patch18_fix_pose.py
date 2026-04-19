#!/usr/bin/env python3
"""Fix generatePose() — correct PhotoMaker version hash, input params, and preset prompts."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. Fix POSE_PRESETS — add 'img' trigger word for PhotoMaker ───
old = """const POSE_PRESETS={
  wave:'3D animated mascot character waving hello with one hand raised high, friendly cheerful pose, full body, white background, same character identity, consistent style',
  point:'3D animated mascot character pointing forward at viewer with index finger, confident pose, full body, white background, same character identity, consistent style',
  think:'3D animated mascot character with hand on chin thinking deeply, curious thoughtful pose, full body, white background, same character identity, consistent style',
  thumbsup:'3D animated mascot character giving enthusiastic thumbs up with big smile, happy cheerful pose, full body, white background, same character identity, consistent style',
  present:'3D animated mascot character gesturing to the side with open palm presenting something, professional pose, full body, white background, same character identity, consistent style',
  sit:'3D animated mascot character sitting casually cross-legged, relaxed friendly pose, full body, white background, same character identity, consistent style',
};"""

new = """const POSE_PRESETS={
  wave:'a 3D animated mascot character img waving hello with one hand raised high, friendly cheerful pose, full body, white background, consistent style',
  point:'a 3D animated mascot character img pointing forward at viewer with index finger, confident pose, full body, white background, consistent style',
  think:'a 3D animated mascot character img with hand on chin thinking deeply, curious thoughtful pose, full body, white background, consistent style',
  thumbsup:'a 3D animated mascot character img giving enthusiastic thumbs up with big smile, happy cheerful pose, full body, white background, consistent style',
  present:'a 3D animated mascot character img gesturing to the side with open palm presenting something, professional pose, full body, white background, consistent style',
  sit:'a 3D animated mascot character img sitting casually cross-legged, relaxed friendly pose, full body, white background, consistent style',
};"""

if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 1. POSE_PRESETS — added 'img' trigger word")
else:
    print("⚠️ 1. POSE_PRESETS not found")

# ─── 2. Fix version hash ───
old_ver = "version:'ea16514e940159c0a1e1da109905d1a5e3648f23e0648e1044699f5d388db1d9',"
new_ver = "version:'ddfc2b08d209f9fa8c1eca692712918bd449f695dabb4a958da31802a9570fe4',"
if old_ver in src:
    src = src.replace(old_ver, new_ver)
    changes += 1
    print("✅ 2. Version hash → PhotoMaker correct hash")
else:
    print("⚠️ 2. Version hash not found")

# ─── 3. Fix input params ───
old_input = """          input:{
            image:refBase64,
            prompt:prompt,
            negative_prompt:'blurry, low quality, distorted, deformed, ugly, realistic photo, human face',
            num_outputs:2,
            guidance_scale:7.5,
            ip_adapter_scale:0.75,
            num_inference_steps:30,
          }"""

new_input = """          input:{
            input_image:refBase64,
            prompt:prompt,
            negative_prompt:'blurry, low quality, distorted, deformed, ugly, realistic photo, human face',
            num_outputs:2,
            guidance_scale:5,
            style_name:'Photographic',
            num_steps:30,
            style_strength_ratio:20,
          }"""

if old_input in src:
    src = src.replace(old_input, new_input)
    changes += 1
    print("✅ 3. Input params → PhotoMaker format (input_image, num_steps, style_name)")
else:
    print("⚠️ 3. Input params not found")

# ─── 4. Auto-prepend 'img' trigger word if user writes custom prompt without it ───
old_prompt_check = "if(!prompt){statusEl.textContent='Describe the pose first';return;}"
new_prompt_check = """if(!prompt){statusEl.textContent='Describe the pose first';return;}
  // Ensure 'img' trigger word is present for PhotoMaker
  const finalPrompt=prompt.includes('img')?prompt:prompt.replace(/character/i,'character img').replace(/mascot/i,'mascot img')||prompt+' img';"""
if old_prompt_check in src:
    src = src.replace(old_prompt_check, new_prompt_check)
    changes += 1
    print("✅ 4. Added auto 'img' trigger word injection")
else:
    print("⚠️ 4. Prompt check not found")

# ─── 5. Use finalPrompt instead of prompt in the API call ───
old_prompt_use = "            prompt:prompt,"
new_prompt_use = "            prompt:finalPrompt,"
if old_prompt_use in src:
    src = src.replace(old_prompt_use, new_prompt_use)
    changes += 1
    print("✅ 5. API call uses finalPrompt with trigger word")
else:
    print("⚠️ 5. prompt usage not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

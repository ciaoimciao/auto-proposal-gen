#!/usr/bin/env python3
"""Replace purple/pink palette with warm earthy tones from user's design system."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── Color mapping ───
# Primary: #7C3AED → #c96442 (terracotta)
# Background gradient: purple-pink → warm off-white
# Foreground: #111827 → #3d3929
# Muted text: #6B7280 → #83827d
# Labels: #4B5563 → #535146
# Light gray: #9CA3AF → #b4b2a7
# Card bg: rgba(255,255,255,.45) → #faf9f5
# Input bg: rgba(255,255,255,.6) → #ffffff
# Border: rgba(0,0,0,.1) → #dad9d4
# Accent bg: rgba(124,58,237,.08) → rgba(201,100,66,.08)

replacements = [
    # 1. Background gradient
    ('background:linear-gradient(135deg,#EDE9FE,#FCE7F3,#EDE9FE)',
     'background:#faf9f5'),

    # 2. Navbar glass
    ('background:rgba(255,255,255,.8);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:16px;border:1px solid rgba(255,255,255,.25);box-shadow:0 4px 24px rgba(0,0,0,.06)',
     'background:rgba(255,255,255,.85);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:16px;border:1px solid #dad9d4;box-shadow:0 4px 24px rgba(0,0,0,.04)'),

    # 3. Logo color
    ('letter-spacing:-.04em;color:#111827;',
     'letter-spacing:-.04em;color:#3d3929;'),

    # 4. Chip
    ('background:#111827;color:#fff;padding:4px 12px',
     'background:#c96442;color:#fff;padding:4px 12px'),

    # 5. Eyebrow → terracotta pill
    ('color:#7C3AED;margin-bottom:.85rem;display:inline-flex;align-items:center;gap:6px;padding:4px 14px;background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.15);border-radius:20px;',
     'color:#c96442;margin-bottom:.85rem;display:inline-flex;align-items:center;gap:6px;padding:4px 14px;background:rgba(201,100,66,.08);border:1px solid rgba(201,100,66,.15);border-radius:20px;'),

    # 6. Title
    ('font-weight:300;font-size:clamp(2.5rem,5vw,4.5rem);line-height:1.05;letter-spacing:-.04em;margin-bottom:1rem;color:#111827;',
     'font-weight:300;font-size:clamp(2.5rem,5vw,4.5rem);line-height:1.05;letter-spacing:-.04em;margin-bottom:1rem;color:#3d3929;'),

    # 7. Title em → terracotta
    ('color:#7C3AED;font-style:normal;font-weight:500;',
     'color:#c96442;font-style:normal;font-weight:500;'),

    # 8. Subtitle
    ('color:#6B7280;line-height:1.7;margin-bottom:1.75rem;max-width:560px;',
     'color:#83827d;line-height:1.7;margin-bottom:1.75rem;max-width:560px;'),

    # 9. CTA button → terracotta
    ('background:#111827;color:#fff;font-family:\'Syne\',sans-serif;font-weight:700;font-size:.88rem;padding:.7rem 1.75rem;border-radius:12px;cursor:pointer;border:none;transition:all .2s ease;',
     'background:#c96442;color:#fff;font-family:\'Syne\',sans-serif;font-weight:700;font-size:.88rem;padding:.7rem 1.75rem;border-radius:8px;cursor:pointer;border:none;transition:all .2s ease;'),

    # 10. CTA hover
    ('transform:scale(1.05);box-shadow:0 8px 24px rgba(17,17,16,.18);background:#1F2937;',
     'transform:scale(1.05);box-shadow:0 8px 24px rgba(201,100,66,.25);background:#b05730;'),

    # 11. Stat card → warm card
    ('background:rgba(255,255,255,.45);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.5);border-radius:16px;padding:1rem 1rem;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;transition:transform .2s,box-shadow .2s;',
     'background:#ffffff;border:1px solid #dad9d4;border-radius:12px;padding:1rem 1rem;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;transition:transform .2s,box-shadow .2s;'),

    # 12. Stat hover
    ('.sh-stat:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.06);}',
     '.sh-stat:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(201,100,66,.1);}'),

    # 13. Stat value
    ('font-weight:700;font-size:1rem;letter-spacing:-.02em;color:#111827;',
     'font-weight:700;font-size:1rem;letter-spacing:-.02em;color:#3d3929;'),

    # 14. Stat label
    ('.sh-stat-lbl{font-size:.72rem;color:#6B7280;line-height:1.4;}',
     '.sh-stat-lbl{font-size:.72rem;color:#83827d;line-height:1.4;}'),

    # 15. Section header border
    ('border-bottom:1px solid rgba(0,0,0,.06);',
     'border-bottom:1px solid #ede9de;'),

    # 16. Section num → terracotta
    ('background:#7C3AED;color:#fff;',
     'background:#c96442;color:#fff;'),

    # 17. Section title
    ('.sec-ttl{font-family:\'Syne\',sans-serif;font-weight:700;font-size:1rem;letter-spacing:-.02em;color:#111827;}',
     '.sec-ttl{font-family:\'Syne\',sans-serif;font-weight:700;font-size:1rem;letter-spacing:-.02em;color:#3d3929;}'),

    # 18. Section subtitle
    ('.sec-sub{font-size:.8rem;color:#6B7280;}',
     '.sec-sub{font-size:.8rem;color:#83827d;}'),

    # 19. Form label
    ('color:#4B5563;margin-bottom:.35rem;',
     'color:#535146;margin-bottom:.35rem;'),

    # 20. Input field
    ('background:rgba(255,255,255,.6);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1.5px solid rgba(0,0,0,.1);border-radius:10px;padding:.6rem .9rem;color:#111827;',
     'background:#ffffff;border:1.5px solid #dad9d4;border-radius:8px;padding:.6rem .9rem;color:#3d3929;'),

    # 21. Input focus → terracotta
    ('border-color:#7C3AED;box-shadow:0 0 0 3px rgba(124,58,237,.1);',
     'border-color:#c96442;box-shadow:0 0 0 3px rgba(201,100,66,.1);'),

    # 22. Placeholder
    ('.fi::placeholder{color:#9CA3AF;}',
     '.fi::placeholder{color:#b4b2a7;}'),

    # 23. Calendar trigger
    ('background:rgba(255,255,255,.6);backdrop-filter:blur(8px);border:1.5px solid rgba(0,0,0,.1);border-radius:10px;padding:.6rem .9rem;color:#111827;',
     'background:#ffffff;border:1.5px solid #dad9d4;border-radius:8px;padding:.6rem .9rem;color:#3d3929;'),

    # 24. Calendar hover
    ('.cal-trig:hover,.cal-trig.open{border-color:#7C3AED;}',
     '.cal-trig:hover,.cal-trig.open{border-color:#c96442;}'),

    # 25. Calendar popup
    ('background:rgba(255,255,255,.9);backdrop-filter:blur(12px);border:1.5px solid rgba(0,0,0,.08);border-radius:14px;padding:1rem;width:272px;box-shadow:0 10px 36px rgba(0,0,0,.1);',
     'background:#ffffff;border:1.5px solid #dad9d4;border-radius:12px;padding:1rem;width:272px;box-shadow:0 10px 36px rgba(0,0,0,.08);'),

    # 26. Calendar month
    ('.cal-mon{font-family:\'Syne\',sans-serif;font-size:.85rem;font-weight:700;color:#111827;}',
     '.cal-mon{font-family:\'Syne\',sans-serif;font-size:.85rem;font-weight:700;color:#3d3929;}'),

    # 27. Calendar nav
    ('border:1px solid rgba(0,0,0,.1);cursor:pointer;color:#6B7280;',
     'border:1px solid #dad9d4;cursor:pointer;color:#83827d;'),

    # 28. Calendar nav hover
    ('.cal-nav:hover{border-color:#7C3AED;color:#7C3AED;}',
     '.cal-nav:hover{border-color:#c96442;color:#c96442;}'),

    # 29. Calendar DOW
    ('.cal-dow{font-size:.6rem;text-align:center;color:#9CA3AF;',
     '.cal-dow{font-size:.6rem;text-align:center;color:#b4b2a7;'),

    # 30. Calendar day
    ('color:#374151;transition:all .15s;',
     'color:#3d3929;transition:all .15s;'),

    # 31. Calendar day hover
    ('background:rgba(124,58,237,.1);color:#7C3AED;',
     'background:rgba(201,100,66,.1);color:#c96442;'),

    # 32. Calendar today
    ('border:1.5px solid #7C3AED;color:#7C3AED;',
     'border:1.5px solid #c96442;color:#c96442;'),

    # 33. Calendar selected
    ('background:#7C3AED!important;',
     'background:#c96442!important;'),

    # 34. Calendar foot
    ('border-top:1px solid rgba(0,0,0,.06);',
     'border-top:1px solid #ede9de;'),

    # 35. Calendar clear
    ('.cal-clr{background:none;border:none;color:#6B7280;',
     '.cal-clr{background:none;border:none;color:#83827d;'),

    # 36. Calendar OK
    ('.cal-ok{background:#7C3AED;',
     '.cal-ok{background:#c96442;'),

    # 37. Roadmap preview
    ('background:rgba(124,58,237,.06);border:1.5px solid rgba(124,58,237,.15);',
     'background:rgba(201,100,66,.06);border:1.5px solid rgba(201,100,66,.15);'),

    # 38. Roadmap title
    ('.rm-prev-ttl{font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;color:#7C3AED;',
     '.rm-prev-ttl{font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;color:#c96442;'),

    # 39. Roadmap date
    ('.rm-pi-d{color:#7C3AED;',
     '.rm-pi-d{color:#c96442;'),

    # 40. Roadmap item text
    ('.rm-pi{font-size:.78rem;color:#4B5563;',
     '.rm-pi{font-size:.78rem;color:#535146;'),

    # 41. API hint
    ('.api-hint{font-size:.7rem;color:#6B7280;',
     '.api-hint{font-size:.7rem;color:#83827d;'),

    # 42. AI status
    ('.ai-st{font-size:.74rem;color:#6B7280;}',
     '.ai-st{font-size:.74rem;color:#83827d;}'),

    # 43. Context box
    ('background:rgba(255,255,255,.4);backdrop-filter:blur(8px);border-radius:10px;border:1.5px solid rgba(0,0,0,.06);',
     'background:#ffffff;border-radius:8px;border:1.5px solid #dad9d4;'),

    # 44. Context label
    ('.ctx-lbl{font-size:.68rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:#6B7280;',
     '.ctx-lbl{font-size:.68rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:#83827d;'),

    # 45. Generate button → terracotta
    ('background:#111827;color:#fff;border:none;border-radius:12px;font-family:\'Syne\',sans-serif;font-size:1rem;font-weight:700;cursor:pointer;transition:all .2s ease;margin-top:1.25rem;',
     'background:#c96442;color:#fff;border:none;border-radius:8px;font-family:\'Syne\',sans-serif;font-size:1rem;font-weight:700;cursor:pointer;transition:all .2s ease;margin-top:1.25rem;'),

    # 46. Generate hover
    ('transform:scale(1.02);box-shadow:0 8px 28px rgba(17,24,39,.25);background:#1F2937;',
     'transform:scale(1.02);box-shadow:0 8px 28px rgba(201,100,66,.3);background:#b05730;'),

    # 47. Golden box inline → terracotta
    ('border-color:rgba(124,58,237,.25);background:rgba(124,58,237,.04)',
     'border-color:rgba(201,100,66,.25);background:rgba(201,100,66,.04)'),

    # 48. Golden box label
    ('style="color:#7C3AED;">',
     'style="color:#c96442;">',),

    # 49. Quote highlight
    ('style="color:#7C3AED;font-weight:700;">Quote them directly',
     'style="color:#c96442;font-weight:700;">Quote them directly'),

    # 50. Tools subtitle
    ('style="color:#6B7280;font-weight:400;">(what Notso.ai replaces)',
     'style="color:#83827d;font-weight:400;">(what Notso.ai replaces)'),

    # 51. AI tags
    ('background:rgba(255,255,255,.5);border:1px solid rgba(0,0,0,.08);color:#4B5563',
     'background:#ede9de;border:1px solid #dad9d4;color:#535146'),

    # 52. AI section box
    ('background:rgba(255,255,255,.4);border-radius:8px;border:1.5px solid rgba(0,0,0,.06)',
     'background:#f5f4ee;border-radius:8px;border:1.5px solid #dad9d4'),

    # 53. Generates label
    ('font-size:.66rem;color:#6B7280',
     'font-size:.66rem;color:#83827d'),

    # 54. Calendar display
    ('<span id="cal-disp" style="color:#9CA3AF;">',
     '<span id="cal-disp" style="color:#b4b2a7;">'),

    # 55. API link
    ('style="color:#7C3AED;">Get a key',
     'style="color:#c96442;">Get a key'),
]

for i, (old, new) in enumerate(replacements, 1):
    if old in src:
        src = src.replace(old, new)
        changes += 1
        print(f"✅ {i}. Applied")
    else:
        print(f"⚠️ {i}. Pattern not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes}/{len(replacements)} changes applied.")

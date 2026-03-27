#!/usr/bin/env python3
"""Fix remaining hardcoded strings missed by patch7."""

with open('index.html','r',encoding='utf-8') as f:
    src = f.read()

changes = 0

# 1. Fix "Emotie selecteren" in chatflow (line ~2049)
old1 = '>Emotie selecteren</div>'
new1 = ">${tx('flow_emotion',L)}</div>"
if old1 in src:
    src = src.replace(old1, new1)
    changes += 1
    print("✅ 1. Fixed 'Emotie selecteren' → tx('flow_emotion',L)")
else:
    print("⚠️ 1. 'Emotie selecteren' not found")

# 2. Fix "Meelevend" emotion tag in chatflow
old2 = '>Meelevend</div>'
new2 = ">${{en:'Sympathetic',nl:'Meelevend',zh:'同理',de:'Mitfühlend',fr:'Compatissant',ja:'共感的',es:'Comprensivo'}[L]||'Sympathetic'}</div>"
if old2 in src:
    src = src.replace(old2, new2)
    changes += 1
    print("✅ 2. Fixed 'Meelevend' → multilingual")
else:
    print("⚠️ 2. 'Meelevend' not found")

# 3. Fix "Add-ons" label in pricing (the one defined inline as addonLbl)
old3 = "addonLbl={en:'Add-ons',nl:'Add-ons',zh:'附加選項',de:'Add-ons',fr:'Options',ja:'オプション',es:'Complementos'};"
new3 = "addonLbl=tx('pr_addons_title',L);"
if old3 in src:
    src = src.replace(old3, new3)
    changes += 1
    print("✅ 3. Fixed Add-ons label to use TX")
else:
    print("⚠️ 3. addonLbl inline definition not found")

# 4. Fix addonLbl[L] references to just addonLbl (now string)
old4a = '${addonLbl[L]||addonLbl.en}'
new4a = '${addonLbl}'
if old4a in src:
    src = src.replace(old4a, new4a)
    changes += 1
    print("✅ 4. Fixed addonLbl reference")
else:
    print("⚠️ 4. addonLbl reference not found")

# 5. Fix BOOK A CALL / book a call in thankyou
old5 = '>BOOK A CALL →</a>'
if old5 in src:
    src = src.replace(old5, ">${tx('ty_book_call',L)} →</a>")
    changes += 1
    print("✅ 5. Fixed BOOK A CALL button")
else:
    # Try other patterns
    import re
    m = re.search(r'>BOOK A CALL[^<]*</a>', src)
    if m:
        src = src.replace(m.group(), ">${tx('ty_book_call',L)} →</a>")
        changes += 1
        print(f"✅ 5. Fixed BOOK A CALL (pattern: {m.group()[:40]})")
    else:
        m2 = re.search(r'BOOK A CALL', src)
        if m2:
            print(f"⚠️ 5. Found 'BOOK A CALL' at pos {m2.start()} but couldn't match full pattern")
        else:
            print("⚠️ 5. 'BOOK A CALL' not in file at all")

# 6. Fix "Ondersteuning voor" in thankyou (Dutch-only audience line)
# Check if there's an audience line that needs translation
old6 = 'Ondersteuning voor'
if old6 in src:
    # Find the context around it
    idx = src.index(old6)
    context = src[idx-100:idx+200]
    print(f"ℹ️ 6. Found 'Ondersteuning voor' — context: ...{src[idx:idx+80]}...")
    # This needs a more targeted fix based on context
else:
    print("⚠️ 6. 'Ondersteuning voor' not found")

# 7. Increase max_tokens from 1200 to 4096 for AI generation
old7 = 'max_tokens:1200'
new7 = 'max_tokens:4096'
if old7 in src:
    src = src.replace(old7, new7)
    changes += 1
    print("✅ 7. Increased max_tokens 1200 → 4096")
else:
    if 'max_tokens:4096' in src:
        print("✅ 7. max_tokens already at 4096")
    elif 'max_tokens:1000' in src:
        src = src.replace('max_tokens:1000', 'max_tokens:4096')
        changes += 1
        print("✅ 7. Increased max_tokens 1000 → 4096")
    else:
        # Search for any max_tokens
        import re
        m = re.search(r'max_tokens:\s*(\d+)', src)
        if m:
            print(f"ℹ️ 7. max_tokens currently at {m.group(1)}")
        else:
            print("⚠️ 7. max_tokens not found")

with open('index.html','w',encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

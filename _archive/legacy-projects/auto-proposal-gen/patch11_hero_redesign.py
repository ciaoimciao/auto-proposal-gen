#!/usr/bin/env python3
"""Redesign setup/landing page with flux-card-hero visual style.
Light gradient bg, floating glass nav, large thin headings, animated cards.
All form functionality stays intact."""

with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

changes = 0

# ─── 1. SETUP VIEW background: dark → light gradient ───
old = '#setup-view{min-height:100vh;background:var(--sb);background-image:radial-gradient(ellipse 80% 50% at 50% -20%,rgba(255,107,61,.08),transparent);}'
new = '#setup-view{min-height:100vh;background:linear-gradient(135deg,#EDE9FE,#FCE7F3,#EDE9FE);}'
if old in src:
    src = src.replace(old, new)
    changes += 1
    print("✅ 1. Setup bg → light purple-pink gradient")
else:
    print("⚠️ 1. Setup bg pattern not found")

# ─── 2. NAVBAR: sticky dark → floating glassmorphism centered ───
old_sn = '.sn{display:flex;align-items:center;justify-content:space-between;padding:1rem 3rem;border-bottom:1px solid var(--bdr);background:rgba(10,10,10,.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);position:sticky;top:0;z-index:100;}'
new_sn = '.sn{display:flex;align-items:center;justify-content:space-between;padding:.65rem 1.5rem;background:rgba(255,255,255,.8);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:16px;border:1px solid rgba(255,255,255,.25);box-shadow:0 4px 24px rgba(0,0,0,.06);position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:100;width:calc(100% - 80px);max-width:960px;}'
if old_sn in src:
    src = src.replace(old_sn, new_sn)
    changes += 1
    print("✅ 2. Navbar → floating glassmorphism")
else:
    print("⚠️ 2. Navbar pattern not found")

# ─── 3. Logo color: light text → dark text ───
old_logo = '.sn-logo{font-family:\'Syne\',sans-serif;font-weight:800;font-size:1.3rem;letter-spacing:-.04em;}'
new_logo = '.sn-logo{font-family:\'Syne\',sans-serif;font-weight:800;font-size:1.3rem;letter-spacing:-.04em;color:#111827;}'
if old_logo in src:
    src = src.replace(old_logo, new_logo)
    changes += 1
    print("✅ 3. Logo → dark text")
else:
    print("⚠️ 3. Logo pattern not found")

# ─── 4. Chip style → dark pill ───
old_chip = '.sn-chip{font-size:.7rem;background:var(--or);color:#fff;padding:3px 10px;border-radius:20px;font-weight:600;}'
new_chip = '.sn-chip{font-size:.7rem;background:#111827;color:#fff;padding:4px 12px;border-radius:20px;font-weight:600;}'
if old_chip in src:
    src = src.replace(old_chip, new_chip)
    changes += 1
    print("✅ 4. Chip → dark style")
else:
    print("⚠️ 4. Chip pattern not found")

# ─── 5. Hero section: 2-col grid → centered with large thin heading ───
old_sh = '.sh{padding:4rem 3rem 3rem;max-width:1000px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;}'
new_sh = '.sh{padding:7rem 3rem 3rem;max-width:1000px;margin:0 auto;display:flex;flex-direction:column;align-items:center;text-align:center;gap:2rem;}'
if old_sh in src:
    src = src.replace(old_sh, new_sh)
    changes += 1
    print("✅ 5. Hero → centered column layout")
else:
    print("⚠️ 5. Hero layout not found")

# ─── 6. Eyebrow → smaller, purple accent ───
old_eye = '.sh-eyebrow{font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--or);margin-bottom:.85rem;}'
new_eye = '.sh-eyebrow{font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#7C3AED;margin-bottom:.85rem;display:inline-flex;align-items:center;gap:6px;padding:4px 14px;background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.15);border-radius:20px;}'
if old_eye in src:
    src = src.replace(old_eye, new_eye)
    changes += 1
    print("✅ 6. Eyebrow → purple pill badge")
else:
    print("⚠️ 6. Eyebrow not found")

# ─── 7. Title → large thin dark heading ───
old_ttl = '.sh-title{font-family:\'Syne\',sans-serif;font-weight:800;font-size:2.8rem;line-height:1.05;letter-spacing:-.05em;margin-bottom:1rem;}'
new_ttl = '.sh-title{font-family:\'Syne\',sans-serif;font-weight:300;font-size:clamp(2.5rem,5vw,4.5rem);line-height:1.05;letter-spacing:-.04em;margin-bottom:1rem;color:#111827;}'
if old_ttl in src:
    src = src.replace(old_ttl, new_ttl)
    changes += 1
    print("✅ 7. Title → large thin dark heading")
else:
    print("⚠️ 7. Title not found")

# ─── 8. Title em color ───
old_em = '.sh-title em{color:var(--or);font-style:normal;}'
new_em = '.sh-title em{color:#7C3AED;font-style:normal;font-weight:500;}'
if old_em in src:
    src = src.replace(old_em, new_em)
    changes += 1
    print("✅ 8. Title em → purple accent")
else:
    print("⚠️ 8. Title em not found")

# ─── 9. Subtitle → gray ───
old_sub = '.sh-sub{font-size:.95rem;color:var(--ink2);line-height:1.7;margin-bottom:1.75rem;}'
new_sub = '.sh-sub{font-size:1rem;color:#6B7280;line-height:1.7;margin-bottom:1.75rem;max-width:560px;}'
if old_sub in src:
    src = src.replace(old_sub, new_sub)
    changes += 1
    print("✅ 9. Subtitle → gray, centered")
else:
    print("⚠️ 9. Subtitle not found")

# ─── 10. CTA → black rounded button ───
old_cta = '.sh-cta{display:inline-flex;align-items:center;gap:8px;background:var(--or);color:#fff;font-family:\'Syne\',sans-serif;font-weight:700;font-size:.88rem;padding:.65rem 1.5rem;border-radius:40px;cursor:pointer;border:none;transition:transform .15s,box-shadow .15s;}'
new_cta = '.sh-cta{display:inline-flex;align-items:center;gap:8px;background:#111827;color:#fff;font-family:\'Syne\',sans-serif;font-weight:700;font-size:.88rem;padding:.7rem 1.75rem;border-radius:12px;cursor:pointer;border:none;transition:all .2s ease;}'
if old_cta in src:
    src = src.replace(old_cta, new_cta)
    changes += 1
    print("✅ 10. CTA → black rounded-lg button")
else:
    print("⚠️ 10. CTA not found")

old_cta_hov = '.sh-cta:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(17,17,16,.2);}'
new_cta_hov = '.sh-cta:hover{transform:scale(1.05);box-shadow:0 8px 24px rgba(17,17,16,.18);background:#1F2937;}'
if old_cta_hov in src:
    src = src.replace(old_cta_hov, new_cta_hov)
    changes += 1
    print("✅ 11. CTA hover → scale effect")
else:
    print("⚠️ 11. CTA hover not found")

# ─── 12. Stats cards → glassmorphism horizontal row ───
old_stats = '.sh-stats{display:flex;flex-direction:column;gap:.65rem;}'
new_stats = '.sh-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:.75rem;width:100%;max-width:900px;}'
if old_stats in src:
    src = src.replace(old_stats, new_stats)
    changes += 1
    print("✅ 12. Stats → 4-col grid")
else:
    print("⚠️ 12. Stats layout not found")

old_stat = '.sh-stat{background:var(--sb2);border:1px solid var(--bdr);border-radius:14px;padding:1rem 1.25rem;display:flex;align-items:center;gap:12px;}'
new_stat = '.sh-stat{background:rgba(255,255,255,.45);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.5);border-radius:16px;padding:1rem 1rem;display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;transition:transform .2s,box-shadow .2s;}'
if old_stat in src:
    src = src.replace(old_stat, new_stat)
    changes += 1
    print("✅ 13. Stat card → glassmorphism")
else:
    print("⚠️ 13. Stat card not found")

# ─── 14. Stat value & label colors ───
old_val = '.sh-stat-val{font-family:\'Syne\',sans-serif;font-weight:800;font-size:1.35rem;letter-spacing:-.04em;}'
new_val = '.sh-stat-val{font-family:\'Syne\',sans-serif;font-weight:700;font-size:1rem;letter-spacing:-.02em;color:#111827;}'
if old_val in src:
    src = src.replace(old_val, new_val)
    changes += 1
    print("✅ 14. Stat value → dark text")
else:
    print("⚠️ 14. Stat value not found")

old_lbl = '.sh-stat-lbl{font-size:.78rem;color:var(--mu);}'
new_lbl = '.sh-stat-lbl{font-size:.72rem;color:#6B7280;line-height:1.4;}'
if old_lbl in src:
    src = src.replace(old_lbl, new_lbl)
    changes += 1
    print("✅ 15. Stat label → gray")
else:
    print("⚠️ 15. Stat label not found")

# ─── 16. Form wrapper ───
old_sf = '.sf{max-width:1000px;margin:0 auto;padding:0 3rem 5rem;}'
new_sf = '.sf{max-width:720px;margin:0 auto;padding:2rem 3rem 5rem;}'
if old_sf in src:
    src = src.replace(old_sf, new_sf)
    changes += 1
    print("✅ 16. Form → narrower, centered")
else:
    print("⚠️ 16. Form wrapper not found")

# ─── 17. Section header ───
old_sec_hdr = '.sec-hdr{display:flex;align-items:center;gap:10px;margin-bottom:1rem;padding-bottom:.6rem;border-bottom:1px solid rgba(255,255,255,.06);}'
new_sec_hdr = '.sec-hdr{display:flex;align-items:center;gap:10px;margin-bottom:1rem;padding-bottom:.6rem;border-bottom:1px solid rgba(0,0,0,.06);}'
if old_sec_hdr in src:
    src = src.replace(old_sec_hdr, new_sec_hdr)
    changes += 1
    print("✅ 17. Section header border → light mode")
else:
    print("⚠️ 17. Section header not found")

# ─── 18. Section number badge ───
old_sec_num = '.sec-num{width:26px;height:26px;border-radius:50%;background:var(--ink);color:#fff;font-family:\'Syne\',sans-serif;font-size:.72rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;}'
new_sec_num = '.sec-num{width:26px;height:26px;border-radius:50%;background:#7C3AED;color:#fff;font-family:\'Syne\',sans-serif;font-size:.72rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;}'
if old_sec_num in src:
    src = src.replace(old_sec_num, new_sec_num)
    changes += 1
    print("✅ 18. Section num → purple badge")
else:
    print("⚠️ 18. Section num not found")

# ─── 19. Section title ───
old_sec_ttl = '.sec-ttl{font-family:\'Syne\',sans-serif;font-weight:700;font-size:1rem;letter-spacing:-.02em;}'
new_sec_ttl = '.sec-ttl{font-family:\'Syne\',sans-serif;font-weight:700;font-size:1rem;letter-spacing:-.02em;color:#111827;}'
if old_sec_ttl in src:
    src = src.replace(old_sec_ttl, new_sec_ttl)
    changes += 1
    print("✅ 19. Section title → dark")
else:
    print("⚠️ 19. Section title not found")

# ─── 20. Section subtitle ───
old_sec_sub = '.sec-sub{font-size:.8rem;color:var(--mu);}'
new_sec_sub = '.sec-sub{font-size:.8rem;color:#6B7280;}'
if old_sec_sub in src:
    src = src.replace(old_sec_sub, new_sec_sub)
    changes += 1
    print("✅ 20. Section subtitle → gray")
else:
    print("⚠️ 20. Section subtitle not found")

# ─── 21. Form label ───
old_fl = '.fl{display:block;font-size:.68rem;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--mu);margin-bottom:.35rem;}'
new_fl = '.fl{display:block;font-size:.68rem;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:#4B5563;margin-bottom:.35rem;}'
if old_fl in src:
    src = src.replace(old_fl, new_fl)
    changes += 1
    print("✅ 21. Form label → dark gray")
else:
    print("⚠️ 21. Form label not found")

# ─── 22. Input field → light glassmorphism ───
old_fi = '.fi{width:100%;background:var(--sb2);border:1.5px solid var(--bdr);border-radius:10px;padding:.6rem .9rem;color:var(--ink);font-family:\'Inter\',\'DM Sans\',sans-serif;font-size:.88rem;transition:border-color .2s,box-shadow .2s;outline:none;}'
new_fi = '.fi{width:100%;background:rgba(255,255,255,.6);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1.5px solid rgba(0,0,0,.1);border-radius:10px;padding:.6rem .9rem;color:#111827;font-family:\'Inter\',\'DM Sans\',sans-serif;font-size:.88rem;transition:border-color .2s,box-shadow .2s;outline:none;}'
if old_fi in src:
    src = src.replace(old_fi, new_fi)
    changes += 1
    print("✅ 22. Input → light glassmorphism")
else:
    print("⚠️ 22. Input not found")

# ─── 23. Input focus ───
old_focus = '.fi:focus{border-color:var(--or);box-shadow:0 0 0 3px rgba(255,107,61,.1);}'
new_focus = '.fi:focus{border-color:#7C3AED;box-shadow:0 0 0 3px rgba(124,58,237,.1);}'
if old_focus in src:
    src = src.replace(old_focus, new_focus)
    changes += 1
    print("✅ 23. Input focus → purple")
else:
    print("⚠️ 23. Input focus not found")

# ─── 24. Placeholder ───
old_ph = '.fi::placeholder{color:var(--mu);}'
new_ph = '.fi::placeholder{color:#9CA3AF;}'
if old_ph in src:
    src = src.replace(old_ph, new_ph)
    changes += 1
    print("✅ 24. Placeholder → light gray")
else:
    print("⚠️ 24. Placeholder not found")

# ─── 25. Calendar trigger ───
old_cal = '.cal-trig{width:100%;background:var(--sb2);border:1.5px solid var(--bdr);border-radius:10px;padding:.6rem .9rem;color:var(--ink);font-family:\'DM Sans\',sans-serif;font-size:.88rem;cursor:pointer;text-align:left;display:flex;align-items:center;justify-content:space-between;transition:border-color .2s;}'
new_cal = '.cal-trig{width:100%;background:rgba(255,255,255,.6);backdrop-filter:blur(8px);border:1.5px solid rgba(0,0,0,.1);border-radius:10px;padding:.6rem .9rem;color:#111827;font-family:\'DM Sans\',sans-serif;font-size:.88rem;cursor:pointer;text-align:left;display:flex;align-items:center;justify-content:space-between;transition:border-color .2s;}'
if old_cal in src:
    src = src.replace(old_cal, new_cal)
    changes += 1
    print("✅ 25. Calendar trigger → light")
else:
    print("⚠️ 25. Calendar trigger not found")

# ─── 26. Calendar hover ───
old_cal_h = '.cal-trig:hover,.cal-trig.open{border-color:var(--or);}'
new_cal_h = '.cal-trig:hover,.cal-trig.open{border-color:#7C3AED;}'
if old_cal_h in src:
    src = src.replace(old_cal_h, new_cal_h)
    changes += 1
    print("✅ 26. Calendar hover → purple")
else:
    print("⚠️ 26. Calendar hover not found")

# ─── 27. Calendar popup ───
old_pop = '.cal-pop{position:absolute;top:calc(100% + 5px);left:0;z-index:400;background:var(--sb2);border:1.5px solid var(--bdr);border-radius:14px;padding:1rem;width:272px;box-shadow:0 10px 36px rgba(17,17,16,.12);}'
new_pop = '.cal-pop{position:absolute;top:calc(100% + 5px);left:0;z-index:400;background:rgba(255,255,255,.9);backdrop-filter:blur(12px);border:1.5px solid rgba(0,0,0,.08);border-radius:14px;padding:1rem;width:272px;box-shadow:0 10px 36px rgba(0,0,0,.1);}'
if old_pop in src:
    src = src.replace(old_pop, new_pop)
    changes += 1
    print("✅ 27. Calendar popup → light glass")
else:
    print("⚠️ 27. Calendar popup not found")

# ─── 28. Calendar month label ───
old_cmon = '.cal-mon{font-family:\'Syne\',sans-serif;font-size:.85rem;font-weight:700;}'
new_cmon = '.cal-mon{font-family:\'Syne\',sans-serif;font-size:.85rem;font-weight:700;color:#111827;}'
if old_cmon in src:
    src = src.replace(old_cmon, new_cmon)
    changes += 1
    print("✅ 28. Calendar month → dark text")
else:
    print("⚠️ 28. Calendar month not found")

# ─── 29. Calendar nav buttons ───
old_cnav = '.cal-nav{background:none;border:1px solid var(--bdr);cursor:pointer;color:var(--ink2);font-size:1rem;padding:1px 7px;border-radius:7px;transition:all .15s;}'
new_cnav = '.cal-nav{background:none;border:1px solid rgba(0,0,0,.1);cursor:pointer;color:#6B7280;font-size:1rem;padding:1px 7px;border-radius:7px;transition:all .15s;}'
if old_cnav in src:
    src = src.replace(old_cnav, new_cnav)
    changes += 1
    print("✅ 29. Calendar nav → light mode")
else:
    print("⚠️ 29. Calendar nav not found")

# ─── 30. Calendar nav hover ───
old_cnav_h = '.cal-nav:hover{border-color:var(--or);color:var(--or);}'
new_cnav_h = '.cal-nav:hover{border-color:#7C3AED;color:#7C3AED;}'
if old_cnav_h in src:
    src = src.replace(old_cnav_h, new_cnav_h)
    changes += 1
    print("✅ 30. Calendar nav hover → purple")
else:
    print("⚠️ 30. Calendar nav hover not found")

# ─── 31. Calendar DOW ───
old_cdow = '.cal-dow{font-size:.6rem;text-align:center;color:var(--mu);padding-bottom:4px;font-weight:600;}'
new_cdow = '.cal-dow{font-size:.6rem;text-align:center;color:#9CA3AF;padding-bottom:4px;font-weight:600;}'
if old_cdow in src:
    src = src.replace(old_cdow, new_cdow)
    changes += 1
    print("✅ 31. Calendar DOW → light gray")
else:
    print("⚠️ 31. Calendar DOW not found")

# ─── 32. Calendar day ───
old_cday = '.cal-day{aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:.78rem;border-radius:7px;cursor:pointer;color:var(--ink2);transition:all .15s;}'
new_cday = '.cal-day{aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:.78rem;border-radius:7px;cursor:pointer;color:#374151;transition:all .15s;}'
if old_cday in src:
    src = src.replace(old_cday, new_cday)
    changes += 1
    print("✅ 32. Calendar day → dark text")
else:
    print("⚠️ 32. Calendar day not found")

# ─── 33. Calendar day hover ───
old_cday_h = '.cal-day:hover:not(.empty):not(.disabled){background:rgba(255,107,61,.1);color:var(--or);}'
new_cday_h = '.cal-day:hover:not(.empty):not(.disabled){background:rgba(124,58,237,.1);color:#7C3AED;}'
if old_cday_h in src:
    src = src.replace(old_cday_h, new_cday_h)
    changes += 1
    print("✅ 33. Calendar day hover → purple")
else:
    print("⚠️ 33. Calendar day hover not found")

# ─── 34. Calendar today ───
old_ctod = '.cal-day.today{border:1.5px solid var(--or);color:var(--or);font-weight:600;}'
new_ctod = '.cal-day.today{border:1.5px solid #7C3AED;color:#7C3AED;font-weight:600;}'
if old_ctod in src:
    src = src.replace(old_ctod, new_ctod)
    changes += 1
    print("✅ 34. Calendar today → purple")
else:
    print("⚠️ 34. Calendar today not found")

# ─── 35. Calendar selected ───
old_csel = '.cal-day.selected{background:var(--or)!important;color:#fff!important;font-weight:700;}'
new_csel = '.cal-day.selected{background:#7C3AED!important;color:#fff!important;font-weight:700;}'
if old_csel in src:
    src = src.replace(old_csel, new_csel)
    changes += 1
    print("✅ 35. Calendar selected → purple")
else:
    print("⚠️ 35. Calendar selected not found")

# ─── 36. Calendar foot ───
old_cfoot = '.cal-foot{margin-top:.65rem;padding-top:.65rem;border-top:1px solid var(--bdr);display:flex;align-items:center;justify-content:space-between;}'
new_cfoot = '.cal-foot{margin-top:.65rem;padding-top:.65rem;border-top:1px solid rgba(0,0,0,.06);display:flex;align-items:center;justify-content:space-between;}'
if old_cfoot in src:
    src = src.replace(old_cfoot, new_cfoot)
    changes += 1
    print("✅ 36. Calendar foot → light border")
else:
    print("⚠️ 36. Calendar foot not found")

# ─── 37. Calendar clear button ───
old_cclr = '.cal-clr{background:none;border:none;color:var(--mu);font-size:.74rem;cursor:pointer;font-family:\'DM Sans\',sans-serif;}'
new_cclr = '.cal-clr{background:none;border:none;color:#6B7280;font-size:.74rem;cursor:pointer;font-family:\'DM Sans\',sans-serif;}'
if old_cclr in src:
    src = src.replace(old_cclr, new_cclr)
    changes += 1
    print("✅ 37. Calendar clear → gray")
else:
    print("⚠️ 37. Calendar clear not found")

# ─── 38. Calendar OK button ───
old_cok = '.cal-ok{background:var(--or);border:none;border-radius:8px;padding:4px 14px;font-size:.76rem;font-weight:700;font-family:\'Syne\',sans-serif;color:#fff;cursor:pointer;}'
new_cok = '.cal-ok{background:#7C3AED;border:none;border-radius:8px;padding:4px 14px;font-size:.76rem;font-weight:700;font-family:\'Syne\',sans-serif;color:#fff;cursor:pointer;}'
if old_cok in src:
    src = src.replace(old_cok, new_cok)
    changes += 1
    print("✅ 38. Calendar OK → purple")
else:
    print("⚠️ 38. Calendar OK not found")

# ─── 39. Roadmap preview ───
old_rm = '.rm-prev{margin-top:.65rem;background:rgba(255,107,61,.08);border:1.5px solid rgba(255,107,61,.2);border-radius:10px;padding:.65rem .9rem;display:none;}'
new_rm = '.rm-prev{margin-top:.65rem;background:rgba(124,58,237,.06);border:1.5px solid rgba(124,58,237,.15);border-radius:10px;padding:.65rem .9rem;display:none;}'
if old_rm in src:
    src = src.replace(old_rm, new_rm)
    changes += 1
    print("✅ 39. Roadmap preview → purple tint")
else:
    print("⚠️ 39. Roadmap preview not found")

# ─── 40. Roadmap preview title ───
old_rmttl = '.rm-prev-ttl{font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;color:var(--or);font-weight:600;margin-bottom:.4rem;}'
new_rmttl = '.rm-prev-ttl{font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;color:#7C3AED;font-weight:600;margin-bottom:.4rem;}'
if old_rmttl in src:
    src = src.replace(old_rmttl, new_rmttl)
    changes += 1
    print("✅ 40. Roadmap title → purple")
else:
    print("⚠️ 40. Roadmap title not found")

# ─── 41. Roadmap date ───
old_rmd = '.rm-pi-d{color:var(--or);min-width:82px;font-weight:600;}'
new_rmd = '.rm-pi-d{color:#7C3AED;min-width:82px;font-weight:600;}'
if old_rmd in src:
    src = src.replace(old_rmd, new_rmd)
    changes += 1
    print("✅ 41. Roadmap date → purple")
else:
    print("⚠️ 41. Roadmap date not found")

# ─── 42. Roadmap item text ───
old_rmi = '.rm-pi{font-size:.78rem;color:var(--ink2);display:flex;gap:8px;line-height:1.65;}'
new_rmi = '.rm-pi{font-size:.78rem;color:#4B5563;display:flex;gap:8px;line-height:1.65;}'
if old_rmi in src:
    src = src.replace(old_rmi, new_rmi)
    changes += 1
    print("✅ 42. Roadmap item → gray")
else:
    print("⚠️ 42. Roadmap item not found")

# ─── 43. API hint ───
old_api = '.api-hint{font-size:.7rem;color:var(--mu);margin-top:.3rem;}'
new_api = '.api-hint{font-size:.7rem;color:#6B7280;margin-top:.3rem;}'
if old_api in src:
    src = src.replace(old_api, new_api)
    changes += 1
    print("✅ 43. API hint → gray")
else:
    print("⚠️ 43. API hint not found")

# ─── 44. AI status text ───
old_aist = '.ai-st{font-size:.74rem;color:var(--mu);}'
new_aist = '.ai-st{font-size:.74rem;color:#6B7280;}'
if old_aist in src:
    src = src.replace(old_aist, new_aist)
    changes += 1
    print("✅ 44. AI status → gray")
else:
    print("⚠️ 44. AI status not found")

# ─── 45. Context box → light glassmorphism ───
old_ctx = '.ctx-box{margin-top:.75rem;padding:.85rem 1rem;background:var(--sb2);border-radius:10px;border:1.5px solid var(--bdr);}'
new_ctx = '.ctx-box{margin-top:.75rem;padding:.85rem 1rem;background:rgba(255,255,255,.4);backdrop-filter:blur(8px);border-radius:10px;border:1.5px solid rgba(0,0,0,.06);}'
if old_ctx in src:
    src = src.replace(old_ctx, new_ctx)
    changes += 1
    print("✅ 45. Context box → light glass")
else:
    print("⚠️ 45. Context box not found")

# ─── 46. Context label ───
old_ctxl = '.ctx-lbl{font-size:.68rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--mu);margin-bottom:.6rem;}'
new_ctxl = '.ctx-lbl{font-size:.68rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:#6B7280;margin-bottom:.6rem;}'
if old_ctxl in src:
    src = src.replace(old_ctxl, new_ctxl)
    changes += 1
    print("✅ 46. Context label → gray")
else:
    print("⚠️ 46. Context label not found")

# ─── 47. Generate button → dark with purple hover ───
old_gen = '.btn-gen{width:100%;padding:.9rem 2rem;background:var(--or);color:#fff;border:none;border-radius:40px;font-family:\'Syne\',sans-serif;font-size:1rem;font-weight:700;cursor:pointer;transition:transform .15s,box-shadow .15s;margin-top:1.25rem;}'
new_gen = '.btn-gen{width:100%;padding:.9rem 2rem;background:#111827;color:#fff;border:none;border-radius:12px;font-family:\'Syne\',sans-serif;font-size:1rem;font-weight:700;cursor:pointer;transition:all .2s ease;margin-top:1.25rem;}'
if old_gen in src:
    src = src.replace(old_gen, new_gen)
    changes += 1
    print("✅ 47. Generate btn → dark rounded")
else:
    print("⚠️ 47. Generate btn not found")

old_gen_h = '.btn-gen:hover{transform:translateY(-1px);box-shadow:0 8px 28px rgba(255,107,61,.35);}'
new_gen_h = '.btn-gen:hover{transform:scale(1.02);box-shadow:0 8px 28px rgba(17,24,39,.25);background:#1F2937;}'
if old_gen_h in src:
    src = src.replace(old_gen_h, new_gen_h)
    changes += 1
    print("✅ 48. Generate btn hover → scale")
else:
    print("⚠️ 48. Generate btn hover not found")

# ─── 49. Fix inline styles in HTML that reference dark-mode vars ───
# Golden box border
old_gbox = 'border-color:rgba(255,107,61,.3);background:rgba(255,107,61,.04)'
new_gbox = 'border-color:rgba(124,58,237,.25);background:rgba(124,58,237,.04)'
if old_gbox in src:
    src = src.replace(old_gbox, new_gbox)
    changes += 1
    print("✅ 49. Golden box → purple tint")
else:
    print("⚠️ 49. Golden box not found")

# Golden box label color
old_glbl = 'style="color:var(--or);">🎯 Most important'
new_glbl = 'style="color:#7C3AED;">🎯 Most important'
if old_glbl in src:
    src = src.replace(old_glbl, new_glbl)
    changes += 1
    print("✅ 50. Golden box label → purple")
else:
    print("⚠️ 50. Golden box label not found")

# Quote highlight color
old_qc = 'style="color:var(--or);font-weight:700;">Quote them directly'
new_qc = 'style="color:#7C3AED;font-weight:700;">Quote them directly'
if old_qc in src:
    src = src.replace(old_qc, new_qc)
    changes += 1
    print("✅ 51. Quote highlight → purple")
else:
    print("⚠️ 51. Quote highlight not found")

# Tools subtitle color
old_tc = 'style="color:var(--mu);font-weight:400;">(what Notso.ai replaces)'
new_tc = 'style="color:#6B7280;font-weight:400;">(what Notso.ai replaces)'
if old_tc in src:
    src = src.replace(old_tc, new_tc)
    changes += 1
    print("✅ 52. Tools subtitle → gray")
else:
    print("⚠️ 52. Tools subtitle not found")

# ─── 53. Generates tags in AI section ───
old_tag_bg = 'background:var(--sb);border:1px solid var(--bdr);color:var(--ink2)'
new_tag_bg = 'background:rgba(255,255,255,.5);border:1px solid rgba(0,0,0,.08);color:#4B5563'
count = src.count(old_tag_bg)
if count > 0:
    src = src.replace(old_tag_bg, new_tag_bg)
    changes += 1
    print(f"✅ 53. AI tags → light glass ({count} occurrences)")
else:
    print("⚠️ 53. AI tags not found")

# AI section box bg
old_ai_box = 'background:var(--sb2);border-radius:8px;border:1.5px solid var(--bdr)'
new_ai_box = 'background:rgba(255,255,255,.4);border-radius:8px;border:1.5px solid rgba(0,0,0,.06)'
if old_ai_box in src:
    src = src.replace(old_ai_box, new_ai_box)
    changes += 1
    print("✅ 54. AI section box → light")
else:
    print("⚠️ 54. AI section box not found")

# "Generates:" label
old_gen_lbl = 'font-size:.66rem;color:var(--mu)'
new_gen_lbl = 'font-size:.66rem;color:#6B7280'
if old_gen_lbl in src:
    src = src.replace(old_gen_lbl, new_gen_lbl)
    changes += 1
    print("✅ 55. Generates label → gray")
else:
    print("⚠️ 55. Generates label not found")

# Cal display color
old_cdisp = '<span id="cal-disp" style="color:var(--mu);">'
new_cdisp = '<span id="cal-disp" style="color:#9CA3AF;">'
if old_cdisp in src:
    src = src.replace(old_cdisp, new_cdisp)
    changes += 1
    print("✅ 56. Calendar display → light gray")
else:
    print("⚠️ 56. Calendar display not found")

# API link color
old_alink = 'style="color:var(--or);">Get a key'
new_alink = 'style="color:#7C3AED;">Get a key'
if old_alink in src:
    src = src.replace(old_alink, new_alink)
    changes += 1
    print("✅ 57. API link → purple")
else:
    print("⚠️ 57. API link not found")

# ─── 58. Add hover animation to stat cards (insert after .sh-stat-lbl) ───
insert_after = new_lbl  # .sh-stat-lbl definition we just set
hover_css = '\n.sh-stat:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.06);}'
if hover_css not in src:
    src = src.replace(insert_after, insert_after + hover_css)
    changes += 1
    print("✅ 58. Added stat hover animation")
else:
    print("✅ 58. Stat hover already exists")

# ─── 59. Add smooth animation to setup page ───
# Insert keyframes before the DECK VIEW comment
deck_comment = '/* ═══════════════════════════════════════\n   DECK VIEW'
setup_anims = """/* Setup page animations */
@keyframes fadeInUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.sh{animation:fadeInUp .6s ease both;}
.sh-stats{animation:fadeInUp .6s ease .15s both;}
.sf{animation:fadeInUp .6s ease .3s both;}

"""
if '@keyframes fadeInUp' not in src and deck_comment in src:
    src = src.replace(deck_comment, setup_anims + deck_comment)
    changes += 1
    print("✅ 59. Added setup page animations")
else:
    print("⚠️ 59. Animation already exists or anchor not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print(f"\n✅ Done — {changes} changes applied.")

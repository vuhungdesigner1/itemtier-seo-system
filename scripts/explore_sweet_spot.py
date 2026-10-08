import csv
import json
from collections import defaultdict

csv_path = r"key/Tu_khoa_2.csv"

rows = []
with open(csv_path, "r", encoding="utf-16le") as f:
    for line in f:
        if line.startswith("Keyword\t"):
            break
    reader = csv.reader(f, delimiter="\t")
    for r in reader:
        if not r or len(r) < 3:
            continue
        kw = r[0].strip()
        if not kw:
            continue
        try:
            vol = int(r[2].strip().replace(',', ''))
        except ValueError:
            vol = 0
        comp = r[5].strip() if len(r) > 5 else "Unknown"
        comp_idx = r[6].strip() if len(r) > 6 else ""
        bid_low = r[7].strip() if len(r) > 7 else ""
        bid_high = r[8].strip() if len(r) > 8 else ""
        rows.append({
            "kw": kw, "vol": vol, "comp": comp, "comp_idx": comp_idx,
            "bid_low": bid_low, "bid_high": bid_high
        })

# Filter sweet spot: 10 <= vol <= 500 and comp in ('Low', 'Medium')
sweet = [r for r in rows if 10 <= r["vol"] <= 500 and r["comp"] in ("Low", "Medium")]

print(f"Total Low/Medium sweet spot: {len(sweet)}")
print("\nSorted by volume desc:")
for s in sorted(sweet, key=lambda x: (x["comp"] == "Low", x["vol"]), reverse=True)[:50]:
    print(f"[{s['comp']}] vol={s['vol']:<4} | {s['kw']}")

# Let's also check all keywords with 'tier list' or 'vs' or 'comparison' or 'alternatives' or 'budget' regardless of comp
print("\n--- ALL TIER LIST / VS / COMPARISON / ALTERNATIVE KEYWORDS ---")
intent_kws = [r for r in rows if any(w in r["kw"].lower() for w in ['tier list', ' vs ', 'versus', 'comparison', 'alternative', 'ranked'])]
for s in sorted(intent_kws, key=lambda x: x["vol"], reverse=True):
    print(f"[{s['comp']}] vol={s['vol']:<5} | {s['kw']}")

import csv
import io
import re
from collections import defaultdict

csv_path = r"key/Tu_khoa_2.csv"

rows = []
with open(csv_path, "r", encoding="utf-16le") as f:
    # Skip until header
    for line in f:
        if line.startswith("Keyword\t"):
            header = line.strip().split("\t")
            break
    
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if not row or len(row) < 3:
            continue
        kw = row[0].strip()
        if not kw:
            continue
        currency = row[1].strip() if len(row) > 1 else ""
        vol_str = row[2].strip() if len(row) > 2 else "0"
        try:
            vol = int(vol_str)
        except ValueError:
            vol = 0
            
        three_m = row[3].strip() if len(row) > 3 else ""
        yoy = row[4].strip() if len(row) > 4 else ""
        comp = row[5].strip() if len(row) > 5 else ""
        comp_idx = row[6].strip() if len(row) > 6 else ""
        bid_low = row[7].strip() if len(row) > 7 else ""
        bid_high = row[8].strip() if len(row) > 8 else ""
        
        rows.append({
            "keyword": kw,
            "volume": vol,
            "three_m": three_m,
            "yoy": yoy,
            "competition": comp,
            "competition_index": comp_idx,
            "bid_low": bid_low,
            "bid_high": bid_high
        })

print(f"Total parsed keywords: {len(rows)}")

# Sort by volume desc
rows_sorted = sorted(rows, key=lambda x: x["volume"], reverse=True)

# Print summary stats
vols = [r["volume"] for r in rows]
print(f"Max Volume: {max(vols)}, Min Volume: {min(vols)}")
print(f"Keywords with Volume >= 50: {len([r for r in rows if r['volume'] >= 50])}")
print(f"Keywords with 50 <= Volume <= 500: {len([r for r in rows if 50 <= r['volume'] <= 500])}")
print(f"Keywords with Volume > 500: {len([r for r in rows if r['volume'] > 500])}")

# Let's see some top keywords
print("\n--- TOP 25 BY VOLUME ---")
for r in rows_sorted[:25]:
    print(f"{r['keyword']}: vol={r['volume']}, comp={r['competition']} ({r['competition_index']})")

# Let's find keywords containing 'tier list' or 'ranked' or 'vs' or 'review' or 'best'
print("\n--- KEYWORDS WITH 'TIER LIST' OR 'RANKED' ---")
tier_kws = [r for r in rows if "tier list" in r["keyword"] or "ranked" in r["keyword"]]
for r in sorted(tier_kws, key=lambda x: x["volume"], reverse=True)[:20]:
    print(f"{r['keyword']}: vol={r['volume']}, comp={r['competition']}")

# Save clean json or inspect clusters

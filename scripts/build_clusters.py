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

print(f"Total rows: {len(rows)}")

# Let's search clusters:
# 1. Earbuds / TWS Tier List
c1 = [r for r in rows if any(x in r['kw'].lower() for x in ['earbud tier list', 'tws tier list', 'wireless earbuds tier list', 'true wireless earbuds tier list', 'best earbuds for phone calls'])]
print("\nCluster 1 (Earbuds):", c1)

# 2. Robot Vacuum Tier List & Pet Hair / Self-Emptying
c2 = [r for r in rows if ('robot vacuum tier list' in r['kw'].lower() or ('roomba' in r['kw'].lower() and ('pet' in r['kw'].lower() or 'hair' in r['kw'].lower() or 'review' in r['kw'].lower())) or 'shark ion robot for pet hair' in r['kw'].lower()) and r['vol'] <= 500]
print("\nCluster 2 (Robot Vacuum):", len(c2))
for x in c2[:10]:
    print(" ", x['comp'], x['vol'], x['kw'])

# 3. Mechanical Keyboard Switches Tier List
c3 = [r for r in rows if any(x in r['kw'].lower() for x in ['keyboard tier list', 'switches tier list', 'keyboard switches', 'keycap tier list', 'budget mechanical keyboard'])]
print("\nCluster 3 (Keyboard):", len(c3))
for x in c3:
    print(" ", x['comp'], x['vol'], x['kw'])

# 4. Air Purifier for Allergies & Tier List
c4 = [r for r in rows if ('air purifier tier list' in r['kw'].lower() or ('air purifier' in r['kw'].lower() and any(y in r['kw'].lower() for y in ['allerg', 'dander', 'pet hair']))) and r['vol'] <= 500]
print("\nCluster 4 (Air Purifier):", len(c4))
for x in c4[:10]:
    print(" ", x['comp'], x['vol'], x['kw'])

# 5. Espresso Machine Tier List & Beginner Picks
c5 = [r for r in rows if any(x in r['kw'].lower() for x in ['espresso machine tier list', 'espresso machine for beginners', 'breville espresso'])]
print("\nCluster 5 (Espresso):", len(c5))
for x in c5:
    print(" ", x['comp'], x['vol'], x['kw'])

# 6. Convection Toaster Oven vs Air Fryer
c6 = [r for r in rows if any(x in r['kw'].lower() for x in ['convection toaster oven vs air fryer', 'air fryer vs convection toaster', 'toaster oven vs convection oven vs air fryer', 'countertop convection oven vs air fryer', 'cuisinart convection toaster oven vs air fryer'])]
print("\nCluster 6 (Air Fryer vs Convection):", len(c6))
for x in c6:
    print(" ", x['comp'], x['vol'], x['kw'])

# 7. Dyson Stick Vacuum Alternatives
c7 = [r for r in rows if ('dyson' in r['kw'].lower() and any(x in r['kw'].lower() for x in ['alternative', 'ranked'])) and r['vol'] <= 500]
print("\nCluster 7 (Dyson Alternatives):", len(c7))
for x in sorted(c7, key=lambda z: z['vol'], reverse=True)[:15]:
    print(" ", x['comp'], x['vol'], x['kw'])

# 8. Sony WH-1000XM5 Alternatives & ANC Tier List
c8 = [r for r in rows if any(x in r['kw'].lower() for x in ['sony wh 1000xm5 alternative', 'sony xm5 alternative', 'noise cancelling headphones tier list', 'wh 1000xm5 alternative', 'sony wh1000xm5 alternatives'])]
print("\nCluster 8 (Sony XM5 Alternatives):", len(c8))
for x in c8:
    print(" ", x['comp'], x['vol'], x['kw'])

# 9. Smart Thermostats Comparison Guide
c9 = [r for r in rows if any(x in r['kw'].lower() for x in ['smart thermostats comparison', 'programmable thermostat comparison', 'are ecobee room sensors worth it', 'are smart thermostats worth it'])]
print("\nCluster 9 (Smart Thermostats):", len(c9))
for x in c9:
    print(" ", x['comp'], x['vol'], x['kw'])

# 10. Standing Desk Tier List & Converters
c10 = [r for r in rows if any(x in r['kw'].lower() for x in ['standing desk tier list', 'vivo vs flexispot', 'standing desk best 2022', 'varidesk vs vivo', 'vivo vs varidesk', 'uplift desk casters reddit'])]
print("\nCluster 10 (Standing Desk):", len(c10))
for x in c10:
    print(" ", x['comp'], x['vol'], x['kw'])

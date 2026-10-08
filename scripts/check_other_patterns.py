import csv

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
        rows.append({"kw": kw, "vol": vol, "comp": comp})

for pattern in ['wifi', 'lock', 'dash cam', 'power station', 'treadmill', 'ring', 'knife', 'water filter']:
    found = [r for r in rows if pattern in r['kw'].lower()]
    print(f"Pattern '{pattern}': {len(found)} keywords, top: {found[:3]}")

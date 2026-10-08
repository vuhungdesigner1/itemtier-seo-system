import csv, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

file_path = r'd:\AI AGENT\itemtier-seo-system\key\Tu_khoa_2.csv'

keywords = []
with open(file_path, mode='r', encoding='utf-16', errors='ignore') as f:
    reader = csv.reader(f, delimiter='\t')
    rows = list(reader)[3:]
    for r in rows:
        if len(r) > 6 and r[0].strip():
            kw = r[0].strip()
            try:
                vol = int(r[2].replace(',', '')) if r[2].strip() else 0
            except ValueError:
                vol = 0
            comp = r[5].strip()
            comp_val = int(r[6].strip()) if r[6].strip().isdigit() else -1
            keywords.append({'kw': kw, 'vol': vol, 'comp': comp, 'comp_val': comp_val})

print(f'Total: {len(keywords)}')
non_zero = [k for k in keywords if k['vol'] > 0]
print(f'Non-zero volume: {len(non_zero)}')

sweet_spot = [k for k in non_zero if 10 <= k['vol'] <= 500]
print(f'Sweet spot (10 <= vol <= 500): {len(sweet_spot)}')

low_med_sweet = [k for k in sweet_spot if k['comp'] in ('Low', 'Medium')]
print(f'Low/Med competition in sweet spot: {len(low_med_sweet)}')

categories = {
    'Robot Vacuum': ['vacuum', 'roomba', 'irobot', 'robotic'],
    'Mechanical Keyboard': ['keyboard', 'switches', 'keycap'],
    'Ergonomic Chair & Desk': ['chair', 'desk', 'herman miller', 'ergonomic', 'standing desk', 'converter'],
    'Audio (Earbuds & Headphones)': ['earbud', 'headphone', 'sony wh', 'anc', 'tws', 'airpod'],
    'Air Purifier': ['air purifier', 'purifier', 'allergies'],
    'Coffee & Espresso': ['espresso', 'coffee', 'breville'],
    'Smart Home (Lock & Thermostat)': ['smart lock', 'thermostat', 'lock', 'homekit'],
    'Monitors & Displays': ['monitor', 'oled', 'qled', 'gaming monitor'],
    'Smart Wearables & Fitness': ['smart ring', 'oura ring', 'walking pad', 'treadmill'],
    'Power & Charging Gear': ['power station', 'power bank', 'charger'],
    'Kitchen Gadgets': ['air fryer', 'knife', 'toaster', 'blender']
}

cat_counts = defaultdict(list)
for k in non_zero:
    kw_lower = k['kw'].lower()
    matched = False
    for cat, terms in categories.items():
        if any(t in kw_lower for t in terms):
            cat_counts[cat].append(k)
            matched = True
            break
    if not matched:
        cat_counts['Other'].append(k)

for cat, kw_list in cat_counts.items():
    print(f"{cat}: {len(kw_list)} keywords, total vol: {sum(x['vol'] for x in kw_list)}")

import json

with open("scripts/audit_rows.json", "r", encoding="utf-8") as f:
    rows = json.load(f)

# Sort by priority score desc, then word count desc
sorted_rows = sorted(rows, key=lambda x: (x["priority_score"], x["words"]), reverse=True)

# Select Top 20 across pillars
top_20 = sorted_rows[:20]

print(f"Top 20 Priority URLs for GSC Submission:")
for idx, r in enumerate(top_20, 1):
    print(f"{idx}. [{r['priority_score']}] {r['url']} | KW: {r['kw']} | Words: {r['words']}")

with open("scripts/top_20_gsc_urls.json", "w", encoding="utf-8") as f:
    json.dump(top_20, f, indent=2, ensure_ascii=False)

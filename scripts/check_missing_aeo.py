import json

with open("scripts/scanned_live_posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

missing_aeo = [p for p in posts if not p.get("has_aeo")]
print(f"Posts missing AEO box: {len(missing_aeo)}")
for p in missing_aeo:
    print(f"ID={p['id']}, Slug={p['slug']}, Status={p['status']}, Title={p['title'][:40]}")

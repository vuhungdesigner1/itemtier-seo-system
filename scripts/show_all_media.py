import json

with open("scripts/wp_media_inventory.json", "r", encoding="utf-8") as f:
    items = json.load(f)

for i in items:
    print(f"ID={i['id']} | Slug={i['slug']}")

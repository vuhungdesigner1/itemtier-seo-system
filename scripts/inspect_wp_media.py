import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {"Authorization": f"Basic {AUTH_TOKEN}"}

import json

r = requests.get(f"{WP_BASE}/media?per_page=100", headers=HEADERS, timeout=20)
if r.status_code == 200:
    items = r.json()
    print(f"Total media items fetched: {len(items)}")
    media_list = [{"id": i["id"], "slug": i["slug"], "url": i.get("source_url", "")} for i in items]
    with open("scripts/wp_media_inventory.json", "w", encoding="utf-8") as f:
        json.dump(media_list, f, indent=2)
    print("Saved to scripts/wp_media_inventory.json")


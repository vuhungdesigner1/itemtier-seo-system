import requests
import base64
import json

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {"Authorization": f"Basic {AUTH_TOKEN}"}

all_media = []
for page in range(1, 5):
    print(f"Fetching media page {page}...")
    r = requests.get(f"{WP_BASE}/media?page={page}&per_page=100", headers=HEADERS, timeout=25)
    if r.status_code == 200:
        items = r.json()
        if not items:
            break
        for i in items:
            all_media.append({
                "id": i["id"],
                "slug": i["slug"],
                "title": i["title"]["rendered"],
                "url": i.get("source_url", "")
            })
    else:
        break

print(f"Total media items fetched: {len(all_media)}")
with open("scripts/wp_media_inventory.json", "w", encoding="utf-8") as f:
    json.dump(all_media, f, indent=2, ensure_ascii=False)
print("Saved all media to scripts/wp_media_inventory.json")

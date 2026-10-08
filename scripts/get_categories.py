import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

r = requests.get(f"{WP_BASE}/categories?per_page=50", headers=HEADERS)
if r.status_code == 200:
    for c in r.json():
        print(f"ID={c['id']}, Name={c['name']}, Slug={c['slug']}")

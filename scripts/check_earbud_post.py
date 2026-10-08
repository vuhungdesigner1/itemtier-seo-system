import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

res = requests.get(f"{WP_BASE}/posts?slug=earbud-tier-list&status=any", headers=HEADERS, timeout=15)
print(f"Check slug 'earbud-tier-list': {res.status_code}")
posts = res.json()
print(f"Found: {len(posts)}")
for p in posts:
    print(f"ID={p['id']}, Status={p['status']}, Title={p['title']['rendered']}")

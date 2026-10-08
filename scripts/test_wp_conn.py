import requests
import base64
import json

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

try:
    res = requests.get(f"{WP_BASE}/posts?per_page=5&status=any", headers=HEADERS, timeout=15)
    print(f"Status Code: {res.status_code}")
    print(f"Total Posts Header: {res.headers.get('X-WP-Total')}")
    if res.status_code == 200:
        posts = res.json()
        print(f"Fetched {len(posts)} posts:")
        for p in posts:
            print(f"ID={p['id']}, Slug={p['slug']}, Status={p['status']}, Title={p['title']['rendered'][:50]}")
except Exception as e:
    print(f"Error: {e}")

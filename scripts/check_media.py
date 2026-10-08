import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

res = requests.get(f"{WP_BASE}/media?search=earbud&per_page=10", headers=HEADERS, timeout=15)
print(f"Media search 'earbud': {res.status_code}")
if res.status_code == 200:
    items = res.json()
    print(f"Found {len(items)} media items:")
    for it in items:
        print(f"ID={it['id']}, Title={it['title']['rendered']}, Source={it['source_url']}")

res2 = requests.get(f"{WP_BASE}/media?search=audio&per_page=10", headers=HEADERS, timeout=15)
print(f"\nMedia search 'audio': {res2.status_code}")
if res2.status_code == 200:
    items2 = res2.json()
    print(f"Found {len(items2)} media items:")
    for it in items2:
        print(f"ID={it['id']}, Title={it['title']['rendered']}, Source={it['source_url']}")

res3 = requests.get(f"{WP_BASE}/media?search=headphone&per_page=10", headers=HEADERS, timeout=15)
print(f"\nMedia search 'headphone': {res3.status_code}")
if res3.status_code == 200:
    items3 = res3.json()
    print(f"Found {len(items3)} media items:")
    for it in items3:
        print(f"ID={it['id']}, Title={it['title']['rendered']}, Source={it['source_url']}")

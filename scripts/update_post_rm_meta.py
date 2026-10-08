import requests
import base64

RM_BASE = "https://itemtier.com/wp-json/rankmath/v1"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()

HEADERS_JSON = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "objectID": 1497,
    "objectType": "post",
    "meta": {
        "rank_math_title": "Earbud Tier List: Best Wireless Earbuds Ranked (2026)",
        "rank_math_description": "Discover our definitive earbud tier list ranking the best wireless earbuds (S to D Tier) by sound, ANC, and battery. Find your perfect pair today!",
        "rank_math_focus_keyword": "earbud tier list"
    }
}

r = requests.post(f"{RM_BASE}/updateMeta", headers=HEADERS_JSON, json=payload, timeout=20)
print(f"Rank Math update status: {r.status_code}")
print(f"Response: {r.text}")

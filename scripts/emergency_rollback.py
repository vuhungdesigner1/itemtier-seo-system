import requests
import base64
import time
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()

HEADERS_JSON = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

target_ids = list(range(1500, 1509))
print("======================================================================")
print("   EMERGENCY ROLLBACK: REVERTING POSTS 1500 - 1508 TO DRAFT STATUS")
print("======================================================================")

results = []
for pid in target_ids:
    print(f"Reverting Post ID {pid} to 'draft'...")
    try:
        r = requests.post(f"{WP_BASE}/posts/{pid}", headers=HEADERS_JSON, json={"status": "draft"}, timeout=20)
        if r.status_code == 200:
            post = r.json()
            status = post.get("status")
            title = post.get("title", {}).get("rendered", "")
            print(f"  SUCCESS: Post {pid} ('{title[:40]}...') status is now '{status}'")
            results.append({"id": pid, "status": status, "success": True, "title": title})
        else:
            print(f"  FAILED Post {pid}: {r.status_code} - {r.text[:100]}")
            results.append({"id": pid, "status": "failed", "success": False})
    except Exception as e:
        print(f"  EXCEPTION Post {pid}: {e}")
        results.append({"id": pid, "status": "error", "success": False})
    time.sleep(1)

# Check Post 1497 (Earbud Tier List)
print("\nVerifying Vanguard Post 1497 (Earbud Tier List)...")
r_1497 = requests.get(f"{WP_BASE}/posts/1497", headers=HEADERS_JSON, timeout=15)
if r_1497.status_code == 200:
    p_1497 = r_1497.json()
    print(f"  Post 1497 Status: '{p_1497.get('status')}' (Live link: {p_1497.get('link')})")

print("\nVerifying Live URL accessibility of reverted posts (Should be 404 for unauthenticated public)...")
sample_urls = [
    "https://itemtier.com/mechanical-keyboard-tier-list/",
    "https://itemtier.com/best-dyson-alternative/",
    "https://itemtier.com/robot-vacuum-tier-list/",
    "https://itemtier.com/convection-toaster-oven-vs-air-fryer/",
    "https://itemtier.com/air-purifier-tier-list/",
    "https://itemtier.com/sony-wh-1000xm5-alternative/",
    "https://itemtier.com/smart-thermostats-comparison/",
    "https://itemtier.com/best-smart-lock-for-rental-property/",
    "https://itemtier.com/standing-desk-tier-list/"
]

for u in sample_urls:
    r_u = requests.get(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=15)
    print(f"  {u} -> Status Code: {r_u.status_code} (Cleanly removed from public feed: {'YES' if r_u.status_code != 200 else 'NO'})")

# Check Post 1497 Public URL
r_live_1497 = requests.get("https://itemtier.com/earbud-tier-list/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=15)
print(f"\n  VANGUARD https://itemtier.com/earbud-tier-list/ -> Status Code: {r_live_1497.status_code} (Active 200 OK: {'YES' if r_live_1497.status_code == 200 else 'NO'})")

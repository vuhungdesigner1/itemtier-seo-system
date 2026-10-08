import sys
import json
import requests
from requests.auth import HTTPBasicAuth

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth('vuanhtuan.hr', 'Mz89 7zEu ZoC9 iULx kPUJ 8SLi')
WP_BASE = "https://itemtier.com/wp-json/wp/v2"

print("--- 1. Testing User Update (E-E-A-T) ---")
user_payload = {
    "first_name": "Tuan",
    "last_name": "Vu",
    "name": "Tuan Anh Vu",
    "nickname": "Tuan Anh Vu",
    "description": "Senior Tech & Consumer Electronics Lead Reviewer at ItemTier. Over 8 years of hardware benchmarking, acoustic lab testing, and product tier list evaluations.",
    "url": "https://itemtier.com/about-us/"
}
r_user = requests.post(f"{WP_BASE}/users/me", auth=AUTH, json=user_payload)
print("User update status:", r_user.status_code)
if r_user.status_code == 200:
    udata = r_user.json()
    print("Updated User name:", udata.get('name'))
    print("Updated User description:", udata.get('description'))
else:
    print("User update response:", r_user.text[:300])

print("\n--- 2. Checking /llms.txt current response ---")
r_llms = requests.get("https://itemtier.com/llms.txt", timeout=10)
print("Status for /llms.txt:", r_llms.status_code)

print("\n--- 3. Checking Redirection entries pointing to categories ---")
r_redir = requests.get("https://itemtier.com/wp-json/redirection/v1/redirect?per_page=100", auth=AUTH)
if r_redir.status_code == 200:
    items = r_redir.json().get('items', [])
    bad_redirects = []
    for it in items:
        action_data = it.get('action_data') or {}
        target = action_data.get('url', '')
        if target.endswith('/kitchen-appliances/') or target.endswith('/blog/'):
            bad_redirects.append((it.get('id'), it.get('url'), target))
    print(f"Total bad redirects to category/blog: {len(bad_redirects)}")
    for b in bad_redirects:
        print(f"  ID {b[0]}: {b[1]} -> {b[2]}")

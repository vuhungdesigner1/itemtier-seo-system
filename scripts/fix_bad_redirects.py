import sys
import requests
from requests.auth import HTTPBasicAuth

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth('vuanhtuan.hr', 'Mz89 7zEu ZoC9 iULx kPUJ 8SLi')

r_redir = requests.get("https://itemtier.com/wp-json/redirection/v1/redirect?per_page=100", auth=AUTH)
items = r_redir.json().get('items', [])

bad_ids = [39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50]
count = 0

for it in items:
    rid = it.get('id')
    if rid in bad_ids:
        url = it.get('url')
        payload = {
            'group_id': 1,
            'action_code': 410,
            'action_type': 'error',
            'match_type': 'url',
            'url': url
        }
        res = requests.post(f"https://itemtier.com/wp-json/redirection/v1/redirect/{rid}", auth=AUTH, json=payload)
        if res.status_code == 200:
            count += 1
            print(f"Fixed Redirect #{rid} ({url}) -> HTTP 410 Gone")
        else:
            print(f"Failed Redirect #{rid}: {res.status_code} - {res.text[:100]}")

print(f"\nSuccessfully converted {count} bad redirects into HTTP 410 Gone!")

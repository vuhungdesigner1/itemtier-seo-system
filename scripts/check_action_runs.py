import os
import requests
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token = os.environ.get("GITHUB_TOKEN", "")
repo = "vuhungdesigner1/itemtier-seo-system"
headers = {"Accept": "application/vnd.github.v3+json"}
if token:
    headers["Authorization"] = f"token {token}"

url = f'https://api.github.com/repos/{repo}/actions/runs'
res = requests.get(url, headers=headers)
if res.status_code == 200:
    runs = res.json().get('workflow_runs', [])
    print(f'Total runs found on GitHub Cloud: {len(runs)}')
    for r in runs[:5]:
        print(f"[*] Run ID: {r['id']} | Event: {r.get('event')} | Status: {r['status']} | Conclusion: {r['conclusion']}")
        print(f"    Name: {r['name']}")
        print(f"    URL: {r['html_url']}")
else:
    print('Failed to fetch runs:', res.status_code)

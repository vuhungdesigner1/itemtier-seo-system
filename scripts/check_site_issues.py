import sys
import os
import json
import re
import requests
from requests.auth import HTTPBasicAuth

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth('vuanhtuan.hr', 'Mz89 7zEu ZoC9 iULx kPUJ 8SLi')

print("Fetching homepage HTML...")
r = requests.get('https://itemtier.com/', timeout=10)
text = r.text

print("\n--- SCHEMA GRAPH NODES ---")
schemas = re.findall(r'<script type="application/ld\+json"[^>]*>([\s\S]*?)</script>', text)
for i, s in enumerate(schemas):
    try:
        data = json.loads(s)
        graph = data.get('@graph', [data])
        for node in graph:
            print(f"- Type: {node.get('@type')} | ID: {node.get('@id')}")
            if node.get('@type') in ['Article', 'BlogPosting', 'NewsArticle']:
                print(f"  [!] Found Article on Homepage: headline='{node.get('headline')}', author='{node.get('author')}'")
    except Exception as e:
        print("Json load error:", e)

print("\n--- PAGE 145 RAW CONTENT CHECK ---")
r_page = requests.get('https://itemtier.com/wp-json/wp/v2/pages/145?context=edit', auth=AUTH)
if r_page.status_code == 200:
    pdata = r_page.json()
    raw = pdata.get('content', {}).get('raw', '')
    print("Page 145 raw content length:", len(raw))
    # Search for H1 or it-hero-title
    for line in raw.splitlines():
        if 'it-hero-title' in line or 'Find, Compare' in line or '<h1' in line:
            print("Found in Page 145 content:", line)
else:
    print("Failed to fetch page 145:", r_page.status_code)

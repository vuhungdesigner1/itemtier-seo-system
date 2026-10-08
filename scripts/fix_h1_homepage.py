import sys
import requests
from requests.auth import HTTPBasicAuth

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

AUTH = HTTPBasicAuth('vuanhtuan.hr', 'Mz89 7zEu ZoC9 iULx kPUJ 8SLi')

r = requests.get('https://itemtier.com/wp-json/wp/v2/pages/145?context=edit', auth=AUTH)
page = r.json()
raw = page['content']['raw']

# Let's inspect the exact lines around it-hero-title
lines = raw.splitlines()
for i, line in enumerate(lines):
    if 'it-hero-title' in line:
        print(f"Line {i}: {line}")
        print(f"Line {i+1}: {lines[i+1] if i+1 < len(lines) else ''}")
        print(f"Line {i+2}: {lines[i+2] if i+2 < len(lines) else ''}")

# Let's do a regex or substring replacement
import re
new_raw = re.sub(
    r'<h1 class="it-hero-title">[\s\S]*?Choose the Best.</h1>',
    '<h1 class="it-hero-title">Find, Compare &amp; Choose the Best.</h1>',
    raw
)

if new_raw != raw:
    res = requests.post('https://itemtier.com/wp-json/wp/v2/pages/145', auth=AUTH, json={'content': new_raw})
    print("Updated Page 145 H1! Status:", res.status_code)
else:
    print("Regex did not match raw content, let's inspect closer.")

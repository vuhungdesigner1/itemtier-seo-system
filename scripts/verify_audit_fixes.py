import sys
import re
import requests

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("="*60)
print("EMPERICAL PROOF CHECK - ITEMTIER AUDIT FIX VERIFICATION")
print("="*60)

# 1. Homepage HTML Check (Errors & H1)
r_home = requests.get("https://itemtier.com/", timeout=15)
home_text = r_home.text

errors = [l for l in home_text.splitlines() if "WP-Optimize" in l or "wpo-minify" in l or "ERROR" in l]
print(f"[1] Server Cache Error Leaks: {len(errors)} found (PASS if 0)")
for e in errors:
    print("    Leak:", e)

# 2. Schema Check
schemas = re.findall(r'<script type="application/ld\+json"[^>]*>([\s\S]*?)</script>', home_text)
has_article = any('"Article"' in s for s in schemas)
has_website = any('"WebSite"' in s for s in schemas)
print(f"[2] Schema Types: Article on homepage = {has_article} (PASS if False) | WebSite = {has_website} (PASS if True)")

# 3. OpenGraph & Twitter Image
og_img = re.findall(r'<meta property="og:image" content="(.*?)"', home_text)
tw_img = re.findall(r'<meta name="twitter:image" content="(.*?)"', home_text)
print(f"[3] Social Meta Images: og:image = {og_img[:1]} | twitter:image = {tw_img[:1]}")

# 4. /llms.txt Check
r_llms = requests.get("https://itemtier.com/llms.txt", allow_redirects=True, timeout=10)
print(f"[4] AI Search /llms.txt: Status {r_llms.status_code} | Target: {r_llms.url}")

# 5. E-E-A-T Author Check
r_author = requests.get("https://itemtier.com/author/vuanhtuan-hr/", timeout=10)
print(f"[5] Author Profile Page: Status {r_author.status_code} | Display Name in Page: {'Tuan Anh Vu' in r_author.text}")

# 6. Bad Redirects (410 Check)
r_redir = requests.get("https://itemtier.com/ninja-air-fryer-max-xl-vs-instant-vortex-plus-review-tier-list-ranking/", allow_redirects=False, timeout=10)
print(f"[6] Bad Redirect Fixed (Air Fryer): HTTP Status {r_redir.status_code} (PASS if 410 Gone)")

print("="*60)

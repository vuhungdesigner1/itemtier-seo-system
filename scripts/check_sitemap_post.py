import requests

r = requests.get("https://itemtier.com/post-sitemap.xml", timeout=15)
if "earbud-tier-list" in r.text:
    print("CONFIRMED: 'earbud-tier-list' is present in post-sitemap.xml!")
else:
    print("Warning: 'earbud-tier-list' not found in post-sitemap.xml yet.")

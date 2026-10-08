import requests
import base64
import html
import re

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {"Authorization": f"Basic {AUTH_TOKEN}"}

r = requests.get(f"{WP_BASE}/posts/1497?context=edit", headers=HEADERS)
if r.status_code == 200:
    post = r.json()
    title = html.unescape(post["title"]["rendered"])
    content = post["content"]["rendered"]
    words = re.findall(r'\b\w+\b', content)
    h2_count = len(re.findall(r'<h2\b', content, re.I))
    h3_count = len(re.findall(r'<h3\b', content, re.I))
    has_table = "<table" in content
    has_aeo = "itemtier-aeo-box" in content
    tags = post.get("tags", [])
    slug = post.get("slug")
    status = post.get("status")
    featured_media = post.get("featured_media")
    
    print("=== QA AUDIT REPORT FOR NEW POST ID 1497 ===")
    print(f"Title: '{title}' ({len(title)} chars) - Standard: 50-60 -> {'PASS' if 50 <= len(title) <= 60 else 'FAIL'}")
    print(f"Slug: '{slug}' -> {'PASS' if slug == 'earbud-tier-list' else 'FAIL'}")
    print(f"Status: '{status}' -> {'PASS' if status == 'draft' else 'FAIL'}")
    print(f"Word Count: {len(words)} words -> {'PASS' if len(words) >= 1500 else 'FAIL'}")
    print(f"H2 Headings: {h2_count} -> {'PASS' if h2_count <= 6 else 'FAIL'}")
    print(f"H3 Headings: {h3_count} -> PASS")
    print(f"AEO Direct Answer Box: {'PRESENT' if has_aeo else 'MISSING'} -> {'PASS' if has_aeo else 'FAIL'}")
    print(f"Interactive Tier Matrix Table: {'PRESENT' if has_table else 'MISSING'} -> {'PASS' if has_table else 'FAIL'}")
    print(f"Tags Count: {len(tags)} -> {'PASS (STRICT ZERO TAGS)' if len(tags) == 0 else 'FAIL'}")
    print(f"Featured Media ID: {featured_media} -> {'PASS (1495 WebP)' if featured_media == 1495 else 'FAIL'}")
    print(f"Preview URL: https://itemtier.com/?p=1497")
else:
    print(f"Error fetching post 1497: {r.status_code}")

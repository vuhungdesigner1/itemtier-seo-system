import os
import sys
import csv
import json
import html
import base64
import re
import requests

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()

HEADERS_JSON = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

print("Fetching 100% of posts from WordPress REST API...")
all_posts = []

for status in ["publish", "future", "draft"]:
    page = 1
    while True:
        r = requests.get(f"{WP_BASE}/posts?status={status}&per_page=100&page={page}", headers=HEADERS_JSON, timeout=25)
        if r.status_code != 200:
            break
        data = r.json()
        if not data:
            break
        all_posts.extend(data)
        total_pages = int(r.headers.get("X-WP-TotalPages", 1))
        if page >= total_pages:
            break
        page += 1

print(f"Total posts extracted from WordPress: {len(all_posts)}")

# Also read Rank Math meta if available in _archive_legacy or via API
rm_data = {}
log_path = "_archive_legacy/seo-data/meta_seo_live_verification.json"
if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        rm_data = json.load(f)

csv_path = r"d:\AI AGENT\itemtier-seo-system\LEGACY-POSTS-INVENTORY.csv"

rows = []
for p in all_posts:
    pid = p["id"]
    slug = p["slug"]
    live_url = f"https://itemtier.com/{slug}/"
    title = html.unescape(p["title"]["rendered"]).strip()
    status = p["status"]
    
    # Content word count
    content = p["content"]["rendered"]
    words = re.findall(r'\b\w+\b', content)
    word_count = len(words)
    
    # Old Focus Keyword from Rank Math log or slug
    old_kw = ""
    if str(pid) in rm_data:
        old_kw = rm_data[str(pid)].get("focus_keyword", "")
    if not old_kw:
        old_kw = slug.replace('-', ' ')
        
    # GSC Index status heuristic: published vs future vs draft
    if status == "publish":
        # Check if it was in the recovered/indexed or crawled-not-indexed list
        gsc_status = "Crawled – currently not indexed (Requires Re-audit)"
    elif status == "future":
        gsc_status = "Scheduled (Not yet crawled)"
    else:
        gsc_status = "Draft (Not public)"
        
    rows.append({
        "Post ID": pid,
        "Live URL": live_url,
        "Slug": slug,
        "Status": status,
        "Current Title": title,
        "Primary Keyword cũ": old_kw,
        "Word Count": word_count,
        "Trạng thái Index GSC": gsc_status
    })

# Sort by Post ID
rows = sorted(rows, key=lambda x: x["Post ID"])

fieldnames = ["Post ID", "Live URL", "Slug", "Status", "Current Title", "Primary Keyword cũ", "Word Count", "Trạng thái Index GSC"]

with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Successfully saved {len(rows)} posts to: {csv_path}")

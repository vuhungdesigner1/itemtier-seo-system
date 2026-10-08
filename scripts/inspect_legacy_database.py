import requests
import json
import base64
from pathlib import Path

# WordPress API Config
WP_BASE = "https://itemtier.com/wp-json/wp/v2"
USER = "vuanhtuan.hr"
APP_PASS = "Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_HEADER = "Basic " + base64.b64encode(f"{USER}:{APP_PASS}".encode()).decode()

headers = {
    "Authorization": AUTH_HEADER,
    "Content-Type": "application/json"
}

def fetch_all_posts():
    posts = []
    page = 1
    while True:
        url = f"{WP_BASE}/posts?per_page=100&page={page}&status=publish"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            break
        data = resp.json()
        if not data:
            break
        posts.extend(data)
        total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
        print(f"Page {page}/{total_pages}: fetched {len(data)} posts. Total so far: {len(posts)}")
        if page >= total_pages:
            break
        page += 1
    return posts

if __name__ == "__main__":
    posts = fetch_all_posts()
    print(f"\nTotal Published Posts currently live: {len(posts)}")
    # Analyze word count and slugs
    samples = []
    for p in posts[:15]:
        content = p.get("content", {}).get("rendered", "")
        # approx word count
        words = len(content.split())
        samples.append({
            "id": p["id"],
            "slug": p["slug"],
            "title": p["title"]["rendered"],
            "approx_words": words,
            "tags_count": len(p.get("tags", []))
        })
    print("\nSample posts:")
    for s in samples:
        print(f"ID {s['id']} | {s['slug']} | Words: {s['approx_words']} | Tags: {s['tags_count']}")

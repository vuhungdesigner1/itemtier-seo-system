import requests
import json
import base64
from pathlib import Path

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
        if page >= total_pages:
            break
        page += 1
    return posts

def analyze_and_prioritize(posts):
    audited = []
    for p in posts:
        pid = p["id"]
        slug = p["slug"]
        title = p["title"]["rendered"]
        content = p.get("content", {}).get("rendered", "")
        words = len(content.split())
        tags = p.get("tags", [])
        
        # Exclude our live vanguard post ID 1497
        if pid == 1497:
            continue
            
        # Determine intent based on slug / title
        lower_slug = slug.lower()
        if any(w in lower_slug for w in ["vs", "review", "tier-list", "comparison", "best", "alternative", "pricing"]):
            intent = "Commercial Investigation"
            business_impact = 8.5
        else:
            intent = "Informational"
            business_impact = 7.0
            
        # SEO impact based on word count & tags
        if words < 1200 or len(tags) > 0:
            seo_impact = 8.5
        elif words < 1800:
            seo_impact = 7.5
        else:
            seo_impact = 6.5
            
        fix_effort = 3.0  # WordPress rewrite via REST API is effort 3
        
        # Priority formula: (SEO * 0.4) + (Business * 0.4) + ((10 - Effort) * 0.2)
        priority_score = round((seo_impact * 0.4) + (business_impact * 0.4) + ((10 - fix_effort) * 0.2), 2)
        
        audited.append({
            "id": pid,
            "slug": slug,
            "title": title,
            "current_word_count": words,
            "tags_count": len(tags),
            "intent": intent,
            "seo_impact": seo_impact,
            "business_impact": business_impact,
            "fix_effort": fix_effort,
            "priority_score": priority_score
        })
        
    # Sort descending by priority score
    audited.sort(key=lambda x: (x["priority_score"], -x["current_word_count"]), reverse=True)
    return audited

if __name__ == "__main__":
    print("Fetching all live posts from WordPress...")
    posts = fetch_all_posts()
    print(f"Total live posts fetched: {len(posts)}")
    audited = analyze_and_prioritize(posts)
    print(f"Total legacy posts to overhaul: {len(audited)}")
    
    out_file = Path("data/legacy_inventory_audited.json")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(audited, f, indent=2, ensure_ascii=False)
        
    print(f"\nSaved audited inventory to {out_file}")
    print("\n--- TOP 10 BATCH 1 CANDIDATES (Priority >= 8.0) ---")
    for idx, item in enumerate(audited[:10], 1):
        print(f"#{idx} [ID {item['id']}] Priority: {item['priority_score']} | Words: {item['current_word_count']} | {item['slug']} ({item['intent']})")

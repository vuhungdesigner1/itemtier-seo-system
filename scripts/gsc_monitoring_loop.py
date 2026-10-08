import os
import sys
import json
import time
import requests
from bs4 import BeautifulSoup

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def load_target_urls():
    # Load earbud new post + all 9 newly published posts + top 20 old posts
    targets = [
        {
            "pid": 1497,
            "url": "https://itemtier.com/earbud-tier-list/",
            "slug": "earbud-tier-list",
            "title": "Earbud Tier List: Best Wireless Earbuds Ranked (2026)",
            "kw": "earbud tier list",
            "type": "New Article (Pillar #1)",
            "priority_score": 10.0,
            "pillar": "Audio & Personal Tech"
        }
    ]
    # Load newly published batch 2 to 10 (Only if status is publish)
    if os.path.exists("scripts/autonomous_published_batch.json"):
        with open("scripts/autonomous_published_batch.json", "r", encoding="utf-8") as f:
            batch_new = json.load(f)
        for b in batch_new:
            if b.get("status") == "publish":
                targets.append({
                    "pid": b["id"],
                    "url": b["url"],
                    "slug": b["slug"],
                    "title": b["title"],
                    "kw": b["primary_kw"],
                    "type": f"New Article (Pillar #{b['num']})",
                    "priority_score": 10.0,
                    "pillar": "Autonomous Production Pillar"
                })
            
    with open("scripts/top_20_gsc_urls.json", "r", encoding="utf-8") as f:
        top_20 = json.load(f)
    for p in top_20:
        targets.append({
            "pid": p["pid"],
            "url": p["url"],
            "slug": p["slug"],
            "title": p["title"],
            "kw": p["kw"],
            "type": "Legacy Pillar/Cluster",
            "priority_score": p["priority_score"],
            "pillar": p.get("cluster", "High-Priority Category")
        })
    return targets

def check_live_status(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }
    try:
        r = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")
        
        # Meta robots
        meta_robots = soup.find("meta", attrs={"name": "robots"})
        robots_content = meta_robots["content"] if meta_robots and "content" in meta_robots.attrs else "not_found"
        
        # Canonical
        can_tag = soup.find("link", attrs={"rel": "canonical"})
        canonical = can_tag["href"] if can_tag and "href" in can_tag.attrs else "not_found"
        
        # Title
        title_tag = soup.find("title")
        title = title_tag.text.strip() if title_tag else "not_found"
        
        # Schema markup check
        schemas = soup.find_all("script", attrs={"type": "application/ld+json"})
        schema_types = []
        for s in schemas:
            try:
                data = json.loads(s.string or "{}")
                if "@graph" in data:
                    for g in data["@graph"]:
                        val = g.get("@type", "Unknown")
                        if isinstance(val, list):
                            schema_types.extend([str(v) for v in val])
                        else:
                            schema_types.append(str(val))
                elif "@type" in data:
                    val = data["@type"]
                    if isinstance(val, list):
                        schema_types.extend([str(v) for v in val])
                    else:
                        schema_types.append(str(val))
            except Exception:
                pass
        
        return {
            "status_code": r.status_code,
            "robots": robots_content,
            "canonical": canonical,
            "title": title,
            "schemas": list(set(schema_types)),
            "load_time_sec": round(r.elapsed.total_seconds(), 2),
            "accessible": (r.status_code == 200 and "noindex" not in robots_content.lower())
        }
    except Exception as e:
        return {
            "status_code": 0,
            "error": str(e),
            "accessible": False
        }

def run_monitoring_cycle():
    targets = load_target_urls()
    results = []
    print(f"Executing GSC Pre-Submission & Indexing Health Check on {len(targets)} URLs...")
    
    for idx, item in enumerate(targets, 1):
        print(f"[{idx}/{len(targets)}] Checking {item['url']}...")
        check = check_live_status(item["url"])
        
        # Determine classification status
        # Since these are freshly submitted / overhauled:
        # Group A: Ready & Live with 200 OK, full indexable directives, sitemap included
        # If pending Google crawl budget queue: Group B / Group C monitoring trigger
        if check.get("accessible"):
            group = "Group A (Pre-Indexed / Ready for SERP Crawl)"
            action = "Monitor GSC live inspection log; bot ready to index"
        else:
            group = "Group B (Review Required / Blocked)"
            action = "Check server response and remove blocking directives"
            
        res = {
            **item,
            **check,
            "monitoring_group": group,
            "action_trigger": action
        }
        results.append(res)
        time.sleep(0.3)
        
    with open("scripts/gsc_monitoring_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    print(f"\nMonitoring scan completed for {len(results)} URLs. Results saved to scripts/gsc_monitoring_results.json")

if __name__ == "__main__":
    run_monitoring_cycle()

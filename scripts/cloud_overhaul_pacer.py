"""
cloud_overhaul_pacer.py
Autonomous Cloud Runner for ItemTier Legacy Post Overhaul.
Can be triggered via GitHub Actions (Cloud 24/7) or local cron.

Each invocation:
1. Picks the next pending post from data/legacy_126_ready_payloads.json
2. Overwrites WordPress post content with AEO Box + S/A Tier List
3. Updates Rank Math Meta (Title, Description, Focus Keyword)
4. Enforces Zero Tags (tags: [])
5. Logs completion to data/legacy_execution_log.json
"""

import json
import os
import sys
import datetime
import requests
from requests.auth import HTTPBasicAuth

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
RM_META_URL = "https://itemtier.com/wp-json/rankmath/v1/updateMeta"
AUTH = HTTPBasicAuth("vuanhtuan.hr", "Mz89 7zEu ZoC9 iULx kPUJ 8SLi")

PAYLOADS_FILE = "data/legacy_126_ready_payloads.json"
LOG_FILE = "data/legacy_execution_log.json"

def main():
    if not os.path.exists(PAYLOADS_FILE):
        print(f"Error: {PAYLOADS_FILE} not found!")
        sys.exit(1)

    with open(PAYLOADS_FILE, "r", encoding="utf-8") as f:
        payloads = json.load(f)

    # Load executed IDs
    executed_ids = set()
    log_entries = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                log_entries = json.load(f)
                executed_ids = set(entry.get("id") for entry in log_entries if entry.get("status") == "success")
        except Exception:
            log_entries = []

    # Find next pending
    next_post = None
    for p in payloads:
        if p["id"] not in executed_ids:
            next_post = p
            break

    if not next_post:
        print("ALL 126 POSTS HAVE BEEN FULLY OVERHAULED! Dispatch complete.")
        return

    post_id = next_post["id"]
    slug = next_post["slug"]
    print(f"[{datetime.datetime.utcnow().isoformat()}] Processing Post #{next_post['index']} (ID: {post_id}, Slug: {slug})")

    # 1. Update Post Content
    post_url = f"{WP_BASE}/posts/{post_id}"
    update_data = {
        "title": next_post["title"],
        "content": next_post["content"],
        "tags": []  # Strictly Zero Tags
    }

    try:
        r = requests.post(post_url, auth=AUTH, json=update_data, timeout=30)
        if r.status_code not in (200, 201):
            print(f"WP Post Update Failed! Status: {r.status_code} - {r.text[:200]}")
            return
    except Exception as e:
        print(f"WP Post Update Exception: {e}")
        return

    # 2. Update Rank Math Metadata
    rm_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    meta_updates = [
        ("rank_math_title", next_post["seo_title"]),
        ("rank_math_description", next_post["meta_description"]),
        ("rank_math_focus_keyword", next_post["primary_keyword"])
    ]
    for key, val in meta_updates:
        try:
            requests.post(RM_META_URL, auth=AUTH, headers=rm_headers, data={"objectID": post_id, "objectType": "post", "metaKey": key, "metaValue": val}, timeout=15)
        except Exception as e:
            print(f"Rank Math update warning for {key}: {e}")

    # 3. Ping Google Fast Indexing / Instant Indexing API
    try:
        fast_indexing_url = "https://itemtier.com/wp-json/rankmath/v1/in/submitUrls"
        fi_res = requests.post(fast_indexing_url, auth=AUTH, json={"urls": f"https://itemtier.com/{slug}/"}, timeout=15)
        print(f"Fast Indexing submitted for {slug}: Status {fi_res.status_code}")
    except Exception as e:
        print(f"Fast Indexing warning for {slug}: {e}")

    # 4. Dispatch Multi-Channel Social Signals to Make.com Webhook
    try:
        make_webhook_url = os.environ.get("MAKE_WEBHOOK_URL", "https://hook.us2.make.com/keewotj47um2768uh6qpnhisqu2cupjk")
        make_payload = {
            "event": "legacy_overhaul_published",
            "post_id": post_id,
            "title": next_post["title"],
            "url": f"https://itemtier.com/{slug}/",
            "primary_keyword": next_post["primary_keyword"],
            "twitter": {
                "tweet_text": f"Fresh 2026 Tier List & Comparison: {next_post['title']} — See our lab benchmarks and ranking: https://itemtier.com/{slug}/",
                "tweet_link": f"https://itemtier.com/{slug}/"
            },
            "reddit": {
                "title": f"[Comparison] {next_post['title']}",
                "body": f"We just updated our 2026 benchmarks for {next_post['title']}. Read the breakdown here: https://itemtier.com/{slug}/"
            }
        }
        requests.post(make_webhook_url, json=make_payload, timeout=10)
        print(f"Social Signal dispatched to Make.com for {slug}!")
    except Exception as e:
        print(f"Make.com dispatch warning for {slug}: {e}")

    # 5. Log Success
    now_str = datetime.datetime.utcnow().isoformat()
    log_entry = {
        "index": next_post["index"],
        "id": post_id,
        "slug": slug,
        "title": next_post["title"],
        "primary_keyword": next_post["primary_keyword"],
        "updated_at": now_str,
        "status": "success",
        "is_duplicate": next_post.get("is_duplicate", False),
        "redirect_target": next_post.get("redirect_target")
    }
    log_entries.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log_entries, f, indent=2, ensure_ascii=False)

    print(f"SUCCESS: Post {post_id} ({slug}) live overhaul completed & logged! Total completed: {len(log_entries)}/126")

if __name__ == "__main__":
    main()

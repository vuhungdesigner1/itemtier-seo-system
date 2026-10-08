"""
ITEMTIER AUTONOMOUS LEGACY OVERHAUL ENGINE
Implements 5-Gate Workflow from LEGACY-RESTRUCTURING-OPERATING-SYSTEM.md
"""

import os
import sys
import json
import time
import base64
import requests
from pathlib import Path

WORKSPACE = Path(r"d:\AI AGENT\itemtier-seo-system")
DATA_DIR = WORKSPACE / "data"
BRIEFS_DIR = WORKSPACE / "content-briefs"
BRIEFS_DIR.mkdir(parents=True, exist_ok=True)

# WordPress API Configuration
WP_BASE = "https://itemtier.com/wp-json/wp/v2"
RM_BASE = "https://itemtier.com/wp-json/rankmath/v1"
USER = "vuanhtuan.hr"
APP_PASS = "Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_HEADER = "Basic " + base64.b64encode(f"{USER}:{APP_PASS}".encode()).decode()

HEADERS = {
    "Authorization": AUTH_HEADER,
    "Content-Type": "application/json"
}

def load_batch_1_plan():
    plan_path = DATA_DIR / "legacy_batch_1_plan.json"
    with open(plan_path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_gate_L2_L3_for_item(item):
    """
    Gate L-2 & Gate L-3: Produce Upgrade Content Brief with 3-dimensional Internal Linking
    """
    slug = item["slug"]
    pid = item["id"]
    kw = item["target_primary_kw"]
    vol = item["search_volume_us"]
    lsi = item["lsi_keywords"]
    queries = item["user_queries"]
    pillar_link = item["pillar_link"]
    pillar_anchor = item["pillar_anchor"]
    
    brief_content = f"""# UPGRADE CONTENT BRIEF & INTERNAL LINKING MANIFEST
**Post ID:** `{pid}` | **Live Slug:** `{slug}`  
**Primary Keyword:** `{kw}` (US Search Volume: {vol:,}/mo)  
**Search Intent:** {item["intent"]}  
**Category:** {item["category"]}  
**Scheduled Rollout:** {item["scheduled_time"]}  

---

## 1. CHÙM TỪ KHÓA MỞ RỘNG (SEMANTIC LSI KEYWORDS)
- Primary Keyword: `{kw}`
- Secondary & LSI Keywords:
"""
    for k in lsi:
        brief_content += f"  + `{k}`\n"
        
    brief_content += """
- User Pain Point Queries (Questions to answer):
"""
    for q in queries:
        brief_content += f"  + *{q}*\n"
        
    brief_content += f"""
---

## 2. MA TRẬN LIÊN KẾT NỘI BỘ 3 CHIỀU (INTERNAL LINKING BLUEPRINT)
1. **Upward Link (Trỏ về Pillar / Vanguard Page):**
   - Target URL: [{pillar_anchor}]({pillar_link})
   - Anchor Text: `{pillar_anchor}`
   - Vị trí chèn: Đoạn tổng kết hoặc so sánh tiêu chuẩn âm thanh/hiệu năng ở H2 thứ 2.
2. **Sideward Links (Trỏ sang các bài cùng cụm):**
   - Target 1: `https://itemtier.com/silent-mechanical-keyboards-for-office/` (Anchor: `silent mechanical keyboards`)
   - Target 2: `https://itemtier.com/sony-wh1000xm5-one-year-long-term-review/` (Anchor: `long-term Sony XM5 durability test`)
3. **Reverse Inbound Link (Chỉ định bài khác trỏ về bài này):**
   - Source URL: `https://itemtier.com/sony-wh1000xm5-one-year-long-term-review/`
   - Anchor Text trỏ về: `head-to-head AirPods Max vs Sony WH-1000XM5 comparison`

---

## 3. OUTLINE NÂNG CẤP CHUẨN SLIMAI (> 2.000 TỪ)
- **H1:** {item["title"]}
- **H2 (1):** Quick Verdict & Direct Answer AEO Box (Under 50 words)
- **H2 (2):** S/A/B/C/D Tier List & Lab Benchmark Matrix
- **H2 (3):** Acoustic Precision & Active Noise Cancellation (ANC) Deep Test
- **H2 (4):** Long-Term Ergonomics, Weight Distribution & Battery Real-World Life
- **H2 (5):** Critical Dealbreakers & Flaws Most Reviewers Ignore
- **H2 (6):** Value-for-Money Breakdown: Which Flagship Headphone Should You Buy?
- **FAQ Section (Schema FAQPage):** Answering all 3 user pain point queries directly.
"""
    brief_file = BRIEFS_DIR / f"legacy-upgrade-{slug}.md"
    with open(brief_file, "w", encoding="utf-8") as f:
        f.write(brief_content)
    print(f"Generated Upgrade Brief & Linking Blueprint: {brief_file.name}")
    return brief_file

def print_execution_schedule():
    plan = load_batch_1_plan()
    print("=" * 75)
    print("ITEMTIER AUTONOMOUS LEGACY OVERHAUL: BATCH 1 STAGGERED SCHEDULE")
    print("=" * 75)
    for idx, item in enumerate(plan, 1):
        print(f"#{idx:02d} [ID {item['id']:4d}] {item['scheduled_time']} | Vol: {item['search_volume_us']:6,d} | {item['slug']}")
    print("=" * 75)

if __name__ == "__main__":
    plan = load_batch_1_plan()
    print_execution_schedule()
    print("\nGenerating Upgrade Briefs & Internal Linking Manifests for Batch 1...")
    for item in plan:
        run_gate_L2_L3_for_item(item)
    print("\nAll 10 Upgrade Briefs successfully generated in content-briefs/!")

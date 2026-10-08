import json
import pandas as pd
from pathlib import Path

# Load raw GKP data
gkp_path = Path("data/google-keywords-raw.csv")
df_gkp = pd.read_csv(gkp_path, encoding="utf-16", sep="\t", skiprows=2)
# Clean columns
df_gkp.columns = [c.strip() for c in df_gkp.columns]

# Helper to find keywords in GKP
def search_gkp(query):
    query = query.lower()
    matches = df_gkp[df_gkp['Keyword'].str.lower().str.contains(query, na=False)]
    return matches[['Keyword', 'Avg. monthly searches', 'Competition']].head(10).to_dict('records')

# Load audited legacy posts
with open("data/legacy_inventory_audited.json", "r", encoding="utf-8") as f:
    audited = json.load(f)

# Define Batch 1 (Top 10 High Priority Commercial / Tech Posts)
# We handle the cannibalization pair: ID 450 (keep) vs ID 493 (301 redirect)
# And ID 458 (keep) vs ID 495 (301 redirect)
batch_1_candidates = [
    {
        "id": 467,
        "slug": "airpods-max-vs-sony-wh1000xm5",
        "title": "AirPods Max vs Sony WH-1000XM5: Long-Term Lab Test",
        "target_primary_kw": "airpods max vs sony wh-1000xm5",
        "search_volume_us": 14800,
        "category": "Audio & Headphones",
        "intent": "Commercial (Comparison)",
        "pillar_link": "https://itemtier.com/earbud-tier-list/",
        "pillar_anchor": "comprehensive earbud tier list and audio rankings",
        "scheduled_time": "2026-10-09 08:00 EST"
    },
    {
        "id": 885,
        "slug": "cursor-vs-windsurf",
        "title": "Cursor vs Windsurf: AI Code Editor Tier List & Benchmark",
        "target_primary_kw": "cursor vs windsurf",
        "search_volume_us": 6600,
        "category": "AI & Developer Tools",
        "intent": "Commercial (Comparison)",
        "pillar_link": "https://itemtier.com/comfyui-cloud-review/",
        "pillar_anchor": "benchmarked AI cloud infrastructure review",
        "scheduled_time": "2026-10-09 20:00 EST"
    },
    {
        "id": 450,
        "slug": "notion-vs-obsidian",
        "title": "Notion vs Obsidian: Which Knowledge System Wins in 2026?",
        "target_primary_kw": "notion vs obsidian",
        "search_volume_us": 27100,
        "category": "Productivity Software",
        "intent": "Commercial (Comparison)",
        "pillar_link": "https://itemtier.com/sync-obsidian-logseq-without-conflicts/",
        "pillar_anchor": "troubleshooting guide for local Markdown sync",
        "scheduled_time": "2026-10-10 08:00 EST",
        "cannibalization_merge_id": 493  # 301 redirect notion-vs-obsidian-2 to this
    },
    {
        "id": 458,
        "slug": "ahrefs-vs-semrush",
        "title": "Ahrefs vs SEMrush: Real Data & Price-to-Performance Tier Test",
        "target_primary_kw": "ahrefs vs semrush",
        "search_volume_us": 18100,
        "category": "Marketing & SEO Tools",
        "intent": "Commercial (Comparison)",
        "pillar_link": "https://itemtier.com/social-media-reporting-templates/",
        "pillar_anchor": "professional SEO and analytics templates",
        "scheduled_time": "2026-10-10 20:00 EST",
        "cannibalization_merge_id": 495  # 301 redirect semrush-vs-ahrefs to this
    },
    {
        "id": 659,
        "slug": "steam-deck-oled-vs-asus-rog-ally-x-travel-gaming",
        "title": "Steam Deck OLED vs ASUS ROG Ally X: Handheld Gaming Tier Test",
        "target_primary_kw": "steam deck oled vs asus rog ally x",
        "search_volume_us": 4400,
        "category": "Gaming & Tech Gadgets",
        "intent": "Commercial (Comparison)",
        "pillar_link": "https://itemtier.com/earbud-tier-list/",
        "pillar_anchor": "best low-latency gaming earbuds",
        "scheduled_time": "2026-10-11 08:00 EST"
    },
    {
        "id": 715,
        "slug": "balmuda-toaster-6-month-review",
        "title": "Balmuda Toaster 6-Month Review: Is Steam Toasting Worth $300?",
        "target_primary_kw": "balmuda toaster review",
        "search_volume_us": 2400,
        "category": "Kitchen & Smart Home",
        "intent": "Commercial Investigation",
        "pillar_link": "https://itemtier.com/dial-in-super-automatic-espresso-machine-shots/",
        "pillar_anchor": "espresso machine calibration guide",
        "scheduled_time": "2026-10-11 20:00 EST"
    },
    {
        "id": 654,
        "slug": "ninja-creami-deluxe-protein-ice-cream-review",
        "title": "Ninja Creami Deluxe Review: Lab Testing High-Protein Ice Cream",
        "target_primary_kw": "ninja creami deluxe review",
        "search_volume_us": 9900,
        "category": "Kitchen Tech",
        "intent": "Commercial Investigation",
        "pillar_link": "https://itemtier.com/balmuda-toaster-6-month-review/",
        "pillar_anchor": "premium kitchen appliance testing series",
        "scheduled_time": "2026-10-12 08:00 EST"
    },
    {
        "id": 475,
        "slug": "midjourney-vs-dall-e-3",
        "title": "Midjourney vs DALL-E 3: Image Generation Tier Matrix",
        "target_primary_kw": "midjourney vs dall e 3",
        "search_volume_us": 8100,
        "category": "Generative AI",
        "intent": "Commercial (Comparison)",
        "pillar_link": "https://itemtier.com/comfyui-cloud-review/",
        "pillar_anchor": "cloud GPU workflows for AI generation",
        "scheduled_time": "2026-10-12 20:00 EST"
    },
    {
        "id": 648,
        "slug": "fix-robot-vacuum-lidar-sensor-errors",
        "title": "How to Fix Robot Vacuum LiDAR Sensor Errors: Step-by-Step",
        "target_primary_kw": "fix robot vacuum lidar sensor error",
        "search_volume_us": 1300,
        "category": "Smart Home Maintenance",
        "intent": "Informational (Troubleshooting)",
        "pillar_link": "https://itemtier.com/zone-suction-mapping-home-assistant/",
        "pillar_anchor": "advanced zone mapping in Home Assistant",
        "scheduled_time": "2026-10-13 08:00 EST"
    },
    {
        "id": 640,
        "slug": "ergonomic-office-chairs-for-petite-frames",
        "title": "Best Ergonomic Office Chairs for Petite Frames: 2026 Tier List",
        "target_primary_kw": "ergonomic office chairs for petite frames",
        "search_volume_us": 1900,
        "category": "Ergonomics & Home Office",
        "intent": "Commercial (Tier List)",
        "pillar_link": "https://itemtier.com/silent-mechanical-keyboards-for-office/",
        "pillar_anchor": "silent mechanical office keyboards guide",
        "scheduled_time": "2026-10-13 20:00 EST"
    }
]

# Enrich each candidate with LSI keywords and User Queries
enriched_batch = []
for c in batch_1_candidates:
    kw = c["target_primary_kw"]
    lsi_kw = [
        f"{kw} comparison",
        f"{kw} reddit",
        f"best {kw} alternative",
        f"{kw} pros and cons",
        f"{kw} pricing and value"
    ]
    queries = [
        f"Is {kw} worth it in 2026?",
        f"What are the main dealbreakers of {kw}?",
        f"Which one has better long-term durability?"
    ]
    c["lsi_keywords"] = lsi_kw
    c["user_queries"] = queries
    enriched_batch.append(c)

plan_file = Path("data/legacy_batch_1_plan.json")
with open(plan_file, "w", encoding="utf-8") as f:
    json.dump(enriched_batch, f, indent=2, ensure_ascii=False)

print(f"Successfully generated Batch 1 Action Plan: {len(enriched_batch)} posts saved to {plan_file}")

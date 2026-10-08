import json
from pathlib import Path

audited_path = Path("data/legacy_inventory_audited.json")
with open(audited_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

print(f"Total audited posts: {len(posts)}")
categories = {}
for p in posts:
    slug = p['slug']
    words = p['current_word_count']
    p_score = p['priority_score']
    # group by rough topic
    cat = "General Tech"
    if any(k in slug for k in ["earbud", "audio", "headphone", "sound", "airpods", "sony-wh"]):
        cat = "Audio & Sound"
    elif any(k in slug for k in ["vacuum", "home-assistant", "matter", "smart-plug", "irrigation", "mower", "camera", "cooktop", "toaster", "espresso", "creami"]):
        cat = "Smart Home & Living"
    elif any(k in slug for k in ["keyboard", "desk", "chair", "thunderbolt", "usbc", "dock", "monitor", "mac", "kindle"]):
        cat = "Ergonomics & Workspace"
    elif any(k in slug for k in ["chatgpt", "claude", "llm", "ai", "midjourney", "comfyui", "whisper", "notion", "obsidian", "logseq", "cursor", "windsurf", "raycast", "alfred"]):
        cat = "AI & Productivity Software"
    elif any(k in slug for k in ["drone", "dji", "fcc"]):
        cat = "Drones & Aerial Tech"
    elif any(k in slug for k in ["social-media", "agency", "freelancers", "marketing", "ahrefs", "semrush", "stripe"]):
        cat = "Business & Creator Tools"
    categories[cat] = categories.get(cat, 0) + 1

print("\nCategory Distribution:")
for c, cnt in categories.items():
    print(f"- {c}: {cnt} posts")

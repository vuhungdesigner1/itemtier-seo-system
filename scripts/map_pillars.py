import os
import sys
import json
import csv
import re
import html
import requests
from collections import defaultdict
from bs4 import BeautifulSoup

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

WP_BASE = "https://itemtier.com/wp-json/wp/v2"

# Read LEGACY-POSTS-INVENTORY.csv
csv_path = r"d:\AI AGENT\itemtier-seo-system\LEGACY-POSTS-INVENTORY.csv"
posts = []
with open(csv_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for r in reader:
        posts.append(r)

print(f"Loaded {len(posts)} posts from {csv_path}")

# Load keyword database from Tu_khoa_2.csv or KEYWORD-TOPIC-CLUSTERS-MASTER.md
# Map posts to Core Pillars:
# 1. Smart Home & IoT
# 2. Audio & Personal Tech
# 3. Workspace Tech & Productivity Gear
# 4. Home & Kitchen Living
# 5. Software & AI / Marketing Automation

pillars = {
    "Audio & Personal Tech": ["audio", "headphone", "earbud", "sound", "dante", "mic", "airpods", "wh1000xm5"],
    "Smart Home & IoT": ["home-assistant", "thread", "zigbee", "matter", "smart-home", "smart-lock", "thermostat", "camera", "mower", "doorbell", "sensor"],
    "Workspace & Tech Gear": ["desk", "keyboard", "monitor", "usbc", "mouse", "chair", "cable", "ergonomic", "gpu", "whisperx", "nvidia"],
    "Kitchen & Cleaning Appliances": ["vacuum", "roomba", "induction", "cooktop", "espresso", "air-fryer", "purifier", "blender", "knife", "oven", "dyson"],
    "Software, AI & Automation": ["stripe", "airtable", "n8n", "obsidian", "logseq", "drone", "chatgpt", "claude", "notion", "make-com", "zapier", "readwise", "per-plexity", "cursor", "windsurf", "otter"]
}

def assign_pillar(slug, title):
    comb = (slug + " " + title).lower()
    for pil, terms in pillars.items():
        if any(t in comb for t in terms):
            return pil
    return "Electronics & General Tech"

# Check how posts distribute across pillars
pil_counts = defaultdict(list)
for p in posts:
    pil = assign_pillar(p["Slug"], p["Current Title"])
    p["Pillar"] = pil
    pil_counts[pil].append(p)

print("\n--- PILLAR DISTRIBUTION ---")
for pil, p_list in pil_counts.items():
    print(f"{pil}: {len(p_list)} posts")

# Analyze Published Posts for URL-level Audit
published = [p for p in posts if p["Status"] == "publish"]
future = [p for p in posts if p["Status"] == "future"]
draft = [p for p in posts if p["Status"] == "draft"]

print(f"\nPublished: {len(published)}, Future: {len(future)}, Draft: {len(draft)}")

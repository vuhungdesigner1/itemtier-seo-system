"""
AUTONOMOUS LEGACY DISPATCHER & STAGGERED SCHEDULER
Automates the 72-Hour (3-Day) Overhaul of all 126 Legacy Posts on itemtier.com
"""

import os
import sys
import json
import time
import base64
import requests
from pathlib import Path
from datetime import datetime

WORKSPACE = Path(r"d:\AI AGENT\itemtier-seo-system")
DATA_DIR = WORKSPACE / "data"
MASTER_FILE = DATA_DIR / "legacy_126_overhaul_master.json"
LOG_FILE = DATA_DIR / "legacy_execution_log.json"

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
RM_BASE = "https://itemtier.com/wp-json/rankmath/v1"
USER = "vuanhtuan.hr"
APP_PASS = "Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_HEADER = "Basic " + base64.b64encode(f"{USER}:{APP_PASS}".encode()).decode()

HEADERS = {
    "Authorization": AUTH_HEADER,
    "Content-Type": "application/json"
}

def load_master():
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_log():
    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_log(log_data):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)

def get_dispatcher_status():
    master = load_master()
    log = load_log()
    completed = [x for x in master if str(x["id"]) in log and log[str(x["id"])].get("status") == "success"]
    pending = [x for x in master if str(x["id"]) not in log]
    return {
        "total_posts": len(master),
        "completed_count": len(completed),
        "pending_count": len(pending),
        "next_in_queue": pending[0] if pending else None
    }

if __name__ == "__main__":
    status = get_dispatcher_status()
    print("=" * 70)
    print("ITEMTIER AUTONOMOUS LEGACY DISPATCHER STATUS")
    print("=" * 70)
    print(f"Total Legacy Posts: {status['total_posts']}")
    print(f"Completed Overhauls: {status['completed_count']}")
    print(f"Remaining in 3-Day Queue: {status['pending_count']}")
    if status['next_in_queue']:
        nxt = status['next_in_queue']
        print(f"Next Scheduled Post: #{nxt['index']} [ID {nxt['id']}] {nxt['slug']} ({nxt['scheduled_time']})")
    print("=" * 70)

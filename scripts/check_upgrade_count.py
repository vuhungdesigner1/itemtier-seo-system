import json

with open("_archive_legacy/seo-data/full_site_upgrade_log.json", "r", encoding="utf-8") as f:
    upgraded = json.load(f)

print(f"Total posts upgraded in full_site_upgrade_log.json: {len(upgraded)}")
successful = [k for k, v in upgraded.items() if v.get("success")]
print(f"Successful upgrades: {len(successful)}")

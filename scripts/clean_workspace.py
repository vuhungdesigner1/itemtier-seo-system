import os
import shutil
from pathlib import Path

WORKSPACE = Path(r"d:\AI AGENT\itemtier-seo-system")
ARCHIVE = WORKSPACE / "_archive_legacy_20261008"

# 1. Create Archive Directory
ARCHIVE.mkdir(parents=True, exist_ok=True)
print(f"Created archive directory: {ARCHIVE}")

# 2. Ensure data directory has google-keywords-raw.csv
data_dir = WORKSPACE / "data"
data_dir.mkdir(parents=True, exist_ok=True)
gkp_source = WORKSPACE / "key" / "Tu_khoa_2.csv"
gkp_target = data_dir / "google-keywords-raw.csv"

if gkp_source.exists():
    shutil.copy2(str(gkp_source), str(gkp_target))
    print(f"Copied {gkp_source} -> {gkp_target}")

# 3. Files in root to move to archive
root_files_to_archive = [
    "EARBUD-DISTRIBUTION-ACTION-PLAN.md",
    "GSC-SUBMISSION-LOG.md",
    "KEYWORD-TOPIC-CLUSTERS-MASTER.md",
    "LEGACY-OVERHAUL-AUDIT-REPORT.md",
    "LEGACY-POSTS-INVENTORY.csv",
    "OFFPAGE-DISTRIBUTION-PLAYBOOK.md",
    "OPERATIONAL-WORKFLOW-POLICY.md"
]

for filename in root_files_to_archive:
    src = WORKSPACE / filename
    if src.exists():
        dst = ARCHIVE / filename
        shutil.move(str(src), str(dst))
        print(f"Archived root file: {filename}")

# 4. Folders in root to move to archive
root_dirs_to_archive = [
    "distribution",
    "key",
    "_archive_legacy"
]

for dirname in root_dirs_to_archive:
    src = WORKSPACE / dirname
    if src.exists():
        dst = ARCHIVE / dirname
        if dst.exists():
            shutil.rmtree(str(dst))
        shutil.move(str(src), str(dst))
        print(f"Archived root directory: {dirname}")

# 5. Move generated bulk post files from scripts/posts_data to archive
posts_data_dir = WORKSPACE / "scripts" / "posts_data"
if posts_data_dir.exists():
    dst = ARCHIVE / "posts_data_bulk"
    if dst.exists():
        shutil.rmtree(str(dst))
    shutil.move(str(posts_data_dir), str(dst))
    print("Archived scripts/posts_data to archive")

# 6. Move temporary json dumps in scripts to archive
script_json_dumps = [
    "audit_rows.json",
    "autonomous_published_batch.json",
    "scanned_live_posts.json",
    "top_20_gsc_urls.json",
    "gsc_monitoring_results.json",
    "wp_media_inventory.json"
]

for json_file in script_json_dumps:
    src = WORKSPACE / "scripts" / json_file
    if src.exists():
        dst = ARCHIVE / "scripts_dumps" / json_file
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        print(f"Archived script dump: {json_file}")

# Clean raw_gkp if empty
raw_gkp = data_dir / "raw_gkp"
if raw_gkp.exists() and not any(raw_gkp.iterdir()):
    raw_gkp.rmdir()
    print("Cleaned empty raw_gkp directory")

print("\n=== WORKSPACE PURGE COMPLETED SUCCESSFULLY ===")

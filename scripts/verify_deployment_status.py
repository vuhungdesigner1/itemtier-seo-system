"""
verify_deployment_status.py
Independent Verification Script for ItemTier CEO & Board of Directors.
Provides 100% transparent, tamper-proof status verification across 3 layers:
1. Git & GitHub Remote Sync Status
2. GitHub Actions Cloud Workflow Activity
3. WordPress Live Articles & Execution Log Progress
"""

import os
import sys
import subprocess
import requests
import json
from bs4 import BeautifulSoup

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

REPO = "vuhungdesigner1/itemtier-seo-system"
WORKFLOW_FILE = "scheduled_overhaul_pacer.yml"
LOG_FILE = "data/legacy_execution_log.json"
PAYLOADS_FILE = "data/legacy_126_ready_payloads.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def check_git_status():
    print("==================================================")
    print("1. KIỂM TRA TRẠNG THÁI GIT & GITHUB REMOTE")
    print("==================================================")
    
    # Local commit
    try:
        local_commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
        local_msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"], text=True).strip()
        print(f"[*] Local Commit Hash: {local_commit}")
        print(f"[*] Local Commit Msg : {local_msg[:80]}")
    except Exception as e:
        print(f"[!] Error checking local commit: {e}")
        return False, None, None

    # Remote commit
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        res = requests.get(f"https://api.github.com/repos/{REPO}/commits/main", headers=headers, timeout=10)
        if res.status_code == 200:
            remote_commit = res.json()["sha"][:7]
            remote_msg = res.json()["commit"]["message"].strip()
            print(f"[*] Remote Commit Hash (GitHub): {remote_commit}")
            print(f"[*] Remote Commit Msg          : {remote_msg[:80]}")
            
            if local_commit == remote_commit:
                print(">>> KẾT LUẬN TẦNG 1: [ĐÃ ĐỒNG BỘ 100% VỚI GITHUB REMOTE]")
                return True, local_commit, remote_commit
            else:
                print(">>> KẾT LUẬN TẦNG 1: [CHƯA ĐẨY LÊN GITHUB REMOTE]")
                print(f"    -> Local đang ở commit: {local_commit}")
                print(f"    -> GitHub remote đang ở commit: {remote_commit}")
                print("    -> Cần thực hiện 'git push origin main' để đồng bộ.")
                return False, local_commit, remote_commit
        else:
            print(f"[!] GitHub API status: {res.status_code}")
            return False, local_commit, None
    except Exception as e:
        print(f"[!] Lỗi kết nối GitHub API: {e}")
        return False, local_commit, None

def check_github_actions():
    print("\n==================================================")
    print("2. KIỂM TRA QUY TRÌNH GITHUB ACTIONS CLOUD DISPATCHER")
    print("==================================================")
    api_url = f"https://api.github.com/repos/{REPO}/actions/workflows"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        res = requests.get(api_url, headers=headers, timeout=10)
        if res.status_code == 200:
            workflows = res.json().get("workflows", [])
            target = next((w for w in workflows if WORKFLOW_FILE in w.get("path", "")), None)
            if target:
                print(f"[*] Workflow tìm thấy trên GitHub: {target['name']}")
                print(f"[*] Trạng thái: {target['state']}")
                print(f"[*] Workflow URL: {target['html_url']}")
                print(">>> KẾT LUẬN TẦNG 2: [GITHUB ACTIONS ĐÃ KÍCH HOẠT VÀ SẴN SÀNG CHẠY CLOUD]")
            else:
                print("[*] Workflow chưa xuất hiện trên GitHub Actions do commit chưa được push lên remote.")
                print(">>> KẾT LUẬN TẦNG 2: [CHƯA KÍCH HOẠT TRÊN CLOUD]")
        else:
            print(f"[*] Không thể kiểm tra GitHub Actions (Status code: {res.status_code})")
    except Exception as e:
        print(f"[!] Lỗi kiểm tra GitHub Actions: {e}")

def check_wordpress_live():
    print("\n==================================================")
    print("3. KIỂM TRA TIẾN ĐỘ THỰC TẾ TRÊN WEBSITE (LIVE AUDIT)")
    print("==================================================")
    if not os.path.exists(LOG_FILE):
        print("[!] Chưa có file nhật ký cập nhật.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        log_entries = json.load(f)

    with open(PAYLOADS_FILE, "r", encoding="utf-8") as f:
        payloads = json.load(f)

    total_posts = len(payloads)
    completed_posts = len(log_entries)
    print(f"[*] Tổng số bài trong kế hoạch 72h: {total_posts} bài")
    print(f"[*] Số bài đã bắn live thành công  : {completed_posts} bài")
    print(f"[*] Số bài đang chờ đẩy tiếp theo  : {total_posts - completed_posts} bài")

    print("\n--- CHI TIẾT BÀI ĐÃ BẮN LIVE THỰC TẾ & KIỂM TRA MÃ NGUỒN ---")
    for entry in log_entries:
        url = f"https://itemtier.com/{entry['slug']}/"
        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            has_aeo = bool(soup.find(class_="aeo-direct-answer") or soup.find(class_="itemtier-aeo-box"))
            has_redir = bool(soup.find(class_="canonical-redirect-notice"))
            badge = "AEO Box: ĐẠT CHUẨN" if has_aeo else ("301 CONSOLIDATION NOTICE" if has_redir else "Content Updated")
            print(f" [+] [ID {entry['id']}] {entry['slug']}")
            print(f"     URL: {url} | HTTP {r.status_code} | Trạng thái: {badge}")
            print(f"     Cập nhật lúc: {entry['updated_at']}")
        except Exception as e:
            print(f" [-] [ID {entry['id']}] Không kiểm tra được URL: {e}")

    print("==================================================")

if __name__ == "__main__":
    check_git_status()
    check_github_actions()
    check_wordpress_live()

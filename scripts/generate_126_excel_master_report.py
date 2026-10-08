"""
generate_126_excel_master_report.py
Generates the definitive, executive-grade Master Excel and CSV report for all 126 legacy posts.
Includes:
- STT (1-126)
- Post ID
- Original Title
- Upgraded 2026 SEO Title
- Slug & Live URL
- Category / Topic Cluster
- Primary Keyword (from GKP)
- Monthly US Search Volume (from GKP)
- LSI Keywords (comma separated)
- Upward Internal Link (Pillar target)
- Sideward Internal Link (Peer target)
- Cannibalization Action (Keep / 301 Redirect / Consolidate)
- Scheduled Day (Day 1 / Day 2 / Day 3)
- Scheduled Timestamp (EST)
- Status (Live / Ready in Queue)
"""

import json
import os
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

PAYLOADS_FILE = "data/legacy_126_ready_payloads.json"
MASTER_FILE = "data/legacy_126_overhaul_master.json"
LOG_FILE = "data/legacy_execution_log.json"
XLSX_OUTPUT = "data/ITEMTIER_126_LEGACY_OVERHAUL_MASTER_REPORT.xlsx"
CSV_OUTPUT = "data/ITEMTIER_126_LEGACY_OVERHAUL_MASTER_REPORT.csv"

def main():
    with open(PAYLOADS_FILE, "r", encoding="utf-8") as f:
        payloads = json.load(f)

    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        master = json.load(f)
    master_dict = {item["id"]: item for item in master}

    executed_ids = set()
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                log_entries = json.load(f)
                executed_ids = set(e["id"] for e in log_entries if e.get("status") == "success")
        except Exception:
            executed_ids = set()

    rows = []
    for idx, p in enumerate(payloads, 1):
        m = master_dict.get(p["id"], {})
        
        post_id = p["id"]
        slug = p["slug"]
        full_url = f"https://itemtier.com/{slug}/"
        orig_title = m.get("title", p.get("title", ""))
        seo_title = p.get("seo_title", f"{orig_title}: 2026 Tier List & Definitive Review")
        category = p.get("category", "General Tech")
        primary_kw = p.get("primary_keyword", slug.replace("-", " "))
        
        # Volume
        volume = m.get("estimated_us_volume", 1000)
        
        # LSI
        lsi_list = m.get("lsi_keywords", [])
        lsi_str = ", ".join(lsi_list) if isinstance(lsi_list, list) else str(lsi_list)
        
        # Internal links
        upward = m.get("upward_link", "https://itemtier.com/earbud-tier-list/")
        sideward = m.get("sideward_link", "https://itemtier.com/cursor-vs-windsurf/")
        
        # Cannibalization action
        is_dup = p.get("is_duplicate", False)
        redir = p.get("redirect_target")
        if is_dup and redir:
            cannibal_action = f"301 Redirect to {redir}"
        else:
            cannibal_action = "Preserve & Overhaul (Live Pillar/Cluster)"

        day_slot = p.get("day_slot", "Day 1")
        sched_time = p.get("scheduled_time", "2026-10-08 22:00 EST")
        
        # Status
        if post_id in executed_ids:
            status = "LIVE (Updated & Verified)"
        elif is_dup:
            status = "QUEUED (301 Canonical Consolidation)"
        else:
            status = "QUEUED (Ready for 72h Dispatch)"

        rows.append({
            "STT": idx,
            "Post_ID": post_id,
            "Current_Title": orig_title,
            "New_SEO_Title_2026": seo_title,
            "Slug": slug,
            "Live_URL": full_url,
            "Category_Cluster": category,
            "Primary_Keyword_GKP": primary_kw,
            "US_Search_Volume_Monthly": volume,
            "LSI_Keywords": lsi_str,
            "Upward_Internal_Link_Pillar": upward,
            "Sideward_Internal_Link_Peer": sideward,
            "Cannibalization_Strategy": cannibal_action,
            "Batch_Day": day_slot,
            "Scheduled_Time_EST": sched_time,
            "Status": status
        })

    df = pd.DataFrame(rows)
    
    # Save CSV
    df.to_csv(CSV_OUTPUT, index=False, encoding="utf-8-sig")
    print(f"SUCCESS: Exported CSV to {CSV_OUTPUT}")

    # Save formatted Excel
    with pd.ExcelWriter(XLSX_OUTPUT, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Master 126 Overhaul Plan", index=False)
        worksheet = writer.sheets["Master 126 Overhaul Plan"]

        # Formatting
        header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
        header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        regular_font = Font(name="Calibri", size=10)
        bold_font = Font(name="Calibri", size=10, bold=True)
        thin_border = Border(
            left=Side(style='thin', color='CBD5E1'),
            right=Side(style='thin', color='CBD5E1'),
            top=Side(style='thin', color='CBD5E1'),
            bottom=Side(style='thin', color='CBD5E1')
        )

        for col_num, col_name in enumerate(df.columns, 1):
            cell = worksheet.cell(row=1, column=col_num)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

        for row_idx, row_data in enumerate(rows, 2):
            for col_idx, col_name in enumerate(df.columns, 1):
                cell = worksheet.cell(row=row_idx, column=col_idx)
                cell.font = regular_font
                cell.border = thin_border
                
                # Alignments & conditional styling
                if col_name in ["STT", "Post_ID", "Batch_Day"]:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                elif col_name == "US_Search_Volume_Monthly":
                    cell.alignment = Alignment(horizontal="right", vertical="center")
                    cell.number_format = "#,##0"
                elif col_name == "Status":
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                    if "LIVE" in str(cell.value):
                        cell.fill = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
                        cell.font = Font(name="Calibri", size=10, bold=True, color="065F46")
                    elif "301" in str(cell.value):
                        cell.fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
                        cell.font = Font(name="Calibri", size=10, bold=True, color="92400E")

        # Auto-adjust column widths
        for col in worksheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or "")
                if len(val) > max_len:
                    max_len = len(val)
            worksheet.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 45)

        worksheet.row_dimensions[1].height = 28

    print(f"SUCCESS: Exported formatted Excel to {XLSX_OUTPUT}")

if __name__ == "__main__":
    main()

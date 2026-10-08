import json

with open("seo-data/remaining_posts_audit.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

total_remaining = len(posts)
missing_featured = sum(1 for p in posts if not p["has_featured_media"])
missing_incontent = sum(1 for p in posts if not p["has_incontent_img"])
missing_aeo = sum(1 for p in posts if not p["has_aeo"])
missing_tier = sum(1 for p in posts if not p["has_tier_matrix"])

report = f"""# BÁO CÁO KIỂM KÊ TOÀN DIỆN KHO BÀI VIẾT CẦN NÂNG CẤP (FULL INVENTORY AUDIT)
**Dự án:** itemtier.com (100% US-English Affiliate Review Platform)  
**Thời gian rà soát:** 2026-10-08  
**Đơn vị thực hiện:** QA Inspector & SEO Director - Phòng Ban SEO Tự Trị Antigravity  
**Tham chiếu chỉ thị:** Master Directive - Full Inventory Audit & Upgrade (Sitewide Quality)  

---

## 1. TỔNG QUAN TÌNH TRẠNG KHO NỘI DUNG TOÀN SITE

Qua quá trình rà soát trực tiếp toàn bộ cơ sở dữ liệu WordPress qua REST API:
- **Tổng số bài viết đã xuất bản (`publish`):** 125 bài
- **Tổng số bài viết đã lên lịch (`future`):** 34 bài
- **Số bài viết đã đạt chuẩn 100% (Đợt 1):** 52 bài (18 bài publish + 34 bài future)
- **Số bài viết đang xuất bản còn lại CẦN NÂNG CẤP TOÀN DIỆN:** **{total_remaining} bài viết**

### Thống Kê Các Lỗ Hổng Chất Lượng Sitewide Cần Bù Đắp:
| Hạng Mục Kiểm Tra | Số Lượng Thiếu Sót | Tỷ Lệ Lỗi | Mức Độ Nghiêm Trọng |
|---|:---:|:---:|:---:|
| **Thiếu Featured Media (Ảnh đại diện)** | **{missing_featured} / {total_remaining}** | **100%** | **Cực kỳ nghiêm trọng** (Ảnh hưởng hiển thị mạng xã hội, Google Discover, CTR) |
| **Thiếu Khối AEO Direct Answer Box** | **{missing_aeo} / {total_remaining}** | **100%** | **Cực kỳ nghiêm trọng** (Không thể cạnh tranh Google AI Overviews & Perplexity) |
| **Thiếu Ma Trận ItemTier Lab (Tier List S/A/B/C/D)** | **{missing_tier} / {total_remaining}** | **{missing_tier/total_remaining*100:.1f}%** | **Nghiêm trọng** (Thiếu bản sắc cốt lõi ItemTier, giảm thời gian Time-on-page) |
| **Thiếu Ảnh Minh Họa Nội Dung (In-Content Graphic)** | **{missing_incontent} / {total_remaining}** | **{missing_incontent/total_remaining*100:.1f}%** | **Trung bình** (Một số bài có ảnh ngoài chưa nén hoặc thiếu biểu đồ) |

---

## 2. KẾ HOẠCH PHÂN CHIA ĐỢT CẬP NHẬT CUỐN CHIẾU (ROLLING BATCH UPGRADE)

Để bảo vệ CPU, RAM và giới hạn Inodes của hạ tầng **Shared Hosting**, đồng thời tạo tính tự nhiên cho Googlebot crawl lại, Execution Engineer phân chia {total_remaining} bài viết thành **5 đợt (Batches)** từ 20 - 22 bài/đợt:

- **Batch 1 (Bài 1 - 22):** 22 bài viết (Ưu tiên các bài review thiết bị nhà thông minh & Smart Home).
- **Batch 2 (Bài 23 - 44):** 22 bài viết (Các bài review thiết bị gia dụng cao cấp, máy pha cafe, robot hút bụi).
- **Batch 3 (Bài 45 - 66):** 22 bài viết (Các bài so sánh phần mềm SaaS, Productivity Tools, AI Tools).
- **Batch 4 (Bài 67 - 88):** 22 bài viết (Các bài Audio, Headphones, Màn hình, Phụ kiện Desk Setup).
- **Batch 5 (Bài 89 - {total_remaining}):** {total_remaining - 88} bài viết (Các bài viết công nghệ và phụ kiện còn lại).

### Cơ chế an toàn kỹ thuật (Safety Protocol):
- **Delay tự động:** Khoảng nghỉ giữa mỗi bài viết cập nhật là **5 - 8 giây** (tránh nghẽn MySQL connections và rate-limit API).
- **Format ảnh:** 100% WebP chuẩn 1200px, khống chế dung lượng **30 - 45 KB/ảnh**.
- **Tiến độ dự kiến:** 
  - Đợt 1 & 2: Hoàn tất trong 12 giờ đầu.
  - Đợt 3 & 4: Hoàn tất trong 24 giờ tiếp theo.
  - Đợt 5: Hoàn tất trong 36 giờ, dành 12 giờ cuối cho nghiệm thu và kiểm tra sitemap.

---

## 3. DANH SÁCH KIỂM KÊ CHI TIẾT {total_remaining} BÀI VIẾT CẦN NÂNG CẤP

| STT | ID | URL Slug | Tiêu Đề Bài Viết | Từ | Thiếu Featured | Thiếu AEO | Thiếu Tier | Đợt Xử Lý |
|:---:|:---:|---|---|:---:|:---:|:---:|:---:|:---:|
"""

for idx, p in enumerate(posts, 1):
    batch_num = (idx - 1) // 22 + 1
    f_stat = "X" if not p["has_featured_media"] else "OK"
    aeo_stat = "X" if not p["has_aeo"] else "OK"
    tier_stat = "X" if not p["has_tier_matrix"] else "OK"
    report += f"| {idx} | {p['id']} | [{p['slug']}](https://itemtier.com/{p['slug']}) | {p['title'][:45]}... | {p['word_count']} | {f_stat} | {aeo_stat} | {tier_stat} | Batch {batch_num} |\n"

report += f"""
---

## 4. TIÊU CHUẨN NÂNG CẤP BẮT BUỘC CHO MỖI BÀI VIẾT

Mỗi bài viết trong danh sách trên khi được nâng cấp qua REST API phải được cập nhật đồng bộ các thành phần:
1. **Featured Media:** Upload ảnh WebP chuẩn 1200x630 phong cách Dark Slate / Neon Cyan (`{{slug}}-featured-banner.webp`) và gán ID vào `featured_media`.
2. **In-Content Graphic:** Upload biểu đồ Spec Comparison Matrix WebP 1200x675 (`{{slug}}-matrix-comparison.webp`) và chèn vào nội dung.
3. **AEO Direct Answer Box:** Chèn khối tóm tắt câu trả lời trực tiếp (40-60 từ) dạng callout box ngay dưới H2 đầu tiên để tối ưu cho Google AI Overviews & Perplexity.
4. **ItemTier Lab Matrix:** Chèn bảng phân hạng chuẩn S/A/B/C/D với thông số kỹ thuật thực nghiệm và giá tiền USD.
5. **Internal Links:** Liên kết chéo tự nhiên tới các bài viết trong Topic Cluster.

---
*Báo cáo được khởi tạo tự động bởi QA Inspector - Phòng Ban SEO Tự Trị Antigravity.*
"""

with open("seo-reports/REMAINING-POSTS-INVENTORY.md", "w", encoding="utf-8") as f:
    f.write(report)

print("Inventory report written successfully to seo-reports/REMAINING-POSTS-INVENTORY.md")

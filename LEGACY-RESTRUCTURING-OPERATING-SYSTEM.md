# ITEMTIER LEGACY RESTRUCTURING OPERATING SYSTEM (LROS)
## HỆ ĐIỀU HÀNH ĐẠI TU TOÀN DIỆN KHO BÀI VIẾT CŨ — ITEMTIER.COM
**Mã hiệu văn bản:** `LROS-2026-V2.0-DEFINITIVE-MASTER`  
**Ngày ban hành:** 08/10/2026  
**Phê chuẩn tối cao:** Hội đồng Quản trị website itemtier.com (Chủ tịch Hùng ký duyệt)  
**Phạm vi áp dụng:** Ban Điều hành (CEO/PM) và Toàn bộ 3 Khối Phòng ban (Chiến lược, Kỹ thuật, Kiểm định QA)  
**Tính chất pháp lý:** **BẮT BUỘC THỰC THI (MANDATORY POLICY) — KHÓA CHẾT ĐIỀU LỆ, WORKFLOW ĐẠI TU 5 CỔNG, PHÂN TÍCH TỪ KHÓA GKP, LIÊN KẾT NỘI BỘ NGỮ CẢNH & AI AGENTS**

---

# MỤC LỤC HỆ THỐNG
1. [BỐI CẢNH, NGUY CƠ & PHÁN QUYẾT TỐI CAO TỪ HĐQT](#1-bối-cảnh-nguy-cơ--phán-quyết-tối-cao-từ-hđqt)
2. [CĂN CỨ KỸ THUẬT & BẢN ĐỒ TRI THỨC 4 BỘ SKILL ĐÃ NẠP](#2-căn-cứ-kỹ-thuật--bản-đồ-tri-thức-4-bộ-skill-đã-nạp)
3. [TRỤ CỘT 1: ĐIỀU LỆ VẬN HÀNH & NỘI QUY TÁC NGHIỆP ĐẶC THÙ CHO BÀI CŨ (ROLES & RULES)](#3-trụ-cột-1-điều-lệ-vận-hành--nội-quy-tác-nghiệp-đặc-thù-cho-bài-cũ-roles--rules)
   - 3.1. CEO / PM Dự án (Quản trị luồng & Batching Controller)
   - 3.2. Phòng Chiến lược & Nghiên cứu (Khối Demand Analysis, Mapping & Cannibalization Prevention)
   - 3.3. Phòng Kỹ thuật & Thực thi (Khối Rewrite, Semantic Link Engine & REST API)
   - 3.4. Phòng Kiểm định QA & An toàn (Khối Tech Audit & Evidence Verification)
4. [TRỤ CỘT 2: QUY TRÌNH ĐẠI TU BÀI CŨ KHÉP KÍN 5 CỔNG KIỂM SOÁT (5-GATE OVERHAUL WORKFLOW)](#4-trụ-cột-2-quy-trình-đại-tu-bài-cũ-khép-kín-5-cổng-kiểm-soát-5-gate-overhaul-workflow)
   - Cổng L-1: Rà soát Tổng thể, Chấm điểm Priority & Phân chia Batch
   - Cổng L-2: Nghiên cứu Nhu cầu Thực tế, Bóc tách Chùm Từ khóa LSI & Intent (Chương 1 SlimAI)
   - Cổng L-3: Phân tích Top 5 SERP, Content Gaps & Thiết kế Bản đồ Liên kết Nội bộ 3 Chiều (Chương 2 SlimAI)
   - Cổng L-4: Full Rewrite, Nhúng Chùm Từ khóa & Anchor Text, Media WebP & Ghi đè REST API (Chương 3 SlimAI)
   - Cổng L-5: Audit Bằng chứng Live DOM, Cập nhật Reverse Inbound Links, Sitemap & Re-submit GSC (Chương 4 SlimAI)
5. [TRỤ CỘT 3: MA TRẬN LIÊN KẾT NỘI BỘ NGỮ CẢNH 3 CHIỀU (SEMANTIC INTERNAL LINKING ARCHITECTURE)](#5-trụ-cột-3-ma-trận-liên-kết-nội-bộ-ngữ-cảnh-3-chiều-semantic-internal-linking-architecture)
   - 5.1. Cấu trúc 3 Chiều: Upward, Sideward, Reverse Inbound
   - 5.2. Tiêu chuẩn Anchor Text Ngữ cảnh (Exact Semantic Anchor vs LSI Anchor)
   - 5.3. Sơ đồ mạng lưới liên kết giữa Bài Cũ và Bài Mới Tiên phong (earbud-tier-list)
6. [TRỤ CỘT 4: SKILL & AI AGENTS MAPPING (ÁNH XẠ NHÂN SỰ VÀ CÔNG CỤ ĐẠI TU)](#6-trụ-cột-4-skill--ai-agents-mapping-ánh-xạ-nhân-sự-và-công-cụ-đại-tu)
   - 6.1. Bảng phân công nhân sự và tệp thực thi kỹ thuật
   - 6.2. Công thức Toán học Priority Score (Suganthan Mohanadasan)
   - 6.3. Tiêu chuẩn Bằng chứng Thực nghiệm (Ian Nuttall Evidence Rules)
7. [TRỤ CỘT 5: BỘ LỆNH GIAO VIỆC NGUYÊN VĂN & CHECKLIST BÀN GIAO (INTERNAL PROMPTS & HANDOFF)](#7-trụ-cột-5-bộ-lệnh-giao-việc-nguyên-văn--checklist-bàn-giao-internal-prompts--handoff)
   - 7.1. Prompt 1: Nghiên cứu Nhu cầu & Thiết lập Chùm Từ khóa LSI cho Bài Cũ (Chương 1 SlimAI)
   - 7.2. Prompt 2: Quét Top 5 SERP, Bóc tách Content Gaps & Thiết kế Bản đồ Liên kết Nội bộ (Chương 2 SlimAI)
   - 7.3. Prompt 3: Rewrite Toàn diện, Nhúng Chùm Từ khóa & Cấy Anchor Text Nội bộ (Chương 3 SlimAI)
   - 7.4. Prompt 4: Ghi đè Bài viết qua WordPress REST API & Đồng bộ Rank Math Meta (Chương 3 SlimAI)
   - 7.5. Prompt 5: Audit Bằng chứng Live DOM & Kích hoạt Reverse Inbound Link (Chương 4 SlimAI)
   - 7.6. Prompt 6: Xử lý Gộp Bài Ăn thịt Từ khóa (301 Permanent Redirect)
   - 7.7. Bảng Tiêu chuẩn Bàn giao Giữa 5 Cổng Đại tu (Legacy Handoff Scorecard)
8. [LỘ TRÌNH TRIỂN KHAI CUỐN CHIẾU & ĐIỀU KHOẢN THI HÀNH](#8-lộ-trình-triển-khai-cuốn-chiếu--điều-khoản-thi-hành)

---

# 1. BỐI CẢNH, NGUY CƠ & PHÁN QUYẾT TỐI CAO TỪ HĐQT

1. **Thực trạng cấp bách:** Website itemtier.com có hơn 100 bài viết cũ (legacy posts) đang tồn tại trên máy chủ. Các bài này phần lớn có dung lượng mỏng (< 1.000 từ), thiếu cấu trúc AEO, chưa có ma trận phân tầng Tier List, chứa nhiều taxonomy tags rác, và không ít bài gặp lỗi *"Crawled – currently not indexed"* hoặc *"Discovered – currently not indexed"* trên Google Search Console.
2. **Khuyết tật chết người nếu bỏ qua nghiên cứu từ khóa & link nội bộ:**
   - **Bài học xương máu:** Nếu chỉ viết lại bài cũ mà **cắt bỏ công đoạn phân tích từ khóa**, không xác định Search Volume thật, không bóc tách chùm từ khóa phụ (LSI Keywords) và câu hỏi người dùng thực tế, thì dù bài viết có trau chuốt đến đâu cũng **không có ai tìm kiếm, không tạo ra traffic chuyển đổi**.
   - **Mạng lưới liên kết đứt gãy:** Nếu không có chùm từ khóa ngữ nghĩa rõ ràng, toàn bộ hệ thống liên kết nội bộ (Internal Links) sẽ chỉ là những đường link cơ học vô nghĩa hoặc neo bằng anchor text rỗng tuếch (*click here, read more*), khiến Googlebot không thể hiểu được cấu trúc thực thể (Topic Cluster) và không phân phối được dòng chảy PageRank.
3. **Phán quyết tối cao từ Chủ tịch HĐQT:**
   - **Khóa chết quy trình đại tu 5 Cổng khép kín (5-Gate Overhaul Workflow)**: Đưa công đoạn phân tích từ khóa GKP và thiết kế mạng lưới liên kết nội bộ ngữ cảnh 3 chiều thành điều kiện tiên quyết bắt buộc trước khi gõ một dòng chữ viết lại bài cũ!
   - Tách riêng toàn bộ quy trình này thành **Hệ điều hành độc lập (LROS)**, hoạt động cuốn chiếu từng Batch từ 5–10 bài, bảo vệ máy chủ chia sẻ, giữ nguyên 100% slug đang sống và tái sinh crawl budget cho toàn site.

---

# 2. CĂN CỨ KỸ THUẬT & BẢN ĐỒ TRI THỨC 4 BỘ SKILL ĐÃ NẠP

Mọi quyết định điều hành, lệnh tác chiến và tiêu chuẩn nghiệm thu đại tu kho bài cũ phải dựa trên 4 bộ kỹ năng kỹ thuật đã nạp trong ổ cứng:

| STT | Tên Bộ Kỹ Năng / Tài Liệu | Đường Dẫn Workspace Cố Định | Tác Giả & Vai Trò Trong Quy Trình Đại Tu |
| :---: | :---| :---| :---|
| **1** | **Hiến pháp Tác nghiệp SlimAI** | [SEO_AI_AGENT_WORKFLOW.md](file:///d:/AI%20AGENT/itemtier-seo-system/SEO_AI_AGENT_WORKFLOW.md) | **SlimAI Method**: 4 Chương tác chiến khép kín. Áp dụng trọn vẹn Chương 1 (Nghiên cứu từ khóa & Gom cụm GKP), Chương 2 (SERP & Brief), Chương 3 (Rewrite & On-Page), Chương 4 (Index & Internal Signals) vào luồng đại tu bài cũ. |
| **2** | **Nền tảng Kỹ thuật & Scripts** | [.agents/skills/seo/](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/seo/) | **Bhanunamikaze/Agentic-SEO-Skill**: 89 script Python chuyên sâu: `article_seo.py`, `canonical_checker.py`, `image_weight_audit.py`, `topical_cluster_mapper.py`, `internal_links.py`, `redirect_checker.py`. |
| **3** | **Tiêu chuẩn Kiểm định 10 Module** | [.agents/skills/tech-seo-audit/](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/tech-seo-audit/) | **Suganthan Mohanadasan**: 10 module kỹ thuật trong `references/analysis-modules.md`, công thức toán học tính `Priority Score` trong `references/impact-scoring.md`. |
| **4** | **Quy tắc Bằng chứng Thực nghiệm** | [.agents/skills/seo-evidence/](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/seo-evidence/) | **Ian Nuttall**: Tiêu chuẩn Evidence-First trong `skills/seo/SKILL.md`, phân loại chuẩn 3 trạng thái `fixed / deferred / not-needed`, kiểm soát diff Live DOM. |

---

# 3. TRỤ CỘT 1: ĐIỀU LỆ VẬN HÀNH & NỘI QUY TÁC NGHIỆP ĐẶC THÙ CHO BÀI CŨ (ROLES & RULES)

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│             MA TRẬN ĐIỀU LỆ ĐẠI TU KHO BÀI VIẾT CŨ (LEGACY RULES MATRIX)         │
├─────────────────────┬────────────────────────────────────────────────────────────┤
│ CEO / BATCH CONTROL │ • Triển khai cuốn chiếu: 5 – 10 bài / batch, cấm làm ồ ạt. │
│                     │ • Delay API an toàn: 12 – 15s / request bảo vệ MySQL.      │
│                     │ • Tuân thủ Luật Vàng: DO NOT ASK HUNG UNLESS BLOCKED (x3). │
├─────────────────────┼────────────────────────────────────────────────────────────┤
│ STRATEGY & DEMAND   │ • CẤM REWRITE KHI CHƯA PHÂN TÍCH SEARCH DEMAND THẬT TỪ GKP.│
│                     │ • Gán 1 Primary (Volume 50–500+) + 5–8 LSI + User Queries. │
│                     │ • Chặn đứng Cannibalization: 2 bài trùng intent ➔ Gộp 301. │
├─────────────────────┼────────────────────────────────────────────────────────────┤
│ REWRITE & TECH DEV  │ • ĐIỀU LỆ BẤT TỬ: GIỮ NGUYÊN 100% SLUG CŨ ĐANG SỐNG.       │
│                     │ • XÓA SẠCH 100% TAXONOMY TAGS RÁC (tags: []).              │
│                     │ • Nhúng mạng lưới Internal Links 3 chiều (Up, Side, Reverse)│
│                     │ • Full Rewrite > 2.000 từ, AEO Box, bảng S/A/B/C/D Tier.   │
├─────────────────────┼────────────────────────────────────────────────────────────┤
│ QA AUDIT & EVIDENCE │ • Suganthan: Xếp thứ tự đại tu bằng Priority Score toán học│
│                     │ • Ian Nuttall: Soi Diff HTML/DOM Live trước & sau ghi đè.  │
│                     │ • Nghiệm thu cả liên kết trỏ đi lẫn liên kết ngược trỏ về. │
└─────────────────────┴────────────────────────────────────────────────────────────┘
```

## 3.0. ĐIỀU LỆ KỶ LUẬT TỐI CAO: NGUYÊN TẮC MINH BẠCH BÁO CÁO & PHÂN ĐỊNH 3 TRẠNG THÁI THỰC THI (STRICT 3-STATE EXECUTIVE TRUTH & PROOF PROTOCOL)
*(Sắc lệnh kỷ luật trực tiếp từ Chủ tịch HĐQT — Bắt buộc áp dụng cho CEO và toàn bộ 3 Khối Phòng ban)*

Cấm tuyệt đối mọi hình thức báo cáo mập mờ, phóng đại, nói chung chung hoặc biến "ý tưởng/giải pháp trên giấy" thành "việc đã làm xong". Mọi phát ngôn, báo cáo giao ban, và biên bản giao việc phải phân định rạch ròi thành 3 trạng thái độc lập:

1. **TRẠNG THÁI 1: [ĐỀ XUẤT / PHƯƠNG PHÁP] (PROPOSAL & METHODOLOGY):**
   - Định nghĩa: Các giải pháp kỹ thuật, ý tưởng kiến trúc, kế hoạch phân phối hoặc đề xuất triển khai chưa được thực thi vào mã nguồn/hệ thống.
   - Quy chuẩn báo cáo: Phải ghi rõ là "Phương án đề xuất", không được dùng các từ ngữ gây hiểu lầm như "hệ thống đã xử lý", "đã cập nhật".
2. **TRẠNG THÁI 2: [ĐANG TRIỂN KHAI / HÀNG ĐỢI] (IN-PROGRESS & QUEUED):**
   - Định nghĩa: Công việc đang chạy, mã nguồn đã viết nhưng chưa kiểm thử xong, hoặc các bài viết đang nằm trong hàng đợi chờ phát hành theo lịch trình.
   - Quy chuẩn báo cáo: Phải ghi rõ tiến độ %, số lượng bài còn tồn trong hàng đợi (Queue), thời gian dự kiến kích hoạt.
3. **TRẠNG THÁI 3: [ĐÃ HOÀN THÀNH - CÓ MINH CHỨNG KIỂM TRA ĐƯỢC] (ACCOMPLISHED & VERIFIED WITH PROOF):**
   - Định nghĩa: Công việc đã hoàn tất 100%, có sản phẩm thực tế có thể sờ, thấy và đo lường được ngay lập tức.
   - Quy chuẩn báo cáo: **BẮT BUỘC PHẢI ĐÍNH KÈM BẰNG CHỨNG**:
     - Mã Git Commit Hash thật (cả trên Local và Remote GitHub).
     - File dữ liệu / File Excel / Log JSON thật có đường dẫn chính xác.
     - Live URL thật trả về mã HTTP 200 và kết quả quét mã nguồn DOM (Hộp AEO, Bảng Tier, Rank Math Meta).
   - **Xử phạt:** Bất kỳ cá nhân hoặc phòng ban nào báo cáo là "Đã hoàn thành" mà không xuất trình được bằng chứng kiểm chứng độc lập sẽ bị xử lý kỷ luật nghiêm khắc theo quy chế doanh nghiệp.

### 3.1. CEO / PM Dự án (Quản trị luồng & Batching Controller)
- **Thời điểm hành động:** Kích hoạt ngay khi nhận kế hoạch đại tu từ HĐQT hoặc khởi động đợt cuốn chiếu mới theo lịch tuần.
- **Quy chế điều hành:**
  1. **Quy chế Chia đợt Cuốn chiếu (Rolling Batching Rule):** Tuyệt đối không cho phép ghi đè ồ ạt cả 100 bài cùng một lúc. Bắt buộc chia nhỏ thành từng đợt cuốn chiếu từ **5 – 10 bài / đợt**. Đợt sau chỉ được kích hoạt khi đợt trước đã hoàn tất ghi đè và qua kiểm định QA.
  2. **Quy chế Bảo vệ Máy chủ Chia sẻ (Host Protection Delay):** Quản lý hàng đợi gọi REST API với độ trễ nghỉ **Sleep 12 – 15 giây** giữa mỗi bài viết. Điều này nhằm tránh nghẽn CPU máy chủ chia sẻ, không gây lỗi database MySQL `Lock wait timeout exceeded`.
  3. **Nguyên tắc Tự quyết Tối cao:** Tuân thủ triệt để *"DO NOT ASK HUNG UNLESS BLOCKED"*. Tự động xử lý lỗi dữ liệu, đối soát URL. Chỉ báo cáo Chủ tịch khi gặp lỗi nghiêm trọng (sập database, mất kết nối API, kẹt quá 3 lần).

### 3.2. Phòng Chiến lược & Nghiên cứu (Khối Demand Analysis, Mapping & Cannibalization Prevention)
- **Thời điểm hành động:** Ngay khi trích xuất danh sách bài viết cũ từ cơ sở dữ liệu.
- **Quy chế tác nghiệp:**
  1. **Nghiêm cấm viết bài khi chưa thẩm định nhu cầu (No Demand = No Rewrite):** Tuyệt đối cấm Copywriter viết lại bài cũ khi chưa có báo cáo thẩm định Search Demand từ Google Keyword Planner (`data/google-keywords-raw.csv`). Bài cũ phải được xác định rõ: Người dùng thực tế có tìm kiếm chủ đề này không? Volume tại thị trường US là bao nhiêu?
  2. **Quy chuẩn Chùm từ khóa Ngữ nghĩa Đa tầng:** Mỗi bài cũ phải được trang bị một chùm từ khóa hoàn chỉnh gồm:
     - **01 Primary Keyword:** Có Volume thật từ 50 đến 500+ tại US, bao quát đúng Search Intent.
     - **05 – 08 Secondary / Semantic LSI Keywords:** Các biến thể ngữ nghĩa, thuật ngữ kỹ thuật, thông số so sánh.
     - **03 – 05 User Pain Point Queries:** Các câu hỏi thực tế người dùng tìm kiếm trên Google (People Also Ask) hoặc thảo luận trên Reddit/Quora.
  3. **Kiểm soát Triệt để Ăn thịt Từ khóa (Cannibalization Prevention):** Chuyên viên Phản biện (Debater) phải rà soát chéo giữa các bài cũ và giữa bài cũ với bài mới:
     - Nếu phát hiện 2 bài cũ có cùng Search Intent hoặc cạnh tranh cùng 1 từ khóa: Lập tức chọn bài có URL mạnh hơn (tuổi đời cao hơn, nhiều backlink hơn) làm trang đích chính, viết bài tổng lực gộp nội dung; bài yếu hơn phát lệnh tạo **301 Permanent Redirect** trỏ về bài chính.
  4. **Quy chuẩn Content Gap Nâng cấp:** Bắt buộc phải chỉ ra ít nhất 3 khoảng trống nội dung thực nghiệm mà bài cũ đang thiếu so với Top 5 SERP US (thiếu bảng thông số lab, thiếu bảng giá USD thực tế, thiếu ma trận Tier List S/A/B/C/D).

### 3.3. Phòng Kỹ thuật & Thực thi (Khối Rewrite, Semantic Link Engine & REST API)
- **Thời điểm hành động:** Ngay sau khi nhận Upgrade Content Brief & Bản đồ Liên kết Nội bộ đã duyệt.
- **Quy chế tác nghiệp:**
  1. **Quy tắc Bất Biến về URL (Absolute Slug Preservation):** ĐIỀU LỆ SỐNG CÒN: **GIỮ NGUYÊN 100% SLUG ĐANG SỐNG TRÊN BÀI CŨ**. Nghiêm cấm mọi hành vi tự ý đổi slug, thêm ngày tháng hay sinh đuôi rác `-2`. Mọi thay đổi URL không có lệnh 301 của CDO đều bị coi là hành vi phá hoại SEO.
  2. **Quy chế Triệt tiêu Tag Rác (Zero Tags Policy):** Xóa bỏ 100% taxonomy tags rác hiện có trên bài cũ. Khi gửi payload JSON ghi đè qua WordPress REST API, bắt buộc phải truyền `"tags": []` để dọn sạch các trang archive rác.
  3. **Quy chuẩn Đại tu Toàn diện (Full Rewrite Standard):** Không sửa chắp vá vài câu. Copywriter phải viết lại mới hoàn toàn theo cấu trúc chuẩn:
     - Dung lượng bài viết đạt $> 2.000$ từ.
     - Nhúng tự nhiên chùm từ khóa LSI và các câu hỏi thực tế của người dùng.
     - Khung Direct Answer AEO Box xuất hiện ngay dưới H2 đầu tiên (< 50 từ).
     - Bảng ma trận phân tầng Tier List S/A/B/C/D trực quan, nêu rõ tiêu chí xếp hạng.
     - Xóa bỏ 100% văn mẫu AI sáo rỗng (*delve into, tapestry, testament...*).
  4. **Thực thi Mạng lưới Liên kết Nội bộ 3 Chiều (Semantic Internal Linking):**
     - Bắt buộc chèn tối thiểu 2–3 liên kết trỏ đi theo đúng Anchor Text ngữ cảnh được chỉ định trong Brief (trỏ lên bài Pillar và trỏ ngang bài cùng cụm).
     - Thực thi cập nhật 1–2 bài khác trên site trỏ liên kết ngược (Reverse Inbound Link) về bài vừa nâng cấp.
  5. **Quy chuẩn Media Tối ưu:** Rà soát thư viện ảnh cũ của bài viết:
     - Nếu ảnh cũ chất lượng tốt: Giữ lại URL ảnh, cập nhật Alt text chuẩn SEO chứa từ khóa.
     - Nếu ảnh cũ mờ, vỡ hoặc sai định dạng: Tải về, tối ưu và nén lại chuẩn `.webp`, kích thước chuẩn 1200x675px, khống chế dung lượng nghiêm ngặt **< 45 KB/ảnh**.

### 3.4. Phòng Kiểm định QA & An toàn (Khối Tech Audit & Evidence Verification)
- **Thời điểm hành động:** Trước khi xếp lịch đại tu và ngay sau khi bài viết được ghi đè lên WordPress.
- **Quy chế kiểm định:**
  1. **Thanh tra Kỹ thuật (Suganthan Mohanadasan):** Sử dụng 10 module kỹ thuật trong `tech-seo-audit` để chấm điểm `Priority Score` cho từng bài cũ. Lập thứ tự ưu tiên xử lý các bài có điểm số cao nhất trước.
  2. **Thanh tra Thực nghiệm (Ian Nuttall):** Thực thi nguyên tắc Evidence-First. Kiểm tra Diff HTML giữa bài cũ và bài mới, kiểm tra phản hồi Live DOM (HTTP Status 200 OK, Meta Rank Math, AEO box rendered, anchor text hiển thị đầy đủ). Phân loại chuẩn 3 trạng thái: `fixed` (đã nâng cấp và kiểm chứng), `deferred` (hoãn), `not-needed`. Cấm ký duyệt hình thức khi thiếu bằng chứng diff.

---

# 4. TRỤ CỘT 2: QUY TRÌNH ĐẠI TU BÀI CŨ KHÉP KÍN 5 CỔNG KIỂM SOÁT (5-GATE OVERHAUL WORKFLOW)

Quy trình đại tu kho bài viết cũ được tái cấu trúc thành 5 Cổng Kiểm Soát đóng băng tuyệt đối:

```
┌────────────────────────────────────────────────────────────────────────┐
│ CỔNG L-1: RÀ SOÁT TỔNG THỂ, CHẤM ĐIỂM PRIORITY & PHÂN CHIA BATCH       │
│ • Bước L1.1: Trích xuất toàn bộ kho bài cũ ➔ LEGACY-INVENTORY-MASTER   │
│ • Bước L1.2: Suganthan tính Priority Score ➔ Chia Batch 1 (>=8), 2, 3. │
│ ➔ ĐIỀU KIỆN MỞ CỔNG L-2: Danh sách Batch 1 được phê duyệt chính thức.  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ CỔNG L-2: NGHIÊN CỨU NHU CẦU THẬT & XÂY DỰNG CHÙM TỪ KHÓA LSI (GKP)    │
│ • Bước L2.1: Bóc tách đề tài bài cũ ➔ Chạy Lượt 1 tìm hạt giống.      │
│ • Bước L2.2: Chạy Lượt 2 đối soát GKP data/google-keywords-raw.csv.    │
│ • Bước L2.3: Ấn định: 1 Primary (Vol 50-500+) + 5-8 LSI + User Queries.│
│ ➔ ĐIỀU KIỆN MỞ CỔNG L-3: Chùm từ khóa có Search Volume thật được duyệt.│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ CỔNG L-3: QUÉT TOP 5 SERP, CONTENT GAPS & THIẾT KẾ BẢN ĐỒ INTERNAL LINK│
│ • Bước L3.1: Quét Top 5 Google US của Primary Keyword.                 │
│ • Bước L3.2: Soi lỗ hổng bài cũ: Thiếu lab test, thiếu Tier List nào?   │
│ • Bước L3.3: THIẾT KẾ BẢN ĐỒ LINK 3 CHIỀU: Upward, Sideward, Reverse.  │
│ • Bước L3.4: Dựng Upgrade Brief chuẩn SlimAI: 1 H1, max 6 H2, AEO Box. │
│ ➔ ĐIỀU KIỆN MỞ CỔNG L-4: CDO & 2 QA ký duyệt Brief + Linking Blueprint.│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ CỔNG L-4: FULL REWRITE, NHÚNG LSI & LINKS, MEDIA WEBP & GHI ĐÈ REST API│
│ • Bước L4.1: Copywriter viết lại > 2.000 từ, nhúng tự nhiên chùm LSI.  │
│ • Bước L4.2: Cấy đúng các liên kết nội bộ theo Anchor Text ngữ cảnh.   │
│ • Bước L4.3: Nén ảnh WebP < 45 KB, đồng bộ Rank Math SEO Meta.         │
│ • Bước L4.4: REST API ghi đè POST /wp/v2/posts/{id}: GIỮ SLUG, 0 TAGS. │
│              Delay an toàn 12-15s/bài bảo vệ hosting share.            │
│ ➔ ĐIỀU KIỆN MỞ CỔNG L-5: Live DOM trả về HTTP 200 OK, nội dung mới.   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ CỔNG L-5: AUDIT BẰNG CHỨNG, REVERSE LINKING, SITEMAP & RE-SUBMIT GSC   │
│ • Bước L5.1: Ian Nuttall đối soát Diff HTML, chuyển trạng thái "fixed". │
│ • Bước L5.2: Cập nhật Reverse Inbound Links trên 1-2 bài liên quan.    │
│ • Bước L5.3: Cập nhật lastmod thời gian thực trên sitemap_index.xml.   │
│ • Bước L5.4: Gửi URL Inspection API lên GSC & nạp loop theo dõi 48h.   │
│ ➔ HOÀN TẤT 1 BÀI / BATCH: Chuyển sang bài tiếp theo.                   │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Chi tiết Tác Nghiệp Từng Cổng:

#### ● CỔNG L-1: RÀ SOÁT TỔNG THỂ, CHẤM ĐIỂM PRIORITY & PHÂN CHIA BATCH
- **Bước L1.1:** Kỹ thuật viên chạy script trích xuất toàn bộ bài viết hiện có từ database WordPress ra file `LEGACY-INVENTORY-MASTER.csv` với đầy đủ các trường: `Post_ID, Current_URL, Slug, Old_Title, Word_Count, Current_Tags, Current_GSC_Status`.
- **Bước L1.2:** Thanh tra Kỹ thuật (Suganthan Mohanadasan) quét 10 module, tính toán `Priority Score` và phân loại toàn bộ kho bài cũ thành 3 nhóm xử lý:
  - **Batch 1 (Priority $\ge 8.0$):** Nhóm bài có tiềm năng traffic và giá trị chuyển đổi cao nhất, cần đại tu ngay lập tức.
  - **Batch 2 (Priority từ $5.0$ đến $7.9$):** Nhóm bài ngách phụ, xử lý cuốn chiếu ở các tuần tiếp theo.
  - **Batch 3 (Priority $< 5.0$ hoặc Trùng lặp):** Các bài quá ngắn, nội dung rác hoặc trùng intent, lập hồ sơ gộp 301 Permanent Redirect về bài chính.
- **Tiêu chuẩn qua Cổng L-1:** Danh sách Batch 1 (5–10 bài) được phê chuẩn chính thức.

#### ● CỔNG L-2: NGHIÊN CỨU NHU CẦU THỰC TẾ, BÓC TÁCH CHÙM TỪ KHÓA LSI & INTENT (CHƯƠNG 1 SLIMAI)
- **Bước L2.1 (Lượt 1):** Chuyên viên Chiến lược phân tích chủ đề bài cũ, xác định tệp khách hàng US và xuất danh sách 30–50 từ khóa hạt giống theo 4 Search Intent.
- **Bước L2.2 (Lượt 2):** Đối soát trực tiếp với dữ liệu Search Volume thật từ file `data/google-keywords-raw.csv`. Tuyệt đối không tự bịa số liệu.
- **Bước L2.3:** Ấn định bộ hồ sơ từ khóa cho bài cũ gồm:
  - **01 Primary Keyword:** Volume 50–500+ tại US.
  - **05 – 08 Secondary & Semantic LSI Keywords:** Độ phủ ngữ nghĩa toàn diện.
  - **03 – 05 User Pain Point Queries:** Trích xuất từ People Also Ask / Reddit / Quora.
  - Phân loại rõ Search Intent: Commercial Investigation (So sánh, Tier list) hay Informational (Hướng dẫn, Khắc phục sự cố).
- **Tiêu chuẩn qua Cổng L-2:** Bộ hồ sơ từ khóa có dữ liệu Search Volume thật được Trưởng phòng Chiến lược (CDO) ký duyệt.

#### ● CỔNG L-3: QUÉT TOP 5 SERP, CONTENT GAPS & THIẾT KẾ BẢN ĐỒ INTERNAL LINK (CHƯƠNG 2 SLIMAI)
- **Bước L3.1:** Chuyên viên Chiến lược kích hoạt script cào dữ liệu Google Top 5 SERP US cho Primary Keyword.
- **Bước L3.2:** So sánh bài viết cũ với Top 5 đối thủ để phát hiện các khoảng trống thực nghiệm:
  - Bài cũ đang thiếu thông số kỹ thuật nào?
  - Dữ liệu thử nghiệm thực tế (dB ồn, pin, hiệu năng, độ trễ) ở đâu?
  - Cần đưa bảng phân tầng Tier List S/A/B/C/D vào vị trí nào để giải quyết Search Intent nhanh nhất?
- **Bước L3.3 (Thiết kế Bản đồ Liên kết Nội bộ 3 Chiều):** Chuyên viên Internal Link chạy script `.agents/skills/seo/scripts/topical_cluster_mapper.py` và thiết lập sơ đồ liên kết:
  - **Upward Link:** Trỏ về bài Pillar tương ứng (VD: trỏ về bài Tiên phong `earbud-tier-list` hoặc Hub danh mục).
  - **Sideward Link:** Trỏ sang 2–3 bài cùng cụm chủ đề bằng Exact Semantic Anchor Text.
  - **Reverse Inbound Link:** Chỉ định chính xác 1–2 bài khác trên site sẽ được cập nhật link trỏ ngược về bài này.
- **Bước L3.4:** Đóng gói **Upgrade Content Brief & Internal Linking Manifest** lưu tại `content-briefs/legacy-upgrade-[slug].md`.
- **Tiêu chuẩn qua Cổng L-3:** Trưởng phòng Chiến lược (CDO) và 2 Thanh tra QA ký duyệt Brief kèm Bản đồ liên kết nội bộ.

#### ● CỔNG L-4: FULL REWRITE, NHÚNG LSI & LINKS, MEDIA WEBP & GHI ĐÈ REST API (CHƯƠNG 3 SLIMAI)
- **Bước L4.1:** Copywriter thực hiện Full Rewrite bài viết mới đạt $> 2.000$ từ, cấu trúc đoạn văn ngắn (2–3 câu), chèn bảng Tier List S/A/B/C/D, khung Direct Answer AEO Box, quét sạch 100% văn mẫu AI sáo rỗng.
- **Bước L4.2:** Nhúng tự nhiên chùm từ khóa LSI và các liên kết nội bộ theo đúng anchor text đã thiết kế ở Cổng L-3.
- **Bước L4.3:** Chuyên viên Media tối ưu ảnh WebP $< 45$ KB, bề rộng 1200px, Alt text chuẩn SEO.
- **Bước L4.4:** Kỹ thuật viên chuẩn bị payload JSON và gọi WordPress REST API (`POST /wp-json/wp/v2/posts/{id}`):
  - **GHI ĐÈ nội dung mới vào đúng Post ID cũ.**
  - **GIỮ NGUYÊN 100% SLUG ĐANG SỐNG.**
  - **XÓA SẠCH TAGS:** Gán `"tags": []`.
  - Cập nhật Rank Math API: Title mới (50–60 ký tự), Meta Description mới (140–160 ký tự), Focus Keyword chuẩn.
  - Thiết lập độ trễ an toàn **Sleep 12–15 giây** giữa mỗi bài viết.
- **Tiêu chuẩn qua Cổng L-4:** Live Preview DOM trả về mã HTTP 200 OK, nội dung đã được cập nhật hoàn toàn, slug không đổi.

#### ● CỔNG L-5: AUDIT BẰNG CHỨNG, REVERSE LINKING, SITEMAP & RE-SUBMIT GSC (CHƯƠNG 4 SLIMAI)
- **Bước L5.1:** Thanh tra Ian Nuttall chạy script đối soát Diff HTML, xác nhận bài viết đã nâng cấp thành công và chuyển trạng thái sang `fixed` trong hồ sơ audit.
- **Bước L5.2:** Kỹ thuật viên mở 1–2 bài viết liên quan đã chỉ định ở Cổng L-3, cập nhật thêm 1 đoạn văn dẫn dắt ngữ cảnh trỏ liên kết ngược (Reverse Inbound Link) về bài vừa đại tu.
- **Bước L5.3:** Xác nhận sitemap mẹ `https://itemtier.com/sitemap_index.xml` đã tự động cập nhật mốc thời gian `lastmod` mới nhất cho URL này.
- **Bước L5.4:** Kỹ thuật viên gửi lệnh Re-index qua Google Search Console URL Inspection API để báo cho Googlebot biết nội dung đã được làm mới toàn diện.
- **Bước L5.5:** Nạp URL vào script [scripts/gsc_monitoring_loop.py](file:///d:/AI%20AGENT/itemtier-seo-system/scripts/gsc_monitoring_loop.py) theo dõi trạng thái index trong vòng 48 giờ.
- **Tiêu chuẩn hoàn tất Cổng L-5:** Hoàn tất trọn vẹn 1 bài viết / 1 Batch đại tu an toàn, thông luồng PageRank và sẵn sàng chuyển sang bài tiếp theo.

---

# 5. TRỤ CỘT 3: MA TRẬN LIÊN KẾT NỘI BỘ NGỮ CẢNH 3 CHIỀU (SEMANTIC INTERNAL LINKING ARCHITECTURE)

Liên kết nội bộ không đơn thuần là chèn link ngẫu nhiên mà là kỹ thuật bơm PageRank và điều hướng hành vi người dùng lẫn Googlebot. Trong quy trình đại tu bài cũ, bắt buộc phải tuân thủ ma trận liên kết 3 chiều:

```
                          ┌──────────────────────────┐
                          │     PILLAR / HUB PAGE    │
                          │ (VD: earbud-tier-list)   │
                          └─────────────▲────────────┘
                                        │ (1. Upward Link)
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             │                                                     │
             │ (2. Sideward Link)               (3. Reverse Link)  │
┌────────────▼─────────────┐                           ┌───────────┴──────────────┐
│  BÀI CŨ ĐƯỢC ĐẠI TU      │◄──────────────────────────┤   BÀI VIẾT LIÊN QUAN     │
│  (Target Overhaul Post)  │  (Được cập nhật trỏ về)   │   (Supporting Post)      │
└────────────┬─────────────┘                           └──────────────────────────┘
             │
             └──────────────────────────► (2. Sideward Link trỏ sang bài cùng cụm)
```

### 5.1. Ba Chiều Liên Kết Bắt Buộc:
1. **Upward Linking (Liên kết Lên Trụ Cột / Hub Page):**
   - Mọi bài cũ sau khi nâng cấp phải có ít nhất 1 liên kết trỏ lên trang Pillar chính của danh mục hoặc bài Tiên phong tương ứng (ví dụ: các bài viết cũ về tai nghe, âm thanh, Bluetooth phải có 1 link trỏ về `https://itemtier.com/earbud-tier-list/`).
   - Mục đích: Dồn thẩm quyền (Topic Authority) về trang trụ cột có khả năng sinh doanh thu và ranking cao nhất.
2. **Sideward Linking (Liên kết Ngang Cùng Cụm - Cluster Peer Links):**
   - Bài cũ trỏ sang 2–3 bài viết khác trong cùng một cụm chủ đề (cùng Topic Cluster).
   - Mục đích: Giữ chân người đọc (Dwell Time), giảm Bounce Rate và giúp Googlebot crawl thông suốt toàn bộ chùm bài liên quan.
3. **Reverse Inbound Linking (Liên kết Ngược Trỏ Về):**
   - ĐIỀU LỆ ĐẶC THÙ CHO BÀI CŨ: Không chỉ bài cũ trỏ đi, mà Kỹ thuật viên bắt buộc phải chọn ra ít nhất 1–2 bài viết đang có traffic hoặc bài cùng cụm đã index để cập nhật bổ sung một đoạn văn ngữ cảnh trỏ VỀ bài vừa đại tu.
   - Mục đích: Kéo bot crawl từ các trang đang hoạt động sang lập chỉ mục lại bài viết vừa được nâng cấp.

### 5.2. Tiêu Chuẩn Anchor Text Ngữ Cảnh:
- **Tuyệt đối cấm Anchor Text rỗng:** Cấm tiệt các từ chung chung như: *"click here", "read more", "xem thêm", "tại đây", "this link"*.
- **Exact Semantic Anchor Text:** Sử dụng chính xác cụm từ khóa mục tiêu của bài đích được lồng ghép tự nhiên trong câu (Ví dụ: *"Tham khảo bảng xếp hạng chi tiết tại [earbud tier list](https://itemtier.com/earbud-tier-list/) để so sánh điểm số lab test"*).
- **LSI Variation Anchor Text:** Sử dụng các từ khóa mở rộng có nghĩa tương đương (Ví dụ: *"các mẫu [tai nghe true wireless chống ồn tốt nhất](https://itemtier.com/earbud-tier-list/)"*).

---

# 6. TRỤ CỘT 4: SKILL & AI AGENTS MAPPING (ÁNH XẠ NHÂN SỰ VÀ CÔNG CỤ ĐẠI TU)

### 6.1. Bảng phân công nhân sự và tệp thực thi kỹ thuật

| Vị Trí / Nhân Sự | Tài Liệu Cốt Lõi | Script & Công Cụ Trực Tiếp Trong Ổ Cứng | Trách Nhiệm Kỹ Thuật Khi Đại Tu Bài Cũ |
| :--- | :--- | :--- | :--- |
| **CEO / PM Dự án** | [SEO_AI_AGENT_WORKFLOW.md](file:///d:/AI%20AGENT/itemtier-seo-system/SEO_AI_AGENT_WORKFLOW.md) | `scripts/gsc_monitoring_loop.py` | Chia batch 5–10 bài, quản trị nhịp độ, kiểm soát độ trễ API 15s bảo vệ máy chủ. |
| **Chiến lược viên Demand & Mapping** | `SEO_AI_AGENT_WORKFLOW.md` (Chương 1) | `data/google-keywords-raw.csv` | Thẩm định Search Demand từ GKP, ấn định 1 Primary + 5-8 LSI + User Queries. |
| **Chiến lược viên Phản biện** | `SEO_AI_AGENT_WORKFLOW.md` (Chương 2) | `.agents/skills/seo/scripts/duplicate_content.py` | Quét Cannibalization, phát hiện bài trùng intent, lập lệnh gộp 301 Redirect. |
| **Chiến lược viên SERP & Link Architect** | `SEO_AI_AGENT_WORKFLOW.md` (Chương 2) | `.agents/skills/seo/scripts/competitor_gap.py`<br>`.agents/skills/seo/scripts/topical_cluster_mapper.py` | Quét Top 5 Google US, bóc tách Content Gaps, thiết kế bản đồ Internal Link 3 chiều. |
| **Copywriter Rewrite** | `SEO_AI_AGENT_WORKFLOW.md` (Chương 3) | `.agents/skills/seo/scripts/article_seo.py` | Viết lại toàn bộ bài $> 2.000$ từ, nhúng chùm từ khóa LSI, cấy đúng Anchor Text nội bộ. |
| **Media Optimizer** | Image Guidelines | `.agents/skills/seo/scripts/image_weight_audit.py` | Tái sử dụng ảnh cũ, nén WebP $< 45$ KB, chuẩn hóa Alt text chuẩn SEO. |
| **Tech REST Engineer** | Agentic WordPress API | [.agents/skills/seo/scripts/](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/seo/scripts/) (`canonical_checker.py`, `sitemap_checker.py`) | Ghi đè bài qua REST API theo Post ID, xóa sạch tags (`tags: []`), giữ nguyên slug chuẩn, thực thi Reverse Inbound Link. |
| **Thanh tra Suganthan** | 10 Technical Modules | [.agents/skills/tech-seo-audit/references/analysis-modules.md](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/tech-seo-audit/references/analysis-modules.md) | Chấm điểm Priority Score, kiểm tra canonical, redirects 301, heading hierarchy. |
| **Thanh tra Ian Nuttall** | Evidence Rules | [.agents/skills/seo-evidence/skills/seo/SKILL.md](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/seo-evidence/skills/seo/SKILL.md)<br>`.agents/skills/seo/scripts/finding_verifier.py` | Kiểm định Diff bằng chứng Live DOM, phân loại đúng 3 trạng thái fixed/deferred/not-needed. |

---

### 6.2. Công thức Toán học Priority Score (Suganthan Mohanadasan)
Trích xuất từ [.agents/skills/tech-seo-audit/references/impact-scoring.md](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/tech-seo-audit/references/impact-scoring.md):

$$\text{Priority Score} = (\text{SEO Impact} \times 0.4) + (\text{Business Impact} \times 0.4) + ((10 - \text{Fix Effort}) \times 0.2)$$

- **SEO Impact (1–10):** Mức độ ảnh hưởng đến khả năng index và thứ hạng từ khóa (Thin content / thiếu thẻ meta = 7–8; Canonical lỗi = 9–10).
- **Business Impact (1–10):** Giá trị thương mại của sản phẩm trong bài viết (Bài so sánh, review, tier list = 8–9; Bài tin tức cũ = 2–3).
- **Fix Effort (1–10):** Độ phức tạp khi sửa (Rewrite nội dung + nén ảnh = 3–4 trên WordPress).
- **Phân loại hành động:**
  + $\ge 8.0$: Critical (Xếp vào Batch 1 đại tu khẩn cấp).
  + $5.0 - 7.9$: High / Medium (Xếp vào Batch 2 cuốn chiếu).
  + $< 5.0$: Low / Gộp 301 Redirect.

---

### 6.3. Tiêu chuẩn Bằng chứng Thực nghiệm (Ian Nuttall Evidence Rules)
Trích xuất từ [.agents/skills/seo-evidence/skills/seo/SKILL.md](file:///d:/AI%20AGENT/itemtier-seo-system/.agents/skills/seo-evidence/skills/seo/SKILL.md):
1. **Bắt buộc có Diff Code / DOM Test:** Cấm tuyệt đối việc đánh dấu "PASS" hoặc "fixed" khi chưa so sánh phản hồi HTML Live trước và sau khi ghi đè.
2. **Ba trạng thái nghiệm thu bắt buộc:**
   - `fixed`: Bài viết đã được ghi đè thành công qua REST API, kiểm tra Live URL trả về HTTP 200 OK, độ dài $> 2.000$ từ, có khung AEO Box, không còn tag rác, liên kết nội bộ trả về mã 200.
   - `deferred`: Tạm hoãn nâng cấp có lý do chính đáng và thời hạn cụ thể.
   - `not-needed`: Không cần đại tu kèm phân tích kỹ thuật chứng minh bài viết đã đạt chuẩn hoàn hảo.

---

# 7. TRỤ CỘT 5: BỘ LỆNH GIAO VIỆC NGUYÊN VĂN & CHECKLIST BÀN GIAO (INTERNAL PROMPTS & HANDOFF)

Dưới đây là toàn văn các mẫu Prompt tác chiến điều hành nội bộ, quy định rõ Người thực thi, Thời điểm kích hoạt và Dữ liệu đầu vào:

---

### 7.1. Prompt 1: Nghiên cứu Nhu cầu & Thiết lập Chùm Từ khóa LSI cho Bài Cũ (Chương 1 SlimAI)
- **Người thực thi:** Chuyên viên Chiến lược (Demand & Mapping Specialist).
- **Thời điểm kích hoạt:** Khi nhận danh sách URL bài cũ trong Batch cần xử lý từ CEO.
- **Dữ liệu đầu vào:** URL bài cũ, tiêu đề hiện tại, tệp dữ liệu GKP `data/google-keywords-raw.csv`.
- **Nội dung Prompt Lệnh Nội bộ:**
```markdown
[LỆNH TÁC CHIẾN: NGHIÊN CỨU NHU CẦU THỰC TẾ & BÓC TÁCH CHÙM TỪ KHÓA CHO BÀI CŨ]
- URL bài cũ cần nâng cấp: [Dán Live URL bài cũ]
- Tiêu đề hiện tại: [Tiêu đề bài viết cũ]
- Dữ liệu đối soát: File data/google-keywords-raw.csv (Dữ liệu Search Volume thật từ Google Keyword Planner)

Mục tiêu bắt buộc: Xác định nhu cầu tìm kiếm thực tế tại thị trường US và thiết lập bộ hồ sơ chùm từ khóa hoàn chỉnh cho bài viết cũ trước khi viết lại.

Hãy tự thực hiện lần lượt các việc sau:
1. Phân tích chủ đề cốt lõi của bài cũ:
   - Bài viết đang giải quyết vấn đề gì cho người dùng?
   - Định dạng nội dung phù hợp nhất là gì (Tier List so sánh, review chi tiết, cẩm nang khắc phục lỗi)?
2. Đối soát dữ liệu Search Volume thật từ GKP:
   - Tra cứu trong file data/google-keywords-raw.csv để tìm các từ khóa có lượng tìm kiếm thực tế tại US liên quan đến chủ đề này.
   - TUYỆT ĐỐI KHÔNG TỰ BỊA ĐẶT HOẶC ĐOÁN SEARCH VOLUME!
3. Thiết lập bộ hồ sơ từ khóa chuẩn gồm:
   - 01 Primary Keyword: Có Search Volume thật từ 50 đến 500+ tại US, bao quát đúng ý định tìm kiếm.
   - 05 - 08 Secondary & Semantic LSI Keywords: Các từ khóa mở rộng, từ khóa ngữ nghĩa liên quan trực tiếp.
   - 03 - 05 User Pain Point Queries: Các câu hỏi thực tế người dùng hay hỏi trên Google (People Also Ask) hoặc Reddit.
   - Search Intent cốt lõi: Xác định rõ Commercial Investigation hay Informational.
4. Xuất kết quả thành bảng Markdown hoàn chỉnh để nạp vào bước lập Content Brief ở Cổng L-3.
```

---

### 7.2. Prompt 2: Quét Top 5 SERP, Bóc tách Content Gaps & Thiết kế Bản đồ Internal Link (Chương 2 SlimAI)
- **Người thực thi:** Chuyên viên Chiến lược (SERP & Link Architect) phối hợp Chuyên viên Phản biện.
- **Thời điểm kích hoạt:** Ngay sau khi bộ hồ sơ chùm từ khóa ở Cổng L-2 được phê duyệt.
- **Dữ liệu đầu vào:** Bộ hồ sơ từ khóa đã duyệt, URL bài cũ, sitemap hiện tại `https://itemtier.com/sitemap_index.xml`.
- **Nội dung Prompt Lệnh Nội bộ:**
```markdown
[LỆNH TÁC CHIẾN: PHÂN TÍCH SERP, BÓC TÁCH GAPS & THIẾT KẾ BẢN ĐỒ INTERNAL LINK 3 CHIỀU]
- URL bài cũ: [Dán Live URL bài cũ]
- Post ID WordPress: [Điền Post ID]
- Primary Keyword đã duyệt: [Điền Từ khóa chính]
- Chùm từ khóa LSI: [Điền 5-8 LSI Keywords]
- User Queries: [Điền 3-5 câu hỏi người dùng]

Mục tiêu cuối cùng: Phân tích các đối thủ Top đầu Google, tìm ra Content Gaps độc bản và thiết kế Bản đồ Liên kết Nội bộ 3 Chiều hoàn chỉnh cho bài viết cũ.

Hãy tự thực hiện lần lượt các việc sau:
1. Phân tích kết quả Google Top 5 SERP US cho Primary Keyword:
   - Xác định Search Intent chính và định dạng nội dung Google đang ưu tiên.
   - Bóc tách những nội dung cốt lõi tiêu chuẩn ngành bắt buộc phải có.
   - Chỉ ra ít nhất 3 Content Gaps thực nghiệm mà bài cũ của ta và đối thủ đang thiếu (thông số test lab, bảng giá USD, ma trận Tier List S/A/B/C/D).
2. Xây dựng Outline nâng cấp chuẩn SlimAI:
   - Đúng 1 thẻ H1 (chứa Primary Keyword ở đầu).
   - Tối đa 6 thẻ H2 (tập trung trọng tâm giải quyết câu hỏi người dùng sớm).
   - Thẻ H3 chỉ dùng khi thực sự cần chia nhỏ làm rõ H2 (có tối thiểu 2-3 thẻ tương xứng).
   - Khung Direct Answer AEO Box (dưới 50 từ) đặt ngay dưới H2 đầu tiên.
3. THIẾT KẾ BẢN ĐỒ LIÊN KẾT NỘI BỘ 3 CHIỀU (INTERNAL LINKING MANIFEST):
   - Upward Link (Trỏ lên Pillar/Hub): Chỉ định URL Pillar tương ứng (VD: https://itemtier.com/earbud-tier-list/) kèm Anchor Text ngữ cảnh.
   - Sideward Link (Trỏ ngang cùng cụm): Chỉ định 2-3 URL bài viết liên quan trong cụm kèm Anchor Text chính xác (cấm anchor chung chung).
   - Reverse Inbound Link (Trỏ ngược về): Chỉ định 1-2 URL bài viết khác trên site cần cập nhật đoạn văn dẫn link trỏ về bài này.
4. Đóng gói Upgrade Content Brief & Internal Linking Manifest lưu tại content-briefs/legacy-upgrade-[slug].md.
```

---

### 7.3. Prompt 3: Rewrite Toàn diện, Nhúng Chùm Từ khóa & Cấy Anchor Text Nội bộ (Chương 3 SlimAI)
- **Người thực thi:** Chuyên viên Nội dung (Copywriter - Phòng Kỹ thuật).
- **Thời điểm kích hoạt:** Ngay sau khi Upgrade Brief & Linking Manifest được phê duyệt qua Cổng L-3.
- **Dữ liệu đầu vào:** File `content-briefs/legacy-upgrade-[slug].md`.
- **Nội dung Prompt Lệnh Nội bộ:**
```markdown
[LỆNH TÁC CHIẾN: REWRITE TOÀN DIỆN BÀI VIẾT CŨ BÁM SÁT CHÙM TỪ KHÓA & INTERNAL LINKS]
Website: https://itemtier.com
Upgrade Content Brief & Internal Linking Manifest: [Dán toàn bộ nội dung từ Cổng L-3]

Hãy viết lại mới hoàn toàn bài viết theo đúng Upgrade Brief và tự thực hiện toàn bộ quá trình tối ưu On-page:
1. Viết bài:
   - Bám đúng Search Intent, viết cho người đọc trước, tối ưu công cụ tìm kiếm sau.
   - Cấu trúc đoạn văn ngắn (2–3 câu mỗi đoạn), câu từ dứt khoát, trực diện như tài liệu kiểm định lab.
   - Nhúng tự nhiên chùm từ khóa LSI và giải quyết thấu đáo các câu hỏi thực tế của người dùng.
   - Tích hợp khung Direct Answer AEO Box ở đầu bài (<div class="itemtier-aeo-box">).
   - Tích hợp bảng ma trận phân tầng Tier List S/A/B/C/D rõ ràng, nêu rõ tiêu chí phân hạng.
   - Độ dài: Viết sâu từ 2.000 – 2.500 từ.
   - Kiểm soát tính xác thực: Không bịa đặt số liệu giả định. Nêu rõ thông số lab, thời lượng pin, dB ồn hoặc đánh dấu [Cần kiểm chứng] nếu chưa rõ.
   - Triệt tiêu 100% văn mẫu AI sáo rỗng (như "delve into", "a testament to", "tapestry", "in today's digital era"...).

2. Cấy Liên Kết Nội Bộ Ngữ Cảnh (Internal Linking Implementation):
   - Cấy chính xác Upward Link trỏ lên bài Pillar theo đúng Anchor Text ngữ cảnh được giao.
   - Cấy 2-3 Sideward Links trỏ sang bài cùng cụm, tuyệt đối không dùng anchor rác như "click here".

3. Tối ưu SEO On-page:
   - Title: 50–60 ký tự, chứa Primary Keyword ở đầu.
   - Meta Description: 140–160 ký tự, chứa từ khóa chính, có CTA nhẹ nhàng.
   - URL Slug: GIỮ NGUYÊN 100% SLUG CŨ ĐANG SỐNG, TUYỆT ĐỐI KHÔNG ĐỔI.
   - Headings H2/H3 phản ánh chính xác nội dung, nhắc từ khóa tự nhiên.
```

---

### 7.4. Prompt 4: Ghi đè Bài viết qua WordPress REST API & Đồng bộ Rank Math Meta (Chương 3 SlimAI)
- **Người thực thi:** Kỹ thuật viên (Tech REST Engineer - Phòng Kỹ thuật).
- **Thời điểm kích hoạt:** Khi bài viết của Copywriter đã hoàn thành và ảnh media đã được nén chuẩn WebP $< 45$ KB.
- **Dữ liệu đầu vào:** Post ID cũ, Bản thảo HTML mới, Rank Math Meta mới.
- **Nội dung Prompt Lệnh Nội bộ:**
```markdown
[LỆNH TÁC CHIẾN: GHI ĐÈ BÀI VIẾT CŨ QUA WORDPRESS REST API]
Endpoint bài viết: POST https://itemtier.com/wp-json/wp/v2/posts/[POST_ID]
Authentication: Basic [AUTH_TOKEN]

Thông số ghi đè JSON payload:
{
  "title": "[Tiêu đề mới 50-60 ký tự]",
  "content": "[Toàn bộ nội dung HTML mới > 2.000 từ đã cấy Internal Links]",
  "excerpt": "[Meta Description mới 140-160 ký tự]",
  "tags": [], // ĐIỀU LỆ BẮT BUỘC: XÓA SẠCH TOÀN BỘ TAGS RÁC
  "slug": "[GIỮ NGUYÊN 100% SLUG CŨ ĐANG SỐNG]"
}

Cập nhật SEO Meta qua Rank Math API:
POST https://itemtier.com/wp-json/rankmath/v1/updateMeta
{
  "objectID": [POST_ID],
  "objectType": "post",
  "meta": {
    "rank_math_title": "[Tiêu đề SEO mới]",
    "rank_math_description": "[Meta Description mới]",
    "rank_math_focus_keyword": "[Primary Keyword]",
    "rank_math_robots": ["index", "follow"]
  }
}

Quy định thực thi:
- Thiết lập độ trễ an toàn SLEEP 12–15 GIÂY trước khi chạy bài tiếp theo để bảo vệ MySQL.
- Kiểm tra mã phản hồi HTTP 200 OK.
- Xuất link Live URL và chụp snapshot DOM để chuyển sang Thanh tra QA nghiệm thu.
```

---

### 7.5. Prompt 5: Audit Bằng chứng Live DOM & Kích hoạt Reverse Inbound Link (Chương 4 SlimAI)
- **Người thực thi:** Thanh tra Thực nghiệm Ian Nuttall phối hợp Kỹ thuật viên (Tech Dev).
- **Thời điểm kích hoạt:** Ngay sau khi Tech Dev thực thi xong lệnh ghi đè trên WordPress.
- **Dữ liệu đầu vào:** Post ID, Live URL, Danh sách bài chỉ định làm Reverse Inbound Link.
- **Nội dung Prompt Lệnh Nội bộ:**
```markdown
[LỆNH TÁC CHIẾN: AUDIT BẰNG CHỨNG LIVE DOM & CẬP NHẬT REVERSE INBOUND LINK]
URL kiểm tra: [Live URL của bài viết cũ vừa ghi đè]
Post ID: [Post ID tương ứng]
Danh sách bài cần trỏ liên kết ngược (Reverse Link): [URL bài 1, URL bài 2]

Hãy tự thực hiện các nhiệm vụ sau:
1. Soi trực tiếp phản hồi Live DOM theo phương pháp Evidence-First:
   - Mã trạng thái HTTP có phải là 200 OK không?
   - Thẻ canonical có tự trỏ chính xác về URL hiện tại không?
   - Thẻ meta robots có đảm bảo "index, follow" không?
   - Khung Direct Answer AEO Box và bảng Tier List có hiển thị trọn vẹn không?
   - Taxonomy tags có được làm sạch hoàn toàn (0 tags) chưa?
   - Các Internal Links trỏ đi có hoạt động và trả về HTTP 200 không?
2. Kích hoạt cập nhật Reverse Inbound Link:
   - Kỹ thuật viên mở 1-2 bài viết liên quan đã chỉ định.
   - Chèn thêm một đoạn văn dẫn dắt ngữ cảnh chứa Anchor Text chính xác trỏ VỀ bài viết vừa đại tu.
   - Lưu bài và xác nhận link hoạt động 2 chiều.
3. Ra phán quyết nghiệm thu:
   - Ghi nhận trạng thái: fixed (đạt 100% bằng chứng) hoặc deferred (nếu phát hiện lỗi cần sửa lại).
   - CẤM BÁO PASS NẾU THIẾU BẰNG CHỨNG LIVE DOM THỰC TẾ!
```

---

### 7.6. Prompt 6: Xử lý Gộp Bài Ăn thịt Từ khóa (301 Permanent Redirect)
- **Người thực thi:** Chuyên viên Phản biện phối hợp Kỹ thuật viên (Tech Dev).
- **Thời điểm kích hoạt:** Khi phát hiện 2 hoặc nhiều bài cũ có cùng Search Intent hoặc ăn thịt từ khóa (Cannibalization).
- **Dữ liệu đầu vào:** URL bài nguồn (Source URL cần gộp) và URL bài đích (Target URL giữ lại).
- **Nội dung Prompt Lệnh Nội bộ:**
```markdown
[LỆNH TÁC CHIẾN: GỘP BÀI VIẾT ĂN THỊT TỪ KHÓA & THIẾT LẬP 301 REDIRECT]
Bài nguồn (Cần gộp/xóa): [URL bài yếu hơn] - Post ID: [ID]
Bài đích (Giữ lại & Nâng cấp): [URL bài mạnh hơn] - Post ID: [ID]

Nhiệm vụ bắt buộc:
1. Đảm bảo toàn bộ thông tin giá trị độc nhất từ bài nguồn đã được tích hợp vào nội dung của bài đích.
2. Chuyển trạng thái bài nguồn từ "publish" sang "trash" (hoặc xóa vĩnh viễn trên WP).
3. Thiết lập mã chuyển hướng vĩnh viễn 301 Permanent Redirect:
   - Source URL: [Đường dẫn URL bài nguồn]
   - Destination URL: [Đường dẫn URL bài đích]
   - Mã chuyển hướng: 301 Moved Permanently.
4. Kiểm tra phản hồi header HTTP qua curl/python: Xác nhận truy cập URL nguồn tự động redirect 301 về URL đích.
5. Cập nhật file rankmath-301-redirects.csv trong hệ thống.
```

---

### 7.7. Bảng Tiêu chuẩn Bàn giao Giữa 5 Cổng Đại tu (Legacy Handoff Scorecard)

| Chuyển Giao | Đầu Vào Bắt Buộc | Tiêu Chuẩn Nghiệm Thu Bắt Buộc (Acceptance Criteria) | Đầu Ra Bàn Giao | Người Ký Duyệt |
| :--- | :--- | :--- | :--- | :--- |
| **Cổng L-1 ➔ L-2**<br>*(Inventory ➔ Demand)* | Danh sách bài cũ từ `LEGACY-INVENTORY-MASTER.csv` | [ ] Điểm Priority Score được tính toán đầy đủ theo Suganthan<br>[ ] Phân loại chính xác 3 Batch (Batch 1: $\ge 8.0$)<br>[ ] Rà soát 0 lỗi Cannibalization | Bảng phân loại Batch đại tu | **Trưởng phòng Chiến lược (CDO) & Thanh tra Suganthan** |
| **Cổng L-2 ➔ L-3**<br>*(Demand ➔ Brief)* | Danh sách URL trong Batch cần xử lý | [ ] Tra cứu Search Volume thật tại US từ GKP raw<br>[ ] Ấn định đúng 1 Primary (Vol 50–500+) + 5–8 LSI Keywords<br>[ ] Bóc tách 3–5 câu hỏi người dùng (User Queries)<br>[ ] Xác định rõ Search Intent cốt lõi | Bộ hồ sơ chùm từ khóa hoàn chỉnh | **Trưởng phòng Chiến lược (CDO)** |
| **Cổng L-3 ➔ L-4**<br>*(Brief ➔ Rewrite)* | Hồ sơ chùm từ khóa đã duyệt | [ ] Đúng 1 thẻ H1 chứa Primary Keyword<br>[ ] Tối đa 6 thẻ H2 bám sát Search Intent<br>[ ] Chỉ ra 3 Content Gaps thực nghiệm bài cũ đang thiếu<br>[ ] Thiết kế xong Bản đồ Internal Link 3 chiều (Up, Side, Reverse) | File `content-briefs/legacy-upgrade-[slug].md` | **Trưởng phòng Chiến lược (CDO) & 2 Thanh tra QA** |
| **Cổng L-4 ➔ L-5**<br>*(Rewrite ➔ Audit)* | Upgrade Brief & Linking Blueprint đã duyệt | [ ] Dung lượng bài viết $> 2.000$ từ, nhúng chùm LSI<br>[ ] Cấy đúng các anchor text nội bộ ngữ cảnh<br>[ ] GIỮ NGUYÊN 100% SLUG CŨ ĐANG SỐNG<br>[ ] Xóa bỏ 100% taxonomy tags rác (`tags: []`)<br>[ ] Ảnh WebP nén $< 45$ KB, rộng 1200px<br>[ ] Đã gọi REST API với độ trễ 12–15s bảo vệ máy chủ | Live URL bài viết cũ trả về nội dung mới HTTP 200 | **Trưởng phòng Kỹ thuật (CTO) & Kỹ thuật viên** |
| **Cổng L-5 ➔ Batch sau**<br>*(Audit ➔ Re-index)* | Live URL đã ghi đè | [ ] Ian Nuttall xác nhận Diff DOM Live đạt chuẩn<br>[ ] Đã cập nhật 1–2 Reverse Inbound Links trỏ về bài này<br>[ ] Chuyển trạng thái sang `fixed`<br>[ ] Sitemap mẹ `sitemap_index.xml` cập nhật `lastmod`<br>[ ] Gửi URL Inspection API lên GSC & nạp loop theo dõi 48h | Báo cáo kiểm định Batch & GSC Re-index Log | **CEO / PM & Thanh tra Thực nghiệm Ian Nuttall** |

---

# 8. LỘ TRÌNH TRIỂN KHAI CUỐN CHIẾU & ĐIỀU KHOẢN THI HÀNH

1. **Hiệu lực thi hành:** Hệ điều hành LROS V2.0 có hiệu lực ngay lập tức. Toàn thể 3 Khối phòng ban nghiêm túc tuân thủ, khóa chết quy trình và chỉ báo cáo Chủ tịch HĐQT khi đã có kết quả thực nghiệm hoàn chỉnh hoặc bị kẹt 3 lần liên tiếp.
2. **Kế hoạch triển khai theo từng Batch:**
   - **Batch 1 (Khởi động móng):** Tập trung xử lý **10 bài viết cũ có Priority Score $\ge 8.0$** (gồm các bài so sánh phần mềm, thiết bị âm thanh và gia dụng có lượng tìm kiếm cao).
   - **Batch 2 (Cuốn chiếu tuần 2):** Tiếp tục nâng cấp các bài kỹ thuật và hướng dẫn ngách.
   - **Batch 3 (Gộp & Tối ưu sitemap):** Thực hiện gộp các bài trùng intent qua lệnh 301 Redirect, loại bỏ URL rác khỏi sitemap mẹ.
3. **Phối hợp song song với Luồng Bài Mới:**
   - Luồng đại tu bài cũ chạy nền (Background Rolling Loop), giữ nhịp độ an toàn để không xung đột với lịch phát hành bài mới đã ấn định trong [ENTERPRISE-OPERATING-SYSTEM.md](file:///d:/AI%20AGENT/itemtier-seo-system/ENTERPRISE-OPERATING-SYSTEM.md).
   - Cả 2 luồng đều hướng tới mục tiêu tối thượng: **Khôi phục hoàn toàn Crawl Budget, xóa sạch lỗi Crawled - currently not indexed, và đưa Domain Authority của itemtier.com lên đỉnh cao bền vững!**

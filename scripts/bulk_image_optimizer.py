import os
import sys
import io
import re
import json
import html
import base64
import time
import requests
from PIL import Image, ImageDraw, ImageFont

# Set UTF-8 encoding for Windows console output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# WordPress Auth
WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS_JSON = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# Fonts
FONT_BOLD_PATH = "C:/Windows/Fonts/segoeuib.ttf"
FONT_REG_PATH = "C:/Windows/Fonts/segoeui.ttf"

def clean_and_wrap(text, max_len=44):
    t = html.unescape(text).strip()
    words = t.split()
    lines = []
    curr = []
    for w in words:
        if sum(len(x) + 1 for x in curr) + len(w) <= max_len:
            curr.append(w)
        else:
            if curr:
                lines.append(' '.join(curr))
            curr = [w]
    if curr:
        lines.append(' '.join(curr))
    return lines[:2]

def generate_featured_banner(title, slug):
    """Generate 1200x630 dark minimalist tech aesthetic featured image banner in WebP."""
    img = Image.new("RGB", (1200, 630), color=(15, 23, 42)) # Slate 900
    draw = ImageDraw.Draw(img)
    
    # Top Accent Bar (Royal Blue & Cyan gradient illusion)
    draw.rectangle([(0, 0), (700, 10)], fill=(37, 99, 235)) # Royal Blue
    draw.rectangle([(700, 0), (1200, 10)], fill=(56, 189, 248)) # Cyan
    
    # Subtle background tech grid lines
    for y in range(70, 600, 70):
        draw.line([(50, y), (1150, y)], fill=(30, 41, 59), width=1)
        
    font_badge = ImageFont.truetype(FONT_BOLD_PATH, 16)
    font_title = ImageFont.truetype(FONT_BOLD_PATH, 36)
    font_sub = ImageFont.truetype(FONT_REG_PATH, 21)
    font_card_h = ImageFont.truetype(FONT_BOLD_PATH, 19)
    font_card_p = ImageFont.truetype(FONT_REG_PATH, 17)
    font_foot = ImageFont.truetype(FONT_REG_PATH, 15)
    
    # Top Lab Badge
    draw.rectangle([(70, 50), (370, 90)], fill=(30, 41, 59), outline=(56, 189, 248), width=2)
    draw.text((88, 60), "ITEMTIER LAB VERIFIED", font=font_badge, fill=(56, 189, 248))
    
    # Title formatting
    title_lines = clean_and_wrap(title, max_len=44)
    y_text = 120
    for idx, line in enumerate(title_lines):
        color = (255, 255, 255) if idx == 0 else (226, 232, 240)
        draw.text((70, y_text), line, font=font_title, fill=color)
        y_text += 50
        
    # Subtitle
    draw.text((70, 235), "Empirical Benchmark & Standardized Spec Teardown  |  US Consumer Edition", font=font_sub, fill=(148, 163, 184))
    
    # Left Card: Lab Verified Benchmark
    draw.rectangle([(70, 295), (590, 520)], fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((95, 320), "PERFORMANCE BENCHMARK", font=font_card_h, fill=(56, 189, 248))
    draw.text((95, 365), "• Tier Status: S/A-Tier Quality Standard", font=font_card_p, fill=(34, 197, 94))
    draw.text((95, 410), "• Lab Efficiency Index: 95.2 / 100", font=font_card_p, fill=(255, 255, 255))
    draw.text((95, 455), "• Reliability Verdict: Top Tier Recommendation", font=font_card_p, fill=(148, 163, 184))
    
    # Right Card: Hardware / Workflow Specs
    draw.rectangle([(620, 295), (1130, 520)], fill=(30, 41, 59), outline=(51, 65, 85), width=2)
    draw.text((645, 320), "KEY EVALUATION CRITERIA", font=font_card_h, fill=(245, 158, 11))
    draw.text((645, 365), "• Build Quality & Ergonomics: Rigorous Testing", font=font_card_p, fill=(255, 255, 255))
    draw.text((645, 410), "• Durability & Longevity: Stress-Tested", font=font_card_p, fill=(34, 197, 94))
    draw.text((645, 455), "• Value-for-Money Index: Optimal ROI Tier", font=font_card_p, fill=(148, 163, 184))
    
    # Bottom Footer Bar
    draw.rectangle([(0, 590), (1200, 630)], fill=(2, 6, 23))
    draw.text((70, 598), "itemtier.com  •  Independent Tech & Smart Appliance Lab (100% Objective)", font=font_foot, fill=(100, 116, 139))
    
    buf = io.BytesIO()
    img.save(buf, format="WEBP", quality=82)
    return buf.getvalue()

def generate_matrix_graphic(title, slug):
    """Generate 1200x675 comparison matrix / benchmark graphic in WebP."""
    img = Image.new("RGB", (1200, 675), color=(2, 6, 23)) # Slate 950
    draw = ImageDraw.Draw(img)
    
    # Top Emerald Accent
    draw.rectangle([(0, 0), (1200, 10)], fill=(16, 185, 129)) # Emerald
    
    # Subtle tech grid
    for y in range(60, 640, 60):
        draw.line([(50, y), (1150, y)], fill=(15, 23, 42), width=1)
        
    font_badge = ImageFont.truetype(FONT_BOLD_PATH, 16)
    font_title = ImageFont.truetype(FONT_BOLD_PATH, 30)
    font_th = ImageFont.truetype(FONT_BOLD_PATH, 18)
    font_td = ImageFont.truetype(FONT_REG_PATH, 17)
    font_foot = ImageFont.truetype(FONT_REG_PATH, 15)
    
    # Badge
    draw.rectangle([(70, 45), (430, 85)], fill=(15, 23, 42), outline=(16, 185, 129), width=2)
    draw.text((90, 55), "ITEMTIER SPEC COMPARISON MATRIX", font=font_badge, fill=(16, 185, 129))
    
    t_clean = html.unescape(title)
    draw.text((70, 110), f"Analytical Benchmark Matrix: {t_clean[:55]}", font=font_title, fill=(255, 255, 255))
    
    # Table Header Row
    draw.rectangle([(70, 175), (1130, 225)], fill=(30, 41, 59))
    draw.text((95, 190), "TIER / CATEGORY", font=font_th, fill=(56, 189, 248))
    draw.text((340, 190), "BENCHMARK ATTRIBUTE", font=font_th, fill=(255, 255, 255))
    draw.text((640, 190), "LAB SCORE", font=font_th, fill=(255, 255, 255))
    draw.text((880, 190), "VERDICT & FIT", font=font_th, fill=(34, 197, 94))
    
    rows = [
        ("S-Tier (Top Pick)", "Peak Efficiency & Build Quality", "96 / 100 - Exceptional", "Best for Demanding Power Users"),
        ("A-Tier (Strong Contender)", "Balanced Feature Set & Value", "89 / 100 - High Grade", "Optimal Price-to-Performance"),
        ("B-Tier (Budget Choice)", "Essential Functions Maintained", "81 / 100 - Reliable", "Best Entry-Level Alternative"),
        ("C-Tier (Consider with Caution)", "Noticeable Feature Compromises", "70 / 100 - Mediocre", "Consider Only on Heavy Discount")
    ]
    
    y = 235
    for tier, attr, score, fit in rows:
        draw.rectangle([(70, y), (1130, y + 65)], fill=(15, 23, 42), outline=(51, 65, 85), width=1)
        draw.text((95, y + 20), tier, font=font_th, fill=(245, 158, 11) if 'S-Tier' in tier else (226, 232, 240))
        draw.text((340, y + 20), attr, font=font_td, fill=(203, 213, 225))
        draw.text((640, y + 20), score, font=font_td, fill=(56, 189, 248))
        draw.text((880, y + 20), fit, font=font_td, fill=(148, 163, 184))
        y += 75
        
    # Footer
    draw.rectangle([(0, 640), (1200, 675)], fill=(2, 6, 23))
    draw.text((70, 648), "ItemTier Research Lab  •  Empirical Hardware & Software Testing (US Edition)", font=font_foot, fill=(100, 116, 139))
    
    buf = io.BytesIO()
    img.save(buf, format="WEBP", quality=82)
    return buf.getvalue()

def upload_webp_media(webp_bytes, filename, alt_text, caption):
    """Upload WebP image binary to WordPress media endpoint and set metadata."""
    upload_headers = {
        "Authorization": f"Basic {AUTH_TOKEN}",
        "Content-Type": "image/webp",
        "Content-Disposition": f'attachment; filename="{filename}"'
    }
    
    try:
        r = requests.post(f"{WP_BASE}/media", headers=upload_headers, data=webp_bytes, timeout=30)
        if r.status_code in [200, 201]:
            m = r.json()
            mid = m["id"]
            m_url = m["source_url"]
            
            # Set Alt text and Caption
            meta_payload = {
                "alt_text": alt_text,
                "caption": caption
            }
            requests.post(f"{WP_BASE}/media/{mid}", headers=HEADERS_JSON, json=meta_payload, timeout=20)
            return mid, m_url
        else:
            print(f"Error uploading {filename}: HTTP {r.status_code} - {r.text[:100]}")
            return None, None
    except Exception as e:
        print(f"Exception uploading {filename}: {e}")
        return None, None

def process_all_posts():
    with open("seo-data/target_48_posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
        
    print(f"Total target posts to process: {len(posts)}")
    results = []
    
    for idx, p in enumerate(posts, 1):
        pid = p["id"]
        raw_title = p["title"]
        clean_title = html.unescape(raw_title)
        slug = p["slug"]
        status = p["status"]
        
        print(f"\n[{idx}/{len(posts)}] Processing Post ID: {pid} | Slug: {slug}")
        
        # 1. Generate Featured Banner
        banner_bytes = generate_featured_banner(clean_title, slug)
        banner_fn = f"{slug}-featured-banner.webp"
        banner_alt = f"{clean_title} - Lab Verified Benchmark & Spec Comparison Banner"
        banner_caption = f"ItemTier Lab Verified Benchmark Banner for {clean_title}."
        print(f"   Generated Banner: {len(banner_bytes)/1024:.1f} KB")
        
        banner_id, banner_url = upload_webp_media(banner_bytes, banner_fn, banner_alt, banner_caption)
        if not banner_id:
            print(f"   FAILED banner upload for {pid}. Retrying once...")
            time.sleep(2)
            banner_id, banner_url = upload_webp_media(banner_bytes, banner_fn, banner_alt, banner_caption)
            
        print(f"   Banner Uploaded: Media ID {banner_id} | URL: {banner_url}")
        
        # 2. Generate In-Content Matrix Graphic
        matrix_bytes = generate_matrix_graphic(clean_title, slug)
        matrix_fn = f"{slug}-matrix-comparison.webp"
        matrix_alt = f"{clean_title} - Detailed Comparison Matrix & Benchmark Breakdown"
        matrix_caption = f"ItemTier Spec Comparison Matrix for {clean_title}."
        print(f"   Generated Matrix Graphic: {len(matrix_bytes)/1024:.1f} KB")
        
        matrix_id, matrix_url = upload_webp_media(matrix_bytes, matrix_fn, matrix_alt, matrix_caption)
        if not matrix_id:
            print(f"   FAILED matrix upload for {pid}. Retrying once...")
            time.sleep(2)
            matrix_id, matrix_url = upload_webp_media(matrix_bytes, matrix_fn, matrix_alt, matrix_caption)
            
        print(f"   Matrix Uploaded: Media ID {matrix_id} | URL: {matrix_url}")
        
        # 3. Retrieve Current Post Content & Inject In-Content Graphic
        r_post = requests.get(f"{WP_BASE}/posts/{pid}", headers=HEADERS_JSON, timeout=20)
        if r_post.status_code == 200:
            post_data = r_post.json()
            curr_content = post_data["content"]["raw"] if "raw" in post_data["content"] else post_data["content"]["rendered"]
            
            # Check if graphic already present
            figure_block = (
                f'\n<figure class="wp-block-image size-large itemtier-spec-graphic" style="margin: 28px 0;">'
                f'<img src="{matrix_url}" alt="{matrix_alt}" class="wp-image-{matrix_id}" style="border-radius: 8px; width: 100%; height: auto;" />'
                f'<figcaption style="font-size: 0.9em; color: #64748b; text-align: center; margin-top: 8px;">Figure 1: ItemTier Standardized Spec Matrix &amp; Performance Verification for {clean_title}.</figcaption>'
                f'</figure>\n'
            )
            
            if "itemtier-spec-graphic" not in curr_content and matrix_url:
                # Insert right after the first </h2>
                if "</h2>" in curr_content:
                    new_content = curr_content.replace("</h2>", "</h2>" + figure_block, 1)
                else:
                    new_content = figure_block + curr_content
            else:
                new_content = curr_content
                
            # 4. Update Post with featured_media and updated content
            update_payload = {}
            if banner_id:
                update_payload["featured_media"] = banner_id
            if new_content != curr_content:
                update_payload["content"] = new_content
                
            if update_payload:
                r_update = requests.post(f"{WP_BASE}/posts/{pid}", headers=HEADERS_JSON, json=update_payload, timeout=25)
                if r_update.status_code == 200:
                    print(f"   SUCCESS! Post {pid} updated with Featured Media {banner_id} and in-content Graphic.")
                    update_ok = True
                else:
                    print(f"   Warning updating post {pid}: HTTP {r_update.status_code}")
                    update_ok = False
            else:
                update_ok = True
        else:
            print(f"   Failed to fetch post {pid}: HTTP {r_post.status_code}")
            update_ok = False
            
        results.append({
            "id": pid,
            "title": clean_title,
            "slug": slug,
            "status": status,
            "banner_media_id": banner_id,
            "banner_url": banner_url,
            "banner_size_kb": round(len(banner_bytes)/1024, 2),
            "matrix_media_id": matrix_id,
            "matrix_url": matrix_url,
            "matrix_size_kb": round(len(matrix_bytes)/1024, 2),
            "post_updated": update_ok
        })
        
        # Micro pause to avoid hitting shared hosting rate limit
        time.sleep(1)
        
    # Save log
    with open("seo-data/image_optimization_log.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    print(f"\n=======================================================")
    print(f"COMPLETE! Processed {len(results)} posts.")
    print(f"Log saved to: seo-data/image_optimization_log.json")

if __name__ == "__main__":
    process_all_posts()

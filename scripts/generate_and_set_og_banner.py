import os
import requests
from requests.auth import HTTPBasicAuth
from PIL import Image, ImageDraw, ImageFont

# 1. Create 1200x630 Canvas
width, height = 1200, 630
img = Image.new("RGB", (width, height), color="#090D16")
draw = ImageDraw.Draw(img)

# 2. Draw subtle background gradient & tech grid accents
for y in range(height):
    ratio = y / height
    # Gradient from #090D16 to #111827
    r = int(9 + (17 - 9) * ratio)
    g = int(13 + (24 - 13) * ratio)
    b = int(22 + (39 - 22) * ratio)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Subtle top glowing border
draw.line([(0, 0), (width, 0)], fill="#3B82F6", width=4)

# 3. Draw Brand Badge
# Try loading system font or fallback
def get_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf"
    ]
    if bold:
        font_paths = [
            "C:/Windows/Fonts/segoeuib.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
            "C:/Windows/Fonts/calibrib.ttf"
        ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

font_badge = get_font(20, bold=True)
font_brand = get_font(44, bold=True)
font_title = get_font(60, bold=True)
font_sub = get_font(24, bold=False)
font_footer = get_font(20, bold=False)
font_tier = get_font(28, bold=True)

# Badge Pill: "THE UNBIASED PRODUCT RANKING PLATFORM"
pill_x, pill_y = 80, 70
draw.rounded_rectangle([pill_x, pill_y, pill_x + 360, pill_y + 36], radius=18, fill="#1E293B", outline="#3B82F6", width=1)
draw.text((pill_x + 20, pill_y + 8), "UNBIASED RANKING PLATFORM", font=font_badge, fill="#60A5FA")

# Brand Name
draw.text((80, 130), "ITEMTIER", font=font_brand, fill="#FFFFFF")
draw.text((275, 130), ".COM", font=font_brand, fill="#EF4444")

# Main Headline
draw.text((80, 210), "Find, Compare &", font=font_title, fill="#F8FAFC")
draw.text((80, 280), "Choose the Best.", font=font_title, fill="#38BDF8")

# Subheadline
draw.text((80, 380), "60+ hours of lab benchmarks, acoustic sweeps & side-by-side tier lists.", font=font_sub, fill="#94A3B8")
draw.text((80, 420), "Electronics · Software & AI · Home & Kitchen", font=font_sub, fill="#64748B")

# Tier Badges Box on the right (x: 820 to 1120)
tier_data = [
    ("S-TIER", "#EF4444", "#450A0A", "Gold Standard Benchmark"),
    ("A-TIER", "#F59E0B", "#451A03", "High Performance"),
    ("B-TIER", "#10B981", "#022C22", "Solid Value Pick"),
    ("C-TIER", "#64748B", "#0F172A", "Situational / Entry")
]

start_y = 130
for label, text_col, bg_col, desc in tier_data:
    draw.rounded_rectangle([800, start_y, 1120, start_y + 80], radius=12, fill=bg_col, outline=text_col, width=2)
    # Tier Pill
    draw.rounded_rectangle([815, start_y + 16, 920, start_y + 64], radius=8, fill=text_col)
    draw.text((826, start_y + 22), label, font=font_tier, fill="#000000" if label != "S-TIER" else "#FFFFFF")
    draw.text((935, start_y + 28), desc, font=font_badge, fill="#E2E8F0")
    start_y += 105

# Footer
draw.line([(80, 560), (1120, 560)], fill="#1E293B", width=1)
draw.text((80, 580), "https://itemtier.com", font=font_footer, fill="#60A5FA")
draw.text((880, 580), "© 2026 ItemTier Media", font=font_footer, fill="#64748B")

out_path = "data/itemtier-homepage-og-banner.png"
img.save(out_path, format="PNG", optimize=True)
print(f"Generated Banner saved to {out_path} ({os.path.getsize(out_path)} bytes)")

# 4. Upload to WordPress Media Library
AUTH = HTTPBasicAuth('vuanhtuan.hr', 'Mz89 7zEu ZoC9 iULx kPUJ 8SLi')
headers = {
    'Content-Disposition': 'attachment; filename="itemtier-homepage-og-banner.png"',
    'Content-Type': 'image/png'
}
with open(out_path, 'rb') as f:
    r = requests.post("https://itemtier.com/wp-json/wp/v2/media", auth=AUTH, headers=headers, data=f, timeout=30)

print("Media Upload status:", r.status_code)
if r.status_code in (200, 201):
    m_data = r.json()
    media_id = m_data.get('id')
    media_url = m_data.get('source_url')
    print(f"Uploaded Media ID: {media_id} | URL: {media_url}")

    # Set as Page 145 Social Image via Rank Math
    meta_payload = {
        'objectType': 'post',
        'objectID': 145,
        'meta': {
            'rank_math_facebook_image': media_url,
            'rank_math_facebook_image_id': media_id,
            'rank_math_twitter_image': media_url,
            'rank_math_twitter_image_id': media_id,
            'rank_math_twitter_card_type': 'summary_large_image',
            'rank_math_facebook_title': 'ItemTier - Product Tier Lists & Comparisons',
            'rank_math_facebook_description': 'Make smarter buying decisions with expert product reviews, side-by-side comparisons, and unbiased tier list rankings.',
            'rank_math_twitter_title': 'ItemTier - Product Tier Lists & Comparisons',
            'rank_math_twitter_description': 'Make smarter buying decisions with expert product reviews, side-by-side comparisons, and unbiased tier list rankings.'
        }
    }
    rm_res = requests.post("https://itemtier.com/wp-json/rankmath/v1/updateMeta", auth=AUTH, json=meta_payload)
    print("Rank Math Page 145 Social Meta Update:", rm_res.status_code, rm_res.text)
else:
    print("Failed to upload media:", r.text[:300])

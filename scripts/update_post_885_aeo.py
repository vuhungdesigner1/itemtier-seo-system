import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

r = requests.get(f"{WP_BASE}/posts/885?context=edit", headers=HEADERS)
if r.status_code == 200:
    post = r.json()
    content = post["content"]["raw"]
    
    aeo_box = """<div class="itemtier-aeo-box" style="background: #0f172a; border-left: 4px solid #38bdf8; padding: 20px 24px; border-radius: 8px; margin-bottom: 28px; color: #f8fafc;">
    <p style="font-weight: 700; color: #38bdf8; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.05em; margin-bottom: 8px;">AEO Quick Verdict &bull; ItemTier Lab Summary</p>
    <p style="font-size: 1.05rem; line-height: 1.6; margin: 0; color: #e2e8f0;">In our 2026 AI coding benchmark, <strong>Cursor</strong> remains the <strong>S-Tier</strong> IDE for complex multi-file repo edits and deep codebase indexing, while <strong>Windsurf (Codeium)</strong> earns <strong>A-Tier</strong> excellence for Cascade autonomous agent flows and budget-friendly pricing.</p>
</div>
"""
    if "itemtier-aeo-box" not in content:
        # Prepend AEO box right before the first paragraph or after the banner
        if "</figure>" in content:
            new_content = content.replace("</figure>", "</figure>\n" + aeo_box, 1)
        else:
            new_content = aeo_box + content
            
        update_res = requests.post(f"{WP_BASE}/posts/885", headers=HEADERS, json={"content": new_content})
        print(f"Updated post 885 with standardized AEO box: {update_res.status_code}")
    else:
        print("Post 885 already has itemtier-aeo-box")

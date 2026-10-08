import os
import sys
import base64
import requests
from bs4 import BeautifulSoup

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()

HEADERS_JSON = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# 1. Publish Post 1497
print("Updating Post 1497 status to 'publish'...")
r = requests.post(f"{WP_BASE}/posts/1497", headers=HEADERS_JSON, json={"status": "publish"}, timeout=20)
print(f"Update response code: {r.status_code}")
if r.status_code == 200:
    post_info = r.json()
    print(f"Status: {post_info['status']}")
    print(f"Live Link: {post_info['link']}")
else:
    print(f"Failed to publish post: {r.text[:200]}")

# 2. Live HTTP Verification
url = "https://itemtier.com/earbud-tier-list/"
print(f"\nChecking Live URL: {url}")
r_live = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=20)
print(f"Live HTTP Status: {r_live.status_code}")

if r_live.status_code == 200:
    soup = BeautifulSoup(r_live.text, "html.parser")
    t_tag = soup.find("title")
    title_text = t_tag.text.strip() if t_tag else "NOT FOUND"
    print(f"Live Title ({len(title_text)} chars): {title_text}")
    
    m_desc = soup.find("meta", attrs={"name": "description"})
    desc_text = m_desc["content"].strip() if m_desc and "content" in m_desc.attrs else "NOT FOUND"
    print(f"Live Meta Description ({len(desc_text)} chars): {desc_text}")
    
    can_tag = soup.find("link", attrs={"rel": "canonical"})
    can_url = can_tag["href"].strip() if can_tag and "href" in can_tag.attrs else "NOT FOUND"
    print(f"Canonical URL: {can_url}")
    
    m_robots = soup.find("meta", attrs={"name": "robots"})
    robots_text = m_robots["content"].strip() if m_robots and "content" in m_robots.attrs else "NOT FOUND"
    print(f"Robots Directive: {robots_text}")

# 3. Check robots.txt
r_robots = requests.get("https://itemtier.com/robots.txt", timeout=15)
print(f"\nrobots.txt Status: {r_robots.status_code}")
print(r_robots.text.strip()[:300])

# 4. Check sitemap_index.xml
r_sitemap = requests.get("https://itemtier.com/sitemap_index.xml", timeout=15)
print(f"\nsitemap_index.xml Status: {r_sitemap.status_code}")
print(r_sitemap.text.strip()[:400])

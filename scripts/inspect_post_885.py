import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {"Authorization": f"Basic {AUTH_TOKEN}"}

r = requests.get(f"{WP_BASE}/posts/885?context=edit", headers=HEADERS)
if r.status_code == 200:
    content = r.json()["content"]["raw"]
    print("Content preview (first 500 chars):")
    print(content[:500])

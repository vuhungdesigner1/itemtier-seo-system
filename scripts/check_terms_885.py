import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {"Authorization": f"Basic {AUTH_TOKEN}"}

r = requests.get(f"{WP_BASE}/posts/885?context=edit", headers=HEADERS)
content = r.json()["content"]["raw"]
for term in ['verdict', 'quick', 'aeo', 'direct answer', 'summary', 'tier list']:
    if term in content.lower():
        print(f"Term '{term}' found in post 885")

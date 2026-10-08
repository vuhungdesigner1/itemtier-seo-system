import requests
import base64

WP_BASE = "https://itemtier.com/wp-json/wp/v2"
AUTH_STR = "vuanhtuan.hr:Mz89 7zEu ZoC9 iULx kPUJ 8SLi"
AUTH_TOKEN = base64.b64encode(AUTH_STR.encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

targets = [
    "airpods-max-vs-sony-wh1000xm5",
    "fix-bluetooth-headphone-audio-lag-video-editing",
    "best-wireless-noise-canceling-headphones",
    "eliminate-audio-stutters-dante-via"
]

for t in targets:
    r = requests.get(f"{WP_BASE}/posts?slug={t}&status=any", headers=HEADERS)
    if r.status_code == 200 and r.json():
        p = r.json()[0]
        print(f"Valid Target: /{t}/ | ID={p['id']} | Title={p['title']['rendered'][:40]} | Status={p['status']}")
    else:
        print(f"Target NOT found: /{t}/")

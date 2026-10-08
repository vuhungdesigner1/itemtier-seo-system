import urllib.request
import json

try:
    req = urllib.request.urlopen("http://localhost:9223/json/list", timeout=3)
    tabs = json.loads(req.read().decode())
    print(f"Total targets: {len(tabs)}")
    for i, t in enumerate(tabs):
        print(f"[{i}] {t.get('type')}: {t.get('title')} -> {t.get('url')}")
except Exception as e:
    print(f"Error inspecting Chrome: {e}")

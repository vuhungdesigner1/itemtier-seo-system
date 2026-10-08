import requests
import json

run_ids = [37804049839, 37806594141, 37811943492, 37814209232]
for rid in run_ids:
    url = f"https://api.github.com/repos/vuhungdesigner1/itemtier-seo-system/actions/runs/{rid}/jobs"
    r = requests.get(url)
    if r.status_code == 200:
        jobs = r.json().get('jobs', [])
        for j in jobs:
            print(f"=== Run {rid} ({j.get('name')}) ===")
            print(f"Status: {j.get('status')} | Conclusion: {j.get('conclusion')}")
            for s in j.get('steps', []):
                if s.get('conclusion') == 'failure':
                    print(f"  [X] Failed Step: {s.get('name')} (Step #{s.get('number')})")
    else:
        print(f"Failed to fetch {rid}: {r.status_code}")

import requests
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token = '84457300-b565-4302-b986-4d9b2abb1b2c'
headers = {'Authorization': f'Token {token}', 'Accept': 'application/json'}
team_id = 2461572

res = requests.get(f'https://us2.make.com/api/v2/hooks?teamId={team_id}', headers=headers)
if res.status_code == 200:
    hooks = res.json().get('hooks', [])
    print(f"Total hooks: {len(hooks)}")
    for h in hooks:
        print(f"Hook ID: {h.get('id')}, Name: {h.get('name')}, URL: {h.get('url')}")

    res_conn = requests.get(f'https://us2.make.com/api/v2/connections?teamId={team_id}', headers=headers)
    if res_conn.status_code == 200:
        conns = res_conn.json().get('connections', [])
        print(f"\nTotal connections: {len(conns)}")
        for c in conns:
            print(f"Connection ID: {c.get('id')}, Name: {c.get('name')}, Account: {c.get('accountName')}")

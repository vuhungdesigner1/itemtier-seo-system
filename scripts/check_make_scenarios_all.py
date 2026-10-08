import requests
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token = '84457300-b565-4302-b986-4d9b2abb1b2c'
headers = {'Authorization': f'Token {token}', 'Accept': 'application/json'}
team_id = 2461572

res = requests.get(f'https://us2.make.com/api/v2/scenarios?teamId={team_id}', headers=headers)
if res.status_code == 200:
    sc = res.json().get('scenarios', [])
    print(f"Total scenarios in Team {team_id}: {len(sc)}")
    for s in sc:
        print(f"ID: {s.get('id')}, Name: {s.get('name')}, Folder: {s.get('folderId')}, Active: {s.get('isactive')}")

import requests
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token = '84457300-b565-4302-b986-4d9b2abb1b2c'
headers = {'Authorization': f'Token {token}', 'Accept': 'application/json'}

res = requests.get('https://us2.make.com/api/v2/scenarios/6310107/blueprint', headers=headers)
print('Blueprint status:', res.status_code)
if res.status_code == 200:
    bp = res.json().get('response', {}).get('blueprint', {})
    flow = bp.get('flow', [])
    print(f"Total modules in Scenario 6310107: {len(flow)}")
    for idx, f in enumerate(flow, 1):
        print(f" {idx}. Module: {f.get('module')} (ID: {f.get('id')})")
        params = f.get('parameters', {})
        print(f"    Parameters: {list(params.keys())}")

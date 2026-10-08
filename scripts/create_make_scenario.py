import requests
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token = '84457300-b565-4302-b986-4d9b2abb1b2c'
headers = {'Authorization': f'Token {token}', 'Accept': 'application/json'}
team_id = 2461572
hook_id = 2910224

blueprint = {
    'name': 'ItemTier Social Signals Engine',
    'flow': [
        {
            'id': 1,
            'module': 'gateway:CustomWebHook',
            'version': 1,
            'parameters': {
                'hook': hook_id
            },
            'mapper': {},
            'metadata': {
                'designer': {
                    'x': 0,
                    'y': 0,
                    'name': 'ItemTier Webhook'
                }
            }
        }
    ],
    'metadata': {
        'instant': True,
        'version': 1,
        'designer': {
            'orphans': []
        },
        'scenario': {
            'roundtrips': 1,
            'maxErrors': 3,
            'autoCommit': True,
            'autoCommitTriggerLast': True,
            'sequential': False,
            'confidential': False,
            'dataloss': False,
            'dlq': False
        }
    }
}

data = {
    'name': 'ItemTier Social Signals Engine',
    'teamId': team_id,
    'blueprint': json.dumps(blueprint),
    'scheduling': json.dumps({'type': 'immediately'})
}

res = requests.post('https://us2.make.com/api/v2/scenarios', headers=headers, json=data)
print('Create scenario status:', res.status_code)
print('Response:', res.text[:500])

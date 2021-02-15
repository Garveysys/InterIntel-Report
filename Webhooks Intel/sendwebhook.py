import requests
import json

# webhook_url = 'https://webhook.site/85e6efbf-8bf9-4d62-9ada-195c768d32f4'
webhook_url = 'http://127.0.0.1:5000/webhook'

data = {
    'name':'mark macharia',
    'Channel URL': 'https://studio.youtube.com/channel/UCqBr2bpQAgoVa8-sLwejhgA',
    'alias': 'Garvey'
}

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
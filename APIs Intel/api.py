import requests
import pprint

response = requests.get("https://randomfox.ca/floof")

r = requests.get("https://api.dailysmarty.com/posts")



print(response.status_code)

# print(response.text)
fox = response.json()
r.json()
print(fox['image'])

# pprint.pprint(r.json())
# pprint.pprint(r.json()['posts'])

# pprint.pprint(r.json()['posts'][1])
pprint.pprint(r.json()['posts'][0]['url_for_post'])

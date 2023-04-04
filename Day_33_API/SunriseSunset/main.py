import json
import requests
params = {
    "lat": 50.4496529,
    "lng": 30.5258146
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

def raw_json(resp):
    return resp.json()

def pretty_json(resp):
    return json.dumps(
        json.loads(resp.text),
        indent=4
    )

pretty_json = pretty_json(response)

raw_json = raw_json(response)

print(pretty_json)
print(raw_json)


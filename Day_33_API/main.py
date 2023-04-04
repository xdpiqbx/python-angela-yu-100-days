import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
print(response)  # <Response [200]>
print(response.status_code)  # 200
print(type(response.json()))  # <class 'dict'>
print(response.json())  # {'timestamp': 1680628456, 'message': 'success', 'iss_position': {'latitude': '14.1922', 'longitude': '49.6868'}}

data = response.json()

print((data['iss_position']['latitude'], data['iss_position']['longitude']))

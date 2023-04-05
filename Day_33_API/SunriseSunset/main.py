import json
import time

import requests
from datetime import datetime

MY_LAT = 50.4496529
MY_LNG = 30.5258146

def raw_json(resp):
    return resp.json()
def pretty_json(resp):
    return json.dumps(
        json.loads(resp.text),
        indent=4
    )

def get_iss_data():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    return response.json()

def get_sunrise_sunset_data():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    return response.json()

def is_iss_overhead(data):
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])
    # iss_dt = datetime.fromtimestamp(data["timestamp"])
    my_range = 5
    is_in_latitude_range = MY_LAT - my_range <= iss_lat <= MY_LAT + my_range
    is_in_longitude_range = MY_LNG - my_range <= iss_lng <= MY_LNG + my_range
    if is_in_latitude_range and is_in_longitude_range:
        return True

def is_night(data):
    results = data["results"]
    now = datetime.now()
    sunrise_dt = datetime.fromisoformat(results["sunrise"])
    sunset_dt = datetime.fromisoformat(results["sunset"])
    if sunset_dt.hour <= now.hour or now.hour <= sunrise_dt.hour:
        return True

iss_data = get_iss_data()
sunrise_sunset_data = get_sunrise_sunset_data()

while True:
    time.sleep(60*60)
    if is_night(sunrise_sunset_data) and is_iss_overhead(iss_data):
        print("Look UP!")




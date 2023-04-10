import requests
from datetime import datetime

from dotenv import dotenv_values
env = dotenv_values("../.env")

class Coords:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

kyiv = Coords(lat=50.449540, lon=30.525393)

def get_weather_by_coords(coords: Coords) -> dict:
    params = {
        "lat": coords.lat,
        "lon": coords.lon,
        "appid": env["OPENWEATHERMAP_API_KEY"],
        "exclude": "current,daily"
    }
    url = "https://api.openweathermap.org/data/2.5/onecall"
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()

hourly_weather = get_weather_by_coords(kyiv)["hourly"]

filtered_from_9_to_21_hours_weather = [item for item in hourly_weather if 8 < datetime.fromtimestamp(item["dt"]).hour < 21]

next_12_hours_weather = filtered_from_9_to_21_hours_weather[:12]

for item in next_12_hours_weather:
    print(datetime.fromtimestamp(item["dt"]))
    if item["weather"][0]["id"] < 700:
        print(item["weather"][0])
        print("Bring an umbrella")
        break


import requests
from dotenv import dotenv_values

env = dotenv_values("../.env")

API_KEY_SHEETY = env["API_KEY_SHEETY"]
SHEETY_TOKEN = env["SHEETY_TOKEN"]
base_url = "https://api.sheety.co"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
        endpoint = f"{base_url}/{API_KEY_SHEETY}/flightDealsDay39/prices"
        requests.get(url=endpoint, headers=headers)

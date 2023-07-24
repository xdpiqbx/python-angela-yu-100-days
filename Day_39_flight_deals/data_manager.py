import os
import json
import requests
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.sheety.co"
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
URL_SHEET_ID = os.environ["URL_SHEET_ID"]
PRICES_FROM_SHEETY_JSON = "./resources/prices_from_sheety.json"


def create_json_with_empty_structure() -> dict:
    with open(PRICES_FROM_SHEETY_JSON, 'w') as json_file:
        empty_data = {"last_update": "", "prices": list()}
        json.dump(empty_data, json_file, indent=4)
        return empty_data


def try_to_get_data_from_prices_json() -> dict:
    try:
        with open(PRICES_FROM_SHEETY_JSON) as json_file:
            return json.load(json_file)
    except (json.JSONDecodeError, FileNotFoundError):
        return create_json_with_empty_structure()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices = list()
        self.headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
        self.url = f"{base_url}/{URL_SHEET_ID}/flightDeals/prices"

        data_from_json = try_to_get_data_from_prices_json()

        if data_from_json.get('last_update') != dt.now().strftime('%d/%m/%Y'):
            print("Prices data update in process ...")
            # ===== get response from sheety
            response = requests.get(url=self.url, headers=self.headers)

            # ===== save response and date of last update to JSON
            with open(PRICES_FROM_SHEETY_JSON, 'w') as json_file:
                date_for_sheet = {'last_update': dt.now().strftime('%d/%m/%Y')}
                date_for_sheet.update(response.json())
                json.dump(date_for_sheet, json_file, indent=4)
            self.__set_current_prices_data(date_for_sheet['prices'])
            print("Prices data was updated")
        else:
            print("Prices data is actual for today")
            self.__set_current_prices_data(data_from_json['prices'])

    def __set_current_prices_data(self, data_from_json):
        self.prices = data_from_json

    def get_current_prices_data(self):
        return self.prices

    def put_iata_codes_to_sheety(self, ids_and_iata_codes_generator):
        for item in ids_and_iata_codes_generator:
            request_body = {'price': {'iataCode': item['iataCode']}}
            requests.put(url=f"{self.url}/{item['id']}", headers=self.headers, json=request_body)

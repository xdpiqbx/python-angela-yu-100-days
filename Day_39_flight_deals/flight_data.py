import os
import json
import requests
from datetime import datetime as dt, timedelta
from dateutil.relativedelta import relativedelta

from dotenv import load_dotenv

load_dotenv()

FLIGHT_DATA_JSON = "./resources/flight_data.json"
tequila_kivi_url = "https://api.tequila.kiwi.com/v2/search"
iso_8601_format = '%Y-%m-%dT%H:%M:%S.%fZ'
tomorrow = dt.now() + timedelta(days=1)

def create_json_with_empty_structure() -> dict:
    print("create_json_with_empty_structure")
    with open(FLIGHT_DATA_JSON, 'w') as json_file:
        empty_data = {"last_update": ""}
        json.dump(empty_data, json_file, indent=4)
        return empty_data


def try_to_get_flight_data_json() -> dict:
    print("try_to_get_flight_data_json")
    try:
        with open(FLIGHT_DATA_JSON) as json_file:
            return json.load(json_file)
    except (json.JSONDecodeError, FileNotFoundError):
        return create_json_with_empty_structure()


class FlightData:
    #  This class is responsible for structuring the flight data.
    def __init__(self):
        print("__init__")
        self.__sheety_prices = list()
        self.__sheet_ids_iata_codes = list()
        self.__flight_data = dict()
        self.__headers = {"apikey": os.environ["KIWI_API"]}

    def set_sheety_prices(self, sheety_prices):
        print("set_sheety_prices")
        self.__sheety_prices = sheety_prices

    def __request_flight_data(self):
        print("__request_flight_data")
        flight_data = dict()
        flight_data['last_update'] = dt.now().strftime('%d/%m/%Y')
        for city in self.__sheety_prices:
            params = {
                'accept': 'application/json',
                'fly_from': 'LON',  # London[LON] # Poland: Warsaw[WAW] | Rzeszów[RZE] | Kraków[KRK]
                'fly_to': city['iataCode'],
                'date_from': tomorrow.strftime('%d/%m/%Y'),
                'date_to': (tomorrow + relativedelta(months=6)).strftime('%d/%m/%Y'),
                'selected_cabins': 'M',  # M (economy), W (economy premium), C (business), or F (first class)
                'max_stopovers': 0,  # 0 it means direct flight
                'nights_in_dst_from': 6,
                'nights_in_dst_to': 13,
                'curr': 'GBP',
                'price_to': city['lowestPrice'],  # 'price_from': 800,
                # 'sort': 'price',
                'sort': 'date',
                # 'limit': 1
            }
            response = requests.get(url=tequila_kivi_url, params=params, headers=self.__headers)
            flight_data[city['city']] = response.json()
        return flight_data

    def init_flight_data(self):
        print('init_flight_data')
        self.__set_flight_data(try_to_get_flight_data_json())
        if self.__flight_data.get('last_update') != dt.now().strftime('%d/%m/%Y'):
            print("last_update FALSE !")
            result = self.__request_flight_data()
            self.__set_flight_data(result)
            with open(FLIGHT_DATA_JSON, 'w') as json_file:
                json.dump(self.__flight_data, json_file, indent=4)

    def __set_flight_data(self, flight_data):
        print("__set_flight_data")
        self.__flight_data = flight_data

    def get_flight_data(self):
        print("get_flight_data")
        return self.__flight_data

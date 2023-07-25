import os
import json
import requests
from datetime import datetime as dt, timedelta
from dateutil.relativedelta import relativedelta

from dotenv import load_dotenv

load_dotenv()

FLIGHT_DATA_JSON = "./resources/flight_data.json"
FILTERED_FLIGHT_DATA_JSON = "./resources/filtered_flight_data.json"
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

def change_date_format(date_to_change):
    return dt.strptime(date_to_change, os.environ["ISO_8601_FORMAT"]).strftime("%d.%m.%Y")


class FlightData:
    #  This class is responsible for structuring the flight data.
    def __init__(self):
        print("__init__")
        self.__sheety_prices = list()
        self.__sheet_ids_iata_codes = list()
        self.__flight_data = dict()
        self.__tickets = list()
        self.__headers = {"apikey": os.environ["KIWI_API"]}

    def set_sheety_prices(self, sheety_prices):
        print("set_sheety_prices")
        self.__sheety_prices = sheety_prices

    def init_flight_data(self):
        print('init_flight_data')
        self.__set_flight_data(try_to_get_flight_data_json())
        if self.__flight_data.get('last_update') != dt.now().strftime('%d/%m/%Y'):
            print("init_flight_data NEW data for today")
            self.__set_flight_data(self.__request_flight_data())
            with open(FLIGHT_DATA_JSON, 'w') as json_file:
                json.dump(self.__flight_data, json_file, indent=4)

    def get_tickets_list(self):
        self.__convert_filtered_flight_data_to_tickets_list()
        return self.__tickets

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
                # 'limit': 1
            }
            response = requests.get(url=tequila_kivi_url, params=params, headers=self.__headers)
            flight_data[city['city']] = response.json()
        return flight_data

    def __get_filtered_flight_data(self):
        to_city_flights = dict()
        to_city_flights['last_update'] = dt.now().strftime('%d/%m/%Y')
        for city in self.__sheety_prices:
            flights = list()
            lowest_price = self.__flight_data[city['city']]['data'][0]['conversion']['GBP']
            for fly_data in self.__flight_data[city['city']]['data']:
                if lowest_price < fly_data['conversion']['GBP']:
                    continue
                flights.append({
                    'cityFrom': fly_data['cityFrom'],
                    'flyFrom': fly_data['flyFrom'],
                    'cityTo': fly_data['cityTo'],
                    'flyTo': fly_data['flyTo'],
                    'price_gbp': fly_data['conversion']['GBP'],  # Price
                    'nightsInDest': fly_data['nightsInDest'],
                    'local_departure': fly_data['local_departure'],
                    'local_arrival': fly_data['local_arrival'],
                    'return_home': fly_data['route'][len(fly_data['route']) - 1]['local_arrival'],
                    'duration': fly_data['duration']['departure'],
                    'virtual_interlining': fly_data['virtual_interlining']
                })
            to_city_flights[city['city']] = sorted(flights, key=lambda x: x['local_departure'])
        with open(FILTERED_FLIGHT_DATA_JSON, 'w') as json_file:
            json.dump(to_city_flights, json_file, indent=4)
        return to_city_flights

    def __set_flight_data(self, flight_data):
        print("__set_flight_data")
        self.__flight_data = flight_data

    def __convert_filtered_flight_data_to_tickets_list(self):
        filtered_flight_data = self.__get_filtered_flight_data()
        for city in self.__sheety_prices:
            data = filtered_flight_data.get(city['city'])[0]
            self.__tickets.append(f"""Trip to {data['cityTo']} for {data['nightsInDest']} nights
From: {data['cityFrom']}[{data['flyFrom']}] to {data['cityTo']}[{data['flyTo']}]
Dates: from {change_date_format(data['local_departure'])} to {change_date_format(data['return_home'])}
Only for: {data['price_gbp']} GBP\n""")

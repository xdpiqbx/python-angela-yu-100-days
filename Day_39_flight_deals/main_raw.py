# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

import json
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

from dotenv import load_dotenv

load_dotenv()

d_manager = DataManager()
sheety_prices = d_manager.get_current_prices_data()

# ==== convert data from json to generator for using in tequila_kivi
# cities = ({'id': city['id'], 'city': city['city']} for city in sheety_prices)
#
# flight_s = FlightSearch()
# flight_s.request_iata_codes_for_cities(cities)
# sheet_ids_iata_codes = flight_s.get_ids_and_iata_codes_for_sheety()

# d_manager.put_iata_codes_to_sheety(sheet_ids_iata_codes)

# === https://api.tequila.kiwi.com
fd = FlightData()
fd.set_sheety_prices(sheety_prices)
fd.init_flight_data()
raw_flight_data = fd.get_flight_data()


iso_8601_format = '%Y-%m-%dT%H:%M:%S.%fZ'
to_city_flights = dict()
for city in sheety_prices:
    flights = list()
    price = city['lowestPrice']
    for fly_data in raw_flight_data[city['city']]['data']:
        return_home_date = dt.strptime(fly_data['local_arrival'], iso_8601_format) + relativedelta(days=fly_data['nightsInDest'])
        flights.append({
            'cityFrom': fly_data['cityFrom'],
            'flyFrom': fly_data['flyFrom'],
            'cityTo': fly_data['cityTo'],
            'flyTo': fly_data['flyTo'],
            'price_gbp': fly_data['conversion']['GBP'],  # Price
            'nightsInDest': fly_data['nightsInDest'],
            'local_departure': fly_data['local_departure'],
            'local_arrival': fly_data['local_arrival'],
            'return_home': return_home_date.strftime(iso_8601_format),
            'total_duration': fly_data['duration']['total'],
            'virtual_interlining': fly_data['virtual_interlining']
        })
    to_city_flights[city['city']] = flights

with open("./resources/result.json", 'w') as json_file:
    json.dump(to_city_flights, json_file, indent=4)


# for item in to_city_flights:
#     to_city_flights[item] = sorted(to_city_flights.get(item), key=lambda x: x['local_departure'])

# sorted_by_duration = sorted(flights, key=lambda x: x['total_duration'])
# print(sorted_by_duration)
# ---------------------------
# date = {
#     'departure': datetime.strptime(fly_data['local_departure'], '%Y-%m-%dT%H:%M:%S.%fZ'),
#     'arrival': datetime.strptime(fly_data['local_arrival'], '%Y-%m-%dT%H:%M:%S.%fZ')
# }
# print(f"{fly_data['cityFrom']} -> {fly_data['cityTo']}[{fly_data['flyTo']}] Price: {fly_data['conversion']}")
# print(f"Local Departure from {fly_data['cityFrom']}: {date.get('departure').strftime('%d.%m.%Y %H:%M:%S')}")
# for route in fly_data['route']:
#     print(f"\t{route['cityFrom']}[{route['cityCodeFrom']}]->{route['cityTo']}[{route['cityCodeTo']}]")
# print(f"Local Arrival to {fly_data['cityTo']}: {date.get('arrival').strftime('%d.%m.%Y %H:%M:%S')}")
# print(f"Total in the way: {date.get('arrival') - date.get('departure')}")
# print()

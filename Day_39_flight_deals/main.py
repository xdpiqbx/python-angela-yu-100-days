# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

import os
import json
from time import sleep
import requests
from datetime import datetime as dt, timedelta
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

load_dotenv()

# === GET cities from "https://api.sheety.co" and save to json_file

# SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
# sheety = "https://api.sheety.co"
# url = f"{sheety}/79ece8eb2a0c55af37f6f40f7cdd6b41/flightDeals/prices"
# headers = {
#     "Authorization": 'Bearer ' + SHEETY_TOKEN
# }
# response = requests.get(url=url, headers=headers)

# ===== save data from sheety to JSON
# with open('./resources/prices_from_sheety_ololo.json', 'w') as json_file:
#     json.dump(response.json(), json_file, indent=4)

# ===== read saved data from JSON
with open('resources/prices_from_sheety_ololo.json') as json_file:
    cities_dict = json.load(json_file)  # dict

# ==== convert data from json to generator for using in tequila_kivi
# cities = ({'id': city['id'], 'city': city['city']} for city in cities_dict['prices'])

# === Using cities search and get they iata codes from https://api.tequila.kiwi.com

# tequila_kivi_url = "https://api.tequila.kiwi.com/locations/query"
# headers = {"apikey": os.environ["KIWI_API"]}
# sheet_ids_iata_codes = list()
# for city in cities:
#     sleep(0.1)
#     params = {
#         "accept": "application/json",
#         "term": city.get('city')
#     }
#     response = requests.get(url=tequila_kivi_url, params=params, headers=headers)
#     sheet_ids_iata_codes.append({'id': city.get('id'), 'iataCode': response.json()['locations'][0]['code']})
# print(sheet_ids_iata_codes)

# === PUT iataCodes to  "https://api.sheety.co"

# SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
# sheety = "https://api.sheety.co"
# url = f"{sheety}/79ece8eb2a0c55af37f6f40f7cdd6b41/flightDeals/prices"
# headers = {"Authorization": 'Bearer ' + SHEETY_TOKEN}
# for item in sheet_ids_iata_codes:
#     sleep(0.1)
#     request_body = {'price': {'iataCode': item['iataCode']}}
#     requests.put(url=f"{url}/{item['id']}", headers=headers, json=request_body)

# === https://api.tequila.kiwi.com
iso_8601_format = '%Y-%m-%dT%H:%M:%S.%fZ'
tequila_kivi_url = "https://api.tequila.kiwi.com/v2/search"
headers = {"apikey": os.environ["KIWI_API"]}
tomorrow = dt.now() + timedelta(days=1)
# cheapest fly to the next 6 month
to_city_flights = dict()
for city in cities_dict['prices']:
    flights = list()
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
        'sort': 'date',
        'limit': 1
    }
    response = requests.get(url=tequila_kivi_url, params=params, headers=headers)
    all_fly_data = response.json()["data"]
    # sleep(0.3)

    price = city['lowestPrice']
    for fly_data in all_fly_data:
        if price < fly_data['conversion']['GBP']:
            price = fly_data['conversion']['GBP']
            continue
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
print(to_city_flights)


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

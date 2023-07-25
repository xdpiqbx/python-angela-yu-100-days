# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

from dotenv import load_dotenv

load_dotenv()

d_manager = DataManager()
sheety_prices = d_manager.get_current_prices_data()

# ==== convert data from json to generator for using in tequila_kivi
# I need it 1 time if I do not have iata for some of the cities #
# cities = ({'id': city['id'], 'city': city['city']} for city in sheety_prices)
# flight_s = FlightSearch()
# flight_s.request_iata_codes_for_cities(cities)
# sheet_ids_iata_codes = flight_s.get_ids_and_iata_codes_for_sheety()
# d_manager.put_iata_codes_to_sheety(sheet_ids_iata_codes)

# === https://api.tequila.kiwi.com
fd = FlightData()
fd.set_sheety_prices(sheety_prices)
fd.init_flight_data()
tickets = fd.get_tickets_list()

# print(tickets)
text = ''
for t in tickets:
    text += t+'\n'

print(text)
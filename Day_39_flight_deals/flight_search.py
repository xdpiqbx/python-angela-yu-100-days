import os
import requests

from dotenv import load_dotenv

load_dotenv()

tequila_kivi_url = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    #  This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.__sheet_ids_iata_codes = list()
        self.__headers = {"apikey": os.environ["KIWI_API"]}

    def request_iata_codes_for_cities(self, cities):
        for city in cities:
            params = {
                "accept": "application/json",
                "term": city.get('city')
            }
            response = requests.get(url=tequila_kivi_url, params=params, headers=self.__headers)
            self.__sheet_ids_iata_codes.append({
                'id': city.get('id'),
                'iataCode': response.json()['locations'][0]['code']
            })

    def get_ids_and_iata_codes_for_sheety(self):
        return (item for item in self.__sheet_ids_iata_codes)

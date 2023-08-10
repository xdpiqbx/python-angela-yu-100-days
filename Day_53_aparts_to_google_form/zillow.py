import os
import re
import json
import requests
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

URL_ZILLOW = ''.join([
    'https://www.zillow.com/search/GetSearchPageState.htm?',
    'searchQueryState={"pagination":{},"mapBounds":',
    '{"north":45.934765171573396,"east":-121.17736409101153,"south":44.92673760314442,"west":-123.65752766523028},'
    '"usersSearchTerm":"Portland OR","regionSelection":[{"regionId":13373,"regionType":6}],"isMapVisible":true,',
    '"filterState":{"price":{"max":268848,"min":192034},"beds":{"min":1},"isForSaleForeclosure":{"value":false},',
    '"monthlyPayment":{"max":1100,"min":800},"isAuction":{"value":false},"isNewConstruction":{"value":false},'
    '"isForRent":{"value":true},"isForSaleByOwner":{"value":false},"isComingSoon":{"value":false},',
    '"isForSaleByAgent":{"value":false}},"isListVisible":true,"mapZoom":9}',
    '&wants={"cat1":["listResults","mapResults"]}&requestId=11'
])

cookies = {
    "_pxvid": os.environ['ZILLOW_PXVID'],
}

headers = {
    "User-Agent": ''.join([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    ]),
    "Accept": ''.join([
        "text/html,application/xhtml+xml,application/xml;",
        "q=0.9,image/avif,image/webp,image/apng,*/*;",
        "q=0.8,application/signed-exchange;v=b3;q=0.7"
    ]),
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
}


def get_from_json() -> dict:
    with open(Path('zillow.json')) as json_file:
        return json.loads(json_file.read())


def get_normalized_price(item):
    price = item.get("hdpData", {}).get("homeInfo", {}).get("priceForHDP", None)
    if not price:
        price = item.get("price", None)
        price = float(re.sub("[$,+/mo]", "", price)) if price else None
        if not price:
            price = item.get("units", {})[0].get("price", None)
            price = float(re.sub("[$,+]", "", price)) if price else None
    return price


def get_normalized_url(raw_url: str):
    if raw_url.startswith("https://"):
        return raw_url
    return "https://www.zillow.com" + raw_url


@dataclass(frozen=True)
class Apartment:
    url: str
    address: str
    price: float


class Zillow:
    def __init__(self):
        response = requests.get(URL_ZILLOW, headers=headers, cookies=cookies)
        self.json_data = response.json()
        # self.json_data = get_from_json()
        self.apartments = iter
        self.length = 0

    def __convert_json_to_apartment_list(self):
        listResults = self.json_data['cat1']['searchResults']['listResults']
        mapResults = self.json_data['cat1']['searchResults']['mapResults']

        self.length = len(listResults) + len(mapResults)

        self.json_data.clear()
        self.apartments = (
            Apartment(
                get_normalized_url(item["detailUrl"]),
                item["address"],
                get_normalized_price(item)
            )
            for item in [*listResults, *mapResults]
        )

    def get_apartments(self):
        self.__convert_json_to_apartment_list()
        print(f"I found {self.length} apartments.")
        return self.apartments

    def get_len(self):
        return self.length

import json
import requests
from pathlib import Path
from datetime import datetime as dt
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0"
}

folder = "./resources"
data_json = "data.json"
urls_json = "urls.json"
test_data_json = "test_data.json"


def create_data_json_if_not_exists(file_name=data_json):
    if not Path(Path(folder, file_name)).is_file():
        save_data_to_json(dict())
        print("File created")


def save_data_to_json(data):
    with open(Path(folder, data_json), 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_data_from_json(file_name=data_json):
    with open(Path(folder, file_name), encoding='utf-8') as json_file:
        return json.loads(json_file.read())


class UkrainianArmorManager:
    def __init__(self):
        create_data_json_if_not_exists()
        self.dt_now = dt.now()
        self.data = get_data_from_json()
        self.scraped_data = dict()
        self.price_has_dropped = dict()
        self.urls = get_data_from_json(urls_json)

    def request_raw_data_from_urls(self):
        urls = get_data_from_json(urls_json)
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            self.__scrap_data(soup)

    def __scrap_data(self, soup: BeautifulSoup):
        title = soup.select_one("h1[data-product-title]").getText().strip()
        date = self.dt_now.strftime('%d.%m.%Y at %H:%M')
        price = soup.select_one("div[data-product-price]")['data-product-price'].strip()
        self.scraped_data[title] = [{
            "date": date,
            "price": int(price)
        }]

    # for tests
    # def request_raw_data_from_urls(self):
    #     self.scraped_data = get_data_from_json(test_data_json)

    def save_scraped_data_to_json(self):
        if not self.data:
            save_data_to_json(self.scraped_data)
            return
        self.__compare_update_data_and_fill_dropped_prices()
        save_data_to_json(self.data)

    def __compare_update_data_and_fill_dropped_prices(self):
        for i, key in enumerate(self.scraped_data):
            data_price = self.data[key][len(self.data[key]) - 1]['price']
            scraped_price = self.scraped_data[key][0]['price']
            if data_price != scraped_price:
                # get price to prices log
                self.data[key].append({
                    "date": self.scraped_data[key][0]['date'],
                    "price": int(scraped_price)
                })
                if data_price > scraped_price:
                    # fill dropped prices
                    self.price_has_dropped[key] = {
                        "old_price": data_price,
                        "new_price": scraped_price,
                        "url_index": i
                    }

    def get_dropped_prices(self):
        return self.price_has_dropped

    def prepared_message_with_dropped_prices(self):
        if not self.price_has_dropped:
            return ""
        msg = "<h3>Зафіксовано зниження цін на наступні товари:</h3>"
        for key in self.price_has_dropped:
            old = self.price_has_dropped[key]['old_price']
            new = self.price_has_dropped[key]['new_price']
            index = self.price_has_dropped[key]['url_index']
            diff = old - new
            msg += (f"<hr><b><a href='{self.urls[index]}' target='_blank'>{key}</a></b>"
                    f"<ul>"
                    f"<li>Стара ціна: {old} грн</li>"
                    f"<li>Нова ціна: {new} грн</li>"
                    f"<li>Різниця: {diff} грн</li>"
                    f"</ul>")
        return msg

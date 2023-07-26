import requests
from bs4 import BeautifulSoup

base_url = "https://www.billboard.com/charts/hot-100/"
class BillboardManager:
    def __init__(self, year, month, day):
        self.response = requests.get(f"{base_url}{year}-{month}-{day}/")
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.raw_hot_100 = self.soup.select('li.o-chart-results-list__item:has(h3)')

    def scrapped_hot_100(self):
        scrapper = {
            "has_spotify_track_id": False,
            "hot_100": list()
        }
        for i, song in enumerate(self.raw_hot_100, start=1):
            scrapper.get("hot_100").append({
                "place": i,
                "title": song.select_one('h3').getText().strip(),
                "group": song.select_one('span').getText().strip()
            })
        return scrapper

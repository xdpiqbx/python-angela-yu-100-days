from dataclasses import dataclass
from datetime import datetime

POSTER_BASE_URL = "https://image.tmdb.org/t/p/w300"
DEFAULT_POSTER = 'static/images/default.jpg'


@dataclass
class ChosenMovie:
    title: str
    year: str
    description: str
    ranking: int
    img_url: str

    def __post_init__(self):
        self.year = str(datetime.strptime(self.year, "%Y-%m-%d").year)
        if not self.img_url:
            self.img_url = DEFAULT_POSTER
            return
        self.img_url = f"{POSTER_BASE_URL}/{self.img_url}"

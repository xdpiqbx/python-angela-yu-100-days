from dataclasses import dataclass
from datetime import datetime

POSTER_BASE_URL = "https://image.tmdb.org/t/p/w300"
DEFAULT_POSTER = 'static/images/default.jpg'


@dataclass
class SelectedMovie:
    mdb_movie_id: int
    image: str
    title: str
    release_date: str
    overview: str
    popularity: float

    def __post_init__(self):
        self.release_date = str(datetime.strptime(self.release_date, "%Y-%m-%d").year)
        if not self.image:
            self.image = DEFAULT_POSTER
            return
        self.image = f"{POSTER_BASE_URL}/{self.image}"

import os
from pprint import pprint

import requests
from ..MoviesDTO.selected_movie import SelectedMovie
from ..MoviesDTO.chosen_movie import ChosenMovie

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['THEMOVIEDB_TOKEN']

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}


class MovieDBService:
    def __init__(self):
        self.movie_title = None
        self.base_url = "https://api.themoviedb.org/3"

    def set_movie_title(self, movie_title):
        self.movie_title = movie_title

    def find_movies(self, page=1) -> dict[str: list[SelectedMovie], str: int]:
        params = {
            "query": self.movie_title,
            "include_adult": False,
            "language": "en-US",
            "page": page
        }
        url = f"{self.base_url}/search/movie"
        response = requests.get(url, params=params, headers=HEADERS)
        selected_movies = list()
        for movie in response.json()['results']:
            selected_movies.append(
                SelectedMovie(
                    mdb_movie_id=movie.get('id'),
                    image=movie.get('poster_path'),
                    title=movie.get('title'),
                    release_date=movie.get('release_date'),
                    popularity=movie.get('popularity'),
                    overview=movie.get('overview')
                )
            )
        return {'movies': selected_movies, 'total_pages': response.json().get('total_pages')}  # Maybe pagination

    def get_movie(self, mdb_movie_id) -> ChosenMovie:
        params = {
            "language": "en-US",
        }
        url = f"{self.base_url}/movie/{mdb_movie_id}"
        response = requests.get(url, params=params, headers=HEADERS)

        return ChosenMovie(
            title=response.json().get('title'),
            year=response.json().get('release_date'),
            description=response.json().get('overview'),
            ranking=response.json().get('vote_average'),
            img_url=response.json().get('poster_path')
        )

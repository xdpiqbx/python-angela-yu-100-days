from datetime import datetime as dt
from dotenv import load_dotenv

from data_validator import DataValidator
from file_manager import FileManager
from billboard_manager import BillboardManager
from spotify_manager import SpotifyManager

load_dotenv()

SAVE_TO = "./already_requested/"

date = input("Which year do you want to travel to? Type the date in this format DD.MM.YYYY : ")

day, month, year = DataValidator().validate_date(date).split('.')
date = f"{day}.{month}.{year}"

file_manager = FileManager(f"{day}_{month}_{year}.json")
file_manager.is_current_file_exists()

if file_manager.is_necessary_to_request():
    print("Request from Billboard")
    billboard = BillboardManager(year, month, day)
    file_manager.save_to_json(
        billboard.scrapped_hot_100()
    )

hot_100 = file_manager.get_from_json()

spotify = SpotifyManager()
if not hot_100.get("has_spotify_track_id"):
    print("Request [track_ids] from Spotify")
    hot_100 = spotify.get_hot_100_with_spotify_track_id(hot_100)
    file_manager.save_to_json(hot_100)

playlist_title = f"Top tracks in: {(dt.strptime(date, '%d.%m.%Y')).strftime('%d %B %Y')}"
playlist = spotify.create_private_playlist_if_not_exists(playlist_title)

track_ids = [item['track_id'] for item in hot_100.get('hot_100') if item['track_id']]
spotify.add_tracks_to_existing_playlist_if_not_in(playlist.get('id'), track_ids)

print(spotify.get_all_playlists_urls())

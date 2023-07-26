import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyManager:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope=["playlist-modify-private", "user-library-read", "playlist-read-private"],
                redirect_uri=os.environ["REDIRECT_URI"],
                client_id=os.environ["SPOTIFY_CLIENT_ID"],
                client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
                cache_path="token.json",
            )
        )
        self.user_data = self.sp.current_user()

    def get_hot_100_with_spotify_track_id(self, hot_100):
        hot_100_with_spotify_uri = {
            "has_spotify_track_id": True,
            "hot_100": list()
        }

        for track_data in hot_100.get("hot_100"):
            artist = "%20".join((track_data['group'].split(" ")))
            track = "%20".join((track_data['title'].split(" ")))
            query = f"remaster%20track:{track}%20artist:{artist}"

            track_info = self.sp.search(q=query, limit=1, offset=0, type='track', market=None)
            track_id = ""
            try:
                track_id = track_info.get('tracks').get('items')[0].get('id')
            except IndexError:
                print(f"For track: [{track_data['title']}], artist: [{track_data['group']}]")
                print(f"We have not [spotify_URI]\n")

            hot_100_with_spotify_uri.get("hot_100").append({
                "place": track_data['place'],
                "title": track_data['title'],
                "group": track_data['group'],
                "track_id": track_id
            })

        return hot_100_with_spotify_uri

    def create_private_playlist_if_not_exists(self, play_list_title):
        for play_list in self.sp.current_user_playlists()['items']:
            if play_list.get('name') == play_list_title:
                return {
                    "id": play_list.get('id'),
                    "name": play_list.get('name'),
                    "status_message": "Playlist already exists"
                }

        play_list = self.sp.user_playlist_create(
            self.user_data.get('id'),
            play_list_title,
            public=False
        )

        return {
            "id": play_list.get('id'),
            "name": play_list.get('name'),
            "status_message": "Playlist was created"
        }

    def add_tracks_to_existing_playlist_if_not_in(self, playlist_id, tracks: list):
        for track in self.sp.playlist(playlist_id).get('tracks').get('items'):
            if track.get('track').get("id") in tracks:
                tracks.remove(track.get('track').get("id"))
        if tracks:
            self.sp.playlist_add_items(playlist_id, tracks)

    def get_all_playlists_urls(self):
        playlists = list()
        for playlist in self.sp.current_user_playlists().get('items'):
            playlists.append({
                "spotify_playlist_id": playlist.get('id'),
                "title": playlist.get('name'),
                "external_url": playlist.get('external_urls').get('spotify'),
            })
        return playlists

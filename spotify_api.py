# spotify_api.py

import requests

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://api.spotify.com/v1"

    def play_song(self, song_name):
        try:
            access_token = self.get_access_token()
            headers = {"Authorization": f"Bearer {access_token}"}
            params = {"q": song_name, "type": "track", "limit": 1}
            response = requests.get(f"{self.base_url}/search", headers=headers, params=params)
            data = response.json()
            if response.status_code == 200 and data["tracks"]["items"]:
                track_uri = data["tracks"]["items"][0]["uri"]
                requests.put(f"{self.base_url}/me/player/play", headers=headers, json={"uris": [track_uri]})
                return f"Now playing {song_name}."
            else:
                return "Sorry, could not find the specified song."
        except Exception as e:
            return f"An error occurred: {e}"

    def search_song(self, query):
        try:
            access_token = self.get_access_token()
            headers = {"Authorization": f"Bearer {access_token}"}
            params = {"q": query, "type": "track", "limit": 5}
            response = requests.get(f"{self.base_url}/search", headers=headers, params=params)
            data = response.json()
            if response.status_code == 200 and data["tracks"]["items"]:
                songs = [track["name"] for track in data["tracks"]["items"]]
                return songs
            else:
                return "Sorry, could not find any songs matching the query."
        except Exception as e:
            return f"An error occurred: {e}"

    def get_access_token(self):
        try:
            auth_response = requests.post("https://accounts.spotify.com/api/token", 
                                          data={"grant_type": "client_credentials"},
                                          auth=(self.client_id, self.client_secret))
            return auth_response.json()["access_token"]
        except Exception as e:
            return f"An error occurred while fetching access token: {e}"

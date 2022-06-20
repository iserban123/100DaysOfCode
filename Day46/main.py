from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

Client_ID = "3e18dafe711d41d2868877adea093986"
Client_Secret = "daa461bbf1774140a597e3d610991c30"


ttime= input("What year you would like to travel to in YYYY-MM-DD: ")
year = ttime[0:4]
print(year)
response = requests.get(f"https://www.billboard.com/charts/hot-100/{ttime}/")
web_songs = response.text
soup = BeautifulSoup(web_songs, "html.parser")
list_songs = soup.find_all(name="h3",id='title-of-a-story', class_="a-no-trucate")
list_artists = soup.find_all(name="span", class_="a-no-trucate")
all_songs = [song.getText().strip() for song in list_songs]
all_artists = [artist.getText().strip() for artist in list_artists]

# with open("songs.text", mode="w") as file:
#      for m in all_songs:
#         file.write(f"{all_songs.index(m) + 1}.{m}-{all_artists[all_songs.index(m)]}\n")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
song_uris = []
for song in all_songs:
    response = sp.search(q=f"track:{song} artist:{all_artists[all_songs.index(song)]} year:{year}", type="track")
    try:
        uri = response["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{ttime} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


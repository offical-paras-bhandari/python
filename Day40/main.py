from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
website = requests.get(url= "https://www.billboard.com/charts/hot-100/2000-08-12/")
website_data = website.text
soup = BeautifulSoup(website_data,"html.parser")
songs_title = soup.find_all(name="h3", id="title-of-a-story",class_="a-no-trucate")
song_title_lists = [song_title.getText() for song_title in songs_title]

print(song_title_lists)
CLIENT_ID = "bcd6deb4e3fd406aa3464de100ea8535"
CLIENT_KEY = "1c4e7235334b4be3862dbb7a04524d15"
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_KEY,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
date_input = input("what year you would like to travel to in YYY-MM-DD format.")
song_names = ["The list of song", "titles from your", "web scrape"]

year = date_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



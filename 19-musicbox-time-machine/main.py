from bs4 import BeautifulSoup
import requests
import spotipy

# date_input = input("Which date (YYYY-MM-DD) you wanna travel to? ")
date_input = "2000-08-12"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_input}/")
soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

# li_tags = soup.findAll(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
# songs = [s.findNext(name="h3").getText().strip() for s in li_tags]
# print(songs)
# bands = [s.findNext(name="span").getText().strip() for s in li_tags]
# print(bands)

songs = [song.getText().strip() for song in soup.select("li ul li h3")]
artists = [song.getText().strip() for song in soup.select("li ul li span")]
tuples = []
for i, s in enumerate(songs):
    tuples.append((s, artists[i]))

spotipy_oauth = spotipy.oauth2.SpotifyOAuth(
    client_id="b685e64498d9478cbc1592434c9d99aa",
    client_secret="0135801187f24fd087154345736b9702",
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    username="camposzen")
auth_token = spotipy_oauth.get_cached_token()
# print(auth_token)

access_token = auth_token['access_token']
client = spotipy.client.Spotify(auth=access_token)
user_id = client.current_user()["id"]
# print(user_id)

headers = {
    "Authorization": f"Bearer {access_token}"
}

playlist = f"{date_input} Billboard 100"
data = {
    "name": playlist,
    "description": f"top 100 songs on {date_input}",
    "public": False
}
response = requests.post(
    url=f"https://api.spotify.com/v1/users/{user_id}/playlists", headers=headers, json=data)
print(response.text)
playlist_id = response.json()[0]["id"]

song_uris = []
for t in tuples:
    # result = sp.search(q=f"track:{song} artist:{artist}", type="track")
    data = {
        "q": f"track:{t[0]} artist:{t[1]}"
    }
    result = response = requests.get(
        url=f"https://api.spotify.com/v1/search", headers=headers, params=data)
    print(result.text)
    result = result.json()
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{t[0]} doesn't exist in Spotify. Skipped.")

data = {
    "uris": song_uris
}
response = requests.post(
    url=f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers=headers, json=data)
print(response.text)





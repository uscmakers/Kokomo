# To access Spotipy
import spotipy
# To View the API response
import json
# To open our song in our default browser
import webbrowser

import spotipy
import webbrowser
from pprint import pprint
from time import sleep
username = 'thegerstman'
clientID = 'b7c64f620a0a4d18ae8379a7aba243c4'
clientSecret = 'f0fd58eb639a4655b07d51671a4454f4'
redirectURI = 'http://google.com/'

# Create OAuth Object
scope = "user-read-playback-state,user-modify-playback-state"
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI,scope=scope)
# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# Create Spotify Object
sp = spotipy.Spotify(auth=token)

user = sp.current_user()
# To print the response in readable format.
print(json.dumps(user,sort_keys=True, indent=4))


# Shows playing devices
res = sp.devices()
pprint(res)

searchQuery = 'yellow submarine'
# Search for the Song.
searchResults = sp.search(searchQuery,1,0,"track")
# Get required data from JSON response.
tracks_dict = searchResults['tracks']
tracks_items = tracks_dict['items']
song = tracks_items[0]['external_urls']['spotify']

# Change track
sp.start_playback(uris=[song])

# Change volume
sp.volume(100)
sleep(2)
sp.volume(50)
sleep(2)
sp.volume(100)
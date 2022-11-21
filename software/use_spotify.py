# To access Spotipy
import spotipy
# To View the API response
import json
# To open our song in our default browser
import webbrowser

import json
import spotipy
import webbrowser
username = 'thegerstman'
clientID = 'b7c64f620a0a4d18ae8379a7aba243c4'
clientSecret = 'f0fd58eb639a4655b07d51671a4454f4'
redirectURI = 'http://google.com/'

# Create OAuth Object
oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
# Create token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
# Create Spotify Object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# To print the response in readable format.
print(json.dumps(user,sort_keys=True, indent=4))

# Get the Song Name.
searchQuery = 'aruba jamaica'
# Search for the Song.
searchResults = spotifyObject.search(searchQuery,1,0,"track")
# Get required data from JSON response.
tracks_dict = searchResults['tracks']
tracks_items = tracks_dict['items']
song = tracks_items[0]['external_urls']['spotify']
# Open the Song in Web Browser
webbrowser.open(song)
print('Song has opened in your browser.')
import json
import spotipy
from time import sleep
import speech_recognition as sr
import requests

username = '[username]'
clientID = '[client-id]'
clientSecret = '[client-secret]'
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
print(res)

# Initialize the recognizer
r = sr.Recognizer()
     
# Exception handling to handle
# exceptions at the runtime
try:
        
    # use the microphone as source for input.
    with sr.Microphone() as source:
            
        audio = r.record(source, duration=5)
        text = r.recognize_google(audio)
            
        print(text)
            
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
        
except sr.UnknownValueError:
    print("unknown error occurred")

key = "[serp-api-key]"
response = requests.get("https://serpapi.com/search", params={"engine": "google", "q": text, "api_key": key})
response_json = response.json()

knowledge_graph = response_json["knowledge_graph"]
song_name = knowledge_graph["title"]
artist_name = knowledge_graph["artist"]
print(song_name)
print(artist_name)

listen = knowledge_graph["listen"]
for result in listen:
    if result['name'] == 'Spotify':
        spotify_url = result['link']

print(f'spotify url is {spotify_url}')
spotify_url = spotify_url.split('https://open.spotify.com/track/')[1]
spotify_url = spotify_url.split('?autoplay=true')[0]
print(f'new spotify url is {spotify_url}')

# Change track
sp.start_playback(uris=[f'spotify:track:{spotify_url}'])

# Change volume
# sp.volume(100)
# sleep(2)
# sp.volume(50)
# sleep(2)
# sp.volume(100)
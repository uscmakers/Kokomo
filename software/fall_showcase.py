import json
import spotipy
import requests
import threading
from time import sleep
import speech_recognition as sr

# Create Spoitfy object that is authenticated to isaac's spotify accounts
spotify_client_id = '[client-id]'
spotify_client_secret = '[client-secret]'
spotify_redirect_uri = 'http://google.com/'
spotify_scope = "user-read-playback-state,user-modify-playback-state"
oauth_object = spotipy.SpotifyOAuth(spotify_client_id,spotify_client_secret,spotify_redirect_uri,scope=spotify_scope)
token = oauth_object.get_access_token(as_dict=False)
spotify_api = spotipy.Spotify(auth=token)

# Intializations for other libraries/keys
tts_recognizer = sr.Recognizer() # Recognizer for text to speech
serp_key = "[serp-key]"

# display Spotify user's info
user = spotify_api.current_user()
user_info = json.dumps(user,sort_keys=True, indent=4)
print("Current Spotify Account: ", user['display_name'])

# Shows spotify user's devices
print('Active Devices:')
res = spotify_api.devices()
for device in res['devices']:
    print('\t-',device['name'], '(ACTIVE)' if device['is_active'] else '(INACTIVE)')

# Recognize lyrics from microphone using tts
try:    
    with sr.Microphone() as source:     # use the microphone as source for input.
        print('Listening...')
        audio = tts_recognizer.record(source, duration=5)
        lyrics = tts_recognizer.recognize_google(audio)  
        print('Lyrics Registered:',  lyrics) 
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
except sr.UnknownValueError:
    print("unknown error occurred")

google_results = requests.get("https://serpapi.com/search", params={"engine": "google", "q": lyrics, "api_key": serp_key}).json()

# Get song name and artist name from google results
knowledge_graph = google_results["knowledge_graph"]
song_name = knowledge_graph["title"]
artist_name = knowledge_graph["artist"]
print('This song is', song_name, 'by', artist_name)

# get spotify uri from google results
listen = knowledge_graph["listen"]
for result in listen:
    if result['name'] == 'Spotify':
        spotify_url = result['link']
spotify_url = spotify_url.split('https://open.spotify.com/track/')[1]
spotify_url = spotify_url.split('?autoplay=true')[0]

# Play song on spotify
print('Playing now!')
spotify_api.start_playback(uris=[f'spotify:track:{spotify_url}'])

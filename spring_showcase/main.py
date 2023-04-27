# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import requests
import pywhatkit

from sound_sensor import SoundSensor

 
# Initialize the recognizer
r = sr.Recognizer()
ss = SoundSensor()
     
# Exception handling to handle
# exceptions at the runtime
try:
        
    # use the microphone as source for input.
    with sr.Microphone() as source:
        print("Recording...")
        audio = r.record(source, duration=5)
        text = r.recognize_google(audio)
            
        print(text)
            
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
        
except sr.UnknownValueError:
    print("unknown error occurred")

key = "2ee39e4a62c53b8925eedda4e64b3e0f3eed31d1d15cad2cc810a34d073c37f6"
response = requests.get("https://serpapi.com/search", params={"engine": "google", "q": text, "api_key": key})

response_json = response.json()

knowledge_graph = response_json["knowledge_graph"]
song_name = knowledge_graph["title"]

pywhatkit.playonyt(song_name + " lyrics")
ss.run()

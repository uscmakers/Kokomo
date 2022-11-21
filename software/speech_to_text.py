# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import pyttsx3
 
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
    
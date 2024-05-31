from gemini import gemin
# from assi import assistant
import speech_recognition as sr
import time
import requests
import json
import pyttsx3
from news import speak_news

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print("sdfghjkl")
def speak(audio):
    engine.stop()
    engine.say(audio)
    engine.runAndWait()


r=sr.Recognizer()
def callgem():
    with sr.Microphone() as source:
        # speak("please say something")
            a=r.listen(source)
            print("you said  : "+r.recognize_google(a,language ='en-us'))
            k=r.recognize_google(a,language ='en-us')
            print(k)
        #     speak(k)
        #     k=k+"in 5 senetences"
            if "news" in k:
                speak_news() 
            else:
                response = gemin(k)
                print(response)
                speak(response)

# callgem()
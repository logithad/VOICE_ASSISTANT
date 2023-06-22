# from dataclasses import replace
# from re import T
import pyttsx3
# import pyaudio
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
        speak("I am C Bot and I am your tourist guide")
    elif hour>12 and hour <=15:
        speak("Good Afternoon!")
        speak("I am C Bot and I am your tourist guide")
    else:
        speak("Welcome Back!") 
        
        speak("I am C Bot and I am your tourist guide")
    speak("How may I help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
#         r.record()
#         audio = r.record(source)
#          pyttsx3.speak("what's your name")
        message = r.record(source, duration=3)
       
        
    try:
        print("Recognizing...")
        query = r.recognize_google(message, language='en-in')
        print(f"You: {query}\n")
        
    except Exception as e:
        print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query
        
        
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")
            
        elif 'open google map' in query:
            webbrowser.open("https:\\www.google.co.in\maps")
            
        elif 'compose mail' in query:
            webbrowser.open("https:\\mail.google.com\mail")
        
        elif 'play music' in query:
            webbrowser.open("https:\\www.spotify.com")
            
        elif 'go for shopping' in query:
            webbrowser.open("https:\\www.amazon.com")
            
        elif 'what about cricket' in query:
            webbrowser.open("https:\\www.cricbuzz.com")
            
        elif 'go for entertainment' in query:
            webbrowser.open("https:\\www.hotstar.com")
            
        elif 'open code' in query:
            codePath = 'C:\\Users\\Lintheshwar S\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
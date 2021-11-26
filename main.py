import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb
import os
import Stopwatch

engine = pyttsx3.init('sapi5')  # sapi is a speech api by microsoft
voices = engine.getProperty('voices') # gets the voices in which our computer will speak
engine.setProperty('voice',voices[1].id)


def speak(audio): #this function is used to speak "audio"
    engine.say(audio)
    engine.runAndWait()

# this function is used to wish a person
def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour >=0  and hour<12:
        speak("Good Morning Gautam! CARPEDIEM")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Gautam! Go for your workout")
    else: 
        speak("Good Evening Gautam!")
    speak("I am Kurama, Your Destop Voice assistant. ")
   
# this function is used to take command from the user
def takeCommand():
    #It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source :  
        print("Listening Sir...")
        r.pause_treshold =1
        audio = r.listen(source)
    try:
        print("Recognizing") 
        query = r.recognize_google(audio,language ="en-in")
        print(f"User said: {query}\n")

    except Exception as e: 
        print(e)
        print("Say that again please......")
        return "None"

    return query

if __name__=="__main__":
    wishMe()
   
    # logic for executing tasks based on queries
    while True:
        speak("How may I help You?") 
        query = takeCommand().lower()
        #logic
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia","")
            results  = wk.summary(query,sentences =2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'youtube' in query:
            wb.open("youtube.com")

        elif 'google' in query:
            wb.open("google.com")

        elif 'open code' in query:
            VSpath = "C:\\Users\\gomci\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(VSpath)
        elif 'quit' in query:
            speak("I AM DYING")
            break
        elif 'start stopwatch' in query:
            Stopwatch.start()


        
            


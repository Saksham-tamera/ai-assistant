import speech_recognition as sr
<<<<<<< HEAD
import pyttsx3
import sounddevice
import requests
import webbrowser
import datetime
import os
import subprocess
import wikipedia
from dotenv import python_dotenv
import openai
print("All modules imported successfully.")
=======
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Kriti....") 
    while True:
        # Listen for the wake word "Kriti"
        # obtain audio from the microphone
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(audio)
            if(command.lower() == "Kriti"):
                speak("Yes, how can I help you?")
                # Listen for the next command
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = r.listen(source)
                    try:
                        command = r.recognize_google(audio)
                        print("You said: " + command)
                        if "open Google" in command:
                            speak("Opening Google")
                            webbrowser.open("https://www.google.com")
                        elif "open YouTube" in command:
                            speak("Opening YouTube")
                            webbrowser.open("https://www.youtube.com")
                        elif "exit" in command:
                            speak("Goodbye!")
                            break
                        else:
                            speak("Sorry, I didn't understand that.")
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))

       

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
>>>>>>> effd3e2 (Updated code)

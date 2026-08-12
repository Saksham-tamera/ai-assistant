from openai import api_key
import speech_recognition as sr
import webbrowser
import pyttsx3
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
aapi_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")


    
    
if __name__ == "__main__":
    speak("Initializing jojo") 
    while True:
        # Listen for the wake word "jojo"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...") 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word= r.recognize_google(audio)
            if "jojo" in word.lower():
                speak("Yes, I am here. How can I assist you?")
                # Listen for the next command
                with sr.Microphone() as source:
                    print("Activate...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    response = client.models.generate_content(
                            model="gemini-3.6-flash",
                            contents=command
                    )
                    answer = response.text
                    answer = answer.replace("*","")
                    answer = answer.replace(",","")
                    answer = answer.replace("#","")
                    speak(answer)
                    print(answer)
            elif "false" in word:
                speak("goodbye!")
                break
            else:
                    speak("Please say the wake word 'jojo' to activate me.")


                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))


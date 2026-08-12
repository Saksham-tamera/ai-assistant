import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

r= sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("assistant:",text)
    engine.say(text)
    engine.runAndWait()





with sr.Microphone() as source:
    audio=r.listen(source)
text = r.recognize_google(audio)
print("say somthing",text)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=text
    )

answer = response.text

print("assistant:",answer)
speak(answer)

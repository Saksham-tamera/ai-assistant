import speech_recognition as sr
import pyttsx3
from open_ai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

r= sr.Recognizer()
engine = pyttsx3.init()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print(os.getenv("OPENAI_API_KEY") is not None)
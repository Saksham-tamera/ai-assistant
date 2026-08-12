import speech_recognition as sr
import pyttsx3
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

r= sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

with sr.Microphone() as source:
    audio=r.listen(source)
text = r.recognize_google(audio)
print("say somthing",text)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "system",
            "content":"""give only the important points from the user's question and give the answer.only give the bullent point. 
              don't give the system process.and any extra line""" 
        },
        {"role": "user", "conent": text}
    ]
)
response.choices[0].message.content


speak(response)

          
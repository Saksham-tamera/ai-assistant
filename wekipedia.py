import speech_recognition as sr
import pyttsx3
import wikipediaapi
#initialize wikipedia api
wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='AI Assistant/1.0'`
    )

#initialize the recognizer
r=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("assistant:",text)
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    print("Listening...")
    audio=r.listen(source)
    audio_text=r.recognize_google(audio)
    print("You said:",audio_text)

    page = wiki.page(audio_text)
    your_title = page.title
    your_summary = page.summary
    
    if page.exists():
        print(your_title)
        speak(your_title)
        print(your_summary)
        
    else:
        print("No page found for:", audio_text)
        speak("No page found for: " + audio_text)
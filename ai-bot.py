import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Jojo: {text}")
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
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
    else:
        speak("I don't know that command yet.")


    
    
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
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word= r.recognize_google(audio)
            if "jojo" in word.lower():
                speak("Yes, I am here. How can I assist you?")
                with sr.Microphone() as source:
                    print("Activate...")
                    audio = r.listen(source)
                try:
                    command = r.recognize_google(audio)
                    processCommand(command)
                except sr.UnknownValueError:
                    speak("I did not catch that command. Please try again.")
                except sr.RequestError:
                    speak("Voice service is unavailable. Please try again later.")
            else:
                speak("Please say the wake word 'jojo' to activate me.")

        except Exception as e:
            print("Error; {0}".format(e))

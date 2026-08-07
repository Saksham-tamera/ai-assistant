import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) #0 is for male and 1 is for female 
engine.say("my self akhand ")
engine.runAndWait()

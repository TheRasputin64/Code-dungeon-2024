# pip install SpeechRecognition pyttsx3 PyAudio
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except:
            return ""

speak("Hello! Say goodbye to exit.")
while True:
    text = listen()
    if 'goodbye' in text:
        speak("Goodbye!")
        break
    elif text:
        speak("You said: " + text)
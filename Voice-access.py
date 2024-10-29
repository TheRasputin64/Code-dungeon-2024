# pip install SpeechRecognition pyttsx3 PyAudio
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
commands = {'grant access', 'open system', 'unlock'}

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except:
            return ""

while True:
    command = listen()
    if command in commands:
        engine.say("Access granted")
        engine.runAndWait()
    elif command == "exit":
        break
    elif command:
        engine.say("Access denied")
        engine.runAndWait()
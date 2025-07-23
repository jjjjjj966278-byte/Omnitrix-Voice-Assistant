import speech_recognition as sr
import webbrowser
import os
import time

# Voice assistant Omnitrix ready!
def speak(text):
    print(f"🗣️ Omnitrix: {text}")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError:
        speak("Network issue.")
        return ""

def process_command(cmd):
    if "play song" in cmd:
        speak("Opening YouTube for song...")
        webbrowser.open("https://www.youtube.com/results?search_query=pal+pal+del+ke+pass")
    elif "open youtube" in cmd:
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")
    elif "open google" in cmd:
        speak("Opening Google...")
        webbrowser.open("https://google.com")
    elif "photo" in cmd:
        speak("Opening gallery...")
        os.system("am start -a android.intent.action.VIEW -d file:///sdcard/DCIM/Camera")
    elif "flashlight on" in cmd:
        os.system("termux-torch on")
        speak("Flashlight turned on")
    elif "flashlight off" in cmd:
        os.system("termux-torch off")
        speak("Flashlight turned off")
    elif "exit" in

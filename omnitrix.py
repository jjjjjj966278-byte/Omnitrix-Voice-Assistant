import kivy
from kivy.app import App
from kivy.uix.button import Button
import speech_recognition as sr
import pyttsx3

class VoiceApp(App):
    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def listen(self, instance):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            self.speak("You said " + text)
        except:
            self.speak("Sorry, I did not understand.")

    def build(self):
        return Button(text="Tap to Speak", on_press=self.listen)

if __name__ == "__main__":
    VoiceApp().run()

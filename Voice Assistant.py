import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes as pj

def spech_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None

def text_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        spoken_text = spech_text()
        if spoken_text is None:
            continue

        data1 = spoken_text.lower()

        if "your name" in data1:
            text_speech("My name is Krishna")

        elif "old are you" in data1:
            text_speech("I am 5 years old")

        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I:%M %p")
            text_speech(f"The current time is {time}")

        elif "youtube" in data1:
            text_speech("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")

        elif "google" in data1:
            text_speech("Opening Google")
            webbrowser.open("https://www.google.co.in/")

        elif "joke" in data1:
            joke_1 = pj.get_joke(language='en', category="neutral")
            print(joke_1)
            text_speech(joke_1)

        elif "stop" in data1:
            text_speech("Thank you sir, shutting down.")
            break

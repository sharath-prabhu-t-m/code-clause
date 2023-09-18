import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the request: {e}")
        return ""

def main():
    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hello! How can I assist you today?")
        elif "your name" in query:
            speak("I am your Python voice assistant.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that. Please repeat.")

if __name__ == "__main__":
    main()
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the request: {e}")
        return ""

def main():
    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hello! How can I assist you today?")
        elif "your name" in query:
            speak("I am your Python voice assistant.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that. Please repeat.")

if __name__ == "__main__":
    main()

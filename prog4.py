import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import os
import random

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
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your audio.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the request: {e}")
        return ""

def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        weather_data = data["main"]
        temperature = weather_data["temp"]
        humidity = weather_data["humidity"]
        description = data["weather"][0]["description"]
        return f"The weather in {city} is {description}. The temperature is {temperature}°C, and humidity is {humidity}%."
    else:
        return "City not found."

def play_music():
    music_folder = "PATH_TO_YOUR_MUSIC_FOLDER"
    music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
    if not music_files:
        return "No music files found in the specified folder."
    random.shuffle(music_files)
    os.system(os.path.join(music_folder, music_files[0]))

def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I assist you today?")
        elif "your name" in query:
            speak("I am your Python voice assistant.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")
        elif "weather" in query:
            speak("Sure! Please tell me the city name.")
            city = listen()
            weather_info = get_weather(city)
            speak(weather_info)
        elif "play music" in query:
            play_music()
        elif "search" in query:
            speak("What would you like me to search for?")
            search_query = listen()
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
        else:
            speak("I didn't understand that. Please repeat.")

if __name__ == "__main__":
    main()

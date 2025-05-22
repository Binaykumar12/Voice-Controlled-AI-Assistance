import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import re

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
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        speak("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        speak("Could not request results, check your internet connection.")
        return ""

def calculate(command):
    numbers = re.findall(r'\d+', command)
    if "sum" in command or "+" in command:
        result = sum(map(int, numbers))
        speak(f"The sum is {result}")
    elif "minus" in command or "-" in command:
        result = int(numbers[0]) - int(numbers[1])
        speak(f"The result is {result}")
    elif "multiply" in command or "times" in command or "*" in command:
        result = int(numbers[0]) * int(numbers[1])
        speak(f"The result is {result}")
    elif "divide" in command or "/" in command:
        if int(numbers[1]) == 0:
            speak("Cannot divide by zero.")
        else:
            result = int(numbers[0]) / int(numbers[1])
            speak(f"The result is {result}")
    else:
        speak("Sorry, I could not perform the calculation.")

def execute_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "play music" in command:
        os.system("start wmplayer")  # Opens Windows Media Player
        speak("Playing music")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    elif any(op in command for op in ["sum", "+", "minus", "-", "multiply", "times", "*", "divide", "/"]):
        calculate(command)
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        user_command = listen()
        if user_command:
            execute_command(user_command)

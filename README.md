# 🎙️ Voice-Controlled Assistant

A simple Python-based voice assistant that can recognize your speech and respond with spoken output. It can perform basic tasks like telling the time, opening websites, playing music, and even simple math operations using natural language.

## 🚀 Features

- 🗣️ Converts speech to text using Google's Speech Recognition API
- 🔊 Responds with voice using `pyttsx3` (offline text-to-speech)
- ⏰ Tells the current time
- 🌐 Opens websites like YouTube and Google
- 🎵 Plays music using Windows Media Player
- ➕ Performs basic calculations (sum, minus, multiply, divide)
- ❌ Exit on voice command

## 🧰 Requirements

Install dependencies with:
pip install speechrecognition pyttsx3 pyaudio

If pyaudio fails, use:

Windows: pip install pipwin && pipwin install pyaudio

Linux: sudo apt-get install python3-pyaudio

▶️ How to Use
Make sure your microphone is enabled.

Run the script:
python voice_assistant.py
Say commands like:

"What time is it?"

"Open YouTube"

"Sum 45 and 32"

"Divide 50 by 5"

"Play music"

"Exit"

🧠 Example Interactions
You: What time is it?
Assistant: The time is 15:34:10

You: Open Google
Assistant: Opening Google

You: Multiply 7 and 8
Assistant: The result is 56

📄 License
This project is for learning and personal use. Licensed under the MIT License.

# MyAlexa Bot

A Python-based AI bot with voice recognition, text-to-speech, and advanced features like NLP, music playback, and document reading.

---

## Features
- **Voice Recognition**: Listen to user commands using `speech_recognition`.
- **Text-to-Speech**: Respond to users with `gTTS` or `pyttsx3`.
- **Natural Language Processing**: Use OpenAI’s GPT for intelligent responses.
- **Music Playback**: Play songs from a local library or Spotify.
- **Document Reading**: Read and summarize PDFs or text files.
- **GUI**: A user-friendly interface built with `tkinter` or `PyQt`.
- **Computer Vision**: Detect objects or faces using OpenCV.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VenkataVasista/myalexa-bot.git
2.Set up a Virtual Enviorment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Run the bot:
python bot.py

Usage
Wake Word: Say "Hey Lexa" to activate the bot.

Commands:

"What’s the time?" → Bot tells the current time.

"Play music" → Bot plays a song.

"Read this document" → Bot reads and summarizes a PDF.

"Set a reminder" → Bot sets a reminder for you.

Documentation
Daily Progress Log
Day 1: Set up the project structure and implemented basic voice recognition.

Day 2: Added text-to-speech functionality and a simple interaction loop.

Day 3: Improved error handling and tested the bot with different phrases.

Day 4: Added wake word detection using pyaudio.

Day 5: Implemented basic commands like time and jokes.

Day 6: Refactored the code for modularity and pushed updates to GitHub.

Day 7: Tested the bot thoroughly and wrote a detailed README.

Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.




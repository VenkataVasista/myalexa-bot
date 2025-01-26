import speech_recognition as sr
from gtts import gTTS
import os

# Function to listen to user input
def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return None

# Function to respond to the user
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # Use "afplay" on macOS or "start" on Windows

# Main interaction loop
def main():
    while True:
        print("Say something...")
        user_input = listen_to_user()
        if user_input:
            if "hello" in user_input.lower():
                speak("Hello! How can I assist you today?")
            elif "bye" in user_input.lower():
                speak("Goodbye! Have a great day.")
                break
            else:
                speak("I didn't understand that. Can you repeat?")

if __name__ == "__main__":
    main()
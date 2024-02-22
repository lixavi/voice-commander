# utils.py

import pyttsx3

def convert_text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred while converting text to speech: {e}")

def convert_speech_to_text():
    try:
        # Code to convert speech to text
        pass
    except Exception as e:
        print(f"An error occurred while converting speech to text: {e}")

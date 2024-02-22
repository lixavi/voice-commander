# voice_commander.py

import speech_recognition as sr
from commands import CommandProcessor

class VoiceCommander:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.command_processor = CommandProcessor()

    def listen_for_command(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing command...")
            command = self.recognizer.recognize_google(audio)
            print("Command:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

    def process_command(self, command):
        if command:
            response = self.command_processor.execute_command(command)
            print("Response:", response)
            # Convert response to speech and speak it out
            self.speak(response)
        else:
            print("No command recognized.")

    def speak(self, text):
        # Code to convert text to speech and play it
        pass

# main.py

from voice_commander import VoiceCommander

def main():
    assistant = VoiceCommander()
    print("VoiceCommander initialized. Listening for commands...")
    try:
        while True:
            command = assistant.listen_for_command()
            assistant.process_command(command)
    except KeyboardInterrupt:
        print("\nExiting VoiceCommander...")

if __name__ == "__main__":
    main()

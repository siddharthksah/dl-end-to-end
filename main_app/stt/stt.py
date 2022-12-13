import speech_recognition as sr

def speech_to_text(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print("Sorry, I could not understand what you said.")

# speech_to_text("path/to/audio/file.wav")

# -*- coding: utf-8 -*-
"""STT-TTS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1msGNzuIxvHpXQfJDC2VTeBKWIKVme_2i
"""

!pip install SpeechRecognition pyaudio

!pip install SpeechRecognition
import speech_recognition as sr

import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech(audio_path):
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)

#Example usage:
input_audio = "/content/drive/MyDrive/123.wav"
recognized_text = recognize_speech(input_audio)
print("Recognized Text:", recognized_text)

import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")  # (de_core_news_sm )for german language

def process_text(text):
    doc = nlp(text)
    # Perform NLP tasks here
    return doc

# Example usage:
#text_to_process = "This is a sample text to process."
#processed_doc = process_text(text_to_process)

!pip install gTTs
import gtts

import gtts

def text_to_speech(text, output_path):
    tts = gTTS(text)
    tts.save(output_path)

from gtts import gTTS

# Text to be converted to speech
text = "Hello, this is a test."

# Language in which you want to convert
language = "en"

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
tts = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a file
tts.save("output.mp3")

def stt_tts(audio_path, output_path):
    # Step 1: Convert speech to text
    recognized_text = recognize_speech(audio_path)

    # Step 2: NLP Processing
    processed_text = process_text(recognized_text)

    # Step 3: Generate speech from processed text
    text_to_speech(processed_text.text, output_path)

# Example usage:

print("Recognized Text:", recognized_text)
from IPython.display import Audio
tts =  gTTS("Hello mam how was our presentation")
tts.save('1.wav')
sound_file = '1.wav'
Audio(sound_file,autoplay = True)

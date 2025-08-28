import queue
from attr import s
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime

# Initialize the Vosk model and TTS engine
model = Model("!AI/L34/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init()

# Callback function to capture audio data
def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))

# Function to process user input and respond
def process_query(query):
    query = query.lower()
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        response = f"The current time is {now}."
    elif "date" in query:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        response = f"Today's date is {today}."
    else:
        response = "I'm sorry, I didn't understand that."
    return response

# Open the audio stream
with sd.RawInputStream:s
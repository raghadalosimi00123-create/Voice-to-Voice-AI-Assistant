import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from dotenv import load_dotenv
from google import genai
from gtts import gTTS
from playsound import playsound


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


sample_rate = 44100
duration = 5

print("🎤 Speak now...")

recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="int16"
)

sd.wait()

write("input.wav", sample_rate, recording)

print(" Recording finished.")


print("Loading Whisper...")

model = whisper.load_model("base")

result = model.transcribe("input.wav")

question = result["text"]

print("\nYou said:")
print(question)


response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=question
)

answer = response.text

print("\nGemini:")
print(answer)


tts = gTTS(
    text=answer,
    lang="en"
)

tts.save("response.mp3")

print("\n Playing response...")

playsound("response.mp3")
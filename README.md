# Voice-to-Voice-AI-Assistant


# Project Overview

This project implements a Voice-to-Voice AI Assistant using Python.
The assistant receives spoken input from the user, converts it into text, sends the text to a Large Language Model (Google Gemini), then converts the generated response back into speech.

# Project Objectives

The project is designed to complete the following three tasks:

1. Speech-to-Text (STT)
2. Large Language Model (LLM) Processing
3. Text-to-Speech (TTS)

# Technologies Used

- Python
- Google Gemini API
- OpenAI Whisper
- gTTS
- SoundDevice
- SciPy
- python-dotenv

# Project Workflow

The application follows the sequence below:

User speaks

Audio is recorded and saved as input.wav

Whisper converts the audio into text


The text is sent to Google Gemini

Gemini generates a response

The response is converted into speech using gTTS

The generated audio is played to the user

# Why is the audio recorded before processing?
Whisper works with audio files instead of directly reading from the microphone.
For this reason, the application first records the user's voice and saves it as a WAV file before performing speech recognition.
This design also provides additional advantages such as:
- Easier debugging.
- Ability to replay recordings.
- Saving conversations if needed.
- Better compatibility with speech recognition models.
# Installation

Install the required libraries:

pip install -r requirements.txt

# API Configuration
Create a .env file and add your Gemini API key:
GEMINI_API_KEY=YOUR_API_KEY

# Running the Project
Run the application using:
python app.py
## Expected Output
1. The application records the user's speech.
2. Whisper converts speech into text.
3. Gemini generates an intelligent response.
4. gTTS converts the response into speech.
5. The generated audio is played automatically.

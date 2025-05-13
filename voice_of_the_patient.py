
# Step 1: Setup Audio Recorder (requires ffmpeg & portaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
from groq import Groq

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Record audio from the microphone and save it as an MP3 file.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert to WAV and then MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")
    
    except Exception as e:
        logging.error(f"An error occurred during recording: {e}")
        
audio_filepath="patient_voice_test_for_patient.mp3"
record_audio(file_path=audio_filepath)

# # step2
# import os
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# client = Groq(api_key=GROQ_API_KEY)
# stt_model="whisper-large-v3"
# audio_file=open(audio_filepath,"rb")
# transcription = client.audio.transcriptions.create(
#     model=stt_model,
#     file=audio_file,
#     language="en",
# )
# print(transcription.text)


# #Step2: Setup Speech to text–STT–model for transcription
# import os
# from groq import Groq

# GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
# stt_model="whisper-large-v3"

# def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
#     client=Groq(api_key=GROQ_API_KEY)
    
#     audio_file=open(audio_filepath, "rb")
#     transcription=client.audio.transcriptions.create(
#         model=stt_model,
#         file=audio_file,
#         language="en"
#     )

#     return transcription.text
    
# Inside groq_utils.py
import requests
import os
from groq import Groq
def transcribe_with_groq(GROQ_API_KEY, audio_filepath, stt_model="whisper-large-v3"):
    endpoint = "https://api.groq.com/openai/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    files = {"file": open(audio_filepath, "rb")}
    data = {"model": stt_model}
    response = requests.post(endpoint, headers=headers, files=files, data=data)
    response.raise_for_status()
    return response.json()["text"]

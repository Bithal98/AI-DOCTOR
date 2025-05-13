# Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS


def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    
input_text = "Hi this is Ai with Bithal!"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


# Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
from elevenlabs import save

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 


#Step2: Use Model for Text output to Voice

import subprocess
import platform

from gtts import gTTS
from playsound import playsound
import os

def text_to_speech_with_gtts(input_text, output_filepath):
    try:
        # Generate the speech and save as mp3
        tts = gTTS(text=input_text, lang='en', slow=False)
        tts.save(output_filepath)

        # Play the audio safely using playsound (cross-platform)
        playsound(output_filepath)

    except Exception as e:
        print(f"An error occurred while trying to process or play the audio: {e}")

# Example usage
input_text = "Hi this is AI with Hassan, autoplay testing!"
output_file = os.path.abspath("gtts_testing_autoplay.mp3")
# text_to_speech_with_gtts(input_text=input_text, output_filepath=output_file)      
        
        
from elevenlabs import save, ElevenLabs
from playsound import playsound
import os

# Ensure your API Key is loaded properly
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        audio = client.generate(
            text=input_text,
            voice="Aria",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )

        save(audio, output_filepath)

        # Use playsound for safe cross-platform autoplay
        playsound(output_filepath)

    except Exception as e:
        print(f"An error occurred while generating or playing the audio: {e}")

# Example usage
input_text = "Hi this is AI with Hassan using ElevenLabs, autoplay testing!"
output_file = os.path.abspath("elevenlabs_testing_autoplay.mp3")
text_to_speech_with_elevenlabs(input_text=input_text, output_filepath=output_file)





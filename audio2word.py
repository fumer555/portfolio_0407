# import openai
from pydub import AudioSegment
from openai import OpenAI
import os


def transcribe_audio(file_path="active_audio.wav"):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )
    audio = AudioSegment.from_wav(file_path)
    print(f"Original sample rate: {audio.frame_rate}, Channels: {audio.channels}")
    audio = audio.set_frame_rate(16000).set_channels(1)
    print(f"Converted sample rate: {audio.frame_rate}, Channels: {audio.channels}")
    # Rest of your code...
    temp_path = "temp_audio.wav"
    audio.export(temp_path, format="wav")

    # 
    with open(temp_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

    return transcript.text

def print_text():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )
    temp_path = "temp_audio.wav"
    with open(temp_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    #openai.audio.transcriptions.create(model=audio_model_name, file=file_name, **extra_args)
    print(transcript.text)

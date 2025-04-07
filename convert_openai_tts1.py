import os
from openai import OpenAI
from gtts import gTTS
from pydub import AudioSegment
from pygame import mixer
import numpy as np
import pyrubberband as pyrb


import librosa
# from pydub import AudioSegment

def time_stretch_librosa(input_file, output_file, speed_factor=1.0):
    # Load audio
    y, sr = librosa.load(input_file, sr=None, mono=False)
    
    # Time-stretch using phase vocoder
    y_stretch = librosa.effects.time_stretch(y, rate=speed_factor)
    
    # For stereo handling
    if y.ndim == 2:
        y_stretch = y_stretch.T
    
    # Convert back to pydub format
    audio = AudioSegment(
        y_stretch.tobytes(),
        frame_rate=sr,
        sample_width=2,
        channels=1 if y.ndim == 1 else 2
    )
    audio.export(output_file, format="wav")

def text_to_speech_and_play(text, lang='zh', output_file='mp3.wav'):
    """
    Full process: Generate speech with gTTS, adjust volume with pydub, and save the file as WAV.
    """
    try:
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
        )
        # Open AI module
        speech_file_path = output_file
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
            speed=1.2,
        )
        response.stream_to_file(speech_file_path)


        print("Playing audio...")
        mixer.init()
        mixer.music.load(output_file)
        mixer.music.play()
        while mixer.music.get_busy():  # Wait for playback to finish
            pass

    except Exception as e:
        print(f"Error during processing: {e}")




def text_to_speech_and_play_2(text, lang='zh', output_file='mp3.wav'):
    """
    Generate speech with OpenAI TTS, double the speed with phase vocoder, and play.
    """
    try:
        # Generate speech with OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text,
        )
        response.stream_to_file(output_file)
        
        # Load the generated audio
        audio = AudioSegment.from_file(output_file)
        
        # Convert to numpy array for processing
        samples = np.array(audio.get_array_of_samples())
        sr = audio.frame_rate
        channels = audio.channels
        
        # Normalize to float32 [-1, 1]
        max_val = 2 ** (8 * audio.sample_width - 1)
        np_samples = samples.astype(np.float32) / max_val
        
        # Reshape for stereo (n_samples, n_channels)
        if channels == 2:
            np_samples = np_samples.reshape((-1, 2))
        
        # Time-stretching with phase vocoder (0.5 = double speed)
        stretched = pyrb.time_stretch(np_samples, sr, 0.5)
        
        # Convert back to integer
        stretched_int = (stretched * max_val).astype(np.int32)
        
        # Create new AudioSegment
        stretched_audio = AudioSegment(
            stretched_int.tobytes(),
            frame_rate=sr,
            sample_width=audio.sample_width,
            channels=channels
        )
        
        # Save processed audio
        stretched_audio.export(output_file, format="wav")
        
        # Play audio with pygame
        mixer.init()
        mixer.music.load(output_file)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
            
    except Exception as e:
        print(f"Error: {e}")


def play_english(text):
    text_to_speech_and_play(text, lang='en', output_file='english.mp3')

def play_chinese(text):
    text_to_speech_and_play(text, lang='zh', output_file='chinese.mp3')

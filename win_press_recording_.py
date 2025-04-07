import subprocess
import signal
import os

class AudioRecorder:
    def __init__(self, device="Microphone (Realtek Audio)"):
        self.device = device
        self.process = None
        self.output_file = None

    def start_recording(self, filename):
        self.output_file = filename
        command = [
            "ffmpeg",
            "-f", "dshow",
            "-i", f"audio={self.device}",
            "-ar", "44100",  # Set sample rate to 44.1 kHz (CD quality)
            "-ac", "1",  # Set number of channels to 1 (mono)
            self.output_file
        ]
        self.process = subprocess.Popen(command)
        print(f"Recording started: {filename}")

    def stop_recording(self):
        if self.process:
            self.process.terminate()  
            self.process.wait() 
            print(f"Recording stopped: {self.output_file}")
            self.process = None
import subprocess
import signal
import os

class AudioRecorder:
    def __init__(self, device="plughw:Device,0"):
        self.device = device
        self.process = None
        self.output_file = None

    def start_recording(self, filename):
        self.output_file = filename
        command = [
            "arecord",
            "-D", self.device,   
            "-f", "cd",          
            "-c", "1",           
            filename             #
        ]
        self.process = subprocess.Popen(command)
        print(f"Recording started: {filename}")

    def stop_recording(self):
        if self.process:
            self.process.terminate()
            self.process.wait() 
            print(f"Recording stopped: {self.output_file}")
            self.process = None
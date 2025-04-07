import subprocess

def record_audio(filename, duration, device="hw:3,0"):
    command = [
        "arecord",
        "-D", device,      
        "-f", "cd",       
        "-c", "1",        
        "-d", str(duration),   
        filename              
    ]
    try:
        print(f"Recording {duration} seconds of audio to {filename}...")
        subprocess.run(command, check=True)  
        print("Recording complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during recording: {e}")
    except FileNotFoundError:
        print("arecord command not found. Please make sure ALSA is installed.")

if __name__ == "__main__":
    record_audio("test.wav", 10, "hw:3,0")  

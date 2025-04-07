from pynput import keyboard
from win_press_recording_ import AudioRecorder
from audio2word import transcribe_audio
from conversation_psy import conversation
from set_env import set_env
from convert_openai_tts1 import play_english
from find_symptom import find_most_relevant_symptom
import time

recorder = AudioRecorder(device="Microphone (Realtek Audio)")
recording = False

def on_press(key):
    global recording
    if key.char == 'b' and not recording:
        print("\n\n")
        recording = True
        timestamp = int(time.time())
        recorder.start_recording(f"audio_{timestamp}.wav")

def on_release(key):
    global recording
    if key.char == 'b' and recording:
        recording = False
        recorder.stop_recording()
        time.sleep(1) 
        set_env()
        prompt = transcribe_audio(recorder.output_file)
        print(f"User: {prompt}")
        behavior = conversation(prompt)
        print(f"Patient's behavior: {behavior}")
        diagnosis, definition = find_most_relevant_symptom(behavior)
        print(f"The patient has {diagnosis}, which is described as following: {definition}")
        play_english(f"The patient has the following behavior: {behavior}, based on the model, the patient most likely has {diagnosis}, which is described as following: {definition}")

if __name__ == "__main__":
    print("Press and hold on the pedal to record. Release to stop and process.")
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("Program stopped by user.")

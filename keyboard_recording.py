from pynput import keyboard
import time

space_pressed = False

def on_press(key):
    global space_pressed
    if key == keyboard.Key.space and not space_pressed:
        print(f"[{time.time()}] Key pressed: SPACE")
        space_pressed = True 

def on_release(key):
    global space_pressed
    if key == keyboard.Key.space:
        print(f"[{time.time()}] Key released: SPACE")
        space_pressed = False

if __name__ == "__main__":
    try:
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()

        print("Listening for keyboard events. Hold SPACE to see behavior.")
        

        while True:
            if space_pressed:
                print(f"[{time.time()}] SPACE is being held.")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nListener stopped by user.")

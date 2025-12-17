import pyautogui
from pynput import keyboard
from pathlib import Path
import time

# Disable PyAutoGUI fail-safe to prevent corner detection issues
pyautogui.FAILSAFE = False

DICTIONARY_FILE = Path(__file__).resolve().parents[1] / "automation" / "dictionary.txt"
click_actions = []  # Stores {"pos": (x, y), "action": "text"}
recording = True
running = True

# Load dictionary
def load_dictionary():
    with open(DICTIONARY_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Save dictionary
def save_dictionary(words):
    with open(DICTIONARY_FILE, "w") as f:
        f.write("\n".join(words))

# Hotkey handlers
def on_press_record(key):
    global recording
    try:
        if key.char.lower() == 'o':
            recording = False
            return False
    except AttributeError:
        pass

def on_press_execute(key):
    global running
    try:
        if key.char.lower() == 'q':
            running = False
            return False
    except AttributeError:
        pass

# Record clicks
def record_clicks():
    global recording
    print("Recording clicks... Click anywhere, then enter action (type 'text'). Press 'O' to stop recording.")
    listener = keyboard.Listener(on_press=on_press_record)
    listener.start()

    while recording:
        # Use a more reliable method to detect mouse clicks
        try:
            # Check if left mouse button is pressed
            if pyautogui.mouseDown(button='left'):
                x, y = pyautogui.position()
                action = input(f"Click at ({x},{y}). Enter action ('text'): ").strip()
                click_actions.append({"pos": (x, y), "action": action})
                print(f"Saved action '{action}' at {x},{y}")
                time.sleep(0.3)  # Avoid duplicate detection
        except Exception as e:
            print(f"Error detecting mouse click: {e}")
            time.sleep(0.1)

    listener.join()
    print("Stopped recording clicks.")

# Execute recorded actions
def execute_actions():
    global running
    dictionary = load_dictionary()
    print("Starting automation. Press 'Q' to stop immediately.")

    listener = keyboard.Listener(on_press=on_press_execute)
    listener.start()

    while running and click_actions:
        for action in click_actions:
            if not running:
                break
            x, y = action["pos"]
            pyautogui.click(x, y)
            if action["action"] == "text":
                if not dictionary:
                    print("Dictionary empty.")
                    running = False
                    break
                word = dictionary.pop(0)
                pyautogui.typewrite(word)
                save_dictionary(dictionary)
            time.sleep(0.2)

    listener.join()
    print("Automation stopped.")

if __name__ == "__main__":
    record_clicks()
    execute_actions()

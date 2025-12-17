import pyautogui
from pynput import keyboard
from pathlib import Path
import time

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

# Configuration - Multiple click positions and key presses
BEFORE_ACTIONS = [
    (742, 1498)
    #"tab",        # Press Tab key
    #"enter",      # Press Enter key
    #(500, 600),   # Click at position
]

AFTER_ACTIONS = [
    (962, 1681),  # Click at position
    "enter",      # Press Enter key
    #"esc",        # Press Escape key
]

DICTIONARY_FILE = Path(__file__).resolve().parent / "dictionary.txt"
running = True
tab_pressed = False

def on_press(key):
    """Handle key press events - only respond to Tab+Q combination"""
    global running, tab_pressed
    try:
        # Check for Tab key
        if key == keyboard.Key.tab:
            tab_pressed = True
        # Check for Q key only if Tab was pressed first
        elif hasattr(key, 'char') and key.char and key.char.lower() == 'q' and tab_pressed:
            print("\n[SAFE KEY COMBINATION PRESSED] Stopping automation...")
            running = False
            return False
        else:
            # Reset tab_pressed if any other key is pressed
            tab_pressed = False
    except AttributeError:
        # Handle special keys - reset tab_pressed
        tab_pressed = False

def load_dictionary():
    """Load words from dictionary file"""
    try:
        with open(DICTIONARY_FILE, "r") as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Dictionary file '{DICTIONARY_FILE}' not found!")
        return []

def save_dictionary(words):
    """Save remaining words back to dictionary file"""
    with open(DICTIONARY_FILE, "w") as f:
        f.write("\n".join(words))

def execute_action(action):
    """Execute a single action (click or key press)"""
    if isinstance(action, tuple):
        # It's a click position (x, y)
        x, y = action
        print(f"  Clicking: ({x}, {y})")
        pyautogui.click(x, y)
    elif isinstance(action, str):
        # It's a key press
        print(f"  Pressing key: {action}")
        pyautogui.press(action)
    time.sleep(0.3)

def click_and_paste():
    """Main function: multiple actions before, paste, then multiple actions after"""
    global running, tab_pressed
    dictionary = load_dictionary()
    
    if not dictionary:
        print("Dictionary is empty!")
        return
    
    # Start keyboard listener for safe key
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    print("Auto Clicker started! Press Tab+Q to stop safely.")
    print(f"Before actions: {len(BEFORE_ACTIONS)} actions")
    print(f"After actions: {len(AFTER_ACTIONS)} actions")
    print("Press Enter to start...")
    input()
    
    while running and dictionary:
        # Get the first word
        word_to_paste = dictionary.pop(0)
        print(f"\nUsing word: '{word_to_paste}'")
        
        if not running:
            break
            
        # Step 1: Multiple actions BEFORE pasting
        print("Step 1: Executing BEFORE actions...")
        for i, action in enumerate(BEFORE_ACTIONS):
            if not running:
                break
            print(f"  Before action {i+1}: ", end="")
            execute_action(action)
        
        if not running:
            break
            
        # Step 2: Type the word
        print(f"Step 2: Typing '{word_to_paste}'")
        pyautogui.typewrite(word_to_paste)
        time.sleep(0.3)
        
        if not running:
            break
            
        # Step 3: Multiple actions AFTER pasting
        print("Step 3: Executing AFTER actions...")
        for i, action in enumerate(AFTER_ACTIONS):
            if not running:
                break
            print(f"  After action {i+1}: ", end="")
            execute_action(action)
        
        if running:
            # Save remaining words back to file
            save_dictionary(dictionary)
            print(f"Remaining words in dictionary: {len(dictionary)}")
            print("Press Tab+Q to stop, or wait 2 seconds for next iteration...")
            time.sleep(2)
    
    listener.stop()
    print("Automation stopped.")

if __name__ == "__main__":
    print("Auto Clicker Tool - Clicks and Key Presses")
    print("Update BEFORE_ACTIONS and AFTER_ACTIONS with your coordinates and keys!")
    print("Safe key combination: Press Tab+Q to stop safely")
    print("\nSupported key names: enter, esc, tab, space, backspace, delete, up, down, left, right, etc.")
    
    click_and_paste()
    print("Done!")


'''

### 2. Auto Clicker Tool (`automation/auto_clicker.py`)
An advanced automation tool that can perform sequences of clicks and key presses.

**Features:**
- Multiple click positions before and after text input
- Keyboard key press support (enter, tab, esc, etc.)
- Dictionary-based word automation
- Safe stop with Tab+Q combination
- Continuous loop through dictionary

**Usage:**
```bash
source venv/bin/activate
python3 automation/auto_clicker.py
```

**Configuration:**
Edit the `BEFORE_ACTIONS` and `AFTER_ACTIONS` lists in the script:
```python
BEFORE_ACTIONS = [
    (742, 1498),  # Click position
    "tab",        # Press Tab key
    "enter",      # Press Enter key
]

AFTER_ACTIONS = [
    (962, 1681),  # Click position
    "enter",      # Press Enter key
    "esc",        # Press Escape key
]
```

## Setup

1. **Clone the repository:**
```bash
git clone <repository-url>
cd CTFTOOLS2025
```

2. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install pyautogui pynput
```

4. **Create dictionary file:**
Create an `automation/dictionary.txt` file with words you want to automate (one per line).

## Dependencies

- `pyautogui` - For mouse and keyboard automation
- `pynput` - For keyboard event listening

## Safety Features

- **Tab+Q combination** to safely stop automation
- **PyAutoGUI fail-safe disabled** (controlled by keyboard shortcuts)
- **Real-time monitoring** of stop conditions

'''

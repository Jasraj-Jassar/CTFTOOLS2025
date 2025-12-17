import pyautogui
from pynput import mouse
import time

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print(f"Click detected at: ({x}, {y})")
        time.sleep(0.1)  # Small delay to avoid duplicate clicks

print("Mouse Click Capture Tool")
print("Click anywhere on the screen to capture coordinates")
print("Press Ctrl+C to exit")

try:
    # Start mouse listener
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\nExiting...")

'''

### 1. Mouse Capture Tool (`automation/mouse_capture.py`)
A simple tool to capture mouse click coordinates on screen.

**Usage:**
```bash
source venv/bin/activate
python3 automation/mouse_capture.py
```

- Click anywhere on the screen to capture coordinates
- Press Ctrl+C to exit

'''

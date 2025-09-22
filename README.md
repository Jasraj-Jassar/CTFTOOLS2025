# CTF Automation Tools

A collection of Python automation tools for CTF (Capture The Flag) challenges and general automation tasks.

## Tools Included

### 1. Mouse Capture Tool (`mouse_capture.py`)
A simple tool to capture mouse click coordinates on screen.

**Usage:**
```bash
source venv/bin/activate
python3 mouse_capture.py
```

- Click anywhere on the screen to capture coordinates
- Press Ctrl+C to exit

### 2. Auto Clicker Tool (`auto_clicker.py`)
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
python3 auto_clicker.py
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
Create a `dictionary.txt` file with words you want to automate (one per line).

## Dependencies

- `pyautogui` - For mouse and keyboard automation
- `pynput` - For keyboard event listening

## Safety Features

- **Tab+Q combination** to safely stop automation
- **PyAutoGUI fail-safe disabled** (controlled by keyboard shortcuts)
- **Real-time monitoring** of stop conditions

## Use Cases

- CTF challenge automation
- Form filling automation
- Login attempt automation
- Search query automation
- Any repetitive click/type tasks

## Warning

Use responsibly and only on systems you own or have permission to automate. These tools can perform actions on your system automatically.

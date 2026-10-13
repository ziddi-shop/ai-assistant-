# 🤖 ziddi AI Assistant

A simple Python-based voice assistant that can listen to voice commands, speak responses, search Wikipedia, open websites, play local music, send emails, and control browser tabs/windows.

> **Current version is designed for Windows desktop.**

---

## ✨ Features

The current code supports:

* 🎤 Voice command recognition
* 🔊 Text-to-speech using Windows SAPI5
* 👋 Automatic greeting based on time
* 📚 Wikipedia search
* 🌐 Open YouTube
* 🌐 Open Google
* 🌐 Open Stack Overflow
* 🎵 Play local music
* 🕐 Tell current time
* 🐍 Open the configured `code.py`
* 📧 Send email through Gmail SMTP
* 🗂️ Switch browser tabs
* 🗂️ Switch to previous browser tab
* 🖥️ Switch Windows
* ➖ Minimize window
* ➕ Maximize window
* ❌ Close tab/window
* 🔎 Zoom in
* 🔍 Zoom out
* 🔄 Reset browser zoom
* 🛑 Exit ziddi

---

# 📋 Requirements

## Operating System

The current code is written specifically with Windows in mind.

Recommended:

```text
Windows 10
Windows 11
```

The code uses:

```python
pyttsx3.init('sapi5')
```

and Windows-specific functionality such as:

```python
os.startfile()
```

and:

```python
pyautogui.hotkey('win', ...)
```

Therefore the current version should be treated as a **Windows desktop assistant**.

---

# 🐍 Python

Recommended Python:

```text
Python 3.10
Python 3.11
Python 3.12
Python 3.13
```

Python 3.12 is recommended for the easiest package compatibility.

Check your Python version:

```bash
python --version
```

or:

```bash
py --version
```

---

# 📦 Installation

Open CMD inside the ziddi project folder.

Example:

```bash
cd C:\Users\YourName\Desktop\ziddi
```

Then install the required packages:

```bash
python -m pip install pyttsx3
python -m pip install SpeechRecognition
python -m pip install wikipedia
python -m pip install pyautogui
python -m pip install PyAudio
```

Or install everything together:

```bash
python -m pip install pyttsx3 SpeechRecognition wikipedia pyautogui PyAudio
```

---

# 🎙️ Microphone Setup

ziddi uses:

```python
speech_recognition
```

with:

```python
sr.Microphone()
```

Make sure Windows can access your microphone.

Go to:

```text
Settings
→ Privacy & Security
→ Microphone
```

Enable:

```text
Microphone access
Allow desktop apps to access your microphone
```

Also make sure the correct microphone is selected in Windows Sound settings.

---

# ▶️ Run ziddi

If your Python file is named:

```text
ziddi.py
```

run:

```bash
python ziddi.py
```

If your file has another name, replace `ziddi.py` with that filename.

Example:

```bash
python main.py
```

---

# 👋 Startup

When ziddi starts, it checks the current time.

### Morning

```text
Good Morning!
Hey, I am ziddi. How may I help you?
```

### Afternoon

```text
Good Afternoon!
Hey, I am ziddi. How may I help you?
```

### Evening

```text
Good Evening!
Hey, I am ziddi. How may I help you?
```

---

# 🎤 Voice Recognition

ziddi uses Google's speech recognition service through:

```python
recognizer.recognize_google(
    audio,
    language='en-in'
)
```

Therefore the current voice recognition language is:

```text
English - India
(en-in)
```

The computer needs an internet connection for this recognition method.

---

# 🗣️ Supported Commands

## 📚 Wikipedia

Say:

```text
Wikipedia Albert Einstein
```

or:

```text
Wikipedia Python
```

ziddi will search Wikipedia and read the result aloud.

The current code requests:

```text
5 sentences
```

from the Wikipedia summary.

---

## 🌐 Open YouTube

Say:

```text
Open YouTube
```

ziddi opens:

```text
https://www.youtube.com
```

in the default browser.

---

## 🌐 Open Google

Say:

```text
Open Google
```

---

## 🌐 Open Stack Overflow

Say:

```text
Open Stack Overflow
```

---

# 🎵 Play Music

Say:

```text
Play music
```

The current code searches this exact folder:

```text
C:\Users\HP\Music
```

Then it selects the first item returned by:

```python
os.listdir(music_dir)
```

and opens it.

### Important

Your current code contains:

```python
music_dir = r'C:\Users\HP\Music'
```

If your Windows username is not `HP`, change this path.

For example:

```python
music_dir = r'C:\Users\ziddi\Music'
```

A better approach is to use:

```python
music_dir = os.path.join(
    os.path.expanduser("~"),
    "Music"
)
```

This automatically uses the current Windows user's Music folder.

---

# 🕐 Time

Say:

```text
What is the time
```

or:

```text
The time
```

ziddi responds with the current time.

Example:

```text
Sir, the time is 16:25:10
```

The current code uses 24-hour format:

```text
%H:%M:%S
```

---

# 🐍 Open Code File

Say:

```text
Open code
```

The current code looks for:

```text
C:/Users/HP/Desktop/ziddi/ziddi/code.py
```

If your project is located somewhere else, update:

```python
codePath = "C:/Users/HP/Desktop/ziddi/ziddi/code.py"
```

---

# 📧 Send Email

Say:

```text
Email to
```

ziddi will ask:

```text
What should I say?
```

You then speak the email content.

The current code sends the message to the hardcoded address:

```text
receiver_email@example.com
```

and uses:

```text
Email from ziddi
```

as the subject.

### ⚠️ Important

You MUST replace:

```python
sender_email = 'your_email@gmail.com'
sender_password = 'your_app_password'
```

with valid Gmail credentials.

---

# 🔐 Gmail App Password

For Gmail SMTP, use a **Google App Password** rather than your normal Gmail password.

The code uses:

```text
SMTP Server:
smtp.gmail.com

Port:
587

Security:
STARTTLS
```

Do not publish your Gmail password or App Password on GitHub, Telegram, Discord, or anywhere public.

---

# 🗂️ Browser Tab Controls

## Next Tab

```text
Switch tab
```

or:

```text
Next tab
```

Uses:

```python
pyautogui.hotkey('ctrl', 'tab')
```

---

## Previous Tab

```text
Previous tab
```

or:

```text
Last tab
```

Uses:

```python
pyautogui.hotkey('ctrl', 'shift', 'tab')
```

---

# 🖥️ Window Controls

## Switch Window

```text
Switch window
```

Uses:

```python
pyautogui.hotkey('alt', 'tab')
```

---

## Minimize

```text
Minimize window
```

Uses:

```python
pyautogui.hotkey('win', 'down')
```

---

## Maximize

```text
Maximize window
```

Uses:

```python
pyautogui.hotkey('win', 'up')
```

---

## Close

```text
Close window
```

or:

```text
Close tab
```

Uses:

```python
pyautogui.hotkey('ctrl', 'w')
```

---

# 🔍 Zoom Controls

## Zoom In

```text
Zoom in
```

Uses:

```python
pyautogui.hotkey('ctrl', '+')
```

---

## Zoom Out

```text
Zoom out
```

Uses:

```python
pyautogui.hotkey('ctrl', '-')
```

---

## Reset Zoom

```text
Reset zoom
```

Uses:

```python
pyautogui.hotkey('ctrl', '0')
```

---

# 🛑 Exit ziddi

Say:

```text
Exit
```

or:

```text
Quit
```

or:

```text
Stop
```

ziddi will say:

```text
Okay, shutting down. Have a nice day!
```

and close the program.

---

# ⚠️ Important: "Who Are You?"

The current version is **not an AI chatbot**.

It uses simple:

```python
if / elif
```

command matching.

Therefore:

```text
Who are you?
```

is NOT currently a supported command.

The program will reach:

```text
I don't have a command for that yet.
```

This is normal for the current code.

To make ziddi answer general questions, an AI API such as Gemini or OpenAI would need to be integrated.

---

# ❗ Troubleshooting

## `SpeechRecognition is not installed`

Install:

```bash
python -m pip install SpeechRecognition
```

Then test:

```bash
python -c "import speech_recognition; print('SpeechRecognition OK')"
```

---

## `No module named pyttsx3`

Install:

```bash
python -m pip install pyttsx3
```

---

## `No module named wikipedia`

Install:

```bash
python -m pip install wikipedia
```

---

## `No module named pyautogui`

Install:

```bash
python -m pip install pyautogui
```

---

## `No module named pyaudio`

Install:

```bash
python -m pip install PyAudio
```

If PyAudio installation fails, try:

```bash
python -m pip install pipwin
python -m pipwin install pyaudio
```

If you're still getting errors, Python 3.12 is recommended.

---

# 🔧 Common Problem: Wrong Python Environment

If you installed a package but ziddi still says:

```text
ModuleNotFoundError
```

make sure the same Python installation is being used.

Check:

```bash
where python
```

Then:

```bash
python -m pip --version
```

Install packages through:

```bash
python -m pip install PACKAGE_NAME
```

instead of using a different `pip`.

---

# 📱 Android / Phone Support

### Current code: ❌ Not directly supported

The current source uses Windows-specific components:

```python
pyttsx3.init('sapi5')
```

```python
os.startfile()
```

```python
C:\Users\HP\...
```

and:

```python
pyautogui.hotkey('win', ...)
```

Therefore this exact version is intended for **Windows PC/laptop**.

It cannot simply be copied to an Android phone and expected to work.

For Android support, the project would need a separate Android/Web interface and platform-specific voice/system-control implementation.

---

# 📁 Current Project Concept

The current version can be thought of as:

```text
ziddi
│
├── Voice Input
│   └── SpeechRecognition
│
├── Voice Output
│   └── pyttsx3 / SAPI5
│
├── Information
│   └── Wikipedia
│
├── Browser
│   └── webbrowser
│
├── Email
│   └── Gmail SMTP
│
├── Music
│   └── Local Music Folder
│
└── Desktop Controls
    └── PyAutoGUI
```

---

# 🔒 Security Warning

This program can control your computer through keyboard shortcuts.

Only run the program from a trusted source.

Never publish:

```text
Gmail password
Gmail App Password
API keys
Tokens
Private credentials
```

inside the source code.

---

# 📜 License

Add your preferred license here.

Example:

```text
MIT License
```

---

# 🤖 ziddi

A simple Python voice assistant designed to automate everyday desktop tasks through voice commands.

### Current Version

```text
Python Voice Assistant
Windows Desktop
Command-Based
```

### Built With

```text
Python
pyttsx3
SpeechRecognition
Wikipedia
PyAutoGUI
PyAudio
webbrowser
smtplib
```

---

## ⭐ Quick Start

```bash
python -m pip install pyttsx3 SpeechRecognition wikipedia pyautogui PyAudio
```

Then:

```bash
python main.py
```

Say:

```text
Open YouTube
```

and ziddi will launch YouTube.

---

**ziddi — Voice-controlled desktop assistance, built with Python.**

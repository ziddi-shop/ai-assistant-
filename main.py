import os
import sys
import platform
import subprocess
import webbrowser
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Optional modules
try:
    import pyautogui
except ImportError:
    pyautogui = None

try:
    import wikipedia
except ImportError:
    wikipedia = None

try:
    import speech_recognition as sr
except ImportError:
    sr = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


# =========================================================
# PLATFORM
# =========================================================

SYSTEM = platform.system().lower()

IS_WINDOWS = SYSTEM == "windows"
IS_LINUX = SYSTEM == "linux"
IS_MAC = SYSTEM == "darwin"
IS_ANDROID = "ANDROID_ARGUMENT" in os.environ or "ANDROID_PRIVATE" in os.environ


# =========================================================
# TTS
# =========================================================

engine = None

if pyttsx3:
    try:
        engine = pyttsx3.init()

        voices = engine.getProperty("voices")

        if voices:
            engine.setProperty("voice", voices[0].id)

        engine.setProperty("rate", 175)
        engine.setProperty("volume", 1.0)

    except Exception:
        engine = None


def speak(text):
    """
    Cross-platform safe speech.
    """

    print(f"ziddi: {text}")

    if engine:
        try:
            engine.say(str(text))
            engine.runAndWait()
            return
        except Exception:
            pass

    # If TTS isn't available, don't crash.
    print("[TTS unavailable]")


# =========================================================
# GREETING
# =========================================================

def wish_me():

    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    speak(greeting)
    speak("Hey, I am ziddi. How may I help you?")


# =========================================================
# SPEECH INPUT
# =========================================================

def take_command():

    if sr is None:
        print("SpeechRecognition is not installed.")
        return input("You: ").strip()

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.pause_threshold = 1

            try:
                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )
            except Exception:
                pass

            audio = recognizer.listen(
                source,
                timeout=None,
                phrase_time_limit=10
            )

        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print(f"You: {query}")

        return query.lower().strip()

    except sr.UnknownValueError:

        speak("I didn't understand that.")

    except sr.RequestError:

        speak("Speech recognition service is unavailable.")

    except Exception as e:

        print(f"Speech error: {e}")

    return ""


# =========================================================
# WEB
# =========================================================

def open_url(url):

    try:
        webbrowser.open(url)
        speak("Opening it.")
    except Exception as e:
        print(f"Browser error: {e}")
        speak("I couldn't open the browser.")


# =========================================================
# TIME
# =========================================================

def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak(f"Sir, the time is {current_time}")


# =========================================================
# WIKIPEDIA
# =========================================================

def search_wikipedia(query):

    if wikipedia is None:

        speak("Wikipedia module is not installed.")

        return

    topic = query.replace("wikipedia", "").strip()

    if not topic:

        speak("What should I search on Wikipedia?")

        return

    try:

        speak("Searching Wikipedia...")

        result = wikipedia.summary(
            topic,
            sentences=3,
            auto_suggest=False
        )

        print("\n" + result + "\n")

        speak(result)

    except wikipedia.DisambiguationError as e:

        options = ", ".join(e.options[:3])

        speak(
            f"The term is ambiguous. "
            f"Possible results are {options}"
        )

    except wikipedia.PageError:

        speak("I couldn't find that Wikipedia page.")

    except Exception as e:

        print(f"Wikipedia error: {e}")

        speak("Wikipedia search failed.")


# =========================================================
# MUSIC
# =========================================================

def play_music():

    music_locations = []

    if IS_WINDOWS:

        music_locations.append(
            os.path.join(
                os.path.expanduser("~"),
                "Music"
            )
        )

    elif IS_LINUX or IS_MAC:

        music_locations.append(
            os.path.join(
                os.path.expanduser("~"),
                "Music"
            )
        )

    elif IS_ANDROID:

        music_locations.extend([
            "/storage/emulated/0/Music",
            "/sdcard/Music"
        ])

    music_dir = next(
        (
            path
            for path in music_locations
            if os.path.exists(path)
        ),
        None
    )

    if not music_dir:

        speak("I couldn't find your music folder.")

        return

    try:

        songs = [
            f for f in os.listdir(music_dir)
            if f.lower().endswith(
                (".mp3", ".wav", ".m4a", ".ogg")
            )
        ]

        if not songs:

            speak("No music files were found.")

            return

        song = os.path.join(
            music_dir,
            songs[0]
        )

        if IS_WINDOWS:

            os.startfile(song)

        elif IS_MAC:

            subprocess.run(
                ["open", song],
                check=False
            )

        elif IS_LINUX:

            subprocess.run(
                ["xdg-open", song],
                check=False
            )

        elif IS_ANDROID:

            speak(
                "Local music playback needs an "
                "Android media player integration."
            )

        speak(f"Playing {songs[0]}.")

    except Exception as e:

        print(f"Music error: {e}")

        speak("I couldn't play the music.")


# =========================================================
# DESKTOP CONTROLS
# =========================================================

def desktop_action(action):

    # Phone / unsupported device
    if pyautogui is None:

        speak(
            "Desktop controls aren't available "
            "on this device."
        )

        return

    try:

        if action == "next_tab":

            pyautogui.hotkey(
                "ctrl",
                "tab"
            )

            speak("Switched to next tab.")

        elif action == "previous_tab":

            pyautogui.hotkey(
                "ctrl",
                "shift",
                "tab"
            )

            speak("Switched to previous tab.")

        elif action == "switch_window":

            if IS_WINDOWS:

                pyautogui.hotkey(
                    "alt",
                    "tab"
                )

                speak("Switching window.")

            else:

                speak(
                    "Window switching is "
                    "not available here."
                )

        elif action == "minimize":

            if IS_WINDOWS:

                pyautogui.hotkey(
                    "win",
                    "down"
                )

                speak("Window minimized.")

        elif action == "maximize":

            if IS_WINDOWS:

                pyautogui.hotkey(
                    "win",
                    "up"
                )

                speak("Window maximized.")

        elif action == "close":

            pyautogui.hotkey(
                "ctrl",
                "w"
            )

            speak("Closed.")

        elif action == "zoom_in":

            pyautogui.hotkey(
                "ctrl",
                "+"
            )

            speak("Zooming in.")

        elif action == "zoom_out":

            pyautogui.hotkey(
                "ctrl",
                "-"
            )

            speak("Zooming out.")

        elif action == "reset_zoom":

            pyautogui.hotkey(
                "ctrl",
                "0"
            )

            speak("Zoom reset.")

    except Exception as e:

        print(f"Desktop control error: {e}")

        speak(
            "That desktop command isn't "
            "supported on this device."
        )


# =========================================================
# EMAIL
# =========================================================

def send_email(to, subject, content):

    sender_email = os.getenv("ziddi_EMAIL")
    sender_password = os.getenv("ziddi_EMAIL_PASSWORD")

    if not sender_email or not sender_password:

        speak(
            "Email credentials are not configured."
        )

        print(
            "Set ziddi_EMAIL and "
            "ziddi_EMAIL_PASSWORD environment variables."
        )

        return False

    try:

        message = MIMEMultipart()

        message["From"] = sender_email
        message["To"] = to
        message["Subject"] = subject

        message.attach(
            MIMEText(
                content,
                "plain",
                "utf-8"
            )
        )

        with smtplib.SMTP(
            "smtp.gmail.com",
            587,
            timeout=20
        ) as server:

            server.starttls()

            server.login(
                sender_email,
                sender_password
            )

            server.sendmail(
                sender_email,
                to,
                message.as_string()
            )

        speak("Email has been sent successfully.")

        return True

    except Exception as e:

        print(f"Email error: {e}")

        speak("I wasn't able to send the email.")

        return False


# =========================================================
# EXIT
# =========================================================

def exit_ziddi():

    speak(
        "Okay, shutting down. "
        "Have a nice day!"
    )

    print("ziddi shutting down...")

    sys.exit(0)


# =========================================================
# COMMAND PROCESSOR
# =========================================================

def process_command(query):

    query = query.lower().strip()

    if not query:
        return True

    # -------------------------
    # Wikipedia
    # -------------------------

    if "wikipedia" in query:

        search_wikipedia(query)

    # -------------------------
    # Websites
    # -------------------------

    elif "open youtube" in query:

        open_url(
            "https://www.youtube.com"
        )

    elif "open google" in query:

        open_url(
            "https://www.google.com"
        )

    elif "open stack overflow" in query:

        open_url(
            "https://stackoverflow.com"
        )

    # -------------------------
    # Music
    # -------------------------

    elif "play music" in query:

        play_music()

    # -------------------------
    # Time
    # -------------------------

    elif "the time" in query or "what time" in query:

        tell_time()

    # -------------------------
    # Desktop controls
    # -------------------------

    elif "next tab" in query or "switch tab" in query:

        desktop_action("next_tab")

    elif "previous tab" in query or "last tab" in query:

        desktop_action("previous_tab")

    elif "switch window" in query:

        desktop_action("switch_window")

    elif "minimize window" in query:

        desktop_action("minimize")

    elif "maximize window" in query:

        desktop_action("maximize")

    elif "close window" in query or "close tab" in query:

        desktop_action("close")

    elif "zoom in" in query:

        desktop_action("zoom_in")

    elif "zoom out" in query:

        desktop_action("zoom_out")

    elif "reset zoom" in query:

        desktop_action("reset_zoom")

    # -------------------------
    # Exit
    # -------------------------

    elif any(
        word in query
        for word in [
            "exit",
            "quit",
            "stop",
            "shutdown ziddi"
        ]
    ):

        exit_ziddi()

    

    else:

        speak(
            "I don't have a command for that yet."
        )

    return True




def main():

    print("=" * 50)
    print("        ziddi CROSS-PLATFORM")
    print("=" * 50)

    print(f"Platform: {SYSTEM}")

    wish_me()

    while True:

        try:

            query = take_command()

            if query:

                process_command(query)

        except KeyboardInterrupt:

            print("\nStopping ziddi...")

            break

        except Exception as e:

            print(
                f"Unexpected error: {e}"
            )

            speak(
                "Something went wrong, "
                "but I am still running."
            )


if __name__ == "__main__":

    main()

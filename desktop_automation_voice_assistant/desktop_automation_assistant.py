import speech_recognition as sr
import pyttsx3

class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        print(f"\n🤖 {text}")
        self.engine.say(text)
        self.engine.runAndWait()

class VoiceAssistant(Assistant):
    def __init__(self):
        super().__init__()
        self.__assistant_name = "Jarvis"
        self.recognizer = sr.Recognizer()
    def listen(self):
        with sr.Microphone() as source:
            print("\n🎤  Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.3)

            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio).lower()

                print(f"✅ YOU SAID: {command}")
                return command
            except sr.UnknownValueError:
                print("❌ Could not understand audio")
                return ""
            except Exception as error_message:
                print("⚠️ ERROR:", error_message)
                return""
import os
import webbrowser

def open_app(self, command):

        if "chrome" in command:
            os.system("start chrome")
            self.speak("Opening Chrome")

        elif "calculator" in command:
            os.system("start calculator")
            self.speak("Opening Calculator")

        elif "notepad" in command:
            os.system("start notepad")
            self.speak("Opening Notepad")

        elif "paint" in command:
            os.system("mspaint")
            self.speak("Opening Paint")

        elif "youtube" in command:
            webbrowser.open("https://youtube.com")
            self.speak("Opening youtube")

        elif "google" in command:
            webbrowser.open("https://google.com")
            self.speak("Opening Google")




def search_google(self,command):

    search_term = command.replace("search","")

    url = f"https://www.google.com/search?q={search_term}"

    webbrowser.open(url)

    self.speak(f"Searching {search_term}")

import pyautogui




def type_text(self, command):

    text = command.replace("type","")

    pyautogui.write(text, interval=0.05)

    self.speak("Typing completed")




def mouse_control(self,command):
    if "move right" in command:
        pyautogui.moveRel(100, 0)

    elif "move left" in command:
        pyautogui.moveRel(-100, 0)

    elif "move up" in command:
        pyautogui.moveRel(0, -100)

    elif "move down" in command:
        pyautogui.moveRel(0, 100)

    elif "click" in command:
        pyautogui.click()
        self.speak("Mouse Clicked")

    elif "double click" in command:
        pyautogui.doubleClick()
        self.speak("Double Click")

    elif "click right" in command:
        pyautogui.rightClick()
        self.speak("Right Clicked")

import time




def scroll_control(self, command):

    if "scroll up" in command:
        pyautogui.scroll(500)

    elif "scroll down" in command:
        pyautogui.scroll(-500)




def take_screenshot(self):

    filename = f"screenshot_{int(time.time())}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    self.speak("Screenshot taken")

import keyboard




def volume_control(self, command):

    if "volume up" in command:

        for count in range(5):
            keyboard.press_and_release("volume up")

    elif "volume down" in command:

        for count in range(5):
            keyboard.press_and_release("volume down")

    elif "mute" in command:
        keyboard.press_and_release("volume mute")




def window_control(self, command):

    if "close window" in command:
        pyautogui.hotkey("alt", "f4")
        self.speak("Closing window")

    elif "minimize" in command:
        pyautogui.hotkey("win", "down")

    elif "copy" in command:
        pyautogui.hotkey("ctrl", "c")

    elif "paste" in command:
        pyautogui.hotkey("ctrl", "v")

assistant = VoiceAssistant()

assistant.speak("Voice assistant started")

while True:

    command = assistant.listen()

    if not command:
        continue

    if "open" in command:
        assistant.open_app(command)

    elif "search" in command:
        assistant.search_google(command)

    elif "type" in command:
        assistant.type_text(command)

    elif "move" in command or "click" in command:
        assistant.mouse_control(command)

    elif "scroll" in command:
        assistant.scroll_control(command)

    elif "screenshot" in command:
        assistant.take_screenshot()

    elif "volume" in command or "mute" in command:
        assistant.volume_control(command)

    elif (
            "close" in command
            or "copy" in command
            or "paste" in command
            or "minimize" in command
    ):
        assistant.window_control(command)

    elif "exit" in command or "quit" in command:
        assistant.speak("Goodbye")
        break












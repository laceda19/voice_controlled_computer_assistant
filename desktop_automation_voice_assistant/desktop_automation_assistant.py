import speech_recognition as sr
import pyttsx3

class Assistant:
    def __init__(self):
        self.engine = pyttsx3()

    def speak(self, text):
        print(f"\🤖 {text}")
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





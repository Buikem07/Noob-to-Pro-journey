import os
import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
import time
import platform

class VoiceAssistant:
    """
    A conversational AI voice assistant using Google Gemini, SpeechRecognition, and pyttsx3.
    """

    def __init__(self):
        """Initializes all necessary components."""
        self.recognizer = sr.Recognizer()
        self.tts_engine = None  # We'll initialize it fresh each time
        self.configure_api()
        self.generative_model = genai.GenerativeModel('gemini-1.5-flash')
        self.conversation_history = []

    def configure_api(self):
        """
        Securely configures the Google Generative AI API key from an environment variable.
        """
        try:
            api_key = os.environ.get("GOOGLE_API_KEY")
            if not api_key:
                print("🟡 GOOGLE_API_KEY environment variable not found.")
                api_key = input("   Please paste your Google API key and press Enter: ")
            
            genai.configure(api_key=api_key)
            print("✅ Google API key configured successfully.")
        except Exception as e:
            print(f"🔴 FATAL: Failed to configure API key: {e}")
            exit()

    def get_tts_engine(self):
        """Creates a FRESH TTS engine instance every time — avoids state corruption."""
        try:
            engine = pyttsx3.init()

            # Optional: Set properties for better voice (uncomment if needed)
            # engine.setProperty('rate', 180)  # Speed
            # engine.setProperty('volume', 1.0) # Volume

            # Platform-specific driver hints (optional)
            system = platform.system()
            if system == "Darwin":  # macOS
                engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
            elif system == "Windows":
                voices = engine.getProperty('voices')
                engine.setProperty('voice', voices[0].id)  # Use first available voice

            return engine
        except Exception as e:
            print(f"⚠️  Could not initialize TTS engine: {e}")
            return None

    def listen(self):
        """
        Captures audio from the microphone and transcribes it to text.
        """
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=15)
            except sr.WaitTimeoutError:
                print("👂 Listening timed out. No speech detected.")
                return None

        try:
            print("🧠 Recognizing speech...")
            text = self.recognizer.recognize_google(audio)
            print(f"👤 You said: {text}")
            return text
        except sr.UnknownValueError:
            print("🤔 Sorry, I couldn't understand that.")
            return None
        except sr.RequestError as e:
            print(f"🔌 Could not request results from speech service; {e}")
            return None

    def think(self, prompt: str):
        """
        Generates a response from the Gemini model based on the conversation history.
        Handles safety filters and malformed responses gracefully.
        """
        print("🤖 Thinking...")
        self.conversation_history.append({'role': 'user', 'parts': [prompt]})
        try:
            response = self.generative_model.generate_content(self.conversation_history)
            
            if not response.candidates:
                raise ValueError("No response candidates returned from model.")
            
            top_candidate = response.candidates[0]
            
            if hasattr(top_candidate, 'finish_reason') and top_candidate.finish_reason == "SAFETY":
                raise ValueError("Response blocked due to safety settings.")

            model_response_content = top_candidate.content
            response_text = "".join(part.text for part in model_response_content.parts)
            
            self.conversation_history.append({
                'role': model_response_content.role,
                'parts': [part.text for part in model_response_content.parts]
            })
            
            return response_text

        except Exception as e:
            print(f"🔴 Error generating response from Gemini: {e}")
            if self.conversation_history and self.conversation_history[-1].get('role') == 'user':
                self.conversation_history.pop()
            return "I'm sorry, I'm having trouble processing that right now."

    def speak(self, text: str):
        """
        Speaks text using a FRESH TTS engine instance. Destroys it after use.
        """
        print(f"🔊 Assistant: {text}")
        try:
            # Get FRESH engine
            self.tts_engine = self.get_tts_engine()
            if not self.tts_engine:
                print("🔇 TTS engine failed — responding silently.")
                return

            # Queue speech
            self.tts_engine.say(text)

            # Speak + wait + cleanup
            self.tts_engine.runAndWait()
            self.tts_engine.stop()  # Explicitly stop
            del self.tts_engine      # Force garbage collection
            self.tts_engine = None   # Reset

        except Exception as e:
            print(f"🔴 Error during TTS playback: {e}")
            if self.tts_engine:
                try:
                    self.tts_engine.stop()
                except:
                    pass
                self.tts_engine = None

    def start(self):
        """
        The main loop that runs the voice assistant.
        """
        print("🚀 Starting Voice Assistant...")
        self.speak("Hello! I'm your AI assistant. How can I help you today?")
        print("💡 Say 'goodbye' to exit.")

        while True:
            user_input = self.listen()

            if user_input:
                if "goodbye" in user_input.lower():
                    self.speak("Goodbye! Have a great day!")
                    print("👋 Shutting down...")
                    break

                ai_response = self.think(user_input)
                time.sleep(0.3)  # Prevent user from talking over
                self.speak(ai_response)

            else:
                continue

def main():
    assistant = VoiceAssistant()
    assistant.start()

if __name__ == "__main__":
    main()
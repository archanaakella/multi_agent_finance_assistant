import whisper
import pyttsx3

from agents.language_agent import generate_market_brief

stt_model = whisper.load_model("small")
tts_engine = pyttsx3.init()

def process_voice_input(audio_file):
    """Convert speech to text, query market, return spoken response."""
    text = stt_model.transcribe(audio_file)["text"]
    response = generate_market_brief(text)
    tts_engine.say(response)
    tts_engine.runAndWait()
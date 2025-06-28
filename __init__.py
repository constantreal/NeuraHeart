# __init__.py
from .core import EmotionEngine
from .voice import speak
from .memory import MemoryStore
from .toxicity import is_toxic

class NeuralSchema:
    def __init__(self):
        self.engine = EmotionEngine()
        self.memory = MemoryStore()

    def process(self, text):
        if is_toxic(text):
            return "⚠️ This input may be harmful. Let's talk calmly."

        detected = self.engine.detect_emotion(text)
        response = f"Detected emotion: {detected['emotion']} with confidence {detected['confidence']}"
        self.memory.save({"input": text, "emotion": detected})
        speak(response, emotion=detected["emotion"])
        return response

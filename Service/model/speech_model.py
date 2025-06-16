from funasr import AutoModel
import os
from Service.config import (
    MODELS_DIR,
    MAIN_MODEL,
    VAD_MODEL,
    PUNC_MODEL,
    GEN_PARAMS
)

class SpeechRecognitionModel:
    def __init__(self):
        self.model = None
        self.load_model()
    
    def load_model(self):
        """Initialize the ASR model with configurations from config"""
        self.model = AutoModel(
            model=os.path.join(MODELS_DIR, MAIN_MODEL["name"]),
            model_revision=MAIN_MODEL["revision"],
            vad_model=os.path.join(MODELS_DIR, VAD_MODEL["name"]),
            vad_model_revision=VAD_MODEL["revision"],
            punc_model=os.path.join(MODELS_DIR, PUNC_MODEL["name"]),
            punc_model_revision=PUNC_MODEL["revision"]
        )

    def transcribe(self, audio_data):
        """Transcribe audio data to text using configured parameters"""
        res = self.model.generate(
            input=audio_data,
            cache={},
            **GEN_PARAMS
        )
        return res[0]["text"] if res else ""
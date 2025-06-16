import base64
import io
import librosa
import numpy as np
import soundfile as sf

from Service.model.non_login import NonLogin
from Service.model.text_to_speech import TTS
from typing import Optional
from scipy.io.wavfile import write
from Service.model.speech_model import SpeechRecognitionModel
from Service.model.non_login_speech_answer import NonLoginSpeechAnswer
from Service.common.non_login_audio_chatbot_response import NonLoginAudioChatbotResponse
from Service.common.non_login_chatbot_response import NonLoginChatBotResponse


# non_login_model = NonLogin()
speech_model = SpeechRecognitionModel()
non_login_speech_answer = NonLoginSpeechAnswer()


# non_login_model = NonLogin()
speech_model = SpeechRecognitionModel()
non_login_speech_answer = NonLoginSpeechAnswer()


non_login_model = NonLogin()
text_to_speech = TTS()

def non_login_chatbot(place: str, info: str):
    if info not in ['文化介绍','特色美食']:
        answer = non_login_model.invoke(place, info)
        return NonLoginChatBotResponse(response = answer)
    else:
        answer = non_login_model.invoke(place, info)
        speech_answer = text_to_speech.text_to_speech_and_show_bytes(answer)
        # buffer = io.BytesIO()
        # write(buffer, 24000, speech_answer.astype(np.float32))  # Bark uses 24kHz
        # audio_bytes = buffer.getvalue()
        # audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        return NonLoginChatBotResponse(response = answer, audio = speech_answer)

def non_audio_chatbot(content: bytes) -> NonLoginAudioChatbotResponse:
    buffer = io.BytesIO(content)
    audio, sr = sf.read(buffer)

    # Convert to mono if stereo
    if len(audio.shape) == 2:
        audio = np.mean(audio, axis=1)

    # Resample to 16kHz using librosa
    if sr != 16000:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
        sr = 16000

    # Write back to bytes as WAV
    out_buffer = io.BytesIO()
    sf.write(out_buffer, audio, sr, format='WAV')
    audio_bytes = out_buffer.getvalue()
    out_buffer.close()
    question = speech_model.transcribe(audio_bytes)
    answer = non_login_speech_answer.invoke(question)
    if '文化介绍' in answer or '最佳路线' in answer:
        # speech_answer = text_to_speech.generate(answer)
        # buffer = io.BytesIO()
        # write(buffer, 24000, speech_answer.astype(np.float32))  # Bark uses 24kHz
        # audio_bytes = buffer.getvalue()
        # audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        speech_answer = text_to_speech.text_to_speech_and_show_bytes(answer)
        return NonLoginAudioChatbotResponse(question = question, answer = answer, audio = speech_answer)
    else:
        return NonLoginAudioChatbotResponse(question = question, answer = answer)

import json
import os
from pathlib import Path

# Load config.json
_CONFIG_PATH = Path(__file__).parent / "config.json"
with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

# API settings
BASE_API_URL = config["api"]["base_url"]
# Image Processing Configs
IMAGE_CONFIG = config["image_processing"]
ENHANCEMENT_RANGES = config["image_enhancement_ranges"]

DEFAULT_CONTRAST = IMAGE_CONFIG["default_contrast"]
DEFAULT_BRIGHTNESS = IMAGE_CONFIG["default_brightness"]
DEFAULT_SATURATION = IMAGE_CONFIG["default_saturation"]
DEFAULT_SHARPNESS = IMAGE_CONFIG["default_sharpness"]
JPEG_QUALITY = IMAGE_CONFIG["jpeg_quality"]
ERROR_HANDLING = IMAGE_CONFIG["error_fallback"]
USE_BASE64 = IMAGE_CONFIG["base64_encoding"]

# Caption Service Configs
CAPTION_CONFIG = config["caption_service"]
DEFAULT_MODEL = CAPTION_CONFIG["default_model"]
DEFAULT_PROMPT = CAPTION_CONFIG["default_prompt"]
API_BASE_URL = CAPTION_CONFIG["api_base_url"]
ALLOWED_MIME_TYPES = CAPTION_CONFIG["allowed_mime_types"]
API_TIMEOUT = CAPTION_CONFIG["api_timeout"]
DEFAULT_STREAM = CAPTION_CONFIG["default_stream"]
ERROR_MESSAGES = CAPTION_CONFIG["error_messages"]

# Qwen Description Model Config
QWEN_DESCRIPTION_CONFIG = config["qwen_description_model"]
QWEN_MODEL_NAME = QWEN_DESCRIPTION_CONFIG["model_name"]
QWEN_BASE_URL = QWEN_DESCRIPTION_CONFIG["base_url"]
DESCRIPTION_PROMPT = QWEN_DESCRIPTION_CONFIG["prompt_template"]

# Qwen Login Model Config
QWEN_LOGIN_CONFIG = config["qwen_login_model"]

# Model Configuration
QWEN_MODEL_NAME = QWEN_LOGIN_CONFIG["model_name"]
QWEN_BASE_URL = QWEN_LOGIN_CONFIG["base_url"]

# Prompt Templates (EXACTLY as in original)
TRAVEL_PROMPT = QWEN_LOGIN_CONFIG["prompts"]["travel"]
FOOD_PROMPT = QWEN_LOGIN_CONFIG["prompts"]["food"]
ACCOMMODATION_PROMPT = QWEN_LOGIN_CONFIG["prompts"]["accommodation"]
SUMMARY_PROMPT = QWEN_LOGIN_CONFIG["prompts"]["summary"]

# Qwen Speech Model Config
QWEN_SPEECH_CONFIG = config["qwen_speech_model"]

# Model Configuration
QWEN_SPEECH_MODEL = QWEN_SPEECH_CONFIG["model_name"]
QWEN_SPEECH_BASE_URL = QWEN_SPEECH_CONFIG["base_url"]

# Prompt Template (EXACTLY as in original)
SPEECH_PROMPT = QWEN_SPEECH_CONFIG["prompts"]["speech_answer"]

# Qwen NonLogin Model Config
QWEN_NONLOGIN_CONFIG = config["qwen_nonlogin_model"]

# Model Configuration
QWEN_NONLOGIN_MODEL = QWEN_NONLOGIN_CONFIG["model_name"]
QWEN_NONLOGIN_BASE_URL = QWEN_NONLOGIN_CONFIG["base_url"]

# Prompt Templates (EXACTLY as in original)
BEST_ROUTE_PROMPT = QWEN_NONLOGIN_CONFIG["prompts"]["best_route"]
TRAFFIC_INFO_PROMPT = QWEN_NONLOGIN_CONFIG["prompts"]["traffic_information"]
CULINARY_PROMPT = QWEN_NONLOGIN_CONFIG["prompts"]["culinary_specialities"]
CULTURAL_PROMPT = QWEN_NONLOGIN_CONFIG["prompts"]["cultural_introduction"]
SIGHTSEEING_PROMPT = QWEN_NONLOGIN_CONFIG["prompts"]["sightseeing_tours"]

# Speech Recognition Config
SPEECH_CONFIG = config["speech_recognition"]

# Paths
MODELS_DIR = SPEECH_CONFIG["model_path"]

# Model Configurations
MAIN_MODEL = SPEECH_CONFIG["models"]["main_model"]
VAD_MODEL = SPEECH_CONFIG["models"]["vad_model"]
PUNC_MODEL = SPEECH_CONFIG["models"]["punc_model"]

# Generation Parameters
GEN_PARAMS = SPEECH_CONFIG["generation_params"]

# Text-to-Speech Config
TTS_CONFIG = config["text_to_speech"]

# Path Configuration
TTS_MODELS_DIR = TTS_CONFIG["models_dir"]

# Model Configuration
BARK_MODEL = os.path.join(TTS_MODELS_DIR, TTS_CONFIG["model_config"]["bark_model"])
VOICE_PRESET = os.path.join(TTS_MODELS_DIR, TTS_CONFIG["model_config"]["voice_preset"])

# Generation Parameters
MAX_CHUNK_LENGTH = TTS_CONFIG["generation_params"]["max_chunk_length"]
PROCESSOR_PARAMS = {
    "padding": TTS_CONFIG["generation_params"]["padding"],
    "truncation": TTS_CONFIG["generation_params"]["truncation"]
}

TASK = config["task"]
SIZE = config["size"]
CKPT_DIR = os.path.abspath(config["ckpt_dir"])
PHANTOM_CKPT = os.path.abspath(config["phantom_ckpt"])
OUTPUT_DIR = os.path.abspath(config["output_dir"])
GENERATE_PY = os.path.abspath(config["generate_py"])
PYTHON_EXECUTABLE = os.path.abspath(config["python_executable"])

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

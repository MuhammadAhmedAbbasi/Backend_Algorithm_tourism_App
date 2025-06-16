from pydantic import BaseModel
from typing import List

class CaptionRequest(BaseModel):
    """Request model for image captioning"""
    images: List[bytes]  # List of raw image bytes
    prompt: str = "Describe this image in detail"
    model: str = "llava:13b"
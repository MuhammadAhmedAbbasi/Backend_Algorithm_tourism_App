from pydantic import BaseModel
from typing import List

class ImageBeautificationRequest(BaseModel):
    """Request model for image beautification (binary payload)"""
    images: List[str]  # List of raw image bytes
from pydantic import BaseModel
from typing import List, Optional

class CaptionResponse(BaseModel):
    captions: List[str]  # List of captions
    success: bool = True
    model: Optional[str] = None  # Now it's optional

class CaptionErrorResponse(BaseModel):
    """Error response for captioning failures"""
    error: str
    details: Optional[str] = None
    success: bool = False
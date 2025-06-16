from pydantic import BaseModel
from typing import List, Optional

class ImageBeautificationResponse(BaseModel):
    enhanced_image: str  # base64 string when return_json=True
    content_type: str
    message: Optional[str] = "Image enhanced successfully"
    success: bool = True
    filename: Optional[str] = None

class BeautificationBatchResponse(BaseModel):
    images: List[ImageBeautificationResponse]

class BeautificationErrorResponse(BaseModel):
    error: str
    details: str
    success: bool = False

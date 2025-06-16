import requests
import base64
from typing import Dict, List
from Service.common.http.caption_request import CaptionRequest
from Service.common.http.caption_response import CaptionResponse, CaptionErrorResponse
from Service.config import (
    DEFAULT_MODEL,
    API_BASE_URL,
    API_TIMEOUT,
    DEFAULT_STREAM,
    ERROR_MESSAGES
)

class Caption:
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model
        self.base_url = API_BASE_URL
        self.timeout = API_TIMEOUT
    
    def invoke(self, data: Dict):
        """Main processing method - now handles multiple images sequentially"""
        try:
            request = CaptionRequest(**data)
            captions = []
            
            for image in request.images:
                payload = {
                    "model": request.model or self.model,
                    "prompt": request.prompt,
                    "stream": DEFAULT_STREAM,
                    "images": [base64.b64encode(image).decode('utf-8')]
                }
                
                response = requests.post(
                    self.base_url,
                    json=payload,
                    timeout=self.timeout
                )
                response.raise_for_status()
                
                caption = response.json().get("response", ERROR_MESSAGES["no_caption"])
                captions.append(caption)
            
            return CaptionResponse(
                captions=captions,
                model=request.model or self.model
            )
            
        except requests.exceptions.RequestException as e:
            return CaptionErrorResponse(
                error=ERROR_MESSAGES["api_failure"],
                details=str(e)
            )
        except Exception as e:
            return CaptionErrorResponse(
                error=ERROR_MESSAGES["processing_failure"],
                details=str(e)
            )

default_caption = Caption()
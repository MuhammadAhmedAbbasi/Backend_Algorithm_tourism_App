from pydantic import BaseModel
from typing import List, Dict, Any

class DescriptionRequest(BaseModel):
    destination: str
from pydantic import BaseModel

class DescriptionResponse(BaseModel):
    answer: str
    success: bool
from pydantic import BaseModel
from typing import List

class SummaryRequest(BaseModel):
    selected_route: str
    selected_food: List[str]
    selected_accommodation: str
    preparation: str
    notes: str
    emergency: str
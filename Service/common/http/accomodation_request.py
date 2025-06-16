from pydantic import BaseModel
from typing import List, Dict, Any

class AccommodationRequest(BaseModel):
    selected_route: str
    date_of_stay: str
    accommodation_type: str
    housing_type: str
    stars: int
    room_rate: int
    total_people: int
    adults: int
    elderly: int
    children: int
    children_age: List[int]
    transportation_preference: str
    
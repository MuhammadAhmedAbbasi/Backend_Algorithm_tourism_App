from pydantic import BaseModel
from typing import Dict, Any, List

class FoodRequest(BaseModel):
    selected_route: str
    date: str
    distance_range: str
    number_of_people: int
    budget: int
    meal_preferences: List[str]
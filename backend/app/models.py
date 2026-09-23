from pydantic import BaseModel, Field
from typing import List, Optional

class TravelerProfile(BaseModel):
    destination: str
    days: int = Field(ge=1, le=30)
    budget: float = Field(gt=0)
    currency: str = "USD"
    interests: List[str] = []
    dietary_preferences: List[str] = []
    avoid_crowds: bool = False
    travel_style: str = "relaxed"

class ItineraryItem(BaseModel):
    time: str
    title: str
    category: str
    duration_minutes: int
    estimated_cost: float
    indoor: bool = False
    reason: Optional[str] = None

class Itinerary(BaseModel):
    destination: str
    days: List[List[ItineraryItem]]
    total_estimated_cost: float
    assumptions: List[str] = []

class ReplanRequest(BaseModel):
    itinerary: Itinerary
    weather_condition: str
    rain_probability: int = Field(ge=0, le=100)
    current_day: int = Field(ge=1)
    remaining_budget: float = Field(ge=0)

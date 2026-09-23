from fastapi import APIRouter
from ..models import TravelerProfile, ReplanRequest
from ..services.planner import build_itinerary, replan
from ..services.tools import get_weather, get_route

router = APIRouter(prefix="/travel", tags=["travel"])

@router.post("/itinerary")
def create_itinerary(profile: TravelerProfile):
    return build_itinerary(profile)

@router.post("/replan")
def replan_itinerary(request: ReplanRequest):
    return replan(request)

@router.get("/weather")
def weather(location: str):
    return get_weather(location)

@router.get("/route")
def route(origin: str, destination: str, mode: str = "transit"):
    return get_route(origin, destination, mode)

from fastapi import APIRouter
from ..services.tools import get_weather

router = APIRouter(prefix="/travel", tags=["travel"])

@router.get("/weather")
def weather(location: str):
    return get_weather(location)

from fastapi import APIRouter, HTTPException
from ..services.weather import get_live_weather

router = APIRouter(prefix="/weather", tags=["weather"])

@router.get("")
async def weather(location: str):
    result = await get_live_weather(location)
    if not result.get("available"):
        raise HTTPException(status_code=503, detail=result)
    return result

from datetime import date
import httpx
from .elevenlabs import settings

async def get_live_weather(location: str):
    """Return live weather when a provider key is configured; otherwise fail clearly.
    This keeps demo data out of the production tool path.
    """
    if not settings.weather_api_key:
        return {
            "location": location,
            "available": False,
            "reason": "WEATHER_API_KEY is not configured",
            "date": date.today().isoformat(),
        }
    # Provider adapter will be added once the chosen weather provider is selected.
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get("https://api.openweathermap.org/data/2.5/weather", params={
            "q": location,
            "appid": settings.weather_api_key,
            "units": "metric",
        })
        response.raise_for_status()
        data = response.json()
    return {
        "location": location,
        "available": True,
        "temperature_c": data.get("main", {}).get("temp"),
        "feels_like_c": data.get("main", {}).get("feels_like"),
        "humidity": data.get("main", {}).get("humidity"),
        "condition": (data.get("weather") or [{}])[0].get("description"),
        "wind_mps": data.get("wind", {}).get("speed"),
    }

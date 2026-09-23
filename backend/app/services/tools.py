def get_weather(location: str):
    """Temporary demo adapter. Replace with a live weather provider next."""
    return {
        "location": location,
        "temperature_c": 31,
        "condition": "partly cloudy",
        "rain_probability": 20,
        "source": "demo",
    }

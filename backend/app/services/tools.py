def get_weather(location: str):
    return {"location": location, "temperature_c": 31, "condition": "partly cloudy", "rain_probability": 20}

def search_activities(location: str, interests: list[str], avoid_crowds: bool):
    return [
        {"name": "Old Dubai Cultural Walk", "price": 25, "indoor": False},
        {"name": "Dubai Museum Experience", "price": 35, "indoor": True},
        {"name": "Desert Experience", "price": 95, "indoor": False},
    ]

def search_restaurants(location: str, dietary_preferences: list[str]):
    return [{"name": "Local Emirati Kitchen", "price": 30}, {"name": "Heritage Dinner", "price": 40}]

def get_route(origin: str, destination: str, mode: str = "transit"):
    return {"origin": origin, "destination": destination, "mode": mode, "duration_minutes": 24, "estimated_cost": 4.0}

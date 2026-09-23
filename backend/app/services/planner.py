from .tools import search_activities, search_restaurants, get_weather

def build_itinerary(profile):
    weather = get_weather(profile.destination)
    activities = search_activities(profile.destination, profile.interests, profile.avoid_crowds)
    restaurants = search_restaurants(profile.destination, profile.dietary_preferences)
    day = [
        {"time":"09:00","title":activities[0]["name"],"category":"culture","duration_minutes":120,"estimated_cost":activities[0]["price"],"indoor":activities[0]["indoor"]},
        {"time":"12:00","title":restaurants[0]["name"],"category":"food","duration_minutes":90,"estimated_cost":restaurants[0]["price"],"indoor":True},
        {"time":"14:00","title":activities[1]["name"],"category":"activity","duration_minutes":150,"estimated_cost":activities[1]["price"],"indoor":activities[1]["indoor"]},
        {"time":"18:30","title":restaurants[1]["name"],"category":"food","duration_minutes":90,"estimated_cost":restaurants[1]["price"],"indoor":True},
    ]
    days = [day for _ in range(profile.days)]
    return {"destination":profile.destination,"days":days,
            "total_estimated_cost":sum(x["estimated_cost"] for x in day)*profile.days,
            "assumptions":[f"Demo weather snapshot: {weather['condition']}"]}

def replan(payload):
    itinerary = payload.itinerary.model_dump()
    if payload.rain_probability >= 60:
        for item in itinerary["days"][payload.current_day-1]:
            if item["category"] == "activity" and not item["indoor"]:
                item["title"] = "Indoor Cultural Experience"
                item["indoor"] = True
                item["estimated_cost"] = 35
                item["reason"] = "Moved because of rain forecast."
    itinerary["total_estimated_cost"] = sum(x["estimated_cost"] for d in itinerary["days"] for x in d)
    itinerary["assumptions"].append("Replanned from supplied weather conditions.")
    return itinerary

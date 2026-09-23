# Architecture
Voice -> ElevenLabs Agent -> Travel Orchestrator -> Tools -> Itinerary Engine -> User confirmation -> Action.

Core tools: weather, places, restaurants, routes, activities, itinerary creation, itinerary replanning.

Guardrails: explicit confirmation before paid actions; provider data for time-sensitive claims; secrets server-side; opt-in location; no fake bookings.

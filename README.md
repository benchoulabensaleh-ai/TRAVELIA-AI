# TRAVELIA AI — MVP
Voice-first adaptive travel agent for the ElevenLabs Future of Voice AI challenge.

MVP: personalized itinerary, weather-aware replanning, places/restaurants/routes tools, budget, and explicit booking confirmation.

## Backend
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

## Frontend
cd frontend
npm install
npm run dev

Copy `.env.example` to `.env` where needed.

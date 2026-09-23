# TRAVELIA AI

Voice-first adaptive travel agent.

## MVP architecture
Voice -> ElevenLabs Agent -> Travel Orchestrator -> Tools -> Itinerary Engine -> User confirmation -> Action.

Initial tools: weather, activities, restaurants, routes, itinerary creation, itinerary replanning.

## Local backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Local frontend
```bash
cd frontend
npm install
npm run dev
```

Never put API secrets in frontend code or commit `.env` files.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.health import router as health_router
from .routes.travel import router as travel_router

app = FastAPI(title="TRAVELIA AI API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(travel_router, prefix="/api")

@app.get("/")
def root():
    return {"name": "TRAVELIA AI", "status": "ok"}

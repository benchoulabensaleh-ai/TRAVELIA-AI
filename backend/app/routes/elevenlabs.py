from fastapi import APIRouter
from ..services.elevenlabs import elevenlabs_configured, settings

router = APIRouter(prefix="/elevenlabs", tags=["elevenlabs"])

@router.get("/status")
def status():
    return {
        "configured": elevenlabs_configured(),
        "agent_id": settings.elevenlabs_agent_id or None,
    }

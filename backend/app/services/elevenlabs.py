"""Server-side ElevenLabs integration boundary."""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    elevenlabs_api_key: str = ""
    elevenlabs_agent_id: str = ""

settings = Settings()

def elevenlabs_configured() -> bool:
    return bool(settings.elevenlabs_api_key and settings.elevenlabs_agent_id)

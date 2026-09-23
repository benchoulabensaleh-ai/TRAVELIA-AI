"""Server-side configuration for TRAVELIA integrations."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    elevenlabs_api_key: str = ""
    elevenlabs_agent_id: str = ""
    weather_api_key: str = ""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()

def elevenlabs_configured() -> bool:
    return bool(settings.elevenlabs_api_key and settings.elevenlabs_agent_id)

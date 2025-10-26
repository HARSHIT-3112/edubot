
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GATEWAY_HOST: str
    GATEWAY_PORT: int
    USER_SERVICE_URL: str
    DOCUMENT_SERVICE_URL: str
    AI_SERVICE_URL: str
    LANG_SERVICE_URL: str

    class Config:
        env_file = ".env"

# Create global settings instance
settings = Settings()

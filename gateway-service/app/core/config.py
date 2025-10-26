
from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    GATEWAY_HOST: str
    GATEWAY_PORT: int
    USER_SERVICE_URL: str
    DOCUMENT_SERVICE_URL: str
    AI_SERVICE_URL: str
    LANG_SERVICE_URL: str
    JWT_SECRET_KEY: str

    model_config = SettingsConfigDict(extra="ignore", env_file=".env")

    

   
# Create global settings instance
settings = Settings()



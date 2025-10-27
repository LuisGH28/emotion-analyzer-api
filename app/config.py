from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    ALLOWED_ORIGINS: List[str] = ["*"]   
    DETECTOR_BACKEND: str = "retinaface" 
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

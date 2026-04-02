from .database import database_settings
from .auth import auth_settings
from .llm import llm_settings
from .cv import cv_settings
from .vlm import vlm_settings

class Settings:
    db = database_settings
    auth = auth_settings
    llm = llm_settings
    cv = cv_settings
    vlm = vlm_settings

settings = Settings()
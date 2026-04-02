from pydantic import ConfigDict

class AuthSettings(ConfigDict):
    SECRET_KEY: str = "supersecret"
    ALGORITHM: str = "HS256"

auth_settings = AuthSettings()
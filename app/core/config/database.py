from pydantic import ConfigDict

class DatabaseSettings(ConfigDict):
    DATABASE_URL: str = "postgresql://user:password@db:5432/app"

    class Config:
        env_file = ".env"

database_settings = DatabaseSettings()
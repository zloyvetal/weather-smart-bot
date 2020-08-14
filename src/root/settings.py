from pydantic import BaseSettings


class Settings(BaseSettings):
    WEATHER_API_KEY: str
    BOT_TOKEN: str
    DEBUG: bool = False
    SERVICE_NAME: str = 'Weather Service'


SETTINGS = Settings(_env_file='.env')

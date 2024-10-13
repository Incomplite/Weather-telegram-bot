import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    bot_token: str = os.getenv('BOT_TOKEN')
    weather_api_key: str = os.getenv('WEATHER_API_KEY')


settings = Settings()

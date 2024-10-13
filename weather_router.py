import requests

from aiogram import Router, types

from config import settings

router = Router()


@router.message()
async def get_weather(message: types.Message):
    city = message.text.strip()
    
    url = (f"http://api.openweathermap.org/data/2.5/weather?q={city}"
           f"&appid={settings.weather_api_key}&units=metric&lang=ru")
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        weather_report = (
            f"Погода в городе {city_name}:\n"
            f"Температура: {temp}°C\n"
            f"Влажность: {humidity}%\n"
            f"Описание: {weather_desc.capitalize()}"
        )

        await message.reply(weather_report)
    else:
        await message.reply("Город не найден, попробуй еще раз.")

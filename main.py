import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import settings
from weather_router import router as weather_router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.reply("Привет! Введи название города, чтобы узнать погоду.")


async def main():
    dp.include_router(weather_router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher

from routers import router as main_router

from dotenv import load_dotenv
import os


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")

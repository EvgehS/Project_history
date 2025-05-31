import asyncio
from aiogram import Bot, Dispatcher
from Config.config import config
from handlers import handlers


async def main():
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(handlers.router)

    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

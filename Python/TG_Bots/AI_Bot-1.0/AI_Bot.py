import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(
      parse_mode=ParseMode.MARKDOWN,
    ))
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
      "👋 Привет! Я пример бота на aiogram\n"
      "Отправь мне любое сообщение, и я его повторю!"
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
      "ℹ **Доступные команды:**\n"
      "/start - начать работу\n"
      "/help - справка\n\n"
      "Просто напиши текст — и я его повторю!"
    )

# Обработчик текстовых сообщений
@dp.message()
async def echo_message(message: Message):
    await message.answer(f"Вы написал: *{message.text}*")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
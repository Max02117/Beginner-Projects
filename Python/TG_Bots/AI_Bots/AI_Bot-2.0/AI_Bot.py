import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from g4f.client import Client

# Токен бота
load_dotenv()
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
      "👋 Привет! Я GPT Bot.\n"
      "Отправь мне любое сообщение, и я на него отвечу!"
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
      "ℹ **Доступные команды:**\n"
      "/start - начать работу\n"
      "/help - справка\n\n"
      "Просто напиши сообщение — и я на него отвечу!"
    )

# Искусственный интеллект
async def send_request_gpt(content: str, message: Message):
    client = Client()
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': content}],
        web_search=False
    )
    await message.answer(response.choices[0].message.content)

# Обработчик текстовых сообщений
@dp.message()
async def message_hundler(message: Message):
    text = message.text + '(без необходимости - подробно не писать)'
    await send_request_gpt(text, message)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    
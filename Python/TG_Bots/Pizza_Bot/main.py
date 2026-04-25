import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)  # Инициализация бота
dp = Dispatcher()  # Класс отвечающий за обработку входящих сообщений

# /start
@dp.message(CommandStart())
async def start_cmd(message: Message) -> None:
    await message.answer("Это была команда start")
    
# Обработчик сообщения
@dp.message()
async def echo(message: Message) -> None:
    text = message.text
    
    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer('И тебе привет!')
    elif text in ['Пока', 'пока', 'До свидания']:
        await message.answer('И тебе пока!')
    else:
        await message.answer(message.text)

async def main() -> None:
    await dp.start_polling(bot)  # запуск polling
    
if __name__ == "__main__":    # Запуск только при прямом выполнении файла (не при импорте)
    asyncio.run(main())  # запуск асинхронной программы
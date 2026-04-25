import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton

from g4f.client import Client

# Токен бота
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(
      parse_mode=ParseMode.MARKDOWN,
    ))
dp = Dispatcher()

history = []
prompt = []

# Нейросеть
async def send_request_gpt(content: str):
    global history, prompt
    history.append({'role': 'user', 'content': content})
    messages = prompt + history
    client = Client()
    response = client.chat.completions.create(
        model='gpt-4',
        messages = messages,
        web_search=False
    )
    response_text = response.choices[0].message.content
    history.append({'role': 'assistant', 'content': response_text})
    return response_text

# Роли
async def send_waiter_request_gpt(content: str):
    global history, prompt
    history.clear()
    prompt_message = 'Ты - официант ресторана русской кухни. (без необходимости - подробно не писать)'
    prompt = [{'role': 'system', 'content': prompt_message}]
    response_text = await send_request_gpt(content)
    return response_text
    
async def send_cook_request_gpt(content: str):
    global history, prompt
    history.clear()
    prompt_message = 'Ты - повар ресторана русской кухни. Ты не принимаешь заказы, это делает официант (без необходимости - подробно не писать)'
    prompt = [{'role': 'system', 'content': prompt_message}]
    response_text = await send_request_gpt(content)
    return response_text
    
async def send_manager_request_gpt(content: str):
    global history, prompt
    history.clear()
    prompt_message = 'Ты - менеджер ресторана русской кухни. Предлагай скидки гостю на блюда или посещения (без необходимости - подробно не писать)'
    prompt = [{'role': 'system', 'content': prompt_message}]
    response_text = await send_request_gpt(content)
    return response_text

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
    
# Клавиатура
keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Официант'), KeyboardButton(text='Повар')], [KeyboardButton(text='Менеджер')]
    ],
    resize_keyboard = True,
    one_time_keyboard = False
)

# Обработчик текстовых сообщений
@dp.message()
async def message_hundler(message: Message):
    text = message.text.lower()
    if text == 'официант':
        response = await send_waiter_request_gpt('Приветствую вас')
    elif text == 'повар':
        response = await send_cook_request_gpt('Приветствую вас')
    elif text == 'менеджер':
        response = await send_manager_request_gpt('Приветствую вас')
    else:
        response = await send_request_gpt(text)
    await message.answer(response)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
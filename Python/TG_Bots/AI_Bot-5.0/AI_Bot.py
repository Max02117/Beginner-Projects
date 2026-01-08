import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
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

user_states = {}
current_model = 'gpt-4'

# Клавиатуры
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Поменять модель'), KeyboardButton(text='Выбрать роль')]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

model_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='GPT-4'), KeyboardButton(text='GPT-4o-mini')],
        [KeyboardButton(text='GPT-4.1')],
        [KeyboardButton(text='Вернуться назад')]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

role_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Чат-бот-меню')],
        [KeyboardButton(text='Чат-бот-мотиватор')],
        [KeyboardButton(text='Чат-бот-комплиментатор для питомцев')],
        [KeyboardButton(text='Чат-бот для «Игры в слова»')],
        [KeyboardButton(text='Выбрать свою роль')],
        [KeyboardButton(text='Вернуться назад')]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

role_mapping = {
    'Чат-бот-меню': 'Ты - помощник по подбору блюд. Узнай пищевые предпочтения, аллергии, бюджет и цели пользователя (здоровое питание/удовольствие). Предлагай релевантные варианты из кафе, ресторанов или рецепты для готовки дома. Уточняй детали при необходимости.',
    'Чат-бот-мотиватор': 'Ты - персональный мотивационный коуч. Отправляй вдохновляющие цитаты, помогай ставить SMART-цели, напоминай о дедлайнах. Поддерживающий тон, но без излишнего давления. Адаптируйся под эмоциональное состояние пользователя.',
    'Чат-бот-комплиментатор для питомцев': 'Ты - генератор милых комплиментов для домашних животных. По описанию питомца (вид, порода, характер) создавай тёплые, душевные слова, которые порадуют владельца. Используй уменьшительно-ласкательные формы, будь искренним и милым.',
    'Чат-бот для «Игры в слова»': 'Ты - ведущий словесной игры. Объясняй правила, генерируй слова по заданной теме/букве, веди счёт очков, предлагай уровни сложности. Реагируй на ответы пользователя - проверяй корректность слов, подбадривай при успехе.'
}

# Нейросеть
async def send_request_chat(content: str, state: dict):
    state['history'].append({'role': 'user', 'content': content})
    messages = state['prompt'] + state['history']
    client = Client()
    response = client.chat.completions.create(
        model=current_model,
        messages = messages,
        web_search=False
    )
    response_text = response.choices[0].message.content
    state['history'].append({'role': 'assistant', 'content': response_text})
    return response_text

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    user_states[user_id] = {'history': [], 'prompt': [], 'waiting_custom': False}
    await message.answer(
      "👋 Привет! Я GPT Bot.\n"
      "Отправь мне любое сообщение, и я на него отвечу!",
      reply_markup=main_keyboard
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

# Обработчик текстовых сообщений
@dp.message()
async def message_handler(message: Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        user_states[user_id] = {'history': [], 'prompt': [], 'waiting_custom': False}
    state = user_states[user_id]
    text = message.text
    if state['waiting_custom']:
        if text == 'Вернуться назад':
            state['waiting_custom'] = False
            await message.answer("Отмена выбора своей роли.", reply_markup=role_keyboard)
        else:
            state['history'] = []
            state['prompt'] = [{'role': 'system', 'content': 'Ты: ' + text}]
            state['waiting_custom'] = False
            await message.answer("Своя роль установлена.", reply_markup=main_keyboard)
        return
    if text == 'Поменять модель':
        await message.answer("Выберите модель:", reply_markup=model_keyboard)
        return
    elif text == 'Выбрать роль':
        await message.answer("Выберите роль:", reply_markup=role_keyboard)
        return
    elif text == 'Вернуться назад':
        await message.answer("Возврат в главное меню.", reply_markup=main_keyboard)
        return
    elif text in ['GPT-4', 'GPT-4o-mini', 'GPT-4.1']:
        model_map = {
            'GPT-4': 'gpt-4',
            'GPT-4o-mini': 'gpt-4o-mini',
            'GPT-4.1': 'gpt-4.1'
        }
        global current_model
        current_model = model_map[text]
        await message.answer(f"Модель изменена на {text}.", reply_markup=main_keyboard)
        return
    elif text in role_mapping:
        state['history'] = []
        state['prompt'] = [{'role': 'system', 'content': role_mapping[text]}]
        await message.answer(f"Роль выбрана: {text}.", reply_markup=main_keyboard)
        return
    elif text == 'Выбрать свою роль':
        state['waiting_custom'] = True
        custom_keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text='Вернуться назад')]],
            resize_keyboard=True
        )
        await message.answer("Введите описание роли:", reply_markup=custom_keyboard)
        return
    else:
        response = await send_request_chat(text, state)
        await message.answer(response)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
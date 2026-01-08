import asyncio
import os
import g4f

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from dotenv import load_dotenv

# Токен бота
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Функции для памяти

BOT_HISTORY = {}

# Добавление роли в тему общения
def add_new_role(user_id, theme, role):
    # Если пользователя нет в памяти - мы добавляем его
    if user_id not in BOT_HISTORY:
        BOT_HISTORY[user_id] = {}
        
    # Если темы общения нет в памяти - мы добавляем её
    if theme not in BOT_HISTORY[user_id]:
        BOT_HISTORY[user_id][theme] = {}
    # Добавляем роль в память
    BOT_HISTORY[user_id][theme]['role'] = {'role': 'system', 'content': role}
    
# Функция добавления нового сообщения
def add_messages(user_id, theme, prompt, answer_ai):
    # Если пользователя нет в памяти - мы добавляем его
    if user_id not in BOT_HISTORY:
        BOT_HISTORY[user_id] = {}
        
    # Если темы общения нет в памяти - мы добавляем её
    if theme not in BOT_HISTORY[user_id]:
        BOT_HISTORY[user_id][theme] = {}
        
    # Если в теме общения нет пока сообщений - добавляем их
    if 'messages' not in BOT_HISTORY[user_id][theme]:
        BOT_HISTORY[user_id][theme]['messages'] = []
        
    # Добавляем новое сообщение
    BOT_HISTORY[user_id][theme]['messages'].append({'role': 'user', 'content': prompt})
    BOT_HISTORY[user_id][theme]['messages'].append({'role': 'assistant', 'content': answer_ai})
    
# Получения роли диалога
def get_role(user_id, theme):
    # если нет данных - вернем False
    if user_id not in BOT_HISTORY:
        return False
    if theme not in BOT_HISTORY[user_id]:
        return False
    if 'role' not in BOT_HISTORY[user_id][theme]:
        return False
    # Иначе возвращаем роль
    return BOT_HISTORY[user_id][theme]['role']['content']

# Получение истории сообщений
def get_messages(user_id, theme):
    # если нет данных - вернем False
    if user_id not in BOT_HISTORY:
        return False
    if theme not in BOT_HISTORY[user_id]:
        return False
    if 'messages' not in BOT_HISTORY[user_id][theme]:
        return False
    # Иначе возвращаем роль
    return BOT_HISTORY[user_id][theme]['messages']

# Функции для общения с GPT
# Обычное общение
def just_get_answer(prompt):
    return g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=[{'role': 'user', 'content': prompt}])

# Общения с ролью
def just_answer_with_role(role, prompt):
    return g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=[{'role': 'system', 'content': role}, {'role': 'user', 'content': prompt}])

# Общения с использованием памяти
def answer_with_history(history, prompt):
    return g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages = history+[{'role': 'user', 'content': prompt}])

# Общение с использованием роли и памяти
def answer_with_history_and_role(role, history, prompt):
    return g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages =[{'role': 'system', 'content': role}] + history + [{'role': 'user', 'content': prompt}])

# Информация о чатах
TG_CHATS = {}

# Добавление темы общения
async def add_theme_tg(user_id, theme, message):
    TG_CHATS[user_id] = theme 
    await message.reply('Добавил тему разговора')

# Смена роли
async def change_role_tg(user_id, role, message):
    if user_id not in TG_CHATS:
        await message.answer('Вы не задали тему общения!')
        return
    add_new_role(user_id, TG_CHATS[user_id], role)
    await message.reply('Добавил роль!')
    
# Простое общение
async def send_answer_tg(message):
    if message.from_user.id not in TG_CHATS:
        await message.answer('Вы не выбрали тему общения!')
        return
    
    role = get_role(message.from_user.id, TG_CHATS[message.from_user.id])
    history = get_messages(message.from_user.id, TG_CHATS[message.from_user.id])
    answer = ''
    if not role and not history:
        answer = just_get_answer(message.text)
    elif not history:
        answer = just_answer_with_role(role, message.text)
    elif not role:
        answer = answer_with_history(history, message.text)
    else:
        answer = answer_with_history_and_role(role, history, message.text)
    add_messages(message.from_user.id, TG_CHATS[message.from_user.id], message.text, answer)
    await message.answer(answer)
    
# Функции для телеграмма
# Инициализация бота и диспетчера
tg_bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(
      parse_mode=ParseMode.MARKDOWN,
    ))
dp = Dispatcher()
    
# Обработчик команды /start
@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
      '👋 Привет! Я GPT Bot! Готов начать работать!\n'
      'Информация об командах в /help'     
    )

# Обработчик команды /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
      'ℹ **Доступные команды:**\n'
      '/start - начать общение\n'
      '/help - справка\n\n'
      'Напишите *"тема общения:" и название темы* - что выбрать тему общения.\n'
      'Напишите *"новая роль:" и название роли* - что выбрать новую роль.\n'
    )

# Отправка сообщения
@dp.message()
async def send_message_tg(message):
    text = message.text.lower()
    
    if 'тема общения:' in text:
        await add_theme_tg(message.from_user.id, text.split(':')[1], message)
    elif 'новая роль:' in text:
        await change_role_tg(message.from_user.id, text.split(':')[1], message)
    else:
        await send_answer_tg(message)

# Запуск бота
async def main():
    await dp.start_polling(tg_bot)

if __name__ == '__main__':
    asyncio.run(main())
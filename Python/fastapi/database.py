from sqlalchemy import create_engine     # Для подключения к БД
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # Для создании сессии

SQL_DB_URL = 'sqlite:///./app.db'

# Соединения с SQLite
engine = create_engine(
    SQL_DB_URL,
    connect_args={'check_same_thread': False}   # Разрешает обращаться к БД из разных потоков
    )

session_local = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
    )

Base = declarative_base(
    )     # Создает базовый класс из моделей для таблиц

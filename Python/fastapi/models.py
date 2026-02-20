from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship    # Для связей между полями
from database import Base

# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)

# Таблица постов
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))    # author_id связывается с users.id
    author = relationship('User') # ссылка на объект User
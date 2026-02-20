from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, session_local
from models import Base, User, Post
from schemas import UserCreate, PostCreate, PostResponse, User as DbUser

app = FastAPI()

Base.metadata.create_all(bind=engine)   # создаёт таблицы из моделей Base в базе данных

# Подключение к БД
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# Создание нового пользователя
@app.post('/users/', response_model=DbUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> DbUser:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

# Создание нового поста
@app.post('/posts/', response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)) -> PostResponse:
    db_user = db.query(User).filter(User.id == post.author_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_user)
    
    return db_post

# Вывод всех статей
@app.get('/posts/', response_model=list[PostResponse])
def posts(db: Session = Depends(get_db)):
    return db.query(Post).all()
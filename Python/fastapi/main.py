from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Session_local
from models import Base, User, Post
from schemas import UserCreate, PostCreate, PostResponse, UserResponse

app = FastAPI()

# Настройка CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

Base.metadata.create_all(bind=engine)   # создаёт таблицы из моделей Base в базе данных

# Подключение к БД
def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()

# Создание нового пользователя
@app.post('/users/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    db_user = User(name=user.name, age=user.age)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail='DB error')
    return db_user

# Создание нового поста
@app.post('/posts/', response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)) -> PostResponse:
    db_user = db.query(User).filter(User.id == post.author_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    try:
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail='DB error')
    
    return db_post

# Вывод всех статей
@app.get('/posts/', response_model=list[PostResponse])
def posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@app.get('/users/{user_id}', response_model=UserResponse)
def users(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user
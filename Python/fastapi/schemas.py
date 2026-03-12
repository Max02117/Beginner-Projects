from pydantic import BaseModel

# Описание структуры любого пользователя (чтобы не дублировать поля)
class UserBase(BaseModel):
    name: str
    age: int

# Клиент отправляет
class UserCreate(UserBase):
    pass

# Сервер возвращает
class UserResponse(UserBase):
    id: int
    model_config = {
        "from_attributes": True    # Разрешает Pydantic читать объект как ORM, а не только dict
    }

class PostBase(BaseModel):       
    title: str
    body: str
    author_id: int
    
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):       
    id: int
    author: UserResponse
    
    model_config = {
        "from_attributes": True
    }

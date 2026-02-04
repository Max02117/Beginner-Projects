from fastapi import FastAPI, HTTPException, Path, Query, Body
from typing import Optional, List, Dict, Annotated
from pydantic import BaseModel, Field

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

class Post(BaseModel):       
    id: int
    title: str
    body: str
    author: User
    
class PostCreate(BaseModel):
    title: str
    body: str
    author_id: int
    
class UserCreate(BaseModel):
    name: Annotated[str, Field(..., title='Имя пользователя', min_length=2, max_length=30)]
    age: Annotated[int, Field(..., title='Возраст', ge=1, le=120)]

users = [
    {'id': 1, 'name': 'John', 'age': 34},
    {'id': 2, 'name': 'Alex', 'age': 12},
    {'id': 3, 'name': 'Bob', 'age': 56}
]

posts = [
    {'id': 1, 'title': 'News 1', 'body': 'Text 1', 'author': users[1]},
    {'id': 2, 'title': 'News 2', 'body': 'Text 2', 'author': users[0]},
    {'id': 3, 'title': 'News 3', 'body': 'Text 3', 'author': users[2]}
]

@app.get('/items')
async def items() -> List[Post]:
    return [Post(**post) for post in posts]

@app.get('/items/{id}')
async def item(id: Annotated[int, Path(ge=1, title='id поста')]) -> Post:
    for post in posts: 
        if post['id'] == id:
            return Post(**post) 
    raise HTTPException(status_code=404, detail='Post not Found')

@app.post('/item/add')
async def add_item(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail='User not Found')
    
@app.post('/user/add')
async def add_user(user: Annotated[UserCreate, Body(..., example={
        'name': 'UserName',
        'ago': 20
    })]) -> User:

    new_user_id = len(posts) + 1
    new_user = {'id': new_user_id, 'name': user.name, 'age': user.age}
    users.append(new_user)
    return User(**new_user)

# для ссылок .../search?post_id=1
@app.get('/search')
async def search(post_id: Annotated[Optional[int], Query(ge=1, title='id поста')]) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return {'data': Post(**post)}
        raise HTTPException(status_code=404, detail='Post not Found')
    else:
        return {'data': None}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Annotated


class User(BaseModel):
    id: int
    name: str
    email: Annotated[str, "User's email address"]
    


users = [
    User(id=1, name="Алексей", email="alexey@example.com"),
    User(id=2, name="Мария", email="maria@example.com"),
    User(id=3, name="Иван", email="ivan@example.com"),
    User(id=4, name="Елена", email="elena@example.com"),
    User(id=5, name="Дмитрий", email="dmitry@example.com")
]
new = 0

print(list(users[new]))



example = [("id", 1), ("name", "Алексей")]

#print(example[1])
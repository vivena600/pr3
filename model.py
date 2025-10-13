from pydantic import BaseModel
from typing import List


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Прочитать следующую главу книги"
            }
        }


class Todo(BaseModel):
    id: int
    item: str


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Пример схемы 1!"},
                    {"item": "Пример схемы 2!"}
                ]
            }
        }
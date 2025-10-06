from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

class Item(BaseModel):
    item: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Пример задачи"
            }
        }
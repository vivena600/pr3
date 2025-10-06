from fastapi import APIRouter
from model import Todo
from fastapi import APIRouter, Path

todo_router = APIRouter()
todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., title="ID задачи", ge=1)
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Задача не найдена"}


from fastapi import FastAPI
from todo import todo_router

app = FastAPI(title="Todo API", description="CRUD приложение для управления"
                                            " задачами")
app.include_router(todo_router)

@app.get("/")
async def welcome() -> dict:
    return {"message": "Добро пожаловать в Todo API"}

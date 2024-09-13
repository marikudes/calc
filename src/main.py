from fastapi import FastAPI
from routers.calc.router import calc_router
from fastapi.staticfiles import StaticFiles
import os

# инициализация приложения
app = FastAPI()

# настройка статических файлов
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# подключение роутера
app.include_router(calc_router, prefix="")

# запуск: uvicorn main:app

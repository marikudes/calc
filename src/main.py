from fastapi import FastAPI
from src.routers import calc_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Dict, Any


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Dict[str, Any], None]:
    # настройка статических файлов
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir, "static")
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    # настройка шаблонов
    templates_dir = os.path.join(current_dir, "templates")
    app.state.templates = Jinja2Templates(
        directory=templates_dir
    )  # Сохранение в состояние приложения

    # подключение роутера
    app.include_router(calc_router, prefix="")

    print("start")
    yield {"state": app.state}
    print("end")


# инициализация приложения
app = FastAPI(lifespan=lifespan)

# запуск: uvicorn main:app

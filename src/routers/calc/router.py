from typing import TYPE_CHECKING

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse

if TYPE_CHECKING:
    from fastapi.templating import Jinja2Templates

from src.operation import Calc

from .schemas import Expression

# Создание роутера
router = APIRouter()


@router.get("/")
def mainpage(request: Request) -> HTMLResponse:
    # Использование шаблонов из состояния приложения
    templates: Jinja2Templates = request.app.state.templates
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/calculate")
async def calculate_expression(expression: Expression) -> JSONResponse:
    try:
        result = Calc.equal(expression.expression)
        return JSONResponse(content={"result": result})
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    except ZeroDivisionError:
        return JSONResponse(content={"error": "Деление на ноль"}, status_code=400)
    except SyntaxError:
        return JSONResponse(content={"error": "Некорректное выражение"}, status_code=400)


@router.post("/cos")
async def cos(expression: Expression) -> JSONResponse:
    try:
        result = Calc.cos(expression.expression)
        return JSONResponse(content={"result": result})
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    except ZeroDivisionError:
        return JSONResponse(content={"error": "Деление на ноль"}, status_code=400)
    except SyntaxError:
        return JSONResponse(content={"error": "Некорректное выражение"}, status_code=400)


@router.post("/sin")
async def sin(expression: Expression) -> JSONResponse:
    try:
        result = Calc.sin(expression.expression)
        return JSONResponse(content={"result": result})
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    except ZeroDivisionError:
        return JSONResponse(content={"error": "Деление на ноль"}, status_code=400)
    except SyntaxError:
        return JSONResponse(content={"error": "Некорректное выражение"}, status_code=400)


@router.post("/tan")
async def tan(expression: Expression) -> JSONResponse:
    try:
        result = Calc.tan(expression.expression)
        return JSONResponse(content={"result": result})
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
    except ZeroDivisionError:
        return JSONResponse(content={"error": "Деление на ноль"}, status_code=400)
    except SyntaxError:
        return JSONResponse(content={"error": "Некорректное выражение"}, status_code=400)

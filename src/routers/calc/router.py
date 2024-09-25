from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from .schemas import Expression
from src.operation import Calc
from fastapi.templating import Jinja2Templates

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
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)


@router.post("/cos")
async def cos(expression: Expression) -> JSONResponse:
    try:
        result = Calc.cos(expression.expression)
        return JSONResponse(content={"result": result})
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)


@router.post("/sin")
async def sin(expression: Expression) -> JSONResponse:
    try:
        result = Calc.sin(expression.expression)
        return JSONResponse(content={"result": result})
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)


@router.post("/tan")
async def tan(expression: Expression) -> JSONResponse:
    try:
        result = Calc.tan(expression.expression)
        return JSONResponse(content={"result": result})
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from schemas import Expression
from operation import Calc
from fastapi.templating import Jinja2Templates
import os

# Настройка шаблонов
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(current_dir, "../../templates")
templates = Jinja2Templates(directory=templates_dir)

# Создание роутера
calc_router = APIRouter()

@calc_router.get("/")
def mainpage(request: Request):
    return templates.TemplateResponse({"request": request}, "index.html")

@calc_router.post("/calculate")
async def calculate_expression(expression: Expression):
    try:
        result = Calc.equal(expression.expression)
        return JSONResponse(content={"result": result})
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)

@calc_router.post("/cos")
async def cos(expression: Expression):
    try:
        result = Calc.cos(expression.expression)
        return JSONResponse(content={"result": result})
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)

@calc_router.post("/sin")
async def sin(expression: Expression):
    try:
        result = Calc.sin(expression.expression)
        return JSONResponse(content={"result": result})
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)

@calc_router.post("/tan")
async def tan(expression: Expression):
    try:
        result = Calc.tan(expression.expression)
        return JSONResponse(content={"result": result})
    except Exception:
        return JSONResponse(content={"result": "Error"}, status_code=400)

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from operation import Calc
import os

# класс приложения
class Calculator_API:
    # Модель для запроса
    class Expression(BaseModel):
        expression: str

    def __init__(self):
        self.app = FastAPI()
        self.calc = Calc()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        static_dir = os.path.join(current_dir, "static")
        templates_dir = os.path.join(current_dir, "templates")
        
        #инициализация шаблонов
        self.templates = Jinja2Templates(directory=templates_dir)

        #инициализация статических файлов
        self.app.mount("/static", StaticFiles(directory=static_dir), name="static")

        #определение маршрутов
        self.app.get("/")(self.mainpage)
        self.app.post("/calculate")(self.calculate_expression)
        self.app.post("/cos")(self.cos)
        self.app.post("/sin")(self.sin)
        self.app.post("/tan")(self.tan)

    #маршрут для главной страницы
    def mainpage(self, request: Request):
        return self.templates.TemplateResponse({"request": request}, "index.html")

    #метод для вычисления значения выражения
    async def calculate_expression(self, expression: Expression):
        try:
            result = self.calc.equal(expression.expression)
            return JSONResponse(content={"result": result})
        except Exception:
            return JSONResponse(content={"result": "Error"}, status_code=400)

    #метод для вычисления cos
    async def cos(self, expression: Expression):
        try:
            result = self.calc.cos(expression.expression)
            return JSONResponse(content={"result": result})
        except Exception:
            return JSONResponse(content={"result": "Error"}, status_code=400)

    #метод для вычисления sin
    async def sin(self, expression: Expression):
        try:
            result = self.calc.sin(expression.expression)
            return JSONResponse(content={"result": result})
        except Exception:
            return JSONResponse(content={"result": "Error"}, status_code=400)

    #метод для вычисления tan
    async def tan(self, expression: Expression):
        try:
            result = self.calc.tan(expression.expression)
            return JSONResponse(content={"result": result})
        except Exception:
            return JSONResponse(content={"result": "Error"}, status_code=400)

#инициализация приложения
calculator = Calculator_API()
app = calculator.app
  
#uvicorn main:app


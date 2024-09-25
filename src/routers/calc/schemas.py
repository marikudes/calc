from pydantic import BaseModel


# Модель для запроса
class Expression(BaseModel):
    expression: str

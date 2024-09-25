import math


class Calc:
    @staticmethod
    def equal(expression: str) -> str:
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)

    @staticmethod
    def cos(expression: str) -> str:
        return str(math.cos(eval(expression)))

    @staticmethod
    def sin(expression: str) -> str:
        return str(math.sin(eval(expression)))

    @staticmethod
    def tan(expression: str) -> str:
        return str(math.tan(eval(expression)))

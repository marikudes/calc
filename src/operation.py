import math

import sympy as sp


class Calc:
    @staticmethod
    def equal(expression: str) -> str:
        result = sp.sympify(expression)
        return str(result)

    @staticmethod
    def cos(expression: str) -> str:
        expr = sp.sympify(expression)
        return str(math.cos(expr))

    @staticmethod
    def sin(expression: str) -> str:
        expr = sp.sympify(expression)
        return str(math.sin(expr))

    @staticmethod
    def tan(expression: str) -> str:
        expr = sp.sympify(expression)
        return str(math.tan(expr))

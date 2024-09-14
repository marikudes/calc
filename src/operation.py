import math

class Calc:
    @staticmethod  
    def equal(expression):
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)
    
    @staticmethod
    def cos(expression):
        return str(math.cos(eval(expression)))

    @staticmethod
    def sin(expression):
        return str(math.sin(eval(expression)))

    @staticmethod
    def tan(expression):
        return str(math.tan(eval(expression)))
import math

class Calc:  
    def equal(self, expression):
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)
    
    def cos(self, expression):
        return str(math.cos(eval(expression)))

    def sin(self, expression):
        return str(math.sin(eval(expression)))

    def tan(self, expression):
        return str(math.tan(eval(expression)))
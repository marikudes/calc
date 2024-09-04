import math

class Calc:  
    def __init__(self):
        #мат выражение
        self.expression = ""

    #функция подсчета значения выражения
    def equal(self):
        self.expression = str(eval(self.expression))

    def cos(self):
        self.expression = str(math.cos(eval(self.expression)))

    def sin(self):
        self.expression = str(math.sin(eval(self.expression)))

    def tan(self):
        self.expression = str(math.tan(eval(self.expression)))
import math
from tkinter import Label

class calc():  
    def __init__(self):
        #мат выражение
        self.expression = ""

    #функция подсчета значения выражения
    def equal(self, x):
        
        if x == "regular":
            self.expression = str(eval(self.expression))
        
        if x == "cos":
            self.expression = str(math.cos(eval(self.expression)))

        if x == "sin":
            self.expression = str(math.sin(eval(self.expression)))
        
        if x == "tan":
            self.expression = str(math.tan(eval(self.expression)))

        

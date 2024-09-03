from tkinter import *
from tkinter import messagebox as mb
import math

class calc():
    def __init__(self):
        #мат выражение
        self.expression = ""
        
        # настройки окна
        self.root = Tk()
        self.root.title('calc')
        self.root.geometry('550x700')   

        # окно с результатом
        self.result_table = Label(text=" ", borderwidth=2, relief="solid", width=50, height=10)
        self.result_table.pack(side=TOP)

        # кнопки мат операций
        action_buttons = Frame(self.root)
        action_buttons.pack(side=RIGHT)

        add_button = Button(action_buttons, text="+", height=3, width=5, command=lambda: self.set_action("+"))
        add_button.pack()

        subtraction_button = Button(action_buttons, text="-", height=3, width=5, command=lambda: self.set_action("-"))
        subtraction_button.pack()

        divide_button = Button(action_buttons, text="/", height=3, width=5, command=lambda: self.set_action("/"))
        divide_button.pack()

        integer_divide_button = Button(action_buttons, text="//", height=3, width=5, command=lambda: self.set_action("//"))
        integer_divide_button.pack()

        multiply_button = Button(action_buttons, text="*", height=3, width=5, command=lambda: self.set_action("*"))
        multiply_button.pack()

        equale_button = Button(action_buttons, text="=", height=3, width=5, command=lambda: self.equale())
        equale_button.pack()

        #доп функционал
        extended_action = Frame(self.root)
        extended_action.pack(side=RIGHT)

        cos_button = Button(extended_action, text="cos", height="3", width="5", command=lambda: self.trig("cos"))
        cos_button.pack()

        sin_button = Button(extended_action, text="sin", height="3", width="5", command=lambda: self.trig("sin"))
        sin_button.pack()

        tan_button = Button(extended_action, text="tan", height="3", width="5", command=lambda: self.trig("tan"))
        tan_button.pack()

        # кнопки с числами
        numbers_buttons = Frame(self.root)
        numbers_buttons.pack(side=LEFT)

        number1_button = Button(numbers_buttons, text='1', width=5, height=5, command=lambda: self.set_value(1))
        number1_button.grid(row=0, column=0)

        number2_button = Button(numbers_buttons, text='2', width=5, height=5, command=lambda: self.set_value(2))
        number2_button.grid(row=0, column=1)

        number3_button = Button(numbers_buttons, text='3', width=5, height=5, command=lambda: self.set_value(3))
        number3_button.grid(row=0, column=2)

        number4_button = Button(numbers_buttons, text='4', width=5, height=5, command=lambda: self.set_value(4))
        number4_button.grid(row=1, column=0)

        number5_button = Button(numbers_buttons, text='5', width=5, height=5, command=lambda: self.set_value(5))
        number5_button.grid(row=1, column=1)

        number6_button = Button(numbers_buttons, text='6', width=5, height=5, command=lambda: self.set_value(6))
        number6_button.grid(row=1, column=2)

        number7_button = Button(numbers_buttons, text='7', width=5, height=5, command=lambda: self.set_value(7))
        number7_button.grid(row=2, column=0)

        number8_button = Button(numbers_buttons, text='8', width=5, height=5, command=lambda: self.set_value(8))
        number8_button.grid(row=2, column=1)

        number9_button = Button(numbers_buttons, text='9', width=5, height=5, command=lambda: self.set_value(9))
        number9_button.grid(row=2, column=2)

        number0_button = Button(numbers_buttons, text='0', width=5, height=5, command=lambda: self.set_value(0))
        number0_button.grid(row=2, column=3) 

        # кнопка очистки
        clear_button = Button(numbers_buttons, text="C", width=5, height=5, command=lambda: self.clear())
        clear_button.grid(row=0, column=3)
    

    # функции для заполнения мат выражения   
    def set_value(self, x):
        self.expression += f"{x}"
        self.result_table.config(text=self.expression)

    def set_action(self, x):
        try: 
            if self.expression[len(self.expression) - 1].isdigit():
                self.expression += f"{x}"
                self.result_table.config(text=self.expression)
        except:
            mb.showwarning(title="", message="ле")

    #функция подсчета значения выражения
    def equale(self):
        self.expression = str(eval(self.expression))
        self.result_table.config(text=f"{(self.expression)}")

    #доп функционал    
    def trig(self, x):
        if x == "cos":
            self.expression = str(math.cos(eval(self.expression)))
            self.result_table.config(text=f"{(self.expression)}")

        if x == "sin":
            self.expression = str(math.sin(eval(self.expression)))
            self.result_table.config(text=f"{(self.expression)}")         

        if x == "tan":
            self.expression = str(math.tan(eval(self.expression)))
            self.result_table.config(text=f"{(self.expression)}")    

    #функция очистки
    def clear(self):
        self.expression = ""
        self.result_table.config(text="")

    def main(self):
        self.root.mainloop()

if __name__ == "__main__":
    calc().main()

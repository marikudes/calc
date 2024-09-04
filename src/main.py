from tkinter import *
from tkinter import messagebox as mb
from operation import Calc

class Gui:
    def __init__(self):
        self.calc = Calc()

        # настройки окна
        self.root = Tk()
        self.root.title('calc')
        self.root.geometry('550x700')   

        # окно с результатом
        self.result_table = Label(text="0", borderwidth=2, relief="solid", width=50, height=10)
        self.result_table.pack(side=TOP)

        # кнопки мат операций
        action_buttons = Frame(self.root)
        action_buttons.pack(side=RIGHT)

        for symbol in ["+", "-", "/", "//", "*", "="]:
            Button(action_buttons, text=symbol, height=3, width=5,
                command=lambda sym=symbol: self.set_action(sym) if sym != "=" else (self.equal(), self.update())).pack()

        # кнопки с доп функционал
        extended_action = Frame(self.root)
        extended_action.pack(side=RIGHT)

        for func in ["cos", "sin", "tan"]:
            Button(extended_action, text=func, height=3, width=5, 
                command=lambda f=func: (getattr(self.calc, f)(), self.update())).pack()

        # кнопки с числами
        numbers_buttons = Frame(self.root)
        numbers_buttons.pack(side=LEFT)

        numbers = [
            (1, 0, 0), (2, 0, 1), (3, 0, 2),
            (4, 1, 0), (5, 1, 1), (6, 1, 2),
            (7, 2, 0), (8, 2, 1), (9, 2, 2),
            (0, 2, 3)
        ]
        
        for num, row, col in numbers:
            Button(numbers_buttons, text=str(num), width=5, height=5, command=lambda n=num: self.set_value(n)).grid(row=row, column=col)

        # кнопка очистки
        clear_button = Button(numbers_buttons, text="C", width=5, height=5, command=lambda: self.clear())
        clear_button.grid(row=0, column=3)

    # функции для заполнения мат выражения   
    def set_value(self, x):
        self.calc.expression += f"{x}"
        self.result_table.config(text=self.calc.expression)

    def set_action(self, x):
        try: 
            if self.calc.expression[len(self.calc.expression) - 1].isdigit():
                self.calc.expression += f"{x}"
                self.result_table.config(text=self.calc.expression)
        except:
            mb.showwarning(title="", message="сначала число")

    #функция подсчета
    def equal(self):
        try:
            self.calc.equal()
        except:
            mb.showwarning(title="", message="Ошибка")
            self.calc.expression = ""
    
    def update(self):
        self.result_table.config(text=self.calc.expression) 
        
    #функция очистки
    def clear(self):
        self.calc.expression = ""
        self.result_table.config(text="")

def main():
    gui = Gui()
    gui.root.mainloop()

if __name__ == "__main__":
    main()

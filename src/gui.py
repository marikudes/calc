from collections.abc import Callable
from tkinter import LEFT, RIGHT, TOP, Button, Frame, Label, Tk
from tkinter import messagebox as mb

from sympy import SympifyError

from src.operation import Calc


class Gui:
    def __init__(self) -> None:
        self.expression: str = ""

        self.root: Tk = Tk()
        self.root.title("calc")
        self.root.geometry("550x700")

        self.result_table: Label = Label(
            text="0",
            borderwidth=2,
            relief="solid",
            width=50,
            height=10,
        )
        self.result_table.pack(side=TOP)

        action_buttons: Frame = Frame(self.root)
        action_buttons.pack(side=RIGHT)

        for symbol in ["+", "-", "/", "//", "*", "="]:
            Button(
                action_buttons,
                text=symbol,
                height=3,
                width=5,
                command=self.create_action_command(symbol),
            ).pack()

        extended_action: Frame = Frame(self.root)
        extended_action.pack(side=RIGHT)

        for func in ["cos", "sin", "tan"]:
            Button(
                extended_action,
                text=func,
                height=3,
                width=5,
                command=self.create_function_command(func),
            ).pack()

        numbers_buttons: Frame = Frame(self.root)
        numbers_buttons.pack(side=LEFT)

        numbers = [
            (1, 0, 0),
            (2, 0, 1),
            (3, 0, 2),
            (4, 1, 0),
            (5, 1, 1),
            (6, 1, 2),
            (7, 2, 0),
            (8, 2, 1),
            (9, 2, 2),
            (0, 2, 3),
        ]

        for num, row, col in numbers:
            Button(
                numbers_buttons,
                text=str(num),
                width=5,
                height=5,
                command=self.create_number_command(num),
            ).grid(row=row, column=col)

        clear_button: Button = Button(
            numbers_buttons,
            text="C",
            width=5,
            height=5,
            command=self.clear,
        )
        clear_button.grid(row=0, column=3)

    def create_action_command(self, symbol: str) -> Callable[[], None]:
        if symbol == "=":
            return self.equal
        return lambda: self.set_action(symbol)

    def create_function_command(self, func: str) -> Callable[[], None]:
        return lambda: self.set_expression(func)

    def create_number_command(self, number: int) -> Callable[[], None]:
        return lambda: self.set_value(number)

    def set_value(self, x: int) -> None:
        self.expression += f"{x}"
        self.result_table.config(text=self.expression)

    def set_action(self, x: str) -> None:
        try:
            if self.expression[-1].isdigit():
                self.expression += f"{x}"
                self.result_table.config(text=self.expression)
        except IndexError:
            mb.showwarning(title="", message="сначала число")

    def equal(self) -> None:
        try:
            self.expression = str(Calc.equal(self.expression))
        except ZeroDivisionError:
            mb.showwarning(title="", message="Деление на ноль")
            self.expression = ""
        except SympifyError:
            mb.showwarning(title="", message="Некорректное выражение")
        self.update()

    def set_expression(self, func: str) -> None:
        self.expression = getattr(Calc, func)(self.expression)
        self.update()

    def update(self) -> None:
        self.result_table.config(text=self.expression)

    def clear(self) -> None:
        self.expression = ""
        self.result_table.config(text="0")


def main() -> None:
    gui = Gui()
    gui.root.mainloop()


if __name__ == "__main__":
    main()

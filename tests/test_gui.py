from tkinter import Label, Tk
from unittest.mock import Mock, patch

import pytest

from src.gui import Gui
from src.operation import Calc


@pytest.fixture
def gui() -> Gui:
    return Gui()


def test_initialization(gui: Gui) -> None:
    assert isinstance(gui.root, Tk)
    assert isinstance(gui.result_table, Label)
    assert len(gui.root.winfo_children()) > 0


def test_set_value(gui: Gui) -> None:
    gui.set_value(5)
    assert gui.expression == "5"
    assert gui.result_table.cget("text") == "5"


def test_set_action(gui: Gui) -> None:
    gui.set_value(5)
    gui.set_action("+")
    assert gui.expression == "5+"
    assert gui.result_table.cget("text") == "5+"


def test_equal(gui: Gui) -> None:
    gui.set_value(5)
    gui.set_action("+")
    gui.set_value(3)
    gui.equal()
    gui.update()
    assert gui.result_table.cget("text") == "8"


def test_clear(gui: Gui) -> None:
    gui.set_value(5)
    gui.clear()
    assert gui.expression == ""
    assert gui.result_table.cget("text") == "0"


@patch.object(Calc, "equal", return_value="8")
def test_update(mock_calc: Mock, gui: Gui) -> None:
    gui.set_value(5)
    gui.set_action("+")
    gui.set_value(3)
    gui.update()
    assert gui.result_table.cget("text") == "5+3"
    gui.equal()
    mock_calc.assert_called_once()

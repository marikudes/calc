import math
from src.operation import Calc


def test_equal() -> None:
    assert Calc.equal("2 + 2") == "4"
    assert Calc.equal("2 - 2") == "0"
    assert Calc.equal("2 / 2") == "1"
    assert Calc.equal("7 // 3") == "2"
    assert Calc.equal("2 * 2") == "4"


def test_cos() -> None:
    assert Calc.cos("math.pi / 2") == str(math.cos(math.pi / 2))


def test_sin() -> None:
    assert Calc.sin("math.pi / 2") == str(math.sin(math.pi / 2))


def test_tan() -> None:
    assert Calc.tan("math.pi / 4") == str(math.tan(math.pi / 4))

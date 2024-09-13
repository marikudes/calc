import pytest
import math
from src.operation import Calc 

@pytest.fixture
def calc():
    return Calc()

def test_equal(calc):
    assert calc.equal("2 + 2") == "4"
    assert calc.equal("2 - 2") == "0"
    assert calc.equal("2 / 2") == "1"
    assert calc.equal("7 // 3") == "2"
    assert calc.equal("2 * 2") == "4"

def test_cos(calc):
    assert calc.cos("math.pi / 2") == str(math.cos(math.pi / 2))

def test_sin(calc):
    assert calc.sin("math.pi / 2") == str(math.sin(math.pi / 2))

def test_tan(calc):
    assert calc.tan("math.pi / 4") == str(math.tan(math.pi / 4))



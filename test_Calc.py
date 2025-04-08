from Calc import Calculator

def test_subtract():
    calc = Calculator()
    result = calc.subtract(5, 2)
    assert result == 3
# def test_multiply():
#     calc = Calculator()
#     result = calc.multiply(3, 4)
#     assert result == 12
def test_divide():
    calc = Calculator()
    result = calc.divide(10, 4)
    assert result == 2.5

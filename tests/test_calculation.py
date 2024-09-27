'''My Calculation Test'''
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_add():
    '''test addition function works'''
    calc = Calculation(2, 2, add)
    assert calc.get_result() == 4

def test_calculation_subtract():
    '''test subtraction function works'''
    calc = Calculation(2, 2, subtract)
    assert calc.get_result() == 0

def test_calculation_multiply():
    '''test multiplication function works'''
    calc = Calculation(2, 2, multiply)
    assert calc.get_result() == 4

def test_calculation_divide():
    '''test division functions works'''
    calc = Calculation(2, 2, divide)
    assert calc.get_result() == 1

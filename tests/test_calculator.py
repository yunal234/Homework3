'''My Calculator Test'''
import pytest
from calculator import Calculator

def test_add():
    '''test add'''
    calc = Calculator()
    result = calc.add(2, 2)
    assert result == 4

def test_subtract():
    '''test subtract'''
    calc = Calculator()
    result = calc.subtract(2, 2)
    assert result == 0

def test_multiply():
    '''test multiply'''
    calc = Calculator()
    result = calc.multiply(2, 2)
    assert result == 4

def test_divide():
    '''test divide'''
    calc = Calculator()
    result = calc.divide(2, 2)
    assert result == 1

def test_divide_by_zero():
    '''test division with zero gives error'''
    calc = Calculator()
    with pytest.raises(ValueError, match="Invalid"):
        calc.divide(2, 0)

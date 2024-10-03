'''This module tests for the basic operations (add, subtract, multiply, divide)'''

import pytest
from calculator.operations import add, subtract, multiply, divide


def test_add():
    '''test the add function'''
    assert add(2, 2) == 4

def test_subtract():
    '''test the subtract function'''
    assert subtract(2, 2) == 0

def test_multiply():
    '''test the multiply function'''
    assert multiply(2, 2) == 4

def test_divide():
    '''test the divide function and check for divide by zero error'''
    assert divide(2, 2) == 1
    with pytest.raises(ValueError):
        divide(2, 0)

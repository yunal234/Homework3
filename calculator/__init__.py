from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''Create the empty history list'''
    def __init__(self):
        self.history = []

    @staticmethod
    def add(a, b):
        calculation = Calculation(a, b, add)
        return calculation.get_result()

    @staticmethod
    def subtract(a, b):
        calculation = Calculation(a, b, subtract) 
        return calculation.get_result()

    @staticmethod
    def multiply(a, b):
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a, b):
        calculation = Calculation(a, b, divide)
        return calculation.get_result()

    def add_to_history(self, operation, a, b, result):
        '''Store the result in history'''
        self.history.append((operation.__name__, a, b, result))

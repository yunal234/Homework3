from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal

class Calculator:
    '''Create the empty history list'''
    def __init__(self):
        self.history = []

    @staticmethod
    def add(a, b):
        calculation = Calculation(Decimal(a), Decimal(b), add)
        return calculation.get_result()

    @staticmethod
    def subtract(a, b):
        calculation = Calculation(Decimal(a), Decimal(b), subtract) 
        return calculation.get_result()

    @staticmethod
    def multiply(a, b):
        calculation = Calculation(Decimal(a), Decimal(b), multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a, b):
        calculation = Calculation(Decimal(a), Decimal(b), divide)
        return calculation.get_result()

    def add_to_history(self, operation, a, b, result):
        '''Store the result in history'''
        self.history.append((operation.__name__, Decimal(a), Decimal(b), Decimal(result)))

    def get_history(self):
        '''Return the history of calcuations'''
        return self.history


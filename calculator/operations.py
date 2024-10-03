from decimal import Decimal

def add(a,b):
    return Decimal(a) + Decimal(b)

def subtract(a,b):
    return Decimal(a) - Decimal(b)

def multiply(a,b):
    return Decimal(a) * Decimal(b)

def divide(a,b):
    if Decimal(b) == 0:
        raise ValueError("Invalid")
    return Decimal(a) / Decimal(b)

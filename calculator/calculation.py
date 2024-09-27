class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        """Perform the operation and return the result."""
        return self.operation(self.a, self.b)


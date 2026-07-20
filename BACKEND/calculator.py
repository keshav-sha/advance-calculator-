from math import sqrt

class Calculator:

    @staticmethod
    def add(a: float, b: float):
        return a + b

    @staticmethod
    def subtract(a: float, b: float):
        return a - b

    @staticmethod
    def multiply(a: float, b: float):
        return a * b

    @staticmethod
    def divide(a: float, b: float):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    @staticmethod
    def modulus(a: float, b: float):
        return a % b

    @staticmethod
    def power(a: float, b: float):
        return a ** b

    @staticmethod
    def square(a: float):
        return a ** 2

    @staticmethod
    def cube(a: float):
        return a ** 3

    @staticmethod
    def square_root(a: float):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return sqrt(a)

    @staticmethod
    def percentage(a: float, b: float):
        if b == 0:
            raise ValueError("The second argument cannot be zero.")
        return (a / b) * 100
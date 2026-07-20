from math import sqrt
# here we are importing the sqrt function from the math module. 
# This function is used to calculate the square root of a number.

class Calculator:
# here we are defining a class named Calculator.
# This class contains static methods for performing basic arithmetic operations such as 
# addition, subtraction, multiplication, division, modulus,
# power, square, cube, square root, and percentage calculations.

    @staticmethod
    def add(a: float, b: float):
        return a + b
# here we are defining a static method named add that takes two float arguments a 
# and b, and returns their sum.

    @staticmethod
    def subtract(a: float, b: float):
        return a - b
# here we are defining a static method named subtract that takes two float arguments a
# and b, and returns the result of subtracting b from a.
    
    @staticmethod
    def multiply(a: float, b: float):
        return a * b
# here we are defining a static method named multiply that takes two float arguments a
# and b, and returns their product.

    @staticmethod
    def divide(a: float, b: float):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
# here we are defining a static method named divide that takes two float arguments a
# and b. If b is zero, it raises a ValueError with the message "Division

    @staticmethod
    def modulus(a: float, b: float):
        return a % b
# here we are defining a static method named modulus that takes two float arguments a
# and b, and returns the remainder of the division of a by b.
    
    @staticmethod
    def power(a: float, b: float):
        return a ** b
# here we are defining a static method named power that takes two float arguments a
# and b, and returns the result of raising a to the power of b.

    @staticmethod
    def square(a: float):
        return a ** 2
# here we are defining a static method named square that takes a float argument a
# and returns the result of squaring a.

    @staticmethod
    def cube(a: float):
        return a ** 3
# here we are defining a static method named cube that takes a float argument a
# and returns the result of cubing a.

    @staticmethod
    def square_root(a: float):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return sqrt(a)
# here we are defining a static method named square_root that takes a float argument a.
# If a is negative, it raises a ValueError with the message "Cannot calculate square root

    @staticmethod
    def percentage(a: float, b: float):
        if b == 0:
            raise ValueError("The second argument cannot be zero.")
        return (a / b) * 100
    # here we are defining a static method named percentage that takes two float arguments a
    # and b. If b is zero, it raises a ValueError with the message "
    
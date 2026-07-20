import math
# here we are importing the math module,
# which provides access to mathematical functions and constants.

class ScientificCalculator:
# here we are defining a class named ScientificCalculator.

    @staticmethod
    def sin(value: float):
        return math.sin(math.radians(value))
# here we are defining a static method named sin that takes a float argument value,
# converts it to radians, and returns the sine of the value.

    @staticmethod
    def cos(value: float):
        return math.cos(math.radians(value))
# here we are defining a static method named cos that takes a float argument value,
# converts it to radians, and returns the cosine of the value.

    @staticmethod
    def tan(value: float):
        return math.tan(math.radians(value))
# here we are defining a static method named tan that takes a float argument value,
# converts it to radians, and returns the tangent of the value.
    @staticmethod
    def asin(value: float):
        return math.degrees(math.asin(value))
# here we are defining a static method named asin that takes a float argument value,
# converts it to degrees, and returns the arcsine of the value.

    @staticmethod
    def acos(value: float):
        return math.degrees(math.acos(value))
# here we are defining a static method named acos that takes a float argument value,
# converts it to degrees, and returns the arccosine of the value.

    @staticmethod
    def atan(value: float):
        return math.degrees(math.atan(value))
# here we are defining a static method named atan that takes a float argument value,
# converts it to degrees, and returns the arctangent of the value.

    @staticmethod
    def log10(value: float):
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        return math.log10(value)
# here we are defining a static method named log10 that takes a float argument value.
# If the value is less than or equal to 0, 
# it raises a ValueError with the message "Value must be greater than 0".

    @staticmethod
    def ln(value: float):
        if value <= 0:
            raise ValueError("Value must be greater than 0")
        return math.log(value)
# here we are defining a static method named ln that takes a float argument value.
# If the value is less than or equal to 0,
# it raises a ValueError with the message "Value must be greater than 0".

    @staticmethod
    def exp(value: float):
        return math.exp(value)
# here we are defining a static method named exp that takes a float argument value,
# and returns the exponential of the value.

    @staticmethod
    def factorial(value: int):
        if value < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(value)
# here we are defining a static method named factorial that takes an integer argument value.
# If the value is negative,
# it raises a ValueError with the message "Factorial is not defined for negative numbers".

    @staticmethod
    def absolute(value: float):
        return abs(value)
# here we are defining a static method named absolute that takes a float argument value,
# and returns the absolute value of the value.

    @staticmethod
    def ceiling(value: float):
        return math.ceil(value)
# here we are defining a static method named ceiling that takes a float argument value, 
# and returns the smallest integer greater than or equal to the value.

    @staticmethod
    def floor(value: float):
        return math.floor(value)
# here we are defining a static method named floor that takes a float argument value,
# and returns the largest integer less than or equal to the value.

    @staticmethod
    def square(value: float):
        return value ** 2
# here we are defining a static method named square that takes a float argument value,
# and returns the result of squaring the value.

    @staticmethod
    def cube(value: float):
        return value ** 3
# here we are defining a static method named cube that takes a float argument value,
# and returns the result of cubing the value.

    @staticmethod
    def sqrt(value: float):
        if value < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(value)
# here we are defining a static method named sqrt that takes a float argument value.
# If the value is negative, it raises a ValueError with the message "Cannot calculate square

    @staticmethod
    def cbrt(value: float):
        if value >= 0:
            return value ** (1 / 3)
        return -((-value) ** (1 / 3))
# here we are defining a static method named cbrt that takes a float argument value.
# If the value is non-negative, it returns the cube root of the value.

    @staticmethod
    def pi():
        return math.pi
# here we are defining a static method named pi that returns the mathematical constant π (pi).

    @staticmethod
    def e():
        return math.e
# here we are defining a static method named e that returns the mathematical constant e (Euler's number).

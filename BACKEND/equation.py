from sympy import (
    symbols,
    Eq,
    solve,
    simplify,
    factor,
    expand,
    diff,
    integrate,
    sympify
)
# here we are importing the necessary functions and classes from the sympy library, which is a Python library for symbolic mathematics. We are importing symbols, Eq, solve, simplify, factor, expand, diff, integrate, and sympify.
# These functions and classes will be used in the EquationSolver class to perform various mathematical operations such as solving equations, simplifying expressions, factoring expressions, expanding expressions, calculating derivatives, and calculating integrals. 

x = symbols("x")
# here we are defining a symbol x using the symbols function from the sympy library. This symbol will be used as a variable in the equations and expressions that we will be working with in the EquationSolver class.

class EquationSolver:
# This class provides static methods for solving linear and quadratic equations, simplifying expressions, factoring expressions, expanding expressions, calculating derivatives, calculating integrals, and evaluating expressions.

    @staticmethod
    def solve_linear(a: float, b: float):
        equation = Eq(a * x + b, 0)
        return solve(equation, x)
# here we are defining a static method called solve_linear that takes two float parameters a and b.
# It creates a linear equation of the form ax + b = 0 using the Eq function from the sympy library, and 
# then solves the equation for x using the solve function. The method returns the solution(s) for x.
  
    @staticmethod
    def solve_quadratic(a: float, b: float, c: float):
        equation = Eq(a * x**2 + b * x + c, 0)
        return solve(equation, x)
# here we are defining a static method called solve_quadratic that takes three float parameters a, b, and c.
# It creates a quadratic equation of the form ax^2 + bx + c = 0 using the Eq function from the sympy library, and
# then solves the equation for x using the solve function. The method returns the solution(s) for x.

    @staticmethod
    def simplify_expression(expression: str):
        return str(simplify(sympify(expression)))
# here we are defining a static method called simplify_expression that takes a string parameter expression.
# It uses the sympify function from the sympy library to convert the string expression into a symbolic expression, 
# and then simplifies the expression using the simplify function.
# The method returns the simplified expression as a string.    
  
    @staticmethod
    def factor_expression(expression: str):
        return str(factor(sympify(expression)))
# here we are defining a static method called factor_expression that takes a string parameter expression.
# It uses the sympify function from the sympy library to convert the string expression into a symbolic expression,
# and then factors the expression using the factor function. The method returns the factored expression as a string.

    @staticmethod
    def expand_expression(expression: str):
        return str(expand(sympify(expression)))
# here we are defining a static method called expand_expression that takes a string parameter expression.
# It uses the sympify function from the sympy library to convert the string expression into a symbolic expression,
# and then expands the expression using the expand function. The method returns the expanded expression as a string.

    @staticmethod
    def derivative(expression: str):
        expr = sympify(expression)
        return str(diff(expr, x))
# here we are defining a static method called derivative that takes a string parameter expression.
# It uses the sympify function from the sympy library to convert the string expression into a symbolic expression,
# and then calculates the derivative of the expression with respect to x using the diff function.

    @staticmethod
    def integral(expression: str):
        expr = sympify(expression)
        return str(integrate(expr, x))
# here we are defining a static method called integral that takes a string parameter expression.
# It uses the sympify function from the sympy library to convert the string expression into
# a symbolic expression, and then calculates the indefinite integral of the expression with respect to x using the integrate function. 
# The method returns the integral as a string.

    @staticmethod
    def evaluate(expression: str):
        expr = sympify(expression)
        return float(expr.evalf())
# here we are defining a static method called evaluate that takes a string parameter expression.
# It uses the sympify function from the sympy library to convert the string expression into
# a symbolic expression, and then evaluates the expression to a floating-point number using the evalf method.
# The method returns the evaluated result as a float.   
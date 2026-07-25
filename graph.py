import numpy as np
from sympy import symbols, lambdify, sympify

x = symbols("x")


class GraphCalculator:

    @staticmethod
    def generate_graph(expression: str,
                       start: float = -10,
                       end: float = 10,
                       points: int = 200):

        expr = sympify(expression)

        function = lambdify(x, expr, "numpy")

        x_values = np.linspace(start, end, points)

        y_values = function(x_values)

        return {
            "x": x_values.tolist(),
            "y": y_values.tolist()
        }
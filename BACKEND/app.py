#==================================================================================================================================================
# IMPORTING REQUIRED MODULES
#==================================================================================================================================================
# FastAPI Imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Calculator Modules
from calculator import Calculator
from scientific import ScientificCalculator
from matrix import MatrixCalculator
from statistics import StatisticsCalculator   # or statistics_calculator if you renamed it
from finance import FinanceCalculator
from currency_converter import CurrencyConverter
from equation import EquationSolver
from graph import GraphCalculator
from history import History
from database import initialize_database

#======================================================================================================================
# CREATING AN INSTANCE OF THE FASTAPI CLASS
#======================================================================================================================
app = FastAPI(
    title="Calculator",
    version="1.0.0"
)

initialize_database()


#================================================================================================================================
# CLASSES FOR REQUEST BODIES
#===================================================================================================================================


class Numbers(BaseModel):
    a: float
    b: float
# here we are defining a data model called Numbers that inherits from BaseModel.

class Number(BaseModel):
    value: float
# here we are defining a data model called Number that inherits from BaseModel.

class MatrixInput(BaseModel):
    matrix: list[list[float]]
# here we are defining a data model called MatrixInput that inherits from BaseModel.

class TwoMatrixInput(BaseModel):
    matrix1: list[list[float]]
    matrix2: list[list[float]]
# here we are defining a data model called TwoMatrixInput that inherits from BaseModel.

class NumberList(BaseModel):
    numbers: list[float]
# here we are defining a data model called NumberList that inherits from BaseModel.

class InterestInput(BaseModel):
    principal: float
    rate: float
    time: float
# here we are defining a data model called InterestInput that inherits from BaseModel.

class EMIInput(BaseModel):
    principal: float
    annual_rate: float
    months: int
# here we are defining a data model called EMIInput that inherits from BaseModel.

class GSTInput(BaseModel):
    amount: float
    gst_percent: float
# here we are defining a data model called GSTInput that inherits from BaseModel.

class DiscountInput(BaseModel):
    price: float
    discount_percent: float
# here we are defining a data model called DiscountInput that inherits from BaseModel.

class ProfitLossInput(BaseModel):
    cost_price: float
    selling_price: float
# here we are defining a data model called ProfitLossInput that inherits from BaseModel.

class ConverterInput(BaseModel):
    value: float
# here we are defining a data model called ConverterInput that inherits from BaseModel.

class CurrencyInput(BaseModel):
    amount: float
    from_currency: str
    to_currency: str
# here we are defining a data model called CurrencyInput that inherits from BaseModel.

class LinearEquationInput(BaseModel):
    a: float
    b: float
# here we are defining a data model called LinearEquationInput that inherits from BaseModel.

class QuadraticEquationInput(BaseModel):
    a: float
    b: float
    c: float
# here we are defining a data model called QuadraticEquationInput that inherits from BaseModel.

class ExpressionInput(BaseModel):
    expression: str
# here we are defining a data model called ExpressionInput that inherits from BaseModel.

class GraphInput(BaseModel):

    expression: str

    start: float = -10

    end: float = 10

    points: int = 200
    

#================================================================================================================================================
# ROUTES FOR THE API
#================================================================================================================================================


@app.get("/")
def home():
    return {
        "message": "The Calculator is running."
    }
# here we are defining a route for the root URL ("/") of the API.

@app.post("/add")
def add(data: Numbers):

    result = Calculator.add(data.a, data.b)

    History.save(
        "Addition",
        f"{data.a}+{data.b}",
        result
    )

    return {

        "result": result

    }
# here we are defining a route for the "/add" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Numbers data model. 
# The function adds the two numbers and returns the result in a JSON response.

@app.post("/subtract")
def subtract(data: Numbers):

    result = Calculator.subtract(data.a, data.b)

    History.save(
        "Subtraction",
        f"{data.a} - {data.b}",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/subtract" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Numbers data model.
# The function subtracts the two numbers and returns the result in a JSON response.


@app.post("/multiply")
def multiply(data: Numbers):

    result = Calculator.multiply(data.a, data.b)

    History.save(
        "Multiplication",
        f"{data.a} × {data.b}",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/multiply" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Numbers data model.
# The function multiplies the two numbers and returns the result in a JSON response.

@app.post("/divide")
def divide(data: Numbers):

    try:

        result = Calculator.divide(data.a, data.b)

        History.save(
            "Division",
            f"{data.a} ÷ {data.b}",
            result
        )

        return {
            "result": result
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
# here we are defining a route for the "/divide" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Numbers data model.
# The function divides the two numbers and returns the result in a JSON response. 
# If a ValueError is raised (for example, if the second number is zero), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/multiply")
def multiply(data: Numbers):

    result = Calculator.multiply(data.a, data.b)

    History.save(
        "Multiplication",
        f"{data.a} × {data.b}",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/modulus" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Numbers data model.
# The function calculates the modulus of the two numbers and returns the result in a JSON response.

@app.post("/power")
def power(data: Numbers):

    result = Calculator.power(data.a, data.b)

    History.save(
        operation="Power",
        expression=f"{data.a}^{data.b}",
        result=result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/power" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Numbers data model. 
# The function calculates the power of the first number raised to the second number and returns the result in a JSON response.

@app.post("/square")
def square(data: Number):

    result = Calculator.square(data.value)

    History.save(
        operation="Square",
        expression=f"({data.value})²",
        result=result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/square" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model. 
# The function calculates the square of the number and returns the result in a JSON response.

@app.post("/cube")
def cube(data: Number):

    result = Calculator.cube(data.value)

    History.save(
        operation="Cube",
        expression=f"({data.value})³",
        result=result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/cube" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model. 
# The function calculates the cube of the number and returns the result in a JSON response.

@app.post("/sqrt")
def sqrt(data: Number):

    try:

        result = Calculator.square_root(data.value)

        History.save(
            "Square Root",
            f"√({data.value})",
            result
        )

        return {
            "result": result
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
# here we are defining a route for the "/sqrt" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model. 
# The function calculates the square root of the number and returns the result in a JSON response. 
# If a ValueError is raised (for example, if the number is negative), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/percentage")
def percentage(data: Numbers):

    try:

        result = Calculator.percentage(data.a, data.b)

        History.save(
            operation="Percentage",
            expression=f"({data.a}/{data.b}) × 100",
            result=result
        )

        return {
            "result": result
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
# here we are defining a route for the "/percentage" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Numbers data model.
# The function calculates the percentage of the first number with respect to the second number and returns the result in a JSON response.


# ================================================================================================================================================
# Scientific Calculator APIs
# =======================================================================================================================================================


@app.post("/scientific/sin")
def sin(data: Number):

    result = ScientificCalculator.sin(data.value)

    History.save(
        "Sin",
        f"sin({data.value})",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/scientific/sin" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model. 
# The function calculates the sine of the number and returns the result in a JSON response.

@app.post("/scientific/cos")
def cos(data: Number):

    result = ScientificCalculator.cos(data.value)

    History.save(
        "Cos",
        f"cos({data.value})",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/scientific/cos" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the cosine of the number and returns the result in a JSON response.

@app.post("/scientific/tan")
def tan(data: Number):

    result = ScientificCalculator.tan(data.value)

    History.save(
        "Tan",
        f"tan({data.value})",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/scientific/tan" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the tangent of the number and returns the result in a JSON response.

@app.post("/scientific/log")
def log(data: Number):

    try:

        result = ScientificCalculator.log10(data.value)

        History.save(
            "Log",
            f"log({data.value})",
            result
        )

        return {
            "result": result
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
# here we are defining a route for the "/scientific/log" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the base-10 logarithm of the number and returns the result in a JSON response. 
# If a ValueError is raised (for example, if the number is less than or equal to zero), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/scientific/ln")
def ln(data: Number):

    try:

        result = ScientificCalculator.ln(data.value)

        History.save(
            "Natural Log",
            f"ln({data.value})",
            result
        )

        return {
            "result": result
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
# here we are defining a route for the "/scientific/ln" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the natural logarithm of the number and returns the result in a JSON response.
# If a ValueError is raised (for example, if the number is less than or equal to zero), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/scientific/factorial")
def factorial(data: Number):

    try:

        result = ScientificCalculator.factorial(int(data.value))

        History.save(
            "Factorial",
            f"{int(data.value)}!",
            result
        )

        return {
            "result": result
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
# here we are defining a route for the "/scientific/factorial" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the factorial of the number (after converting it to an integer) and returns the result in a JSON response.
# If a ValueError is raised (for example, if the number is negative), an HTTPException is raised with a status code of 400 and the error message.

@app.get("/scientific/pi")
def pi():

    result = ScientificCalculator.pi()

    History.save(
        "Pi",
        "π",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/scientific/pi" URL of the API.
# This route accepts GET requests and does not expect any payload.
# The function returns the value of pi in a JSON response.

@app.get("/scientific/e")
def e():

    result = ScientificCalculator.e()

    History.save(
        "Euler Number",
        "e",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/scientific/e" URL of the API.
# This route accepts GET requests and does not expect any payload.
# The function returns the value of e in a JSON response.


# ==================================================================================================================================================
# Matrix Calculator APIs
# =============================================================================================================================================

@app.post("/matrix/add")
def matrix_add(data: TwoMatrixInput):

    result = MatrixCalculator.add(
        data.matrix1,
        data.matrix2
    )

    History.save(
        "Matrix Addition",
        f"{data.matrix1} + {data.matrix2}",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/matrix/add" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the TwoMatrixInput data model

@app.post("/matrix/subtract")
def matrix_subtract(data: TwoMatrixInput):

    result = MatrixCalculator.subtract(
        data.matrix1,
        data.matrix2
    )

    History.save(
        "Matrix Subtraction",
        f"{data.matrix1} - {data.matrix2}",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/matrix/subtract" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the TwoMatrixInput data model.

@app.post("/matrix/multiply")
def matrix_multiply(data: TwoMatrixInput):

    result = MatrixCalculator.multiply(
        data.matrix1,
        data.matrix2
    )

    History.save(
        "Matrix Multiplication",
        f"{data.matrix1} × {data.matrix2}",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/matrix/multiply" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the TwoMatrixInput data model.

@app.post("/matrix/transpose")
def matrix_transpose(data: MatrixInput):

    result = MatrixCalculator.transpose(data.matrix)

    History.save(
        "Matrix Transpose",
        f"transpose({data.matrix})",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/matrix/transpose" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the MatrixInput data model.

@app.post("/matrix/determinant")
def determinant(data: MatrixInput):

    result = MatrixCalculator.determinant(
        data.matrix
    )

    History.save(
        "Matrix Determinant",
        f"det({data.matrix})",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/matrix/determinant" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the MatrixInput data model.

@app.post("/matrix/inverse")
def inverse(data: MatrixInput):

    try:

        result = MatrixCalculator.inverse(data.matrix)

        History.save(
            "Matrix Inverse",
            f"inverse({data.matrix})",
            result
        )

        return {
            "result": result
        }

    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Matrix is singular and cannot be inverted."
        )
# here we are defining a route for the "/matrix/inverse" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the MatrixInput data model.

@app.post("/matrix/rank")
def rank(data: MatrixInput):

    result = MatrixCalculator.rank(
        data.matrix
    )

    History.save(
        "Matrix Rank",
        f"rank({data.matrix})",
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/matrix/rank" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the MatrixInput data model.

# ==================================================================================================================================================
# Statistics Calculator APIs
# =========================================================================================================================================

@app.post("/statistics/mean")
def mean(data: NumberList):

    result = StatisticsCalculator.mean(
        data.numbers
    )

    History.save(
        "Mean",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/mean" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.

@app.post("/statistics/median")
def median(data: NumberList):

    result = StatisticsCalculator.median(
        data.numbers
    )

    History.save(
        "Median",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/median" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.

@app.post("/statistics/mode")
def mode(data: NumberList):

    result = StatisticsCalculator.mode(
        data.numbers
    )

    History.save(
        "Mode",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/mode" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.


@app.post("/statistics/variance")
def variance(data: NumberList):

    result = StatisticsCalculator.variance(
        data.numbers
    )

    History.save(
        "Variance",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/variance" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.

@app.post("/statistics/std")
def standard_deviation(data: NumberList):

    result = StatisticsCalculator.standard_deviation(
        data.numbers
    )

    History.save(
        "Standard Deviation",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/std" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.

@app.post("/statistics/min")
def minimum(data: NumberList):

    result = StatisticsCalculator.minimum(
        data.numbers
    )

    History.save(
        "Minimum",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/min" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.

@app.post("/statistics/max")
def maximum(data: NumberList):

    result = StatisticsCalculator.maximum(
        data.numbers
    )

    History.save(
        "Maximum",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/max" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.

@app.post("/statistics/range")
def value_range(data: NumberList):

    result = StatisticsCalculator.value_range(
        data.numbers
    )

    History.save(
        "Range",
        str(data.numbers),
        result
    )

    return {
        "result": result
    }
# here we are defining a route for the "/statistics/range" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the NumberList data model.


#==================================================================================================================================================
# Financial Calculator APIs
#==================================================================================================================================================


@app.post("/finance/simple-interest")
def simple_interest(data: InterestInput):

    result = FinanceCalculator.simple_interest(
        data.principal,
        data.rate,
        data.time
    )

    History.save(
        "Simple Interest",
        f"P={data.principal}, R={data.rate}, T={data.time}",
        result
    )

    return {"result": result}
# here we are defining a route for the "/finance/simple-interest" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the InterestInput data model.

@app.post("/finance/compound-interest")
def compound_interest(data: InterestInput):

    result = FinanceCalculator.compound_interest(
        data.principal,
        data.rate,
        data.time
    )

    History.save(
        "Compound Interest",
        f"P={data.principal}, R={data.rate}, T={data.time}",
        result
    )

    return {"result": result}
# here we are defining a route for the "/finance/compound-interest" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the InterestInput data model.

@app.post("/finance/emi")
def emi(data: EMIInput):

    result = FinanceCalculator.emi(
        data.principal,
        data.annual_rate,
        data.months
    )

    History.save(
        "EMI",
        f"P={data.principal}, Rate={data.annual_rate}, Months={data.months}",
        result
    )

    return {"result": result}
# here we are defining a route for the "/finance/emi" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the EMIInput data model.

@app.post("/finance/gst")
def gst(data: GSTInput):

    result = FinanceCalculator.gst(
        data.amount,
        data.gst_percent
    )

    History.save(
        "GST",
        f"Amount={data.amount}, GST={data.gst_percent}%",
        result
    )

    return result
# here we are defining a route for the "/finance/gst" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the GSTInput data model.

@app.post("/finance/discount")
def discount(data: DiscountInput):

    result = FinanceCalculator.discount(
        data.price,
        data.discount_percent
    )

    History.save(
        "Discount",
        f"Price={data.price}, Discount={data.discount_percent}%",
        result
    )

    return result
# here we are defining a route for the "/finance/discount" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the DiscountInput data model.    

@app.post("/finance/profit-loss")
def profit_loss(data: ProfitLossInput):

    result = FinanceCalculator.profit_loss(
        data.cost_price,
        data.selling_price
    )

    History.save(
        "Profit/Loss",
        f"CP={data.cost_price}, SP={data.selling_price}",
        result
    )

    return result
# here we are defining a route for the "/finance/profit-loss" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the ProfitLossInput data model


#==================================================================================================================================================
# Unit Converter APIs
#================================================================================================================================================== 


class UnitConverter:

    # =====================================
    # Length
    # =====================================

    @staticmethod
    def meter_to_kilometer(value: float):
        return value / 1000

    @staticmethod
    def kilometer_to_meter(value: float):
        return value * 1000

    @staticmethod
    def meter_to_centimeter(value: float):
        return value * 100

    @staticmethod
    def centimeter_to_meter(value: float):
        return value / 100

    @staticmethod
    def meter_to_millimeter(value: float):
        return value * 1000

    @staticmethod
    def millimeter_to_meter(value: float):
        return value / 1000

    @staticmethod
    def kilometer_to_mile(value: float):
        return value * 0.621371

    @staticmethod
    def mile_to_kilometer(value: float):
        return value / 0.621371

    @staticmethod
    def inch_to_centimeter(value: float):
        return value * 2.54

    @staticmethod
    def centimeter_to_inch(value: float):
        return value / 2.54

    @staticmethod
    def foot_to_meter(value: float):
        return value * 0.3048

    @staticmethod
    def meter_to_foot(value: float):
        return value / 0.3048


    # =====================================
    # Weight
    # =====================================

    @staticmethod
    def kilogram_to_gram(value: float):
        return value * 1000

    @staticmethod
    def gram_to_kilogram(value: float):
        return value / 1000

    @staticmethod
    def kilogram_to_pound(value: float):
        return value * 2.20462

    @staticmethod
    def pound_to_kilogram(value: float):
        return value / 2.20462

    @staticmethod
    def gram_to_milligram(value: float):
        return value * 1000

    @staticmethod
    def milligram_to_gram(value: float):
        return value / 1000


    # =====================================
    # Temperature
    # =====================================

    @staticmethod
    def celsius_to_fahrenheit(value: float):
        return (value * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(value: float):
        return (value - 32) * 5 / 9

    @staticmethod
    def celsius_to_kelvin(value: float):
        return value + 273.15

    @staticmethod
    def kelvin_to_celsius(value: float):
        return value - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(value: float):
        return (value - 32) * 5 / 9 + 273.15

    @staticmethod
    def kelvin_to_fahrenheit(value: float):
        return (value - 273.15) * 9 / 5 + 32


    # =====================================
    # Time
    # =====================================

    @staticmethod
    def seconds_to_minutes(value: float):
        return value / 60

    @staticmethod
    def minutes_to_seconds(value: float):
        return value * 60

    @staticmethod
    def minutes_to_hours(value: float):
        return value / 60

    @staticmethod
    def hours_to_minutes(value: float):
        return value * 60

    @staticmethod
    def hours_to_days(value: float):
        return value / 24

    @staticmethod
    def days_to_hours(value: float):
        return value * 24


    # =====================================
    # Area
    # =====================================

    @staticmethod
    def square_meter_to_square_kilometer(value: float):
        return value / 1_000_000

    @staticmethod
    def square_kilometer_to_square_meter(value: float):
        return value * 1_000_000

    @staticmethod
    def hectare_to_square_meter(value: float):
        return value * 10000

    @staticmethod
    def square_meter_to_hectare(value: float):
        return value / 10000


    # =====================================
    # Volume
    # =====================================

    @staticmethod
    def liter_to_milliliter(value: float):
        return value * 1000

    @staticmethod
    def milliliter_to_liter(value: float):
        return value / 1000

    @staticmethod
    def liter_to_cubic_meter(value: float):
        return value / 1000

    @staticmethod
    def cubic_meter_to_liter(value: float):
        return value * 1000


    # =====================================
    # Speed
    # =====================================

    @staticmethod
    def kmh_to_mps(value: float):
        return value / 3.6

    @staticmethod
    def mps_to_kmh(value: float):
        return value * 3.6

    @staticmethod
    def kmh_to_mph(value: float):
        return value * 0.621371

    @staticmethod
    def mph_to_kmh(value: float):
        return value / 0.621371


    # =====================================
    # Pressure
    # =====================================

    @staticmethod
    def pascal_to_bar(value: float):
        return value / 100000

    @staticmethod
    def bar_to_pascal(value: float):
        return value * 100000


    # =====================================
    # Energy
    # =====================================

    @staticmethod
    def joule_to_calorie(value: float):
        return value / 4.184

    @staticmethod
    def calorie_to_joule(value: float):
        return value * 4.184


    # =====================================
    # Data Storage
    # =====================================

    @staticmethod
    def bit_to_byte(value: float):
        return value / 8

    @staticmethod
    def byte_to_bit(value: float):
        return value * 8

    @staticmethod
    def kb_to_mb(value: float):
        return value / 1024

    @staticmethod
    def mb_to_kb(value: float):
        return value * 1024

    @staticmethod
    def mb_to_gb(value: float):
        return value / 1024

    @staticmethod
    def gb_to_mb(value: float):
        return value * 1024

    @staticmethod
    def gb_to_tb(value: float):
        return value / 1024

    @staticmethod
    def tb_to_gb(value: float):
        return value * 1024

# =============================================================================================================================
# Currency Converter APIs
# ========================================================================================================================================

@app.post("/currency/convert")
def convert_currency(data: CurrencyInput):

    try:

        result = CurrencyConverter.convert(
            data.amount,
            data.from_currency,
            data.to_currency
        )

        History.save(
            "Currency Conversion",
            f"{data.amount} {data.from_currency} → {data.to_currency}",
            result["converted_amount"]
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
# here we are defining a route for the "/currency/convert" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the CurrencyInput data model.

@app.get("/currency/list")
def currency_list():

    return CurrencyConverter.supported_currencies()
# here we are defining a route for the "/currency/list" URL of the API.
# This route accepts GET requests and does not expect any payload.


# =====================================================================================================================
# Equation Solver APIs
# ===================================================================================================================================


@app.post("/equation/linear")
def solve_linear(data: LinearEquationInput):

    result = EquationSolver.solve_linear(
        data.a,
        data.b
    )

    History.save(
        "Linear Equation",
        f"{data.a}x + {data.b} = 0",
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/linear" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the LinearEquationInput data model

@app.post("/equation/quadratic")
def solve_quadratic(data: QuadraticEquationInput):

    result = EquationSolver.solve_quadratic(
        data.a,
        data.b,
        data.c
    )

    History.save(
        "Quadratic Equation",
        f"{data.a}x² + {data.b}x + {data.c} = 0",
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/quadratic" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the QuadraticEquationInput data

@app.post("/equation/simplify")
def simplify(data: ExpressionInput):

    result = EquationSolver.simplify_expression(
        data.expression
    )

    History.save(
        "Simplify Expression",
        data.expression,
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/simplify" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the ExpressionInput data model.

@app.post("/equation/factor")
def factor_expression(data: ExpressionInput):

    result = EquationSolver.factor_expression(
        data.expression
    )

    History.save(
        "Factor Expression",
        data.expression,
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/factor" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the ExpressionInput data model.

@app.post("/equation/expand")
def expand_expression(data: ExpressionInput):

    result = EquationSolver.expand_expression(
        data.expression
    )

    History.save(
        "Expand Expression",
        data.expression,
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/expand" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the ExpressionInput data model.

@app.post("/equation/derivative")
def derivative(data: ExpressionInput):

    result = EquationSolver.derivative(
        data.expression
    )

    History.save(
        "Derivative",
        data.expression,
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/derivative" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the ExpressionInput data model.

@app.post("/equation/integral")
def integral(data: ExpressionInput):

    result = EquationSolver.integral(
        data.expression
    )

    History.save(
        "Integral",
        data.expression,
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/integral" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the ExpressionInput data model.

@app.post("/equation/evaluate")
def evaluate(data: ExpressionInput):

    result = EquationSolver.evaluate(
        data.expression
    )

    History.save(
        "Evaluate Expression",
        data.expression,
        result
    )

    return {"result": result}
# here we are defining a route for the "/equation/evaluate" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the ExpressionInput data model.

# ====================================
# History APIs
# ====================================

@app.get("/history")
def history():

    return {

        "history": History.get_all()

    }


@app.delete("/history/{record_id}")
def delete_history(record_id: int):

    History.delete(record_id)

    return {

        "message": "History deleted."

    }


@app.delete("/history")
def clear_history():

    History.clear()

    return {

        "message": "History cleared."

    }


#==============================================================================================================================================
# graph APIS
#=====================================================================================================================================


@app.post("/graph")
def graph(data: GraphInput):

    result = GraphCalculator.generate_graph(

        data.expression,

        data.start,

        data.end,

        data.points

    )

    History.save(

        "Graph",

        data.expression,

        "Graph Generated"

    )

    return result
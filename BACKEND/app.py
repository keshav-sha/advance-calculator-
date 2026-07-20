import scientific
from matrix import MatrixCalculator

from fastapi import FastAPI, HTTPException 
# here we are importing FastAPI and HTTPException from the fastapi module.
# FastAPI is a modern web framework for building APIs with Python, and
# HTTPException is used to handle errors and return appropriate HTTP responses.\

from pydantic import BaseModel
# here we are importing BaseModel from the pydantic module.
# BaseModel is a class that allows us to define data models with type validation and serialization.

from scientific import ScientificCalculator
# here we are importing the ScientificCalculator class from the scientific module.

from calculator import Calculator
# here we are importing the Calculator class from the calculator module.

app = FastAPI(
    title="Calculator",
    version="1.0.0",
    description="Professional Calculator Backend"
)
# here we are creating an instance of the FastAPI class and assigning it to the variable app.

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

@app.get("/")
def home():
    return {
        "message": "The Calculator is running."
    }
# here we are defining a route for the root URL ("/") of the API.

@app.post("/add")
def add(data: Numbers):
    return {
        "result": Calculator.add(data.a, data.b)
    }
# here we are defining a route for the "/add" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Numbers data model. The function adds the two numbers and returns the result in a JSON response.

@app.post("/subtract")
def subtract(data: Numbers):
    return {
        "result": Calculator.subtract(data.a, data.b)
    }
# here we are defining a route for the "/subtract" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Numbers data model. The function subtracts the two numbers and returns the result in a JSON response.


@app.post("/multiply")
def multiply(data: Numbers):
    return {
        "result": Calculator.multiply(data.a, data.b)
    }
# here we are defining a route for the "/multiply" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Numbers data model. The function multiplies the two numbers and returns the result in a JSON response.

@app.post("/divide")
def divide(data: Numbers):
    try:
        return {
            "result": Calculator.divide(data.a, data.b)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
# here we are defining a route for the "/divide" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Numbers data model. The function divides the two numbers and returns the result in a JSON response. If a ValueError is raised (for example, if the second number is zero), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/modulus")
def modulus(data: Numbers):
    return {
        "result": Calculator.modulus(data.a, data.b)
    }
# here we are defining a route for the "/modulus" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Numbers data model. The function calculates the modulus of the two numbers and returns the result in a JSON response.

@app.post("/power")
def power(data: Numbers):
    return {
        "result": Calculator.power(data.a, data.b)
    }
# here we are defining a route for the "/power" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Numbers data model. The function calculates the power of the first number raised to the second number and returns the result in a JSON response.

@app.post("/square")
def square(data: Number):
    return {
        "result": Calculator.square(data.value)
    }
# here we are defining a route for the "/square" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Number data model. The function calculates the square of the number and returns the result in a JSON response.

@app.post("/cube")
def cube(data: Number):
    return {
        "result": Calculator.cube(data.value)
    }
# here we are defining a route for the "/cube" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Number data model. The function calculates the cube of the number and returns the result in a JSON response.

@app.post("/sqrt")
def square_root(data: Number):
    try:
        return {
            "result": Calculator.square_root(data.value)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
# here we are defining a route for the "/sqrt" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Number data model. The function calculates the square root of the number and returns the result in a JSON response. If a ValueError is raised (for example, if the number is negative), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/percentage")
def percentage(data: Numbers):
    return {
        "result": Calculator.percentage(data.a, data.b)
    }
# here we are defining a route for the "/percentage" URL of the API. This route accepts POST requests and expects a JSON payload that matches the Numbers data model. The function calculates the percentage of the first number with respect to the second number and returns the result in a JSON response.


# =====================================================================================
# Scientific Calculator APIs
# =====================================================================================


@app.post("/scientific/sin")
def sin(data: Number):
    return {"result": ScientificCalculator.sin(data.value)}
# here we are defining a route for the "/scientific/sin" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model. 
# The function calculates the sine of the number and returns the result in a JSON response.

@app.post("/scientific/cos")
def cos(data: Number):
    return {"result": ScientificCalculator.cos(data.value)}
# here we are defining a route for the "/scientific/cos" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the cosine of the number and returns the result in a JSON response.

@app.post("/scientific/tan")
def tan(data: Number):
    return {"result": ScientificCalculator.tan(data.value)}
# here we are defining a route for the "/scientific/tan" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the tangent of the number and returns the result in a JSON response.

@app.post("/scientific/log")
def log10(data: Number):
    try:
        return {"result": ScientificCalculator.log10(data.value)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
# here we are defining a route for the "/scientific/log" URL of the API. 
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the base-10 logarithm of the number and returns the result in a JSON response. 
# If a ValueError is raised (for example, if the number is less than or equal to zero), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/scientific/ln")
def ln(data: Number):
    try:
        return {"result": ScientificCalculator.ln(data.value)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
# here we are defining a route for the "/scientific/ln" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the natural logarithm of the number and returns the result in a JSON response.
# If a ValueError is raised (for example, if the number is less than or equal to zero), an HTTPException is raised with a status code of 400 and the error message.

@app.post("/scientific/factorial")
def factorial(data: Number):
    try:
        return {"result": ScientificCalculator.factorial(int(data.value))}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
# here we are defining a route for the "/scientific/factorial" URL of the API.
# This route accepts POST requests and expects a JSON payload that matches the Number data model.
# The function calculates the factorial of the number (after converting it to an integer) and returns the result in a JSON response.
# If a ValueError is raised (for example, if the number is negative), an HTTPException is raised with a status code of 400 and the error message.

@app.get("/scientific/pi")
def pi():
    return {"result": ScientificCalculator.pi()}
# here we are defining a route for the "/scientific/pi" URL of the API.
# This route accepts GET requests and does not expect any payload.
# The function returns the value of pi in a JSON response.

@app.get("/scientific/e")
def e():
    return {"result": ScientificCalculator.e()}
# here we are defining a route for the "/scientific/e" URL of the API.
# This route accepts GET requests and does not expect any payload.
# The function returns the value of e in a JSON response.


# ====================================
# Matrix Calculator APIs
# ====================================

@app.post("/matrix/add")
def matrix_add(data: TwoMatrixInput):
    return {
        "result": MatrixCalculator.add(
            data.matrix1,
            data.matrix2
        )
    }


@app.post("/matrix/subtract")
def matrix_subtract(data: TwoMatrixInput):
    return {
        "result": MatrixCalculator.subtract(
            data.matrix1,
            data.matrix2
        )
    }


@app.post("/matrix/multiply")
def matrix_multiply(data: TwoMatrixInput):
    return {
        "result": MatrixCalculator.multiply(
            data.matrix1,
            data.matrix2
        )
    }


@app.post("/matrix/transpose")
def matrix_transpose(data: MatrixInput):
    return {
        "result": MatrixCalculator.transpose(data.matrix)
    }


@app.post("/matrix/determinant")
def determinant(data: MatrixInput):
    return {
        "result": MatrixCalculator.determinant(data.matrix)
    }


@app.post("/matrix/inverse")
def inverse(data: MatrixInput):
    try:
        return {
            "result": MatrixCalculator.inverse(data.matrix)
        }
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Matrix is singular and cannot be inverted."
        )


@app.post("/matrix/rank")
def rank(data: MatrixInput):
    return {
        "result": MatrixCalculator.rank(data.matrix)
    }
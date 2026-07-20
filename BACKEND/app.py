from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from calculator import Calculator

app = FastAPI(
    title="Advanced Calculator API",
    version="1.0.0",
    description="Professional Calculator Backend"
)


class Numbers(BaseModel):
    a: float
    b: float


class Number(BaseModel):
    value: float


@app.get("/")
def home():
    return {
        "message": "Advanced Calculator API is running."
    }


@app.post("/add")
def add(data: Numbers):
    return {
        "result": Calculator.add(data.a, data.b)
    }


@app.post("/subtract")
def subtract(data: Numbers):
    return {
        "result": Calculator.subtract(data.a, data.b)
    }


@app.post("/multiply")
def multiply(data: Numbers):
    return {
        "result": Calculator.multiply(data.a, data.b)
    }


@app.post("/divide")
def divide(data: Numbers):
    try:
        return {
            "result": Calculator.divide(data.a, data.b)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/modulus")
def modulus(data: Numbers):
    return {
        "result": Calculator.modulus(data.a, data.b)
    }


@app.post("/power")
def power(data: Numbers):
    return {
        "result": Calculator.power(data.a, data.b)
    }


@app.post("/square")
def square(data: Number):
    return {
        "result": Calculator.square(data.value)
    }


@app.post("/cube")
def cube(data: Number):
    return {
        "result": Calculator.cube(data.value)
    }


@app.post("/sqrt")
def square_root(data: Number):
    try:
        return {
            "result": Calculator.square_root(data.value)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/percentage")
def percentage(data: Numbers):
    return {
        "result": Calculator.percentage(data.a, data.b)
    }
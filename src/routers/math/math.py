from fastapi import APIRouter
from enum import Enum

router = APIRouter(prefix="/math", tags=["math"])

class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"

@router.get("/add")
def add_nums(a:int, b:int):
    return {"result": a + b}

@router.get("/subtract")
def subtract_nums(a: int, b:int):
    return {"result": a - b}

@router.get("/calculate")
def calculate(operation: Operation, a: float, b: float):
    operations = {
        Operation.add: a + b,
        Operation.subtract: a - b,
        Operation.multiply: a * b,
        Operation.divide: a / b if b != 0 else None
    }
    return {"result": operations[operation]}
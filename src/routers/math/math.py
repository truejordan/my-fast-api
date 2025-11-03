from fastapi import APIRouter

router = APIRouter(prefix="/math", tags=["math"])

@router.get("/add")
def add_nums(a:int, b:int):
    return {"result": a + b}

@router.get("/subtract")
def subtract_nums(a: int, b:int):
    return {"result": a - b}

@router.get("/calculate")
def calculate(operation: str, a: float, b: float):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else None
    }
    result = operations.get(operation)
    if result is None:
        return {"error": "Invalid operation"}
    return {"result": result}
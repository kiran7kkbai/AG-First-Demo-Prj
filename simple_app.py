from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# 1. Simple GET Endpoint
@app.get("/api/hello")
def read_root():
    return {"message": "Hello World from FastAPI!"}

# 2. GET Endpoint with Path Parameter
@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 3. POST Endpoint with JSON Body
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str  # "add", "subtract", "multiply", "divide"

@app.post("/api/calculate")
def calculate(request: CalculationRequest):
    result = 0
    if request.operation == "add":
        result = request.num1 + request.num2
    elif request.operation == "subtract":
        result = request.num1 - request.num2
    elif request.operation == "multiply":
        result = request.num1 * request.num2
    elif request.operation == "divide":
        if request.num2 == 0:
            return {"error": "Cannot divide by zero"}
        result = request.num1 / request.num2
    else:
        return {"error": "Invalid operation"}
    
    return {"result": result, "operation": request.operation}

# Mount the static directory to serve HTML files
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

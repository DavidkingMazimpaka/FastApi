from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="This is my First Fast API Project")

@app.get("/")
def index():
    return {"Status": "Hello World"}

@app.get("/{name}/{age}")
def get_name(name, age):
    y_ob = 2024 - int(age)
    return {"name" : name, "year of birth" : y_ob}

@app.get("/{num1}/{num2}")
def get_sum(num1, num2):
    return {"sum" : int(num1) + int(num2)}

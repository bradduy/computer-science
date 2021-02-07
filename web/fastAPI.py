from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json

app = FastAPI()

class Dog(BaseModel):
    id: float
    name: str
    status: str = 'good'

@app.get("/")
async def getAll():
    return JSONResponse({"Notification": "Empty data, so pls come back later"})

@app.post("/detectDog")
async def detectDog(dog: Dog):
    return JSONResponse({str(dog.name): "is " + str(dog.status)})


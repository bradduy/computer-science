from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Dog(BaseModel):
    id: int
    name: str
    status: str = 'good'


@app.get("/")
async def getAll():
    return JSONResponse({"Notification": "Empty data, so pls come back later"})


@app.get("/getDogById/{id}")
async def getDogById(id: int):
    return JSONResponse({"Result": "You are finding the dog number " + str(id)})


@app.get("/getDogByIdOrName")
async def getADog(id: int, name: Optional[str]):
    if name == None or name == "":
        return JSONResponse({"Result": "You are finding the dog number " + str(id)})

    return JSONResponse(
        {
            "firsResult": "You are finding the dog number " + str(id),
            "secondResult": "You are finding the dog name " + str(name),
        }
    )


@app.post("/detectDog")
async def detectDog(dog: Dog):
    return JSONResponse({str(dog.name): "is " + str(dog.status)})

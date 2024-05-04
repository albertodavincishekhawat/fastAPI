#importing fastAPI
from fastapi import FastAPI

#instance of fastapi
app = FastAPI()

#path operations
@app.get("/")
async def root():
    return {"message": "Hello World"}
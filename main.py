#importing fastAPI
from fastapi import FastAPI

#instance of fastapi
app = FastAPI()

#path operations/ROUTE
@app.get("/")                  # @decorator.http_method("/url")
async def root():              #function
    return {"message": "welcome to api"}


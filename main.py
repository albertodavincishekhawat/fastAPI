#importing fastAPI
from fastapi import FastAPI

#instance of fastapi
app = FastAPI()

#path operations/ROUTE
@app.get("/")                  # @decorator.http_method("/url")
async def root():              #function
    return {"message": "welcome to api"}


#path operations/ROUTE
@app.get("/posts")                  # @decorator.http_method("/url")
async def get_post():              #function
    return {"data": "This is your post."}


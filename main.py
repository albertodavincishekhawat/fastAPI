"""
1. import fastapi, create fastapi instance then paste path operator or route
"""

from fastapi import FastAPI

# instance of fast api
app = FastAPI()     


# route or path operation (3 lines below)
@app.get("/")                           # called a decorator
def root():                             # basic python function  # async is optional if needed 
    return {"message": "Hello world"}





"""
*how to run it on server?
main.py = entry point in the application
app = fastapi instance here

#type this straight in console
*we are using 'uvicorn' library for server: 
     uvicorn main:app           i.e,  uvicorn file:fastapi instance     
"""

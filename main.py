#imports
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel




#instance of fastapi
app = FastAPI()



class Post(BaseModel):
    title: str
    content: str





#path operations/ROUTE
@app.get("/")            # @decorator.http_method("/url")
def root():              #function
    return {"message": "welcome to api"}


@app.get("/posts")              
def get_post():
    return {"data": "This is your post."}


@app.post("/createposts")              
def create_posts(new_post:Post):  # type: ignore
    print("new_post")
    return {"data":"new post"}

#title str, content str, category,Bool publish
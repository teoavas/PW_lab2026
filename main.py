from fastapi import FastAPI
app = FastAPI()

@app.get("/items/pippo")
def hello_world_pippo():
    return f"Hello World! - ENDPOINT pippo"
@app.get("/items/{item_id}")
def hello_world(item_id: str):
    return f"Hello World! item_id={item_id}"

#def hello_world(item_id:int , param1:int, param2:int=2):
#    return f"Hello World! item_id={item_id}, param1: {param1}, param2: {param2}"


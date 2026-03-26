
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montiamo la cartella static
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        name="home.html",
        request=request,
        context={"text": "Welcome to the store"}
    )

@app.get("/products", response_class=HTMLResponse)
def products(request: Request):

    products = [
        {"name": "Laptop", "price": 1000, "image": "laptop.jpg"},
        {"name": "Mouse", "price": 25, "image": "mouse.jpg"},
        {"name": "Keyboard", "price": 45, "image": "keyboard.jpg"}
    ]

    return templates.TemplateResponse(
        name="products.html",
        request=request,
        context={"products": products}
    )


'''@app.get("/{username}")
def username_webpage(
    username: str
):
    return f"Hello {username}!"


@app.get("/{username}/orders/{order_id}")
def order_webpage(
    username: str,
    order_id: int
):
    return f"Hello {username}! Your order id is {order_id}."'''



#@app.get("/items/pippo")
#def hello_world_pippo():
#    return f"Hello World! - ENDPOINT pippo"
#@app.get("/items/{item_id}")
#def hello_world(item_id: str):
#    return f"Hello World! item_id={item_id}"

#def hello_world(item_id:int , param1:int, param2:int=2):
#    return f"Hello World! item_id={item_id}, param1: {param1}, param2: {param2}"


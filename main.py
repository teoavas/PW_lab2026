from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import Field, BaseModel


class Product(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=30)]
    price: Annotated[float, Field(gt=0)]
    location: Annotated[str, Field(min_length=2)]

#product=Product(name="Notebook DELL", price=2000, location="Cagliari")
product = Product.model_validate(
    {"name":"Notebook DELL", "price":2000, "location":"Cagliari"}
)

app = FastAPI()

# Montiamo la cartella static
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

product_list = []

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
        {"name": "Laptop", "price": 1000, "location": "A1"},
        {"name": "Mouse", "price": 25, "location": "B2"},
        {"name": "Keyboard", "price": 45, "location": "C3"}
    ] + product_list

    return templates.TemplateResponse(
        name="products.html",
        request=request,
        context={"products": products}
    )

@app.get("/product_form", response_class=HTMLResponse)
def add_product(
    request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name="product_form.html"
    )

@app.post("/insert_product")
def insert_product(
    product: Annotated[Product, Form()]
):
    product_list.append(product.model_dump())
    return "Product Added Successfully"

@app.post("/insert_product_json")
def insert_product_json(
    product: Product
):
    print(product)




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


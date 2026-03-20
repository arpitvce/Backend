from fastapi import FastAP:I
from models import Product

app=FastAPI()

@app.get("/")
def greet():
    return "Welcome"

# Pydantic data validation

products=[
        Product(id=1,name="laptop",description="gaming laptop",price=999,quantity=6),Product(id=2,name="Phone",description="Mobile Phone",price=99,quantity=4)
        ]

@app.get("/products")
def gettall():
    return products

@app.get("/product/{id}")
def getid(id:int):
    for product in products:
        if product.id==id:
            return product
    return "product not found or wrong id"

@app.post("/product")
def add(product:Product):
    products.append(product)
    return product

@app.put("/product")
def update(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return products
    return "Enter correct id"

@app.delete("/product")
def deletestuff(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del(products[i])
            return products
    return "Enter a Valid ID"

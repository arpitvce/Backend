from fastapi import FastAPI
from models import Product
from database import session,engine
from sqlalchemy.orm import Session
import dbmodels

app=FastAPI()
dbmodels.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome"

# Pydantic data validation

products=[
        Product(id=1,name="laptop",description="gaming laptop",price=999,quantity=6),Product(id=2,name="Phone",description="Mobile Phone",price=99,quantity=4)
        ]
def get_db(db:Session=Depends(get_db)):
    db=session()
    try:
        yeild db
    finally:
        db.close()

def init_db():
    db=session()
    count=db.query(dbmodels.Product).count
    if count==0:
      for product in products:
        db.add(dbmodels.Product(**product.model_dump()))
      db.commit()

init_db()


@app.get("/products")
def gettall():
    #db=session()
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

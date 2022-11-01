from typing import List

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import joinedload

import sys
sys.path.append('..')

from core.models import Product, Category
from core.schemas import CategorySchema, ProductSchema
from core import Session, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online-Shop")

with Session() as session:
    category1 = Category(name="Laptops and computers")
    category2 = Category(name="Apple laptops")
    category3 = Category(name="Apple Technologies")
    category4 = Category(name="beauty and health")

    product1 = Product(name="MacBook Air (M2)")
    product2 = Product(name="Apple Watch 7")
    product3 = Product(name="HUAWEI Matebook D14")
    product4 = Product(name="Shark plush toy")

    product1.categories = [category1, category2, category3]
    product2.categories = [category3]
    product3.categories = [category1]

    session.add_all([product1, product2, product3, product4, category1, category2, category3, category4])
    session.commit()


def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "All working!"}


@app.get("/product/{id}", response_model=ProductSchema)
async def get_product(id: int, db: session = Depends(get_db)):
    db_products = db.query(Product).options(joinedload(Product.categories)). \
        where(Product.id == id).one()
    return db_products


@app.get("/products", response_model=List[ProductSchema])
async def get_products(db: session = Depends(get_db)):
    db_products = db.query(Product).options(joinedload(Product.categories)).all()
    return db_products


@app.get("/category/{id}", response_model=CategorySchema)
async def get_product(id: int, db: session = Depends(get_db)):
    db_categories = db.query(Category).options(joinedload(Category.products)). \
        where(Category.id == id).one()
    return db_categories


@app.get("/categories", response_model=List[CategorySchema])
async def get_categories(db: session = Depends(get_db)):
    db_categories = db.query(Category).options(joinedload(Category.products)).all()
    return db_categories


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8895)

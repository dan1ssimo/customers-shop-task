from fastapi import Depends, FastAPI, HTTPException
import models
from models import Product, Category, product_categories
from schemas import ProductBase, CategoryBase, CategorySchema, ProductSchema
from database import session, engine, Base
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online-Shop")

# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/product/{id}", response_model=ProductSchema)
async def get_product(id: int, db: session = Depends(get_db)):
    db_products = db.query(Product).options(joinedload(Product.categories)).\
        where(Product.product_id == id).one()
    return db_products

@app.get("/products", response_model=list[ProductSchema])
async def get_products(db: session = Depends(get_db)):
    db_products = db.query(Product).options(joinedload(Product.categories)).all()
    return db_products

@app.get("/category/{id}", response_model=CategorySchema)
async def get_product(id: int, db: session = Depends(get_db)):
    db_categories = db.query(Category).options(joinedload(Category.products)).\
        where(Catrgory.category_id == id).one()
    return db_categories

@app.get("/categories", response_model=list[CategorySchema])
async def get_categories(db: session = Depends(get_db)):
    db_categories = db.query(Category).options(joinedload(Category.products)).all()
    return db_categories


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    category1 = Category(category_name="Laptops and computers")
    category2 = Category(category_name="Apple laptops")
    category2 = Category(category_name="beauty and health")

    product1 = Product(product_name="MacBook Air (M2)")
    product2 = Product(product_name="MacBook Pro (M1) Late 2020")
    product3 = Product(product_name="Shark plush toy")

    product1.categories = [category1, category2]
    product2.categories = [category1, category2]

    session.add_all([product1, product2, product3, category1, category2])
    session.commit()
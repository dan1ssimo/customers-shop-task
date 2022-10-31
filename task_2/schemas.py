from pydantic import BaseModel

class ProductBase(BaseModel):
    product_id: int
    product_name: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    category_id: int
    category_name: str

    class Config:
        orm_mode = True


class CategorySchema(CategoryBase):
    authors: list[ProductBase]

class ProductSchema(ProductBase):
    books: list[CategoryBase]

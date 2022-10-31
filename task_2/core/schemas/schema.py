from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategorySchema(CategoryBase):
    products: List[ProductBase]


class ProductSchema(ProductBase):
    categories: List[CategoryBase]

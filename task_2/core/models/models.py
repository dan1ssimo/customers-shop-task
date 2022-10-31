from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from task_2.core.settings import Base

product_categories = Table('product_categories', Base.metadata,
                           Column('product_id', ForeignKey('products.id'), primary_key=True),
                           Column('category_id', ForeignKey('categories.id'), primary_key=True)
                           )


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    categories = relationship("Category", secondary="product_categories", back_populates='products')


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    products = relationship("Product", secondary="product_categories", back_populates='categories')

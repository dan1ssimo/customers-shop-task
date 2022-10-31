from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from database import Base

product_categories = Table('product_categories', Base.metadata,
    Column('product_id', ForeignKey('product.product_id'), primary_key=True),
    Column('category_id', ForeignKey('category.category_id'), primary_key=True)
)

class Product(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    categories = relationship("Category", secondary="product_category", back_populates='product')

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    products = relationship("Product", secondary="product_category", back_populates='category')

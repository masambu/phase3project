from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    """
    User class representing the users table in the database.

    Attributes:
        id (int): The primary key for the user.
        username (str): The username of the user.
        orders (relationship): Relationship to the Order class representing orders associated with the user.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    orders = relationship("Order", back_populates="user")

class Order(Base):
    """
    Order class representing the orders table in the database.

    Attributes:
        id (int): The primary key for the order.
        product_id (int): Foreign key referencing the product associated with the order.
        user_id (int): Foreign key referencing the user who placed the order.
        product (relationship): Relationship to the Product class representing the product associated with the order.
        user (relationship): Relationship to the User class representing the user who placed the order.
    """
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    product = relationship("Product", back_populates="orders")
    user = relationship("User", back_populates="orders")

class Product(Base):
    """
    Product class representing the products table in the database.

    Attributes:
        id (int): The primary key for the product.
        name (str): The name of the product.
        orders (relationship): Relationship to the Order class representing orders associated with the product.
    """
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    orders = relationship("Order", back_populates="product")

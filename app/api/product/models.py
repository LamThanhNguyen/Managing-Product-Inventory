from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.types import Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from utils.enums import Category
from db.base import Base
from db.session import engine

# Define the Product model (represents products in the inventory)
class Product(Base):
    """
    Represents a product in the inventory.

    Attributes:
        id (int): Primary key.
        name (str): Name of the product.
        description (str): Description of the product.
        price (float): Price of the product.
        category (Enum): Category of the product (e.g., ELECTRONICS, CLOTHING).
        image (str): Path to the product image.

    Relationships:
        - inventory: One-to-One relationship with the associated inventory item.
    """
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255))
    price = Column(Float, index=True)
    category = Column(SQLAlchemyEnum(Category), nullable=False)
    image = Column(String(255), index=True)
    
    # Add a relationship to Inventory (One-to-One relationship)
    inventory = relationship('Inventory', uselist=False, cascade='all, delete-orphan', back_populates='product')


# Try to create tables using the defined models and bind them to the engine
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    # If an exception occurs during table creation, print an error message
    print("Error creating tables:", e)
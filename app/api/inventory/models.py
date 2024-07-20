from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.types import Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from utils.enums import InventoryStatus
from sqlalchemy.sql import func
from db.base import Base
from db.session import engine

# Define the Inventory model (tracks the current state of inventory for each product)
class Inventory(Base):
    """
    Represents the inventory for a product.

    Attributes:
        id (int): Primary key.
        product_id (int): Foreign key referencing the associated product.
        quantity (int): Current quantity of the product in the inventory.
        last_updated (DateTime): Timestamp of the last update to the inventory.
        status (Enum): Status of the inventory item (e.g., IN_STOCK, OUT_OF_STOCK).

    Relationships:
        - product: One-to-One relationship with the associated product.
        - orders: One-to-Many relationship with orders made for this product.
    """
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(ForeignKey("products.id", ondelete='CASCADE'), unique=True)
    quantity = Column(Integer)
    last_updated = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    status = Column(SQLAlchemyEnum(InventoryStatus), nullable=False)

    product = relationship('Product', back_populates='inventory')
    orders = relationship('Order', back_populates='inventory')

# Try to create tables using the defined models and bind them to the engine
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    # If an exception occurs during table creation, print an error message
    print("Error creating tables:", e)
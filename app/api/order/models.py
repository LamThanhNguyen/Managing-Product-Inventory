from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.base import Base
from db.session import engine

# Define the Order model (represents orders records)
class Order(Base):
    """
    Represents a orders record.

    Attributes:
        id (int): Primary key.
        inventory_id (int): Foreign key referencing the associated inventory item.
        quantity_sold (int): Quantity of the product sold.
        order_date (DateTime): Timestamp of the order.

    Relationships:
        - inventory: Many-to-One relationship with the associated inventory item.
    """
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"))
    quantity_sold = Column(Integer)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    inventory = relationship('Inventory', back_populates='orders')

# Try to create tables using the defined models and bind them to the engine
try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    # If an exception occurs during table creation, print an error message
    print("Error creating tables:", e)
from pydantic import BaseModel
from datetime import datetime

# OrderCreate schema for creating a new order record
class OrderCreate(BaseModel):
    """
    Schema for creating a new order record.

    Attributes:
        inventory_id (int): ID of the associated inventory item.
        quantity_sold (int): Quantity of the product sold in the order record.
    """
    inventory_id: int
    quantity_sold: int

# OrderResponse schema for retrieving details of a order record
class OrderResponse(BaseModel):
    """
    Schema for getting details of a order record.

    Attributes:
        id (int): Unique identifier for the order record.
        inventory_id (int): ID of the associated inventory item.
        quantity_sold (int): Quantity of the product sold in the order record.
        order_date (datetime): Timestamp of the order record.
    """
    id: int
    inventory_id: int
    quantity_sold: int
    order_date: datetime
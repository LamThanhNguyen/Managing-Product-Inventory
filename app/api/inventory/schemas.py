from typing import List, TypeVar, Generic
from pydantic import BaseModel
from api.inventory.models import InventoryStatus
from datetime import datetime

# ----------------------------------- Inventory Schemas ----------------------------------

class CreateInventory(BaseModel):
    """
    Schema for creating a new inventory item.

    Attributes:
        product_id (int): ID of the associated product.
        quantity (int): Initial quantity of the inventory item.
        status (InventoryStatus): Status of the inventory item.
    """
    product_id: int
    quantity: int
    status: InventoryStatus

class GetInventory(BaseModel):
    """
    Schema for getting details of an inventory item.

    Attributes:
        id (int): Unique identifier for the inventory item.
        product_id (int): ID of the associated product.
        quantity (int): Current quantity of the inventory item.
        last_updated (datetime): Timestamp when the inventory item was last updated.
        status (InventoryStatus): Status of the inventory item.
    """
    id: int
    product_id: int
    quantity: int
    last_updated: datetime
    status: InventoryStatus
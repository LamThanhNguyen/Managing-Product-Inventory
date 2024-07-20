from sqlalchemy.orm import Session
from api.order.models import Order
from api.inventory.models import Inventory
from utils.enums import InventoryStatus
from api.order.schemas import OrderCreate

# ---------------------------- Orders Functions ---------------------------------------

# Function to create a new Order
def create_order(db: Session, inventory: Inventory, order: OrderCreate):
    """
    Create a new order and update the inventory.

    Args:
        db (Session): Database session.
        inventory (Inventory): Inventory item associated with the order.
        order (OrderCreate): Data for creating a new order.

    Returns:
        Order: Created order instance.
    """
    # Update inventory status
    inventory.quantity -= order.quantity_sold
    if inventory.quantity <= 2:
        inventory.status = InventoryStatus.LOW
    elif inventory.quantity == 0:
        inventory.status = InventoryStatus.OUT_OF_STOCK

    # Create and store the Order
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
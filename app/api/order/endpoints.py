from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from api.order import crud as order_crud
from api.inventory import cruds as inventory_cruds
from api.order.schemas import OrderCreate, OrderResponse

router = APIRouter()

# ------------------------ Orders Routes -----------------------------------------------------------

# Endpoint to create a order
@router.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """
    Create a new order record.

    Args:
        order (OrderCreate): Order creation data.
        db (Session): Database session.

    Returns:
        OrderResponse: Created order record.
    """
    # Fetch the corresponding inventory item
    inventory = inventory_cruds.get_inventory_by_id(db, order.inventory_id)

    # Check if the inventory exists and has enough quantity for the order
    if not inventory or inventory.quantity < order.quantity_sold:
        raise HTTPException(status_code=400, detail="Invalid order request")

    # Create the order and update inventory
    return order_crud.create_order(db=db, inventory=inventory, order=order)
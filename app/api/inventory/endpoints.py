from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from api.inventory.schemas import GetInventory
from api.inventory import cruds as inventory_cruds

router = APIRouter()

# ------------------------ Inventory Routes -----------------------------------------------------------

@router.get('/')
async def get_all_inventory(db: Session = Depends(get_db)):
    """
    Get all inventory items.

    Args:
        db (Session): Database session.

    Returns:
        List[GetInventory]: List of inventory items.
    """
    return inventory_cruds.get_all_inventory(db)

# Endpoint to get inventory level for a specific product.
@router.get('/{id}', response_model=GetInventory)
async def get_inventory(id, db: Session = Depends(get_db)):
    """
    Get inventory level for a specific product.

    Args:
        id (int): ID of the inventory to get details

    Returns:
        GetProduct: The product details.

    Raises:
        HTTException: If the inventory is not found.
    """
    inventory = inventory_cruds.get_inventory_by_id(db, id)
    if inventory is None:
        raise HTTPException(400, detail="Could not find inventory")
    return inventory
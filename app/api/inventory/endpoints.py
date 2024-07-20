from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from api.inventory import cruds as inventory_cruds

router = APIRouter()

# ------------------------ Inventory Routes -----------------------------------------------------------

@router.get("/inventory")
async def get_all_inventory(db: Session = Depends(get_db)):
    """
    Get all inventory items.

    Args:
        db (Session): Database session.

    Returns:
        List[GetInventory]: List of inventory items.
    """
    return inventory_cruds.get_all_inventory(db)
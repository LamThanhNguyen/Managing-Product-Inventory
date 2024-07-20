from sqlalchemy.orm import Session
from api.inventory import models

# Function to create a new inventory item
def create_inventory(db: Session, inventory_data):
    """
    Create a new inventory item.

    Args:
        db (Session): Database session.
        inventory_data (dict): Data for creating the inventory item.

    Returns:
        Inventory: Created inventory item.
    """
    db_inventory = models.Inventory(**inventory_data)
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

# Function to retrieve all inventory items
def get_all_inventory(db: Session):
    """
    Retrieve all inventory items.

    Args:
        db (Session): Database session.

    Returns:
        List[Inventory]: List of inventory items.
    """
    return db.query(models.Inventory).all()

# Function to retrieve an inventory item by its ID
def get_inventory_by_id(db: Session, inventory_id: int):
    """
    Retrieve an inventory item by its ID.

    Args:
        db (Session): Database session.
        inventory_id (int): ID of the inventory item.

    Returns:
        Inventory: Retrieved inventory item.
    """
    return db.query(models.Inventory).filter(models.Inventory.id == inventory_id).first()
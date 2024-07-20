from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from api.product.schemas import CreateProduct, UpdateProduct, GetProduct
from api.inventory.schemas import CreateInventory
from api.inventory.models import InventoryStatus
from api.product import cruds as product_cruds
from api.inventory import cruds as inventory_cruds

router = APIRouter()

# ------------------------------ Product Routes -------------------------------------------------------

# Endpoint to create a new product
@router.post("/", response_model=GetProduct)
async def create_product(product: CreateProduct, db: Session = Depends(get_db)):
    """
    Create a new product.

    Args:
        product (CreateProduct): Data for creating a product.
        db (Session): Database session.

    Returns:
        GetProduct: Created product.
    """
    new_product = product_cruds.create_product(db, product.model_dump())

    if new_product is None:
        raise HTTPException(400, detail="Could not create product")

    inventory = CreateInventory(
        product_id=new_product.id,
        quantity=product.quantity,
        status=InventoryStatus.AVAILABLE
    )
    new_inventory = inventory_cruds.create_inventory(db, inventory.model_dump())

    if new_inventory is None:
        raise HTTPException(400, detail="Could not create inventory")

    return new_product

@router.put("/{id}", response_model=GetProduct)
async def update_product(
    id: int,
    update_data: UpdateProduct,
    db: Session = Depends(get_db)
):
    """
    Update an entire product item.

    Args:
        id (int): ID of the product item to update.
        product_data (UpdateProduct): New data for the product item.
        db (Session): Database session.

    Returns:
        GetProduct: Updated product item.
    """

    product = product_cruds.get_product_by_id(db, id)

    if product is None:
        raise HTTPException(400, detail="Could not find product")

    # Update the entire product item with provided data
    updated_product = product_cruds.update_product(db=db, current_product=product, new_product=update_data)
    return updated_product

# Endpoint to delete a product
@router.delete("/{id}", response_model=GetProduct)
def delete_product(id, db: Session = Depends(get_db)):
    """
    Delete a product (deleting the product will also delete corresponding inventory).

    Args:
        id (int): ID of the product to be deleted.

    Returns:
        GetProduct: The deleted product details.

    Raises:
        HTTException: If the product is not deleted or found.
    """
    product = product_cruds.get_product_by_id(db, id)
    if product is None:
        raise HTTPException(400, detail="Could not find product")
    product_cruds.delete_product(db, product)
    return product

# Endpoint to get all products
@router.get("/")
async def get_all_products(
    skip: int = 0,
    limit: int = 10,
    name: Optional[str] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)):
    """
    Get all products.

    Args:
        skip (int): Number of items to skip for pagination.
        limit (int): Number of items to return for pagination.
        name (Optional[str]): Filter products by name.
        category (Optional[str]): Filter products by category.
        db (Session): Database session.

    Returns:
        List[GetProduct]: List of products.
    """
    products = product_cruds.get_all_products(db, skip, limit, name, category)
    return products

# Endpoint to get details of a specific product.
@router.get("/{id}", response_model=GetProduct)
async def get_product(id, db: Session = Depends(get_db)):
    """
    Get details of a specific product.

    Args:
        id (int): ID of the product to get details

    Returns:
        GetProduct: The product details.

    Raises:
        HTTException: If the product is not found.
    """
    product = product_cruds.get_product_by_id(db, id)
    if product is None:
        raise HTTPException(400, detail="Could not find product")
    return product
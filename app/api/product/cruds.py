from typing import Optional, List
from sqlalchemy.orm import Session
from api.product import models
from utils.enums import Category, get_enum_key_from_value

# ------------------------------ Product Functions ------------------------------------------

# Function to create a new product
def create_product(db: Session, product_data):
    """
    Create a new product.

    Args:
        db (Session): Database session.
        product_data (dict): Data for creating the product.

    Returns:
        Product: Created product.
    """
    product_data.pop('quantity')  # Remove 'quantity' from product_data
    db_product = models.Product(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, current_product: models.Product, new_product):
    """
    Update an existing product.

    Args:
        db (Session): Database session.
        current_product (Product): Current data for the product item.
        new_product (GetProduct): New data for the product item.

    Returns:
        Product: Updated product item.
    """
    # Update fields from the provided data
    current_product.name = new_product.name
    current_product.description = new_product.description
    current_product.price = new_product.price
    current_product.category = new_product.category

    # Save the changes
    db.commit()
    db.refresh(current_product)
    return current_product

# Function to delete a product
def delete_product(db: Session, product: models.Product):
    """
    Delete a product.

    Args:
        db (Session): Database session.
        product (Product): Product to be deleted.

    Returns:
        dict: Result of the deletion.
    """
    db.delete(product)
    db.commit()
    return {"ok": True}

# Function to retrieve all products
def get_all_products(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        name: Optional[str] = None,
        category: Optional[str] = None
    ) -> List[models.Product]:
    """
    Get all products with optional pagination and filtering.

    Args:
        db (Session): Database session.
        skip (int): Number of items to skip for pagination.
        limit (int): Number of items to return for pagination.
        name (Optional[str]): Filter products by name.
        category (Optional[str]): Filter products by category.

    Returns:
        List[Product]: List of all products.
    """

    query = db.query(models.Product)

    if name:
        query = query.filter(models.Product.name.ilike(f"%{name}%"))
    
    if category:
        category_key = get_enum_key_from_value(Category, category)
        if category_key:
            category_filter = category_key
        else:
            category_filter = category
        query = query.filter(models.Product.category == category_filter)

    return query.offset(skip).limit(limit).all()

# Function to retrieve a product by its ID
def get_product_by_id(db: Session, product_id: int):
    """
    Get a product by its ID.

    Args:
        db (Session): Database session.
        product_id (int): ID of the product.

    Returns:
        Product: Retrieved product.
    """
    return db.query(models.Product).filter(models.Product.id == product_id).first()
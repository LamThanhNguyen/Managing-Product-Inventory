from pydantic import BaseModel
from api.product.models import Category
from typing import Optional

# -------------------------- Product Schemas --------------------------------

class CreateProduct(BaseModel):
    """
    Schema for creating a new product.

    Attributes:
        name (str): Name of the product.
        description (str, optional): Description of the product (default is an empty string).
        price (float): Price of the product.
        quantity (int): Initial quantity of the product in inventory.
        category (Category): Category of the product.
        image (Optional[str]): Image URL or file path of the product (optional).
    """
    name: str
    description: str = ""
    price: float
    quantity: int
    category: Category

class UpdateProduct(BaseModel):
    """
    Schema for updating an existing product.

    Attributes:
        name (str): Name of the product.
        description (str, optional): Description of the product (default is an empty string).
        price (float): Price of the product.
        category (Category): Category of the product.
    """
    name: str
    description: str = ""
    price: float
    category: Category

class GetProduct(BaseModel):
    """
    Schema for getting details of a product.

    Attributes:
        id (int): Unique identifier for the product.
        name (str): Name of the product.
        description (str, optional): Description of the product (default is an empty string).
        price (float): Price of the product.
        quantity (int): Current quantity of the product in inventory.
        category (Category): Category of the product.
        image (Optional[str]): Image URL or file path of the product (optional).
    """
    id: int
    name: str
    description: str = ""
    price: float
    category: Category
    image: Optional[str] = None
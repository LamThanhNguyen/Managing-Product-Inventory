from enum import Enum

# Define an enumeration for product categories
class Category(Enum):
    """
    Enumeration representing product categories.

    Categories:
        - SMART_PHONES: Smart Phones category.
        - LAPTOPS: Laptops category.
        - IPHONES: iPhones category.
    """
    SMART_PHONES = "Smart Phones"
    LAPTOPS = "Laptops"
    IPHONES = "iPhones"


# Define an enumeration for inventory statuses
class InventoryStatus(Enum):
    """
    Enumeration representing inventory statuses.

    Statuses:
        - AVAILABLE: Product is available in the inventory.
        - OUT_OF_STOCK: Product is out of stock.
        - IN_TRANSIT: Product is in transit.
        - DAMAGED: Product is damaged.
        - RESERVED: Product is reserved for a specific purpose.
        - DISCONTINUED: Product is discontinued.
        - LOW: Low quantity of the product in inventory.
    """
    AVAILABLE = "Available"
    OUT_OF_STOCK = "Out of Stock"
    IN_TRANSIT = "In Transit"
    DAMAGED = "Damaged"
    RESERVED = "Reserved"
    DISCONTINUED = "Discontinued"
    LOW = "Low"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from api.product.models import Product
from api.inventory.models import Inventory
from api.order.models import Order
from decouple import config
import random
from utils.enums import Category, InventoryStatus  # Import the enums

DATABASE_URL = config("DATABASE_URL")

# Create the engine
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = Session()

# Sample data for populating the tables
def generate_random_status():
    return random.choice(list(InventoryStatus))

# Populate the product table
for i in range(1, 31):
    db_product = Product(
        name=f"Product {i}",
        description=f"Description {i}",
        price=random.uniform(10.0, 100.0),
        category=random.choice(list(Category)),  # Use the Category enum
        image=f"image_{i}.jpg",
    )
    db.add(db_product)

# Commit the changes to the database
db.commit()

# Populate the Inventory table
for i in range(1, 31):
    # Ensure that the product_id exists in the products table
    product_record = db.query(Product).filter(Product.id == i).first()
    
    if product_record:
        # Check if a record with the same product_id already exists in the inventory table
        existing_inventory = db.query(Inventory).filter(Inventory.product_id == i).first()

        if not existing_inventory:
            # If not, create a new record
            db_inventory = Inventory(product_id=i, quantity=random.randint(1, 100), status=generate_random_status())
            db.add(db_inventory)
        else:
            # If a record already exists, you can either update it or skip it, depending on your logic
            pass

# Commit the changes to the database
db.commit()

# Populate the Order table
for i in range(1, 31):
    # Get the corresponding Inventory record
    inventory_record = db.query(Inventory).filter(Inventory.product_id == i).first()

    if inventory_record:
        # Check if the quantity is greater than 1 before generating a random quantity_sold
        if inventory_record.quantity > 1:
            quantity_sold = random.randint(1, inventory_record.quantity)
        else:
            quantity_sold = 1

        db_order = Order(
            inventory_id=inventory_record.id,
            quantity_sold=quantity_sold,
        )
        db.add(db_order)

# Commit the changes to the database
db.commit()

# Close the session
db.close()
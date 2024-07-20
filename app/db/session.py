from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

# Load the database URL from the environment file
DATABASE_URL = config("DATABASE_URL")

try:
    # Attempt to create the database engine
    engine = create_engine(DATABASE_URL)
    
    # Attempt to create a session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    # Handle the exception (print a warning, log it, etc.)
    print(f"Warning: Unable to connect to the database. {e}")
    
    # Set SessionLocal to None to indicate that the database connection is not available
    SessionLocal = None

# Use SessionLocal as needed in your application

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
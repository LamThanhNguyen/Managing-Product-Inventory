# E-Commerce Inventory API
This project showcases the backend of a product inventory management system built using FastAPI as the framework and MySQL as the database, followed by a Layered Architecture.

## 📑 Table of Contents
- [Project Overview and Features](#project-overview-and-features)
- [Setup Instructions](#setup-instructions)
- [Dependencies](#dependencies)
- [Database](#database)
- [API Endpoints](#api-endpoints)
- [Examples Using](#examples-using)
- [Conclusion](#conclusion)

## Project Overview and Features
This repository contains a robust backend API for managing a product inventory.
This API will be designed to be easily integrated with any future front-end application. 
The API is designed to power a web admin dashboard for e-commerce managers, providing detailed insights into inventory status and allowing the registration of new products.

## Setup Instructions

To run the API using Docker Compose, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/LamThanhNguyen/Managing-Product-Inventory.git
   cd Managing-Product-Inventory
   ```

2. **Create Environment File:**

   Create a `.env` file in the root directory and define the required environment variables. For example:

   ```plaintext
   DATABASE_URL=mysql+mysqlconnector://admin_x:letdoit123@mysql/managing_product_inventory
   MYSQL_DATABASE=managing_product_inventory
   MYSQL_USER=admin_x
   MYSQL_PASSWORD=letdoit123
   MYSQL_ROOT_PASSWORD=root_secure_345@
   ENVIRONMENT=development
   ```

   Update the values based on your database setup.

3. **Build and Run with Docker Compose:**

   ```bash
   docker-compose up --build -d
   ```

   This command will build the Docker images and start the containers in detached mode.

4. **Optional: Initialize Database:**

   If you want to fill the database with test entries, run the `init_database.py` script inside the `app` folder.

   ```bash
   docker exec -it managing-product-inventory-webapp-1 python init_database.py
   ```

## Dependencies

The API uses the following libraries and frameworks:

- **FastAPI:** A modern, fast (high-performance), web framework for building APIs with Python.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **MySQL Connector/Python:** A MySQL database connector for Python.
- **Pydantic:** A data validation and settings management library using Python type hints.
- **Uvicorn:** An ASGI server implementation for running FastAPI applications.

## Database

The database includes the following tables:

- **products:** Represents products in the inventory.
- **inventory:** Tracks the current state of inventory for each product.
- **orders:** Records orders transactions.

The relationships between these tables are defined using foreign keys and are crucial for maintaining data integrity.

## API Endpoints
![Swagger API Documentation](swagger_api_documentation.png)

### The link to Swagger API documentation:
   * ### http://localhost:8000/docs

The API provides the following endpoints:

- **Product Endpoints:**
  - `GET /products`:  Get a list of all products with pagination and filtering(name, category) options.
  - `GET /products/{id}`: Get details of a specific product.
  - `POST /products`: Create a new product.
  - `PUT /products/{id}`: Update an existing product.
  - `DELETE /products/{id}`: Delete a product.

- **Inventory Endpoints:**
  - `GET /inventory`: Get inventory levels for all products.
  - `GET /inventory/{id}`: Get inventory level for a specific product.

- **Order Endpoints:**
  - `POST /orders/`:  Create a new order (updating inventory).

## Examples Using
- **Get a list of all products with pagination and filtering by name and category.**
![list of all products](usage_images/get_list_product.png)
- **Get details of a specific product.**
![details of a specific product](usage_images/get_detail_a_product.png)
- **Create a new product.**
![create a new product](usage_images/create_a_product.png)
- **Update an existing product.**
![update an existing product](usage_images/update_product.png)
- **Delete a product.**
![delete a product](usage_images/delete_product.png)
- **Get inventory levels for all products.**
![get inventory levels for all products](usage_images/get_list_inventory.png)
- **Get inventory level for a specific product.**
![get inventory level for a specific product](usage_images/detail_inventory_by_id.png)
- **Create a new order (updating inventory).**
![create a new order](usage_images/create_an_orders.png)

## Conclusion
Feel free to explore and use these endpoints to manage your e-commerce inventory application efficiently.
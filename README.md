# E-Commerce Database Management System

A structured E-Commerce DBMS built with **Python** and **MySQL**, designed to demonstrate core **Object-Oriented Programming (OOP)** concepts.

## Project Structure

```
├── main.py                 # CLI entry point (Facade pattern)
├── database.py             # Singleton database connection manager
├── requirements.txt
│
├── models/                 # Domain entities (OOP layer)
│   ├── base.py             # Abstract BaseModel (inheritance, polymorphism)
│   ├── user.py             # User entity (encapsulation via properties)
│   ├── product.py          # Product entity (validation, stock logic)
│   ├── cart.py             # Cart & CartItem (composition)
│   └── order.py            # Order & OrderItem (composition)
│
└── services/               # Business logic layer
    ├── base_service.py     # Abstract base service (inheritance)
    ├── user_service.py     # User CRUD & authentication
    ├── product_service.py  # Product catalog & inventory
    ├── cart_service.py     # Shopping cart operations
    └── order_service.py    # Order placement & lifecycle
```

## OOP Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| **Classes & Objects** | `User`, `Product`, `Cart`, `Order` model classes |
| **Encapsulation** | Private attributes (`_name`, `_price`) with `@property` getters/setters |
| **Inheritance** | `BaseModel` → all models; `BaseService` → all services |
| **Polymorphism** | Abstract `to_dict()` / `from_dict()` methods in `BaseModel` |
| **Composition** | `Cart` contains `CartItem` objects; `Order` contains `OrderItem` objects |
| **Singleton** | `Database` class ensures a single connection instance |
| **Facade** | `ECommerceApp` class wraps all services behind a simple CLI |

## Prerequisites

- Python 3.8+
- MySQL Server 8.0+

## Setup

### 1. Create MySQL Database

```sql
CREATE DATABASE ecommerce_db;
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

On first launch, enter your MySQL credentials. Tables are created automatically.

## Features

- **User Management** — Register, login, update profile
- **Product Catalog** — Add, browse, search products
- **Shopping Cart** — Add, remove, update quantities
- **Order Processing** — Checkout, view orders, cancel orders
- **Inventory Control** — Stock validation and automatic deduction on purchase
- **Admin Operations** — Add products, view all orders, update order status

## Database Schema

| Table | Description |
|-------|-------------|
| `users` | Registered customer accounts |
| `products` | Product catalog with pricing and stock |
| `cart_items` | Active shopping cart entries per user |
| `orders` | Placed order headers |
| `order_items` | Line items within each order |

## Sample Workflow

1. Register a new user account
2. Add products to the catalog (option 10)
3. Browse products and add items to cart
4. View cart and place an order
5. View order history and track status

## Tech Stack

- **Language:** Python 3
- **Database:** MySQL
- **Driver:** mysql-connector-python

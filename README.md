# E-Commerce Database Management

A simple E-Commerce DBMS using **Python** and **MySQL**, built around OOPs concepts.

## Project structure

```
ecommerce_project/
│
├── main.py
├── database.py
├── products.txt
├── requirements.txt
│
├── models/
│   ├── user.py
│   ├── product.py
│   ├── cart.py
│   └── order.py
│
├── services/
│   ├── user_service.py
│   ├── product_service.py
│   ├── cart_service.py
│   └── order_service.py
│
└── README.md
```

## OOP used

- **Classes and objects :** `User`, `Employee`, `Product`, `Cart`, `Order`
- **Inheritance :** `User` and `Employee` inherit from `Person`
- **Encapsulation :** data and methods live inside each class
- **Polymorphism :** `display()` works differently for User and Employee
- **Composition :** a `Cart` contains `CartItem` objects; an `Order` contains `OrderItem` objects

## Setup

1. Create the database in MySQL :

```sql
CREATE DATABASE ecommerce_db;
```

2. Install Python packages :

```bash
pip install -r requirements.txt
```

3. Add sample products (optional) :

Open MySQL and run the queries from `products.txt`.

4. Run the app :

```bash
python main.py
```

## Logins

- **User:** register with name and email, then login with email only (no password).
- **Employee:** login with name and password.
  - Default employee : `admin`
  - Default password : `admin123`

## What each role can do

**User**
- Display products
- Add to cart
- Checkout
- View own orders

**Employee**
- Display products
- Add products
- Update products

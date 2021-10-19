
import json
import sqlite3
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Scott Silver",
        "email": "scott@silver.com",
        "password": "scott"
    },
    {
        "id": 2,
        "name": "Steve Brownlee",
        "email": "steve@coach.com",
        "password": "steve"
    },
    {
        "id": 3,
        "name": "Hannah Hall",
        "email": "hannah@hall.com",
        "password": "hannah"
    },
    {
        "id": 4,
        "name": "Kylie Anyce",
        "email": "kylie@anyce.com",
        "password": "kylie"
    }
]

def get_all_customers():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            c.id,
            c.name,
            c.email,
            c.password
        FROM customer c
        """)

        customers = []
        
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT *
        FROM customer
        WHERE id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['email'], data['password'])
        return json.dumps(customer.__dict__)
  

def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    customer_index = -1 # Set this as -1 so we don't accidentally pop() the last index

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    
    if customer_index >= 0:  # Condition that ensures we don't pop something if no index is found
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.email,
            c.password
        FROM customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['email'],
            row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
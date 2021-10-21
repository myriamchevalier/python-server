
import json
import sqlite3
from models import Customer

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
  

def create_customer(new_customer):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO customer
            ( name, email, password )
        VALUES ( ?, ?, ? );
        """, (new_customer['name'], new_customer['email'], new_customer['password']))

        id = db_cursor.lastrowid

        new_customer['id'] = id

    return json.dumps(new_customer)

def delete_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))

def update_customer(id, new_customer):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE customer
            SET
                name = ?,
                email = ?,
                password = ?
        WHERE id = ?
        """, (new_customer['name'], new_customer['email'], new_customer['password'], id, ))

    return json.dumps(new_customer)
    
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
        WHERE email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['email'],
            row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
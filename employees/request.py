import sqlite3
import json
from models import Employee
from models.location import Location


def get_all_employees() :
    with sqlite3.connect("./kennel.db") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN location l
            ON l.id = e.location_id
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])
            employee.location = location.__dict__
            employees.append(employee.__dict__)
    
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT *
        FROM employee
        WHERE id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data ['address'], data['location_id'])

        return json.dumps(employee.__dict__)

def create_employee(new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO employee
            ( name, address, location_id )
        VALUES ( ?, ?, ? ) ;
        """, (new_employee['name'], new_employee['address'], new_employee['location_id']) )

        id = db_cursor.lastrowid

        new_employee['id'] = id

    return json.dumps(new_employee)
    

def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE employee
            SET 
                name = ?,
                address = ?,
                location_id = ?
        WHERE id = ?;
        """, (new_employee['name'], new_employee['address'], new_employee['location_id'], id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True
            
def get_employees_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT *
        FROM employee
        WHERE location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)
    
    return json.dumps(employees)
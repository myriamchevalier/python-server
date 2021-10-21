import sqlite3
import json
from models import Location


def get_all_locations():
    
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            l.id,
            l.name,
            l.address
        FROM location as l
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row['id'], row['name'], row['address']) 
            locations.append(location.__dict__)

    return json.dumps(locations)


def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT *
        FROM location
        WHERE id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        location = Location(data['id'], data['name'], data['address'])
        return json.dumps(location.__dict__)


  

def create_location(new_location):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO location
            ( name, address )
        VALUES ( ?, ? ) ;
        """, (new_location['name'], new_location['address'], ))

        id = db_cursor.lastrowid

        new_location['id'] = id
    
    return json.dumps(new_location)


def delete_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

def update_location(id, new_location):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE location
            SET
                name = ?,
                address = ?
        WHERE id = ?;
        """, (new_location['name'], new_location['address'], id, ))
    
    return json.dumps(new_location)

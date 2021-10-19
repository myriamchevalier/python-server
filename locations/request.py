import sqlite3
import json
from models import Location

LOCATIONS = [
    {"id": 1, "name": "Nashville North"},
    {"id": 2, "name": "Nashville South"}
]

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


  

def create_location(location):

    max_id = LOCATIONS[-1]["id"] # finds id of last index
    new_id = max_id + 1 # creates new id
    location["id"] = new_id #adds new id to location dictionary
    LOCATIONS.append(location) 

    return location

def delete_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break

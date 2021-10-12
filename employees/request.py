
EMPLOYEES = [
    {
        "id": 1,
        "name": "Ben Gregory",
        "address": "100 Oak St.",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Cassie Tesauro",
        "address": "78 Golden Ave",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Erin Truman",
        "address": "305 Artist Way",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Matthew Singler",
        "address": "794 Music Sq.",
        "locationId": 2
    }
]

def get_all_employees() :
    return EMPLOYEES

def get_single_employee(id):
    
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
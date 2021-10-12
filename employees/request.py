
EMPLOYEES = [
    {
        "id": 1,
        "name": "Ben Gregory",
        "email": "ben@gregory.com"
    },
    {
        "id": 2,
        "name": "Cassie Tesauro",
        "email": "cassie@tesauro.com"
    },
    {
        "id": 3,
        "name": "Erin Truman",
        "email": "erin@truman.com"
    },
    {
        "id": 4,
        "name": "Matthew Singler",
        "email": "matthew@singler.com"
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
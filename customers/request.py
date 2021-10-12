
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
    return CUSTOMERS

def get_single_customer(id):

    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    
    return requested_customer

def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)

    return customer
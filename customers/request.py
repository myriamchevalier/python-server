
CUSTOMERS = [
    {
        "id": 1,
        "name": "Scott Silver",
        "email": "scott@silver.com"
    },
    {
        "id": 2,
        "name": "Steve Brownlee",
        "email": "steve@coach.com"
    },
    {
        "id": 3,
        "name": "Hannah Hall",
        "email": "hannah@hall.com"
    },
    {
        "id": 4,
        "name": "Kylie Anyce",
        "email": "kylie@anyce.com"
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
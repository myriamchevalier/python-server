LOCATIONS = [
    {"id": 1, "name": "Nashville North"},
    {"id": 2, "name": "Nashville South"}
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):

    max_id = LOCATIONS[-1]["id"] # finds id of last index
    new_id = max_id + 1 # creates new id
    location["id"] = new_id #adds new id to location dictionary
    LOCATIONS.append(location) 

    return location

def delete_location(id):
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break

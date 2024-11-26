import random
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime=109345121):
    capacity = int(num_elements / load_factor)
    while not mf.is_prime(capacity):
        capacity += 1

    table = lt.new_list()
    for _ in range(capacity):
        lt.add_last(table, None)

    nuevo_mapa = {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
        "type": "PROBING",
    }
    return nuevo_mapa

def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key) % my_map["capacity"]
    found, position = find_slot(my_map, key, hash_value)

    if found:
        lt.change_info(my_map["table"], position, (key, value))
    else:
        lt.change_info(my_map["table"], position, (key, value))
        my_map["size"] += 1
    if my_map["size"] / my_map["capacity"] > my_map["limit_factor"]:
        rehash(my_map)


def contains(my_map, key):
    
    if key < len(my_map["table"]):
        if my_map["table"][key] != "":
            return True
    else:
        return False
        
def get(my_map, key):
    hash_value = mf.hash_value(my_map, key) % my_map["capacity"]
    table = my_map["table"]
    
    found, position = find_slot(my_map, key, hash_value)
    if found:
        return lt.get_element(table, position)[1]
    return None 


def remove(my_map, key):
    remove = ""
    my_map["table"][key] = remove
    return my_map

def size (my_map):
    size = len(my_map["table"])
    return size

def is_empty (my_map):
    if size(my_map) == 0:
        return True
    else: 
        return False
    
def key_set(my_map):
    keys = []
    for element in my_map["table"]:
        if element is not None and isinstance(element, tuple):
            keys.append(element[0])
    return keys


    
def value_set(my_map):
    values = []
    for i in my_map["table"]:
        values.append(i)
    return values

def find_slot(my_map, key, hash_value):
    capacity = my_map["capacity"]
    table = my_map["table"]
    position = hash_value % capacity

    while True:
        element = lt.get_element(table, position)
        if element is None or (isinstance(element, str) and element == "__EMPTY__"):
            return False, position
        if isinstance(element, tuple) and default_compare(key, element):
            return True, position
        position = (position + 1) % capacity
        if position == hash_value % capacity:
            break

    return False, None


def is_available(table, pos):
    element = lt.get_element(table, pos)
    return element is None or element == "__EMPTY__"

def rehash(my_map):
    old_table = my_map["table"]
    old_capacity = my_map["capacity"]
    new_capacity = old_capacity * 2
    new_table = lt.new_list()

    for _ in range(new_capacity):
        lt.add_last(new_table, None)
    
    for i in range(old_capacity):
        element = lt.get_element(old_table, i)
        if element is not None and element != "__EMPTY__":
            key = element[0] 
            hash_value = hash(key) 
            available = find_slot(my_map, key, hash_value)
            new_index = available[1] 
            lt.add_last(new_table, element)
    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    
    return my_map

def default_compare(key, element):
    if not isinstance(element, tuple) or len(element) < 1:
        return False
    element_key = element[0]
    if key == element_key:
        return True
    return False

    
def keys(my_map):
    return [entry[0] for entry in my_map["table"] if entry is not None]
    
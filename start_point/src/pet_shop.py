# WRITE YOUR FUNCTIONS HERE

# return the name of the shop
def get_pet_shop_name(shop_name):
    return shop_name["name"]

# return total anount of cash
def get_total_cash(pet_shop):
    return pet_shop ["admin"]["total_cash"]

# add cash or remove cash (remember 'adding' negative amount of cash will remove it)
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] +=  cash

# get the total number of pets sold
def get_pets_sold(pets_sold):
    return pets_sold ["admin"]["pets_sold"]

# add to the total number of pets sold
def increase_pets_sold (new_pet_sold, pets_sold):
    new_pet_sold ["admin"]["pets_sold"] += pets_sold

# doing a count of pets in stock
def get_stock_count(pets_in_shop):
    return len(pets_in_shop["pets"])

# return pets by their breed, when the breed is found (returns count) or not found (returns 0)
def get_pets_by_breed(pet_shop, pet_breed):
    num_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            num_pets.append(pet)
    return num_pets

# find pet by their name - similar to above, except we want to return None instead of 0
def find_pet_by_name(pet_shop, pet_name):
    pet_by_name = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_by_name = pet
    return pet_by_name

# remove pet by their name
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

# add a new pet to the stock list
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# return the customer cash
def get_customer_cash(customers):
    return customers["cash"]

# remove cash from customer
def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

# count the number of pets customer has
def get_customer_pet_count(customers):
    return len(customers["pets"])

# add pet to customer
def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

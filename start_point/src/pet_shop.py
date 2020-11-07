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
        if pet["name"] == pet_by_name:
            pet_by_name = pet
    return pet_by_name



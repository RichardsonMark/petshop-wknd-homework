# WRITE YOUR FUNCTIONS HERE

# return the name of the shop
def get_pet_shop_name(shop_name):
    return shop_name["name"]

# return total cash
def get_total_cash(pet_shop):
    return pet_shop ["admin"]["total_cash"]

# add cash or remove cash
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] +=  cash

# get number of pets sold
def get_pets_sold(pets_sold):
    return pets_sold ["admin"]["pets_sold"]

# add to the number of pets sold
def increase_pets_sold (new_pet_sold, pets_sold):
    new_pet_sold ["admin"]["pets_sold"] += pets_sold


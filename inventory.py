inventory = []

def show_inventory():
    print("")
    if len(inventory) > 0:
        print("you are carrying:\n")
        for i in inventory:
            print(i)
    else:
        print("there is nothing in your inventory")
    print("")

def add_to_inventory(item):
    inventory.append(item)

def remove_from_inventory(item):
    if item in inventory:
        item_index = inventory.index(item)
        if (item_index > -1):
            the_item = inventory[item_index]
            return inventory.pop(item_index)
    return ""

from inventory import *
from user_input import *
from rooms import *

# game state variables
current_room = 0
prev_room = -1
        
def experience_room(command_parts):
    display_message = ""
    cur_room_data = rooms[current_room]
    if command_parts[0] == "north":
        if cur_room_data[ROOM_NORTH] > -1:
            return cur_room_data[ROOM_NORTH]
        else:
            display_message = "You can't go that way"
    elif command_parts[0] == "south":
        if cur_room_data[ROOM_SOUTH] > -1:
            return cur_room_data[ROOM_SOUTH]
        else:
            display_message = "You can't go that way"
    elif command_parts[0] == "east":
        if cur_room_data[ROOM_EAST] > -1:
            return cur_room_data[ROOM_EAST]
        else:
            display_message = "You can't go that way"
    elif command_parts[0] == "west":
        if cur_room_data[ROOM_WEST] > -1:
            return cur_room_data[ROOM_WEST]
        else:
            display_message = "You can't go that way"
    elif command_parts[0] == "up":
        if cur_room_data[ROOM_UP] > -1:
            return cur_room_data[ROOM_UP]
        else:
            display_message = "You can't go that way"
    elif command_parts[0] == "down":
        if cur_room_data[ROOM_DOWN] > -1:
            return cur_room_data[ROOM_DOWN]
        else:
            display_message = "You can't go that way"
    elif command_parts[0] == "take":
        if len(command_parts) < 2:
            display_message = "Take what?"
        else:
            room_items = cur_room_data[ROOM_ITEMS]
            item_to_take = " ".join(command_parts[1:])
            if item_to_take in room_items:
                item_index = room_items.index(item_to_take)
                item_description = cur_room_data[ROOM_ITEM_DESCRIPTIONS][item_index]
                add_to_inventory(item_to_take)
                cur_room_data[ROOM_ITEMS].remove(item_to_take)
                cur_room_data[ROOM_ITEM_DESCRIPTIONS].remove(item_description)
                display_message = item_to_take + " taken"
            else:
                display_message = "There is no " + item_to_take + " here"
    elif command_parts[0] == "drop":
        if len(command_parts) < 2:
            display_message = "Drop what?"
        else:
            item_to_drop = " ".join(command_parts[1:])
            item_from_inventory = remove_from_inventory(item_to_drop)
            if item_from_inventory == "":
                display_message = "You do not have a " + item_to_drop
            else:
                display_message = item_from_inventory + " dropped"
                cur_room_data[ROOM_ITEMS].append(item_from_inventory)
                cur_room_data[ROOM_ITEM_DESCRIPTIONS].append(
                    "A " + item_from_inventory + " is laying on the floor."
                )
            
    else:
        display_message = "I don't understand that"
        
    # Display output
    print("")
    print(display_message)
    print("")
    return current_room

# Game loop
while True:
    if current_room != prev_room:
        display_room_info(current_room)
        prev_room = current_room
        
    command_parts = get_user_input(current_room)
    
    # Change the game state
    if command_parts[0] == "quit":
        break
    elif command_parts[0] == "inv" or command_parts[0] == "inventory":
        show_inventory()
    elif command_parts[0] == "look":
        prev_room = -1
    else:
        current_room = experience_room(command_parts)
   
print("Thanks for playing!")

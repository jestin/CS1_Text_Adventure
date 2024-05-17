from inventory import *
from user_input import *
from rooms import *

# game state variables
current_room = 0
prev_room = -1

def can_enter_room(room_index):
    for required_item in rooms[room_index][ROOM_ITEM_REQUIREMENTS]:
        if required_item not in inventory:
            return False
    return True

def print_message(message, max_length):
    words = message.split()
    words.reverse()
    line = words.pop()
    words.reverse()

    for word in words:
        if len(word) + 1 + len(line) > max_length:
            print(line)
            line = word
        else:
            line = line + " " + word

    if len(line) > 0:
        print(line)

def display_room_info(room):
    os.system('cls||clear')
    print("----------------")
    print(rooms[room][ROOM_NAME])
    print("")
    print_message(rooms[room][ROOM_DESCRIPTION], 70)
    if len(rooms[room][ROOM_ITEM_DESCRIPTIONS]):
        print("  ".join(rooms[room][ROOM_ITEM_DESCRIPTIONS]))
    print("----------------")

        
def experience_room(command_parts):
    display_message = ""
    cur_room_data = rooms[current_room]
    direction = -1
    if command_parts[0] in ["north", "south", "east", "west", "up", "down"]:
        if command_parts[0] == "north":
            direction = ROOM_NORTH
        elif command_parts[0] == "south":
            direction = ROOM_SOUTH
        elif command_parts[0] == "east":
            direction = ROOM_EAST
        elif command_parts[0] == "west":
            direction = ROOM_WEST
        elif command_parts[0] == "up":
            direction = ROOM_UP
        elif command_parts[0] == "down":
            direction = ROOM_DOWN

        if cur_room_data[direction] < 0:
            display_message = "You can't go that way"
        elif not can_enter_room(cur_room_data[direction]):
            display_message = rooms[cur_room_data[direction]][ROOM_ITEM_REQUIREMENTS_MESSAGE]
        else:
            return cur_room_data[direction]
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
    print_message(display_message, 70)
    print("")
    return current_room

# Game loop
while True:
    if current_room != prev_room:
        display_room_info(current_room)
        prev_room = current_room
        
    command_parts = get_user_input(current_room)

    if len(command_parts) < 1:
        continue
    
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

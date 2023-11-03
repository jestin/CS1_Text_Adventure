room_name = ""
room_description = ""

west_of_house_name = "WEST OF HOUSE"
west_of_house_description = "You are standing in front of an old, white, dilapidated house."

front_porch_name = "FRONT PORCH"
front_porch_description = "You are stading on the front porch of an old, dilapidated house."

def printRoomDescription():
    print("")
    print("####################")
    print(room_name)
    print("####################")
    print("")
    print(room_description)
    print("")

def getUserInstruction():
    user_instruction = ""
    while user_instruction == "":
        instruction = input("What do you do?  ")
        
        if instruction == "north" or instruction == "North" or instruction == "NORTH":
            user_instruction = "NORTH"
        elif instruction == "south" or instruction == "South" or instruction == "SOUTH":
            user_instruction = "SOUTH"
        elif instruction == "east" or instruction == "East" or instruction == "EAST":
            user_instruction = "EAST"
        elif instruction == "west" or instruction == "West" or instruction == "WEST":
            user_instruction = "WEST"
        elif instruction == "look" or instruction == "Look" or instruction == "LOOK":
            user_instruction = "LOOK"
        elif instruction == "exit" or instruction == "Exit" or instruction == "EXIT":
            user_instruction = "EXIT"
        elif instruction == "quit" or instruction == "Quit" or instruction == "QUIT":
            user_instruction = "EXIT"
    return user_instruction

room_name = west_of_house_name
room_description = west_of_house_description

# Game loop
while(1):
    # print current room description
    printRoomDescription()

    # get instruction from the user
    instruction = getUserInstruction()

    # handle general instructions
    if instruction == "LOOK":
        continue
    if instruction == "EXIT":
        break

    # handle room-specific instructions
    if room_name == west_of_house_name:
        if instruction == "EAST":
            room_name = front_porch_name
            room_description = front_porch_description
            continue
    if room_name == front_porch_name:
        if instruction == "WEST":
            room_name = west_of_house_name
            room_description = west_of_house_description
            continue

    print("")
    print("That doesn't work here")
    print("")

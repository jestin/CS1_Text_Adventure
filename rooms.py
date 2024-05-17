import os

ROOM_NAME = 0
ROOM_DESCRIPTION = 1
ROOM_NORTH = 2
ROOM_SOUTH = 3
ROOM_EAST = 4
ROOM_WEST = 5
ROOM_UP = 6
ROOM_DOWN = 7
ROOM_ITEMS = 8
ROOM_ITEM_DESCRIPTIONS = 9

def display_room_info(room):
    os.system('cls||clear')
    print("----------------")
    print(rooms[room][ROOM_NAME])
    print("")
    print(rooms[room][ROOM_DESCRIPTION])
    if len(rooms[room][ROOM_ITEM_DESCRIPTIONS]):
        print("  ".join(rooms[room][ROOM_ITEM_DESCRIPTIONS]))
    print("----------------")

entrance_data = (
    "Entrance",
    "You stand in a large entranceway.  There are rooms to the east and west, a hallway leading north, and a grand staircase leading to the upper floors.",
    1,
    -1,
    4,
    -1,
    5,
    -1,
    [],
    []
)

dining_room_data = (
    "Dining Room",
    "There is a fancy table surrounded by several equally fancy chairs.  There are doorways to the north, west, and south.",
    3,
    0,
    -1,
    2,
    -1,
    -1,
    ["fork", "knife", "spoon"],
    [
        "There is a single fork on the table.",
        "There is an ornate steak knife on the table.",
        "There is a fancy spoon on the table."
    ]
)

drawing_room_data = (
    "Drawing Room",
    "Several fancy chairs and a minibar line the walls.",
    -1,
    -1,
    1,
    -1,
    -1,
    -1,
    ["decantor"],
    ["There is a decantor on the minibar."]
)

kitchen_data = (
    "Kitchen",
    "A large kitchen with several prep tables, a stove, an oven, and a sink.",
    -1,
    1,
    -1,
    -1,
    -1,
    -1,
    ["cookbook"],
    ["A cookbook laying open on one of the prep tables."]
)

ballroom_data = (
    "Ballroom",
    "An elegant ballroom decorated with lavish curtains, a priceless chandelier, and a gleaming wooden dance floor.",
    -1,
    -1,
    -1,
    0,
    -1,
    -1,
    [],
    []
)

upstiars_hallway_data = (
    "Upstairs Hallway",
    "A wide hallway with doors to the east, west and south.  There is an end table near a window that has a birdcage sitting on it.",
    -1,
    -1,
    -1,
    -1,
    -1,
    0,
    [],
    []
)


rooms = (
    entrance_data,
    dining_room_data,
    drawing_room_data,
    kitchen_data,
    ballroom_data,
    upstiars_hallway_data
)

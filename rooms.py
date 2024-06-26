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
ROOM_ITEM_TAKEN_DESCRIPTIONS = 10
ROOM_ITEM_REQUIREMENTS = 11
ROOM_ITEM_REQUIREMENTS_MESSAGE = 12

entrance_data = (
    "Entrance",
    "You stand in a large entranceway.  There are rooms to the east and west, a hallway leading north ends in a closed door, and a grand staircase leading to the upper floors.",
    1,
    -1,
    4,
    6,
    5,
    -1,
    [],
    [],
    [],
    [],
    ""
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
    ],
    ["", "", ""],
    ["bronze key"],
    "The door is locked"
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
    ["decanter"],
    ["There is a decanter on the minibar."],
    [""],
    [],
    ""
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
    ["A cookbook laying open on one of the prep tables."],
    [""],
    [],
    ""
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
    ["bronze key"],
    ["A bronze key sits on a windowsill"],
    [""],
    [],
    ""
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
    [],
    [],
    [],
    ""
)

parlor_data = (
    "Parlor",
    "Fancy sofas and comfortable looking armchairs are arranged along the walls of this room, which are adorned with old portraits of long-dead former owners of the house.  There is a door to the north.",
    7,
    -1,
    0,
    -1,
    -1,
    -1,
    [],
    [],
    [],
    [],
    ""
)

powder_room_data = (
    "Powder Room",
    "An elegant bathroom with a shining vanity, makeup lights, and a tacky fuzzy toilet seat cover.",
    -1,
    6,
    -1,
    -1,
    -1,
    8,
    ["rug"],
    ["A rug matching the toilet seat cover is in front of the toilet.  Gross."],
    ["Removing the rug reveals a trap door"],
    ["decanter"],
    "A ghostly yet booming voice yells \"Bring me a drink if you wish to pass!\""
)

crawl_space_data = (
    "Crawl Space",
    "A dark, musty crawl space under the house extends east to west.",
    -1,
    -1,
    -1,
    -1,
    7,
    -1,
    [],
    [],
    [],
    ["rug"],
    "Through the gross rug?"
)


rooms = (
    entrance_data,
    dining_room_data,
    drawing_room_data,
    kitchen_data,
    ballroom_data,
    upstiars_hallway_data,
    parlor_data,
    powder_room_data,
    crawl_space_data
)

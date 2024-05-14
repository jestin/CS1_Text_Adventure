def get_user_input(room):
    # Get input from the player
    parts = []
    while len(parts) == 0:
        parts = input("What do you want to do?  ").lower().split()
        if len(parts) == 1:
            if parts[0] == "exit":
                parts[0] = "quit"
            return parts
        elif len(parts) > 1:
            if parts[0] == "pick" and parts[1] == "up":
                parts = ["take"].extend(parts[2:])
                return parts
            elif parts[0] == "drop" or parts[0] == "leave":
                parts[0] = "drop"
                return parts
            elif parts[0] == "go" or parts[0] == "move":
                return parts[1:]
            else:
                return parts
        else:
            return " ".join(parts)
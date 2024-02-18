place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("Light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You find a hidden passage!")
    elif action == "proceed in the dark":
        print("You stumble upon a mysterious artifact!")

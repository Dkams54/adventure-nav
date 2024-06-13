import random

def display_intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious dungeon with several rooms.")
    print("Your goal is to find the hidden treasure and escape the dungeon.")
    print("Good luck!\n")

def show_status(location, inventory):
    print("\nYou are in the " + location)
    print("Inventory:", inventory)
    print("What do you want to do?")

def move_location(current_location, direction, rooms):
    if direction in rooms[current_location]:
        return rooms[current_location][direction]
    else:
        print("You can't go that way!")
        return current_location

def main():
    display_intro()
    
    rooms = {
        'Hall': {'south': 'Kitchen', 'east': 'Dining Room', 'item': 'key'},
        'Kitchen': {'north': 'Hall', 'item': 'monster'},
        'Dining Room': {'west': 'Hall', 'south': 'Garden', 'item': 'potion'},
        'Garden': {'north': 'Dining Room', 'item': 'treasure'}
    }
    
    current_location = 'Hall'
    inventory = []
    game_over = False

    while not game_over:
        show_status(current_location, inventory)
        move = input("> ").strip().lower()
        
        if move in ['north', 'south', 'east', 'west']:
            current_location = move_location(current_location, move, rooms)
        elif move == 'take':
            if 'item' in rooms[current_location]:
                item = rooms[current_location]['item']
                if item == 'monster':
                    print("A monster has got you... GAME OVER!")
                    game_over = True
                else:
                    inventory.append(item)
                    print(f"{item.capitalize()} taken!")
                    del rooms[current_location]['item']
            else:
                print("There's nothing here to take.")
        elif move == 'quit':
            print("Thanks for playing!")
            game_over = True
        else:
            print("Invalid move. Try 'north', 'south', 'east', 'west', 'take', or 'quit'.")
        
        if 'treasure' in inventory:
            print("Congratulations! You have found the treasure and won the game!")
            game_over = True

if __name__ == "__main__":
    main()

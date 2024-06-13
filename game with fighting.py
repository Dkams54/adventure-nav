

import random

class Game:
    def __init__(self):
        self.rooms = {
            'Hall': {'south': 'Kitchen', 'east': 'Library', 'west': 'Armory', 'item': None},
            'Kitchen': {'north': 'Hall', 'enemy': 'Goblin'},
            'Library': {'west': 'Hall', 'south': 'Boss Room', 'item': 'Magic Book'},
            'Armory': {'east': 'Hall', 'item': 'Sword'},
            'Boss Room': {'north': 'Library', 'enemy': 'Dragon', 'boss': True}
        }
        self.current_location = 'Hall'
        self.inventory = []
        self.hp = 100
        self.game_over = False

    def display_intro(self):
        print("Welcome to Dkams Adventure Game!")
        print("You find yourself in a mysterious dungeon with several rooms.")
        print("Your goal is to find and defeat the Dragon to escape the dungeon.")
        print("Good luck!\n")

    def show_status(self):
        print(f"\nYou are in the {self.current_location}")
        print(f"Inventory: {self.inventory}")
        print(f"HP: {self.hp}")
        if 'item' in self.rooms[self.current_location]:
            item = self.rooms[self.current_location]['item']
            if item:
                print(f"You see a {item}")
        if 'enemy' in self.rooms[self.current_location]:
            enemy = self.rooms[self.current_location]['enemy']
            print(f"A {enemy} is here!")

    def move_location(self, direction):
        if direction in self.rooms[self.current_location]:
            self.current_location = self.rooms[self.current_location][direction]
        else:
            print("You can't go that way!")

    def take_item(self):
        if 'item' in self.rooms[self.current_location]:
            item = self.rooms[self.current_location]['item']
            if item:
                self.inventory.append(item)
                print(f"{item.capitalize()} taken!")
                self.rooms[self.current_location]['item'] = None
            else:
                print("There's nothing here to take.")
        else:
            print("There's nothing here to take.")

    def fight_enemy(self):
        if 'enemy' in self.rooms[self.current_location]:
            enemy = self.rooms[self.current_location]['enemy']
            if 'Sword' in self.inventory:
                print(f"You fight the {enemy} with your Sword!")
                if random.random() > 0.5:
                    print(f"You have defeated the {enemy}!")
                    del self.rooms[self.current_location]['enemy']
                    if 'boss' in self.rooms[self.current_location]:
                        self.game_over = True
                        print("Congratulations! You have defeated the Dragon and won the game!")
                else:
                    print(f"The {enemy} hits you!")
                    self.hp -= 20
                    if self.hp <= 0:
                        self.game_over = True
                        print("You have been defeated... GAME OVER!")
            else:
                print(f"The {enemy} attacks you!")
                self.hp -= 20
                if self.hp <= 0:
                    self.game_over = True
                    print("You have been defeated... GAME OVER!")
        else:
            print("There's no enemy here to fight.")

    def play(self):
        self.display_intro()
        while not self.game_over:
            self.show_status()
            move = input("> ").strip().lower()
            if move in ['north', 'south', 'east', 'west']:
                self.move_location(move)
            elif move == 'take':
                self.take_item()
            elif move == 'fight':
                self.fight_enemy()
            elif move == 'quit':
                print("Thanks for playing!")
                self.game_over = True
            else:
                print("Invalid move. Try 'north', 'south', 'east', 'west', 'take', 'fight', or 'quit'.")

if __name__ == "__main__":
    game = Game()
    game.play()

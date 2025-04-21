import random
import json
import os

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.inventory = []
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to your inventory!")

    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP!")
        if self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)  # Increase XP needed for next level
        self.health += 20
        self.attack += 5
        self.defense += 3
        print(f"Congratulations! You leveled up to Level {self.level}!")
        print(f"Your stats have improved: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}")

    def show_status(self):
        print(f"{self.name}'s Status: Level {self.level}, Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}")
        print(f"XP: {self.xp}/{self.xp_to_next_level}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

    def to_dict(self):
        """Convert player data to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "health": self.health,
            "attack": self.attack,
            "defense": self.defense,
            "inventory": self.inventory,
            "level": self.level,
            "xp": self.xp,
            "xp_to_next_level": self.xp_to_next_level,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Player object from a dictionary."""
        player = cls(data["name"])
        player.health = data["health"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.inventory = data["inventory"]
        player.level = data["level"]
        player.xp = data["xp"]
        player.xp_to_next_level = data["xp_to_next_level"]
        return player

# Enemy class
class Enemy:
    def __init__(self, name, health, attack, defense, xp_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

# Combat function
def combat(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print("\n--- Combat Menu ---")
        print("1. Attack")
        print("2. Run")
        choice = input("Choose an action: ")

        if choice == "1":
            player_damage = random.randint(1, player.attack)
            enemy_damage = random.randint(1, enemy.attack)

            print(f"You attack the {enemy.name} for {player_damage} damage!")
            enemy.take_damage(player_damage)

            if enemy.is_alive():
                print(f"The {enemy.name} attacks you for {enemy_damage} damage!")
                player.take_damage(enemy_damage)
            else:
                print(f"You defeated the {enemy.name}!")
                player.add_item("Gold")
                player.gain_xp(enemy.xp_reward)
                break

        elif choice == "2":
            print("You run away!")
            break

        player.show_status()
        print(f"{enemy.name}'s Health: {enemy.health} and Defense: {enemy.defense}")

    if not player.is_alive():
        print("You have been defeated. Game Over!")
        exit()

# Save game function
def save_game(player):
    with open("savefile.json", "w") as file:
        json.dump(player.to_dict(), file)
    print("Game saved!")

# Load game function
def load_game():
    if os.path.exists("savefile.json"):
        with open("savefile.json", "r") as file:
            data = json.load(file)
        player = Player.from_dict(data)
        print("Game loaded!")
        return player
    else:
        print("No save file found.")
        return None

# Main game loop
def game():
    print("Welcome to the Text RPG!")
    player = None

    # Check if a save file exists
    if os.path.exists("savefile.json"):
        load_choice = input("Do you want to load your saved game? (yes/no): ").lower()
        if load_choice == "yes":
            player = load_game()

    if not player:
        player_name = input("Enter your character's name: ")
        player = Player(player_name)
        print(f"\nHello, {player.name}! Let's begin your adventure.")

    while True:
        print("\n--- Main Menu ---")
        print("1. Explore")
        print("2. Check Status")
        print("i. Check inventory")
        print("3. Save Game")
        print("4. Quit")
        choice = input("Choose an action: ")

        if choice == "1":
            event = random.choice(["combat", "treasure", "nothing"])
            if event == "combat":
                enemy = Enemy("Goblin", random.randint(20, 40), random.randint(5, 10), random.randint(2, 5), xp_reward=random.randint(20, 50))
                combat(player, enemy)
            elif event == "treasure":
                print("\nYou found a treasure chest!")
                player.add_item("Potion")
            else:
                print("\nYou explore the area but find nothing.")

        elif choice == "2":
            player.show_status()
            
        elif choice == "i":
            player.show_status()

        elif choice == "3":
            save_game(player)

        elif choice == "4":
            print("Thanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the game
if __name__ == "__main__":
    game()
import json
import random
#import prettytable

# Create character
class Character:
    def __init__(self,name, hp, mp, attack, defense, level=1, age=1):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = 0
        self.age = 0
         
         
    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)
        
    def is_alive(self):
        return self.hp > 0
    
    def has_energy(self):
        return self.mp > 0
    
    def gain_exp(self, exp):
        self.experience += exp
        
        if self.experience >= self.hp * 10:
            levelup()
            
    def level_up(self):
        self.level += 1
        self.hp+= 10
        self.attack += 10
        self.defense += 2
        self.experience = 0
        print(f"{self.name} has leveled up to {self.level}")
        
# Warrior
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, mp=20, attack=20, defense=10, level=1, age=1)

# Mage
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=80, mp=100, attack=30, defense=5, level=1, age=1)

# --- Inventory --
# item class
class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type
        self.effect = effect
    
    # define usage of items
    def use(self, character):
        if self.item_type == "heal":
            character.hp = min(character.hp + self.effect , character.level * 10 +90)
            print(f"{character.name} used {self.name} and gained {self.effect} Health!")
        
        if self.item_type == "mana":
            character.mp = min(character.mp + self.effect , character.level * 10 +90)
            print(f"{character.name} used {self.name} and gained {self.effect} Energy!")

# Inventory
class Inventory:
    def __init__(self):
        self.items = []
    
    # Add items
    def add_item(self, item):
        self.items.append(item)
    
    # Delete items
    def remove_item(self, item):
        self.items.remove(item)
        
    # Use an item
    def use_item(self, item_name, character):
        for item in self.items:
            if item.name == item_name:
                item.use(character)
                self.remove_item(item)
        # if item not found
        print("Item not found in inventory.")
        return False
    
    # we can save inventory
    def save_inventory(self, filename):
        with open(filename, 'w') as file:
            json.dump([item.__dict__ for item in self.items], file)
            
    # load inventory
    def load_inventory(self, filename):
        with open(filename, 'r') as file:
            items = json.dump(file)
            self.items = [Item(
                item['name'],
                item['item_type'],
                item['effect']) 
            for item in items]
    
## cc everything else
# Battle System
def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        enemy.take_damage(player.attack)
        if enemy.is_alive():
            player.take_damage(enemy.attack)
        print(f"{player.name} HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy.hp}")
    if player.is_alive():
        print("You won the battle!")
        player.gain_experience(10)
    else:
        print("You were defeated...")

# Map Exploration
class Map:
    def __init__(self, size):
        self.size = size
        self.map = [['.' for _ in range(size)] for _ in range(size)]
        self.player_pos = [size // 2, size // 2]

    def move_player(self, direction):
        if direction == 'north' and self.player_pos[0] > 0:
            self.player_pos[0] -= 1
        elif direction == 'south' and self.player_pos[0] < self.size - 1:
            self.player_pos[0] += 1
        elif direction == 'east' and self.player_pos[1] < self.size - 1:
            self.player_pos[1] += 1
        elif direction == 'west' and self.player_pos[1] > 0:
            self.player_pos[1] -= 1

        event = random.choice(['enemy', 'treasure', 'npc', 'nothing'])
        return event

# Quests and Storyline
class Quest:
    def __init__(self, description, reward):
        self.description = description
        self.completed = 0
        self.reward = reward

    def complete_quest(self, player):
        self.completed = 2
        player.gain_experience(self.reward)
        print(f"Quest '{self.description}' completed! You gained {self.reward} experience.")

def load_quests(filename):
    quests = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 2:
                print(f"Skipping invalid line in quests file: {line}")
                continue
            description, reward = parts
            try:
                reward = int(reward)
                quests.append(Quest(description, reward))
            except ValueError:
                print(f"Invalid reward value: {reward} in line: {line}")
    return quests

# NPC Interactions
class NPC:
    def __init__(self, name, dialog, quest=None):
        self.name = name
        self.dialog = dialog
        self.quest = quest

    def interact(self, player):
        print(f"{self.name}: {self.dialog}")
        if self.quest and not self.quest.completed == 1:
            print(f"Quest available: {self.quest.description}")
            accept = input("Do you accept the quest? (yes/no): ")
            if accept.lower() == 'yes':
                self.quest.completed == 1
                return self.quest
        return None

# Main Game
def main():
    print("Welcome to QuestMaster: The Text-Based RPG Adventure!")
    while True:
        print("\nMain Menu:")
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            start_new_game()
        elif choice == '2':
            load_game()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def start_new_game():
    name = input("Enter your character's name: ")
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    class_choice = input("Choose a class: ")

    if class_choice == '1':
        player = Warrior(name)
    elif class_choice == '2':
        player = Mage(name)
    else:
        print("Invalid choice, defaulting to Warrior.")
        player = Warrior(name)

    inventory = Inventory()
    inventory.add_item(Item("Health Potion", "potion", 20))
    inventory.add_item(Item("Iron Sword", "weapon", 10))
    game_map = Map(5)
    
    # load quests
    quests = load_quests("quests.txt")
    
    # Check if quests are available
    if not quests:
        print("No quests available. Please add quests to 'quests.txt'.")
        return
        
    npc1 = NPC("Old Man", "Welcome to our village! We need your help.", quests[0])
    npc2 = NPC("Painter", "Hello Champ. Create your vision", quests[2])
    npc3 = NPC("Magi", "Your inner worlds are best to explore", quests[5])
    
    npcs = [npc1, npc2, npc3]
                

    while player.is_alive():
        print("\nGame Menu:")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. View Quests")
        print("4. Save Game")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            event = game_map.move_player(random.choice(['north', 'south', 'east', 'west']))
            if event == 'enemy':
                enemy = Warrior("Goblin")
                print("An enemy appears!")
                battle(player, enemy)
            elif event == 'treasure':
                print("You found a treasure! ")
                inventory.add_item(Item("Gold", "treasure", 0))
                print("You found a Gold")
            elif event == 'npc':
                npc = random.choice(npcs)
                print(f"You meet {npc.name}.")
                quest = npc.interact(player)
                if quest:
                    quests.append(quest)
            else:
                print("Nothing happens.")
        elif choice == '2':
            print(f"Inventory: {[item.name for item in inventory.items]}")
            item_choice = input("Enter item name to use or 'back' to return: ")
            if item_choice != 'back':
                inventory.use_item(item_choice, player)
        elif choice == '3':
            print("Quests:")  
            for quest in quests:
                if quest.completed == 2:
                    status = "Completed"
                elif quest.completed == 1:
                    status = "Doing"
                else:
                    status ="Avaliable"
            print(f"- {quest.description} [{status}]")
        elif choice == '4':
            save_game(player, inventory, game_map, quests)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

def save_game(player, inventory, game_map, quests):
    with open('save_game.json', 'w') as file:
        game_state = {
            'player': {
                'name': player.name,
                'hp': player.hp,
                'attack': player.attack,
                'defense': player.defense,
                'level': player.level,
                'experience': player.experience
            },
            'inventory': [item.__dict__ for item in inventory.items],
            'player_pos': game_map.player_pos,
            'quests': [{'description': quest.description, 'completed': quest.completed, 'reward': quest.reward} for quest in quests]
        }
        json.dump(game_state, file)
    print("Game saved.")

def load_game():
    try:
        with open('save_game.json', 'r') as file:
            game_state = json.load(file)
            player_data = game_state['player']
            player = Character(player_data['name'], player_data['hp'], player_data['attack'], player_data['defense'], player_data['level'])
            player.experience = player_data['experience']
            
            inventory = Inventory()
            for item_data in game_state['inventory']:
                inventory.add_item(Item(item_data['name'], item_data['item_type'], item_data['effect']))
            
            game_map = Map(5)
            game_map.player_pos = game_state['player_pos']
            
            quests = []
            for quest_data in game_state['quests']:
                quest = Quest(quest_data['description'], quest_data['reward'])
                quest.completed = quest_data['completed']
                quests.append(quest)
        
            npc1 = NPC("Old Man", "Welcome to our village! We need your help.", quests[0])
            npc2 = NPC("Painter", "Hello Champ. Create your vision", quests[2])
            npc3 = NPC("Magi", "Your inner worlds are best to explore", quests[5])
            
            npcs = [npc1, npc2, npc3]
            
            while player.is_alive():
                print("\nGame Menu:")
                print("1. Explore")
                print("2. Check Inventory")
                print("3. View Quests")
                print("4. Save Game")
                print("5. Quit")
                choice = input("Choose an option: ")

                if choice == '1':
                    event = game_map.move_player(random.choice(['north', 'south', 'east', 'west']))
                    if event == 'enemy':
                        enemy = Warrior("Goblin")
                        print("An enemy appears!")
                        battle(player, enemy)
                    elif event == 'treasure':
                        print("You found a treasure!")
                        inventory.add_item(Item("Gold", "treasure", 0))
                        print("You found a Gold")
                    elif event == 'npc':
                        npc = random.choice(npcs)
                        print(f"You meet {npc.name}.")
                        quest = npc.interact(player)
                        if quest:
                            quests.append(quest)
                    else:
                        print("Nothing happens.")       
                elif choice == '2':
                    print(f"Inventory: {[item.name for item in inventory.items]}")
                    item_choice = input("Enter item name to use or 'back' to return: ")
                    if item_choice != 'back':
                        inventory.use_item(item_choice, player)
                elif choice == '3':
                    print("Quests:")
                    for quest in quests:
                        if quest.completed == 2:
                            status = "Completed"
                        elif quest.completed == 1:
                            status = "Doing"
                        else:
                            status ="Avaliable"
                        print(f"- {quest.description} [{status}]")
                elif choice == '4':
                    save_game(player, inventory, game_map, quests)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice, please try again.")
    except FileNotFoundError:
        print("No saved game found. Starting a new game.")
        start_new_game()

if __name__ == "__main__":
    main()
            
            
            
            
            
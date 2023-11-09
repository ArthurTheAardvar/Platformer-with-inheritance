import random

class Player:
    def __init__(self, health):
        self.health = health
        self.inventory = ["healing_potion"]



class MagicWand:
    def __init__(self, materials, spellpower, durability):
        self.material = materials
        self.spellpower = spellpower
        self.durability = durability
    

    def made(self):
        print(f"This staff is made out of", self.material)

    def power(self):
        print(f"The spellpower of this wand is", self.spellpower)
        


    def incdurability(self):
        print(f"The durability of this wand is", self.durability)
        


class MagicPotion:
    def __init__(self, name, potency, flavor ):
        self.name = name
        self.potency = potency
        self.flavor = flavor
    
    def drink(self):
        if self.potency > 0:
            print(f"Drank {self.name}. Feel invigorated!")
            self.potency -= 1
        else:
            print(f"No more {self.name} left!")
    
    def refill(self):
        print(f"Refilling {self.name}.")
        self.potency = random.randint(1, 5)

    def taste(self):
        self.list = ["Lemon", "Strawberry", "Watermelon"]
        

        if self.list== 0:
            print(f"tastes like Lemon")
        elif self.list == 1:
            print(f"tastes like Strawberry")
        elif self.list == 2:
            print(f"tastes like Watermelon")

# Create two MagicPotion objects
healing_potion = MagicPotion("Healing Potion", 3, 0)
strength_potion = MagicPotion("Strength Potion", 2, 1)

p1 = Player(100)
p2 = Player(100)

wand = MagicWand("Wood", 344, 500)

# Game loop
while p1.health > 0:
    print("\n=== Magic Potion Game ===")
    action = input("What would you like to do? (drink_healing, drink_strength, refill, wand_material, increase_durability, power, quit): ")
    if len(p1.inventory) == "healing_potion":

        if action == "drink_healing":
            healing_potion.drink()
            healing_potion.taste()
            p1.health+=10
            p2.health+=10
        elif action == "drink_strength":
            strength_potion.drink()
            strength_potion.taste()
    else:
        print("You dont have this item")

    if action == "refill":
        choice = input("Refill which potion? (healing, strength): ")
        if choice == "healing":
            healing_potion.refill()
        elif choice == "strength":
            strength_potion.refill()
        else:
            print("Invalid choice.")

    elif action == "wand_materials":
        wand.made()
        
    
    elif action == "increase_durability":
        wand.incdurability()

    elif action == "power":
        wand.power()

    elif action == "quit":
        print("Exiting game.")
        break
    else:
        print("Invalid action.")
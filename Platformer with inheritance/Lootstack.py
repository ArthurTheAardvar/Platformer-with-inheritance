import random

class LootStack:
    def __init__(self):
        self.loot = []
        self.dict = {
            "Potions": 0,
            "Swords": 0,
            
            }
        
    def is_empty(self):
        return len(self.loot) == 0
    
    def push_loot(self, item):
        print(f"Acquired {item}!")
        self.loot.append(item)

        if self.loot.append == "sword":
            self.dict +=1
        print(self.dict)
    
    def pop_loot(self):
        if not self.is_empty():
            removed_item = self.loot.pop()
            print(f"Used {removed_item}.")
            return removed_item
        else:
            print("Your loot bag is empty!")
    
    def peek_loot(self):
        if not self.is_empty():
            return self.loot[-1]
        else:
            print("Your loot bag is empty!")

    #def dictionary(self):
        #self.nary = {
       #     "Portions":
        #    "Weapons":
       #     "Miscellaneous":
       # }


# Initialize LootStack object
player_loot = LootStack()

# Simple game loop for interaction
while True:
    print("\n=== Loot Bag Menu ===")
    print("1: Acquire new loot")
    print("2: Use loot")
    print("3: Check top loot item")
    print("4: Exit")
    choice = input("What would you like to do? ")

    if choice == '1':
        new_loot = input("Enter the name of the loot item you acquired: ")
        player_loot.push_loot(new_loot)
    elif choice == '2':
        player_loot.pop_loot()
    elif choice == '3':
        top_loot = random.randrange(len(player_loot.loot))
        if top_loot:
            print(f"The top loot item is: {top_loot}")
    elif choice == '4':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
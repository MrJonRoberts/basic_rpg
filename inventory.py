import random
from item import Item

class Inventory:

    def __init__(self, name, max_weight=20, max_vol=2, max_capacity=10):
        self.name = name
        self.max_weight = max_weight
        self.current_weight = 0
        self.max_vol = max_vol
        self.current_volume = 0
        self.max_capacity = max_capacity

        self.inventory = []
        self.current_capacity = len(self.inventory)


    # fucntion to add an item to the inventory.
    def add_item(self, item):
        # check weight
        if self.max_weight < self.current_weight + item.weight:
            print(f"Too much weight, you drop the {item.name}")
            return

        if self.max_vol < self.current_volume + item.vol:
            print(f"It wont fit. No matter how hard you shove, the {item.name} will not fit.")
            return

        if self.max_capacity < self.current_capacity + 1:
            print(f"You can only fit {self.max_capacity} items in your {self.name}. Get rid of something. Maybe {random.choice(self.inventory)}")
            return

        self.current_weight += item.weight
        self.current_volume += item.vol
        self.inventory.append(item)
        self.current_capacity = len(self.inventory)

    # function to show the inventory
    def show_inventory(self):
        inv = f"Inventory: {self.name}\n"
        if self.current_capacity > 0:
            inv += f"\tweight: {self.current_weight}\n"
            inv += f"\tTotal volume: {self.current_volume}\n"
            inv += f"\tTotal capacity: {self.max_capacity}\n"
            inv += len(f"Inventory: {self.name}") * "_" + "\n"
            for item in self.inventory:
                inv += f"\t{item.name}: {item.weight}\n"
            return inv
        else:
            return "Empty Inventory"

    def __str__(self):
        return self.show_inventory()
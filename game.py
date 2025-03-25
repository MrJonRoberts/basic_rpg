'''
basic OOP classes.

'''

from item import Item
from player import Player

# create a player.
name = input("What name do you want to be called?")
if name == "":
    name = "Unknown"
print(f"You will be known as : {name} and are 20 years old.")
# create the player - this comes from player __init__
player = Player(name, 20)

# output the player - this comes from player __str__
print(player)

# create an item
item1 = Item("Banana", "half rotten", 0.5, .2, .1, "junk")
print(f"You see a {item1.name} before you.")
print(f"You look closely and see that the {item1.name} is {item1.desc}")

# pick up the item - from player .pickup item.
player.pick_up_item(item1)
# output the player.
print(player)

# a heavy item
item_heavy = Item("Sword of Justice", "used to fight evil. It looks very expensive and heavy.", 1000, 20, 10, "Epic")
print(f"You see a {item_heavy.name} before you.")
print(f"You look closely and see that the {item_heavy.name} is {item_heavy.desc}")

player.pick_up_item(item_heavy)

print(player)
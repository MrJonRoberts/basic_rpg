from inventory import Inventory

'''
basic player class
'''
class Player:
    # constructor called player = Player("Fred", 20)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = Inventory("Backpack")


    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # used when we print(player)
    def __str__(self):
        return f'{self.name} is {self.age} years old\n {self.inventory}\n'

    # player.pick_up_item an item
    def pick_up_item(self, item):
        self.inventory.add_item(item)


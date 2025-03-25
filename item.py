

class Item:
    # create an item.
    # item = Item("Shoe", "a left shoe")
    # some default values
    def __init__(self, name, desc="", value=1, weight=1, vol=1, quality="Poor"):
        self.name = name
        self.desc = desc
        self.value = value
        self.weight = weight
        self.vol = vol
        self.quality = quality

    def __str__(self):
        return f"{self.name} {self.desc} {self.value} {self.weight} {self.vol} {self.quality}"
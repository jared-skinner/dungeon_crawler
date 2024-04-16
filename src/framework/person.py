from framework.item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

class Person:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()

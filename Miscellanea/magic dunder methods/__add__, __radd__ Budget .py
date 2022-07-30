class Budget:
    def __init__(self) -> None:
        self.list_item = []
    def add_item(self, it):
        self.list_item.append(it)
    def remove_item(self,indx):
        self.list_item.pop(indx)
    def get_items(self):
        return self.list_item
class Item:
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other , Item):
            return self.money + other.money
    def __radd__(self, other):
        if type(other) in (float, int):
            return other + self.money


class Thing:
    def __init__(self, name, mass) -> None:
        self.name : str = name
        self.mass = mass
    def __eq__(self, __o: object) -> bool:
        return self.name.lower() == __o.name.lower() and self.mass == __o.mass
    def __ne__(self, __o: object) -> bool:
        return self.name.lower() != __o.name.lower() or self.mass != __o.mass
    def __repr__(self) -> str:
        return f'{self.name} + {self.mass}'
class Box:
    def __init__(self) -> None:
        self.box = []
    def add_thing(self, obj: object):
        self.box.append(obj)
    def get_things(self):
        return self.box
    def __len__(self):
        return len(self.box)
    def __eq__(self, other: object) -> bool:
        if len(self) != len(other):
            return False
        for x in self.box:
            if x not in other.box:
                return False
        return True
    def __ne__(self, other: object) -> bool:
        return not self == other
b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print (res)
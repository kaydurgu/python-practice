class Animal:
    def __init__(self, name, old) -> None:
        self.name = name
        self.old = old
class Cat(Animal):
    def __init__(self,name, old, color, weight) -> None:
        super().__init__(name, old)
        self.color = color
        self.weight = weight
    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"

class Dog(Animal):
    def __init__(self, name, old, breed, size) -> None:
        super().__init__(name, old)
        self.breed = breed
        self.size = size
    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"
cat = Cat('кот', 4, 'black', 2.25)

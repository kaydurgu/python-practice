class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure
    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'
    def __repr__(self) -> str:
        return f'{self.name}: {self.volume}, {self.measure}'
    # название: объем, ед. изм.
    
class Recipe:
    def __init__(self,*args):
        self.rec = list(args)
    def add_ingredient(self, ing):
        self.rec.append(ing)
    def remove_ingredient(self,ing):
        self.rec.remove(ing)
    def get_ingredients(self):
        return tuple(self.rec)
    def __len__(self):
        return len(self.rec)
      
recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)


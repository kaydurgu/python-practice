

class InRange:
    def __init__(self, mn , mx) -> None:
        self.mn = mn 
        self.mx = mx
    def __checkout(self, value):
        return self.mn<=value<=self.mx
    def __set_name__(self, owner, name):
        self.name = '__'+ name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        if self.__checkout(value):
            return setattr(instance, self.name, value)
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    a = InRange(MIN_DIMENSION, MAX_DIMENSION)
    b = InRange(MIN_DIMENSION, MAX_DIMENSION)
    c = InRange(MIN_DIMENSION, MAX_DIMENSION)
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def __len__(self):
        return self.a * self.b * self.c
    def __gt__(self, other)-> bool:
        return len(self) > len(other)
    def __ge__(self, other)-> bool:
        return len(self) >= len(other)
    def __lt__(self, other)-> bool:
        return len(self) < len(other)
    def __le__(self, other)->bool:
        return len(self) <= len(other)

class ShopItem:
    def __init__(self, name, price , dim: Dimensions) -> None:
        self.name = name
        self.price = price
        self.dim = dim
    def __setattr__(self, __name: str, __value) -> None:
        if any([
            __name == 'name' and type(__value) == str , 
            __name == 'price' and type(__value) in (float, int ) , 
            __name == 'dim' and isinstance(__value, Dimensions)
            ]):
            object.__setattr__(self, __name, __value)
        else:
            raise ValueError(f'No there is attribute named{__name}')
    def __repr__(self) -> str:
        return f'{self.name}, {len(self.dim)}'

lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]
lst_shop_sorted = sorted(lst_shop, key= lambda x: x.dim)

for obj in lst_shop_sorted:
    print(f'{obj.name:12} {obj.dim.a * obj.dim.b * obj.dim.c}')
import sys

class ShopItem:
    def __init__(self, name, weight, price) -> None:
        self.name = name
        self.weight = weight
        self.price = price
    def __hash__(self) -> int:
        return hash((self.name.lower(), self.weight, self.price))
    def __eq__(self, __o: object) -> bool:
        return hash(self) == hash(__o)
    def __repr__(self) -> str:
        return f'{self.name}: {self.price}'

lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = dict()
temp_list = []
for x in lst_in:
    temp_list.append(ShopItem(x.split(':')[0], *x.split(':')[1].split()))

for x in temp_list:
    if shop_items.get(x, None) is None:
        shop_items[x] = [x , 1]
        continue
    temp = shop_items[x]
    temp[0], temp[1] = x, temp[1] + 1
    shop_items[x] = temp

print(shop_items)
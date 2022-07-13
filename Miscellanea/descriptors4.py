class StringValue:
    def validator(self, value):
        return type(value) is str and self.min_length<=len(value)<=self.max_length
    def __init__(self, min_length = 2, max_length = 50):
        self.min_length = min_length
        self.max_length = max_length
    def __set_name__(self, owner, name):
        self.name = '_'+ name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value
class PriceValue:
    
    def validator(self, value):
        return type(value) in (int ,float) and 0<=value<=self.max_value
    
    def __init__(self, max_value = 10000):
        self.max_value = max_value
    def __set_name__(self, owner, name):
        self.name = '_'+ name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value

class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)
    def __init__(self, name, price):
        self.name = name
        self.price = price

class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []
    def add_product(self, product):
        self.goods.append(product)
    def remove_product(self, product):
        self.goods.remove(product)

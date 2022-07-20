class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []
    def add_product(self , product: object):
        self.goods.append(product)
    def remove_product(self,product: object):
        self.goods.remove(product)
        
class Product:
    ids = 1
    def __init__(self, name, weight, price):
        self.id = None
        self.name = name
        self.weight = weight
        self.price = price
    def __setattr__(self, key, value):
        is_id : bool = False
        if key is 'id' and value is None:
            object.__setattr__(self, key, Product.ids)
            Product.ids += 1
            is_id = True
        elif key in ('id', 'price' ,'weight'):
            if type(value) not in (int,):
                raise TypeError("Неверный тип присваиваемых данных.")
            if value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in ('name',):
            if type(value) not in (str,):
                raise TypeError("Неверный тип присваиваемых данных.")
        if not is_id:
            object.__setattr__(self, key, value)
    def __delattr__(self, __name):
        if __name is 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, __name)
            

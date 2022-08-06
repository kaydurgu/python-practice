
class Thing:
    __id = 0
    def __init__(self, name, price, weight = None, dims = None, memory = None, frm = None) -> None:
        #required
        
        self.id = Thing.__id + 1
        self.name = name 
        self.price = price
        Thing.__id += 1

        #optional
        
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm
    def get_data(self):
        return  (self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm)

class Table(Thing):
    def __init__(self, name, price, weight, dims) -> None:
        super().__init__(name, price, weight=weight, dims=dims)
class ElBook(Thing):
    def __init__(self, name, price, memory, frm) -> None:
        super().__init__(name, price, memory = memory, frm = frm)

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
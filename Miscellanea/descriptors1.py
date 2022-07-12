class FloatValue:
    @classmethod
    def isFloat(cls, value):
        if type(value)!=float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
    def __set_name__(self, owner,name):
        self.name = '_'+name
    def __get__(self, instance ,onwer):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        self.isFloat(value)
        setattr(instance, self.name, value)
class Cell:
    value = FloatValue()
    def __init__(self, value):
        self.value = value
class TableSheet:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.cells = [[Cell(1.0 + j + i * m) for j in range(m)] for i in range(n)]

table = TableSheet(5, 3)




import math

class PositiveNumeric:
    @classmethod
    def checker(cls , value):
        if value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
    def __set_name__(self, owner, name):
        self.name = '__'+name
    def __set__(self, instance, value):
        PositiveNumeric.checker(value)
        instance.__dict__[self.name] = value
    def __get__(self, instance , owner):
        return instance.__dict__[self.name]
    

class Triangle:
    a = PositiveNumeric()
    b = PositiveNumeric()
    c = PositiveNumeric()
    @classmethod
    def isTriangle(cls, *args):
        lst = list(args)
        lst.sort()
        if not lst[0] + lst[1] > lst[2]:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
        Triangle.isTriangle(a,b,c)
    def __len__(self):
        return int (self.a + self.b +self.c)
    def __call__(self):
        p = len(self) / 2
        return math.sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))


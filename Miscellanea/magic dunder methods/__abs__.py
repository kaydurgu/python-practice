import math


class Complex:
    def __init__(self, real, img):
        self.real = real 
        self.img = img

    @classmethod
    def validator(cls, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")

    @property
    def real(self):
        return self.__real
    @real.setter
    def real(self, value):
        Complex.validator(value)
        self.__real = value
    
    
    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, value):
        Complex.validator(value)
        self.__img = value
    
    
    
    def __abs__(self):
        return math.sqrt(self.real ** 2+ self.img** 2)
    
cmp = Complex(7,8)

cmp.real = 3 
cmp.img = 4

c_abs = abs(cmp)

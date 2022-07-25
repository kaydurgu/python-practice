class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    def __init__(self, a, b, c):
        self.__a, self.__b, self.__c = None, None, None 
        self.a = a
        self.b = b
        self.c = c
    def validate(self, value):
        return Dimensions.MIN_DIMENSION<=value<=Dimensions.MAX_DIMENSION
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, value):
        if self.validate(value):
            self.__a = value
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, value):
        if self.validate(value):
            self.__b = value
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, value):
        if self.validate(value):
            self.__c = value  
    def __setattr__(self, __name: str, __value) -> None:
        if __name in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, __name, __value)
    def __getattr__(self,__name):
        return False

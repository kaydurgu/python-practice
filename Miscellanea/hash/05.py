
class Positive:
    @classmethod
    def check_numb(cls, NumberString):
        print (NumberString, type(NumberString))

    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance ,value):
        
        if float(value) <=0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

class Dimensions:
    a = Positive()
    b = Positive()
    c = Positive()
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def __hash__(self) -> int:
        return hash((self.a ,self.b ,self.c))
    def __gt__(self, other):
        return hash(self) > hash(other)
    def __ge__(self, other):
        return hash(self) >= hash(other)
    def __lt__(self, other):
            return hash(self) < hash(other)
    def __le__(self, other):
        return hash(self) <= hash(other)
    def __ne__(self, other):
            return hash(self) != hash(other)
    def __eq__(self, other):
        return hash(self) == hash(other)   
    def __repr__(self) -> str:
        return f'({self.a}, {self.b}, {self.c})'        
s_inp = input()
lst_dims  = s_inp.split(';')
print (lst_dims )
lst_dims  = [Dimensions(*x.split()) for x in lst_dims ]
lst_dims.sort()
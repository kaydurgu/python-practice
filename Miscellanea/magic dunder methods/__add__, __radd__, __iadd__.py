class ListMath:
    def __init__(self, arr = []) -> None:
        self.lst_math = [x for x in arr if type(x) in (int, float)]
    def __add__(self, other):
        return ListMath([x + other for x in self.lst_math])
    def __radd__(self, other):
        return ListMath([x + other for x in self.lst_math])
    def __iadd__(self, other):
        for x in range(len(self.lst_math)):
            self.lst_math[x] += other
        return self

    def __sub__(self,other):
        return ListMath([x - other for x in self.lst_math])
    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])
    def __isub__(self, other):
        for x in range(len(self.lst_math)):
            self.lst_math[x] -= other
        return self

    def __mul__(self, other):
        return ListMath([x * other for x in self.lst_math])
    def __rmul__(self, other):
        return ListMath([x * other for x in self.lst_math])
    def __imul__(self, other):
        for x in range(len(self.lst_math)):
            self.lst_math[x] *= other
        return self

    def __truediv__(self, other):
        return ListMath([x / other for x in self.lst_math])
    def __rtruediv__(self, other):
        return ListMath([other / x for x in self.lst_math]) 
    def __itruediv__(self, other):
        for x in range(len(self.lst_math)):
            self.lst_math[x] /= other
        return self


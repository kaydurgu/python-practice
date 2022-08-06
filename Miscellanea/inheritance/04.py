class Vector:
    def __init__(self, *args) -> None:
        self.args = list(args)
    def __repr__(self) -> str:

        return ' '.join([str(x) for x in self.args])

    def __len__(self):
        return len(self.args)
    def get_coords(self):
        return tuple(self.args)
    @classmethod
    def check(cls , first, second):
        if len(first) != len(second):
            raise ArithmeticError('размерности векторов не совпадают')
    def __eq__(self, other: object) -> bool:
        if len(self) != len(other):
            return False
        return all([self.args[i] == other.args[i] for i in range(len(self.args))])
    def __ne__(self, other: object) -> bool:
        Vector.check(self, other)
        return not self == other
    def __add__(self, other):
        if isinstance(other, (Vector,VectorInt)):
            Vector.check(self, other)
            if type(self)!=type(other):
                 return Vector(*[x + y for x, y in zip(self.args, other.args)])
            return type(self)(*[x + y for x, y in zip(self.args, other.args)])
        return type(self)(*[x + other for x in self.args])
    def __sub__(self, other):
        if isinstance(other,  (Vector,VectorInt)):
            Vector.check(self, other)
            return type(self)(*[x - y for x, y in zip(self.args, other.args)])
        return type(self)(*[x - other for x in self.args])    
    def __mul__(self, other):
        if isinstance(other,  (Vector,VectorInt)):
            type(self).check(self, other)
            return type(self)(*[x * y for x, y in zip(self.args, other.args)])
        return type(self)(*[x * other for x in self.args])  

    def __iadd__(self, other):
        if isinstance(other,  (Vector,VectorInt)):
            Vector.check(self, other)
            self.args = [x + y for x, y in zip(self.args, other.args)]
            return self
        self.args = [x + other for x in self.args]
        return self

    def __isub__(self, other):
        if isinstance(other,  (Vector,VectorInt)):
            Vector.check(self, other)
            self.args = [x - y for x, y in zip(self.args, other.args)]
            return self
        self.args = [x - other for x in self.args]
        return self
   
    def __imul__(self, other):
        if isinstance(other, (Vector,VectorInt)):
            Vector.check(self, other)
            self.args = [x * y for x, y in zip(self.args, other.args)]
            return self
        self.args = [x * other for x in self.args]
        return self

class VectorInt(Vector):
    def __init__(self, *args):
        for x in args:
            if not type(x) is int:
                raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)


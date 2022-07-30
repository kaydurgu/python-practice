class Box3D:
    def __init__(self, width, height, depth) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __str__(self) -> str:
        return f'{self.width}, {self.height}, {self.depth}'

    def __add__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width + other.width , self.height + other.height, self.depth + other.depth)
        elif isinstance(other, (int, float)):
            return Box3D(self.width + other, self.height + other, self.depth + other)
    def __radd__(self,other):
        if isinstance(other, (int, float)):
            return Box3D(self.width + other, self.height + other, self.depth + other)

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width - other.width , self.height - other.height, self.depth - other.depth)
        elif isinstance(other, (int, float)):
            return Box3D(self.width - other, self.height - other, self.depth - other)
    def __rsub__(self,other):
        if isinstance(other, (int, float)):
            return Box3D(other - self.width,other-self.height, other - self.depth)
    
    def __mul__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width * other.width , self.height * other.height, self.depth * other.depth)
        elif isinstance(other, (int, float)):
            return Box3D(self.width * other, self.height * other, self.depth * other)
    def __rmul__(self,other):
        if isinstance(other, (int, float)):
            return Box3D(other * self.width , other*self.height, other * self.depth)

    def __floordiv__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width // other.width , self.height // other.height, self.depth // other.depth)
        elif isinstance(other, (int, float)):
            return Box3D(self.width // other, self.height // other, self.depth // other)  
    def __rfloordiv__(self,other):
        if isinstance(other, (int, float)):
            return Box3D(other // self.width, other//self.height, other // self.depth) 

    def __mod__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width % other.width , self.height % other.height, self.depth % other.depth)
        elif isinstance(other, (int, float)):
            return Box3D(self.width % other, self.height % other, self.depth % other) 
    def __rmod__(self, other):
        if isinstance(other, (int, float)):
            return Box3D(other % self.width, other % self.height, other % self.depth)





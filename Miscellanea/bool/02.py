import math

class Line:
    def __init__(self, x1, y1, x2 ,y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def __len__(self):
        return math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)

#Если нету магического метода __bool__ ,проверяется __len__

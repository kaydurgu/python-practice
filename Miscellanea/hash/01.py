# hashable - только неизменяемые типы данных
'''
p1 = Point(1, 2)
p2 = Point(1, 2)

То есть, с точки зрения функции hash() – это два разных объекта. Но как она понимает, равные объекты или разные? Все просто. Если оператор сравнения:

print (p1 == p2)
'''
class PathLine:
    def __init__(self, dist, angle):
        self.dist = dist
        self.angle = angle

    def __eq__(self, other):
        return abs(self.dist) == abs(other.dist)
    def __hash__(self) -> int:
        return hash(self.dist)
p1 = PathLine(10, 1.57)
p2 = PathLine(-10, 0.49)
h1, h2 = hash(p1), hash(p2)

print (h1)
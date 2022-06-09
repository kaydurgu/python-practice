#abstraction - can be a skeleton of the classes  
#It allows you to create a set of methods that must be created within any child classes built from the abstract class
#all abstract methods from class should be initialized in subclass
#isinstance(object , class) -> boolean checks if object is instance of class
#issubclass(class1 , class1) -> boolean checks if class1 is subclass of class2


from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def perimetr(self):
        pass
class Square(Polygon):
    def __init__(self, side = None) -> None:
        self.__side = side
    @property
    def side(self):
        return self.__side
    @side.setter
    def side(self, val):
        self.__side = val
    def area(self):
        print ('Are of square is:',self.__side*self.__side)
    def sides(self):
        print ('Square has 4 sides')
    def perimetr(self):
        print('Perimetr is', 4 * self.__side )


class Rectancle(Polygon):
    def __init__(self, sideA = None ,sideB = None) -> None:
        self.__sideA = sideA
        self.__sideB = sideB
    @property
    def sideA(self):
        return self.__sideA
    @sideA.setter
    def side(self, val):
        self.__sideA = val
    @property
    def sideB(self):
        return self.__sideB
    @sideB.setter
    def sideB(self, val):
        self.__sideB = val




    def area(self):
        print ('Are of square is:',self.__side*self.__side)
    def sides(self):
        print ('Square has 4 sides')
    def perimetr(self):
        print('Perimetr is', 4 * self.__side )
a = Square(4)

a.area()
a.sides()
a.__side = 2
a.perimetr()
a.side = 3 
a.perimetr()
print(isinstance(a , Square))
print(issubclass(Square , Polygon))
#print (a.perimetr)
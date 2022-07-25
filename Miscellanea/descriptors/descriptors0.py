
class PositiveInteger:
    # self - ссылка на создаваемый экземпляр класса 
    # owner - ссылка на класс Point3D 
    # name - имя атрибута (для первого объекта x затем y, z)
    # instance в данном случае ссылка на объект pt


    # при присваивании автоматически срабатывает метод __set_name__, __set__
    # при считивании автоматическии срабатывает метод __get__

    @classmethod
    def IsPositive(cls, value):
        if value < 0:
            raise ValueError('Should be Positive Number')
    def __set_name__(self, owner, name):
        self.name = '_'+name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        #return instance.__dict__[self.name]
    def __set__(self, instance, value):
        self.IsPositive(value)
        setattr(instance,self.name, value)
        #instance.__dict__[self.name] = value

# лучше использовать getattr and setattr чисто питоновская хуйня 

class Point3D:
    x = PositiveInteger()
    y = PositiveInteger()
    z = PositiveInteger()
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
pt = Point3D(1, 2, 3)
print (pt.__dict__)
print (Point3D.__dict__)


# data-descriptor                     non-data descriptor
# По сути это геттеры и сеттеры но чтобы не писать геттер сеттер на каждый аттрибут мы 
# пишем descriptor

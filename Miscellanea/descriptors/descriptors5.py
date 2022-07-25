import functools
class String:
    @staticmethod
    def isString(value):
        if type(value) != str:
            raise ValueError('Должен быть str')
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        String.isString(value)
        setattr(instance ,self.name, value)
        
class IntOrFloat:
    @classmethod
    def isIntOrFloat(cls, value):
        if type(value) not in (int ,float):
            raise ValueError('Должен быть str или float')
    def __set_name__(self, instance, name):
        self.name = '_' + name
    def __get__(self, instance,owner):
        return getattr(instance ,self.name)
    def __set__(self, instance, value):
        self.isIntOrFloat(value)
        setattr(instance, self.name , value)
      
class Thing:
    name = String()
    weight = IntOrFloat()
    def __init__(self, name , weight):
        self.name = name
        self.weight = weight

      
class Bag:
    def __init__(self, max_weight):
        self.__initital = max_weight
        self.max_weight = max_weight
        self.__things = []
    @property
    def things(self):
        return self.__things
    def add_thing(self, thing):
        if self.max_weight - thing.weight >=0:
            self.max_weight-=thing.weight
            self.__things.append(thing)
    def remove_thing(self,thing):
        if thing in self.__things:
            self.max_weight+=thing.weight
            self.__things.remove(thing)
    def get_total_weight(self):
       return self.__initital-self.max_weight


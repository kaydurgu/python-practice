
class Singleton:
    _Single = None
    def __new__(cls , *args, **kwargs):
        if Singleton._Single is None:
            Singleton._Single = object.__new__(cls)
        return Singleton._Single

class Game(Singleton):
    def __init__(self, name) -> None:
        if self.__dict__.get('name', None) is None: 
            self.name = name
        '''
        or
        if not hasattr(self, 'name'):
            self.name=  name 
        '''
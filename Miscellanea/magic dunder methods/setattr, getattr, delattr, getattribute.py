class Book:
    def __init__(self, title = '', author='', pages= 0 , year = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
    def __setattr__ (self, key , value): # aвтоматически вызывается при изменении свойства key класса;
        if key in ('title', 'author'):
            if not type(value) is str:
                print ('str')
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in ('pages', 'year'):
            if not type(value) is int:
                print ('int')
                raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self,key ,value)
        
    def __getattr__(self, item): # автоматически вызывается при получении несуществующего свойства item класса;
        print ('__getattr__', item )
    
    def __delattr__(self, __name: str) -> None: # автоматически вызывается при удалении свойства item (не важно: существует оно или нет).
        print ('__delattr__', __name)
        object.__delattr__(self, __name)
    def __getattribute__(self, __name: str): # автоматически вызывается при получении свойства класса с именем item;
        print("__getattribute__", __name)
        return object.__getattribute__(self, __name)
        

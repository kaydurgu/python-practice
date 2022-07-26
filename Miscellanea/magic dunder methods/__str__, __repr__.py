class Model:
    def __init__(self):
        self.model = 'Model'
    def query(self,**kwargs):
        self.model +=':' + ', '.join([f"{k} = {v}" for k, v in kwargs.items()])
    def __str__(self):
        return self.model
#__str__() – магический метод для отображения информации об объекте класса для пользователей (например, для функций print, str);
#__repr__() – магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков).

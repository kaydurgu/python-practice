class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []
    def add_module(self, lesson):
        self.modules.append(lesson)
    def remove_module(self, indx):
        self.modules.pop(indx - 1)
class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []
    def add_lesson(self, lesson):
        self.lessons.append(lesson)
    def remove_lesson(self, indx):
        self.lessons.pop(indx - 1)
class LessonItem:
    def __init__(self, title  , practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration
    def __setattr__(self, key, value):
        if key in ('practices', 'duration',) and (type(value) != int or value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'title' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)
    def __getattr__(self, __name):
        return False
    def __delattr__(self, __name):
        if not __name in ('title' , 'practices', 'duration'):
            object.__delattr__(self, __name)

import functools
import datetime

def moment_zahoda(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        print (f'Время использования функции "{func.__name__}" {datetime.datetime.now()}')
    return wrapper
@moment_zahoda
def x():
    print('Функция x')
@moment_zahoda
def y():
    print ('Функция y')
x()
print()
y()
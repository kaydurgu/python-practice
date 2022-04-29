def say_hello(name):
    print (f'Приветик {name}')
def say_buy(name):
    print (f'Пока {name}')

def all(func):
    return func('Zhanbolot')

all(say_hello)
import functools

#twice functiom

def decorator_twice(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        func(*args , **kwargs)
        return func (*args , **kwargs)
    return wrapper
@decorator_twice
def say_end_return(name):
    print (f'Hello {name} with print')
    return (f'Hello {name} with return')

say_end_return('Zhanbolot')
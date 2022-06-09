import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        arg = [repr(i) for i in args]
        signature = ''.join(arg)
        #не стал пистаь signature на **kwargs
        print (f'Вызывается функция {func.__name__}({signature})')
        val = func(*args , **kwargs)
        print (f'{func.__name__}({signature}) возвращает {val}')
        return val
    return wrapper

@debug
def fact(n):
    if n == 1:
        return int(1)
    return n * fact(n - 1)
fact(5)
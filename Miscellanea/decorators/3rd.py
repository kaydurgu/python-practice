import functools
import time

#countdown with delap if from_number 

def slow_down(func):
    @functools.wraps(func)
    def wrapper(*args , **kwargs):
        time.sleep(1)
        func(*args , **kwargs)
    return wrapper
@slow_down
def count_down(from_number):
    if from_number < 1:
        print ('Поехали')
    else:
        print (from_number)
        count_down(from_number - 1)
count_down(5)
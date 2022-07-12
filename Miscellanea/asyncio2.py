import asyncio
import random
import time 

def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        print(end - start, 'time took to end function' ,func.__name__)
        return val 
    return wrapper
def task(pid):
    time.sleep(random.randint(0, 1))
    print (f'Task {pid} done')


async def task_cor(pid):
    await asyncio.sleep(random.randint(0, 1))
    print (f'Task {pid} done')
@timer
def synchronous():
    for i in range(1, 11):
        task(i)
@timer
async def asynchronous():
    task = [asyncio.ensure_future(task_cor(i)) for i in range(1,11)]
    await asyncio.wait(task)
print ('Synchronous')

synchronous()
start = time.time()
ioloop = asyncio.get_event_loop()
print ('Asynchronous')
ioloop.run_until_complete(asynchronous())
ioloop.close()
end = time.time()

print (end - start )


'''
Synchronous
Task 1 done
Task 2 done
Task 3 done
Task 4 done
Task 5 done
Task 6 done
Task 7 done
Task 8 done
Task 9 done
Task 10 done

6.031006813049316 time took to end function synchronous


Asynchronous
0.0 time took to end function asynchronous
Task 4 done
Task 8 done
Task 9 done
Task 10 done
Task 1 done
Task 3 done
Task 7 done
Task 6 done
Task 2 done
Task 5 done
1.0059022903442383

'''

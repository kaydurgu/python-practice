import random

PLUGINS = dict()

#registers all functions 

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Привет, {name}!"

@register
def be_awesome(name):
    return f"Привет, {name}, классно быть вместе!"

for key, val in PLUGINS.items():
    print (key , val('Zhanbolot'))
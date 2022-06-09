from json import load
from dotenv import load_dotenv
import os

class Person:
    def __init__(self , name ,surname) -> None:
        self.name = name
        self.surname = surname
    @property
    def fullname(self):
        return '{} + {}'.format(self.name , self.surname)

k = Person('Zhanbolot' , 'Bakytbek uulu')

print (k.fullname)
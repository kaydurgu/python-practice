from collections import namedtuple
from dataclasses import dataclass

pern = namedtuple("person", "name, age")

zhanbolot = pern('Zhanbolot', '21')

# same with namedtuples but dataclass is mutable 
# we can use @dataclass(frozen=True) do to class immutable 
@dataclass
class Kishi:
    name : str = None 
    surname : str = None
    age :int = 0
khan = Kishi('Zh', 'Ba' , 21)

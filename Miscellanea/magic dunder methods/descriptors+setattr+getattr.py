import time 

class PositveVeshes:
    @classmethod 
    def validator(cls, value):
        if not type(value) in (int, float,):
            return False
        if value <= 0:
            return False
        return True
    def __set_name__(self, owner, name):
        self.name = '_'+name
    def __get__(self, instance, owner): 
        return getattr(instance, self.name)
    def __set__(self, instance, value):
        if PositveVeshes.validator(value):
            setattr(instance, self.name, value)

class Mechanical:
    date = PositveVeshes()
    def __init__(self, date):
        self.date = date
    def __setattr__(self, key, value):
        if key in ('_date','date') and self.date == False:
            object.__setattr__(self, key, value)
    def __getattr__(self, __name):
        return False
            
class Aragon:
    date = PositveVeshes()
    def __init__(self,date):
        self.date = date
    def __setattr__(self, key, value):
        if key in ('_date','date') and self.date == False:
            object.__setattr__(self, key, value)
    def __getattr__(self, __name):
        return False
            
class Calcium:
    date = PositveVeshes()
    def __init__(self, date):
        self.date = date
    def __setattr__(self, key, value):
        if key in ('_date','date') and self.date == False:
            object.__setattr__(self, key, value)    
    def __getattr__(self, __name):
        return False
class GeyserClassic:
    MAX_DATE_FILTER = 100
    def __init__(self):
        self.slots = [None, None, None]
    def add_filter(self, slot_num, filter):
        if self.slots[slot_num - 1] == None:
            if slot_num == 1 and isinstance(filter, Mechanical):
                self.slots[0] = filter
            if slot_num == 2 and isinstance(filter, Aragon):
                self.slots[1] = filter
            if slot_num == 3 and isinstance(filter, Calcium):
                self.slots[2] = filter               
    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = None
    def get_filters(self):
        return tuple(self.slots)
    def water_on(self):
        for filter in self.slots:
            if not filter:
                return False
            if not (0<=time.time() - filter.date<=GeyserClassic.MAX_DATE_FILTER):
                return False
        return all(self.slots) 

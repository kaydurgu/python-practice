class CentralBank:
    def __new__(cls):
        return None
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
    registered = []
    @classmethod
    def register(cls, smth):
        smth.cb = CentralBank

class Money:
    type = None
    def __init__(self,volume) -> None:
        self.volume = volume
        self.cb = None
    @property
    def volume(self):
        return self.__volume
    @volume.setter
    def volume(self, volume):
        if type(volume) in (int ,float):
            self.__volume = volume

    @property
    def cb(self):
        return self.__cb
    @cb.setter
    def cb(self, cb):
            self.__cb = cb
    @classmethod
    def __convert(cls, money):
        if money.cb is None:
            raise ValueError("Неизвестен курс валют.")
        if money.type == 'rub':
            return money.__volume
        else:
            return money.__volume * money.cb.rates['rub'] 
    def __eq__(self, other: object) -> bool:
        return Money.__convert(self) == Money.__convert(other)
    def __ne__(self, other: object) -> bool:
        return Money.__convert(self) != Money.__convert(other)
    def __gt__(self, other: object) -> bool:
        return Money.__convert(self) > Money.__convert(other)    
    def __ge__(self, other: object) -> bool:
        return Money.__convert(self) >= Money.__convert(other)
    def __lt__(self, other: object) -> bool:
        return Money.__convert(self) < Money.__convert(other)
    def __le__(self, other: object) -> bool:
        return Money.__convert(self) <= Money.__convert(other)
class MoneyR(Money):
    type = 'rub'
class MoneyD(Money):
    type = 'dollar'
class MoneyE(Money):
    type = 'Euro'

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)
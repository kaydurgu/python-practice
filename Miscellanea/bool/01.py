import sys

class Player:
    def __init__(self, name:str,old : int, score :int) -> None:
        self.name = name
        self.old = old
        self.score = score
    def __repr__(self) -> str:
        return f'{self.name}:{self.score}'
    def __bool__(self):
        return bool(self.score)

lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']
lst_in = [Player(x.split('; ')[0], int (x.split('; ')[1]), int (x.split('; ')[2])) for x in lst_in]

players_filtered = list(filter(bool, lst_in))



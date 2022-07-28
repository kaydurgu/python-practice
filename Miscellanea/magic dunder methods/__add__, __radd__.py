from collections import Counter
class NewList:
    def __init__(self, arr = []):
        self.arr = arr
    def get_list(self):
        return self.arr
    @staticmethod
    def __subrack_list(take , me):
        mp = collections.defaultdict(int)
        new_arr = []
        for x in me:
            mp[x] = mp[x] + 1
        for x in take:
            flag : bool = True
            for y in me:
                if x == y and type(x) == type(y) and mp[x] > 0:
                    mp[x]-=1
                    flag = False
                    break                    
            if flag:
                new_arr.append(x)
        return new_arr
    def __sub__(self, other):
        if isinstance(other, type(self)):
            return NewList(NewList.__subrack_list(self.arr, other.arr))
        if isinstance(other, list): 
            return NewList(NewList.__subrack_list(self.arr, other))
    def __rsub__(self, other):
        return NewList(NewList.__subrack_list(other, self.arr))

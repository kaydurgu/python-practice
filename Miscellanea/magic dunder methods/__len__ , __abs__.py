import math
class RadiusVector:
    def __init__(self, *n):
        if len(n) == 1:
            self.coords = [ 0 ]*n[0]
        else:
            self.coords = list(n)
    def set_coords(self, *args):
        for i in range(min(len(self.coords), len(args))):
            self.coords[i] = args[i]
    def get_coords(self):
        return tuple(self.coords)
    def __abs__(self):
        return math.sqrt(sum([x ** 2 for x in self.coords]))
    def __len__(self):
        return len(self.coords)

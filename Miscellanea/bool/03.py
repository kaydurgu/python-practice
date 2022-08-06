
class Ellipse:
    def __init__(self, *args) -> None:
        if len(args):
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return bool(self.__dict__)
    def get_coords(self):
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2)
lst_geom = [Ellipse(),  Ellipse(2, 1, 2, 1), Ellipse(), Ellipse(5, 6, 7, 8)]
ek = Ellipse()
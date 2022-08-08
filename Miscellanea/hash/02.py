import sys
class BookStudy:
    def __init__(self, name, author, year) -> None:
        self.name = name
        self.author = author
        self.year = year
    def __hash__(self) -> int:
        return hash((self.name, self.author, ))
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = []
for x in lst_in:
    name, author, year = x.split('; ')
    lst_bs.append(BookStudy(name, author, year))
unique_books = len(set([hash(x) for x in lst_bs]))

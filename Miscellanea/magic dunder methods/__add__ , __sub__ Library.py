class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title
    
class Lib:
    def __init__(self, arr = []) -> None:
        self.book_list = arr
    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        if isinstance(other, Book):
            return Lib(self.book_list + [other])
    def __radd__(self, other):
        if isinstance(other, Book):
            return Lib([other]+self.book_list)        
    def __iadd__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
            return self

    def __sub__(self, other):
        if isinstance(other, Book):
            if other in self.book_list:
                self.book_list.remove(other)
            return Lib(self.book_list)
        elif isinstance(other, int):
            self.book_list.pop(other)
            return Lib(self.book_list)

    def __isub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif isinstance(other, int):
            self.book_list.pop(other)
        return self
b1 =  Book('Sherlock Holmes', 'Konan Doyle', '1892')
b2 = Book('Comrades', 'Chyngyz Aitmatov', '1975')
b3 = Book('Ak Keme', 'Chyngyz Aitmatov', '1945')

lib = Lib()

lib = lib + b1
lib = lib + b2
lib += b3

lib -= 1

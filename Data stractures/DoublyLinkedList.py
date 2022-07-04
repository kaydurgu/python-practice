class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None
    def set_next(self, obj):
        self.__next = obj
    def set_prev(self, obj):
        self.__prev = obj
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

class DoublyLinkedList:
    head = None
    tail = None
    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            if self.head == self.tail:
                self.tail = obj
                self.head.set_next(self.tail)
                self.tail.set_prev(self.head)
            else:
                self.tail.set_next(obj)
                self.tail.get_next().set_prev(self.tail)
                self.tail = self.tail.get_next()

    def remove_obj(self):
        if self.tail == self.head or self.head is None:
            self.tail = self.head = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
    def get_data(self):
        new, arr = self.head, []
        while new:
            arr.append(new.get_data())
            new = new.get_next()
        return arr


ob = ObjList("данные 1")

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))

lst.remove_obj()
lst.remove_obj()
lst.add_obj(ob)
print (lst.get_data())

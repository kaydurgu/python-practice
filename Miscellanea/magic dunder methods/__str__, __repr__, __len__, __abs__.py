class ObjList:
    def __init__(self, data) -> None:
        self.__data = data
        self.__prev = None
        self.__next = None
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value
    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self, value):
        self.__prev = value
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, value):
        self.__next = value
    def __str__(self) -> str:
        return self.__data

class LinkedList:
    def __init__(self) -> None:
    
        self.head = None
        self.tail = None
        self.elements = 0
    
    def add_obj(self, obj:ObjList):

        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            self.tail.next.prev = self.tail
            self.tail = obj
        self.elements+=1

    def show(self):

        head = self.head
        while head:
            print (head.data, end=' ')
            head = head.next
        print ()

    def remove_obj(self,indx):
        if self.elements == 1:
            self.head = None
            self.tail = None
        elif indx == 0:
            self.head = self.head.next
            self.elements -= 1
        else:
            head = self.head
            idx = 0
            while head:    
                if idx == indx:
                    if head == self.tail:
                        self.tail = self.tail.prev
                        self.tail.next = None
                    else:
                        head.prev.next = head.next
                        head.next.prev = head.prev
                    self.elements-=1
                    return 
                head = head.next
                idx += 1
    def __len__(self):
        return self.elements
    def __call__(self, indx):
        idx, head = 0, self.head
        while head:
            if indx == idx:
                return head.data
            head = head.next
            idx+=1
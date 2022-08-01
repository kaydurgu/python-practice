class StackObj:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data 
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj):
            self.__next = obj
        else:
            self.__next = None
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, new_value):
        self.__data = new_value
class Stack:
    def __init__(self, top = None) -> None:
        self.top = top
    def push_back(self, obj : StackObj):
        if self.top is None:
            self.top = obj
        else:
            root = self.top
            while not root.next is None:
                root = root.next
            root.next = obj

    def pop_back(self):
        if self.top is None or self.top.next is None:
            self.top = None
        else:
            root = self.top
            while root.next:
                root = root.next
            root.next = None


    def __add__(self , other):
        if isinstance(other, StackObj):
            root = Stack(self.top)
            root.push_back(other)
            return root

    def __iadd__(self, other):
        if isinstance(other, StackObj):
            self.push_back(other)
        return self
    
    def __mul__(self, other):
        if isinstance(other, list):
            root = Stack(self.top)
            for x in other:
                root.push_back(StackObj(x))
            return root
    def __imul__(self, other):
        if isinstance(other, list):
            for x in other:
                self.push_back(StackObj(x))
            return self
    def show(self):
        root = self.top
        while root:
            print (root.data, end = ' ')
            root = root.next
        print('\n')

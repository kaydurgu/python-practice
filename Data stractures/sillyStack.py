class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.prev = None
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, val):
        if isinstance(val, StackObj) or val is None:
            self.__next = val
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, val):
        self.__data = val
    
class Stack:
    def __init__(self):
        self.top = None
        self.last = None
    def push(self, Obj):
        if self.top is None:
            self.top = Obj
            self.last = Obj
        else:
            self.last.next = Obj
            self.last.next.prev = self.last
            self.last = self.last.next
    def pop(self):
        if self.top == self.last:
            self.top = None
            self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None
    def get_data(self):
        k = self.top
        arr = []
        while k:
            arr.append(k.data)
            k = k.next
        return arr
        
        
    
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()





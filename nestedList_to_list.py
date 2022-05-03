class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.new_list = []
        self.deletes(nestedList)
        print (self.new_list)
        
    def deletes(self, nestedlst: [NestedInteger]):
        for i in nestedlst:
            if i.isInteger():
                self.new_list.append(i.getInteger())
            else:
                self.deletes(i.getList())
    def next(self) -> int:
        return self.new_list.pop(0)
    def hasNext(self) -> bool:
        if len(self.new_list)>0:
               return True
        return False

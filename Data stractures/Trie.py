class Node:
    def __init__(self, me = '') -> None:
        self.me = me
        self.childrens = [None] * 26 
        self.whole_word = False
    def __repr__(self) -> str:
        return self.me
class Trie:
    
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for x in word:
            if root.childrens[ord(x) % 97]:
                root = root.childrens[ord(x) % 97]
                continue
            root.childrens[ord(x) % 97] = Node(x)
            root = root.childrens[ord(x) % 97]
        root.whole_word = True
    def search(self, word: str) -> bool:
        root = self.root
        for x in word:
            if root.childrens[ord(x) % 97] is None:
                return False
            root = root.childrens[ord(x) % 97]
        return root.whole_word
        
    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for x in prefix:
            if root.childrens[ord(x) % 97] is None:
                return False
            root = root.childrens[ord(x) % 97]
        return True

from venv import create


class Node:
    def __init__(self,val = None) -> None:
        self.left = None
        self.val = val
        self.right = None
    def __repr__(self) -> str:
        return f'Left: {self.left} | Value : {self.val} | Right : {self.right}'

class Tree:
    def __init__(self ,root = None) -> None:
        self.root = None
    def createNode(self, val)->Node:
        return Node(val)
    def insert(self, val):
        old = self.root
        if self.root == None:
            old = Node(val)
            self.root = Node(val)
        else:
            while True:
                if val < self.root.val:
                    if self.root.left == None:
                        self.root.left = Node(val)
                        break
                    else:
                        self.root = self.root.left
                else:
                    if self.root.right == None:
                        self.root.right = Node(val)
                        break
                    else:
                        self.root = self.root.right
        self.root = old
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print (root.val)
            self.inorder(root.right)
k = Node(5)
tree = Tree()

tree.insert(5)
tree.insert(721)
tree.insert(81)
tree.insert(9)


tree.inorder(tree.root)

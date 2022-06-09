from random import randint


class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.data = data
        self.right = None
        self.level = randint(1,20)

class Tree:
    def createNode(self, data):
        return Node(data)
    def insert(self, root : Node, data):
        if root == None:
            print (data)
            return Node(data)
        if data < root.data:

            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data , k.level)
            self.inorderTraversal(root.right)
k = Node(5)

tree = Tree()

tree.insert(k , 2)
tree.insert(k , 1)
tree.insert(k , 7)
tree.insert(k , 9)
tree.insert(k , 8)

tree.inorderTraversal(k)
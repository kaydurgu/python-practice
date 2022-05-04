class Node:
    def __init__(self, value):
        self.left = None 
        self.data = value
        self.right = None
class Tree:
    def createNode(self,value):
        return Node(value)
    def insert(self, node , data ):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    def display(self, node : Node):
        print (node.data)
    def inorder(self , root :Node):
        if root:
            self.inorder(root.left)
            self.display(root)
            self.inorder(root.right )


tree = Tree()
root = Node(5)

tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

tree.inorder(root)

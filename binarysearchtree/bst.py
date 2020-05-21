class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data)

             

       
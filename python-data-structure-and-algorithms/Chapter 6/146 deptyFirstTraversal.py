class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def preorder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder(current.left_child)
        self.preorder(current.right_child)
    
    def postorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.preorder(current.left_child)
        self.preorder(current.right_child)
        print(current.data)
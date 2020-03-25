RED = True
BLACK = False

class Node:
    def __init__(self, key, val, nodes, color=False, left=None, right=None):
        self.key = key
        self.val = val
        self.n = nodes
        self.color = color
        self.left = left
        self.right = right


class RedBlackBST:
    def __init__(self):
        self.root = None

    def isRed(self, node):
        return node is not None and node.color == RED

    def rotate_left(self, h):
        right = h.right
        h.right = right.left
        right.left = h
        right.color = h.color
        h.color = RED
        right.n = h.n
        h.n = 1 + h.left.n + h.right.n
        return right

    def rotate_right(self, h):
        left = h.left
        h.left = left.right
        left.right = h
        left.color = BLACK
        h.color = RED
        left.n = h.n
        h.n = 1 + h.left.n + h.right.n

    def flipColors(self, h):
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

    def get(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node.val
        elif node.key > key:
            return self.get(node.left, key)
        else:
            return self.get(node.right, key)

    def put(self, key, val):
        self.root = self.put(self.root, key, val)
        self.root.color = BLACK

    def put(self, node, key, val):
        if node is None:
            return Node(key, val, 1, RED)
        if node.key == key:
            node.val = val
        elif node.key < key:
            node.right = self.put(node.right, key, val)
        else:
            node.left = self.put(node.left, key, val)
        if self.isRed(node.right) and not self.isRed(node.left):
            self.rotate_left(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            self.rotate_right(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        node.n = node.left.n + node.right.n + 1
        return node

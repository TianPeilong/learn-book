class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

expr = '4 5 + 5 3 - *'.split()
stack = []

for term in expr:
    if term in '+-*/':
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(float(term))
    stack.append(node)

def cal(node):
    if node.data == '+':
        return cal(node.left) + cal(node.right)
    elif node.data == '-':
        return cal(node.left) - cal(node.right)
    elif node.data == '*':
        return cal(node.left) * cal(node.right)
    elif node.data == '/':
        return cal(node.left) / cal(node.right)
    else:
        return node.data

root_node = stack.pop()
print(cal(root_node))
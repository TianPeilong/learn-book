class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
    
    # different with book
    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        return None
    
    # different with book
    def peek(self):
        return self.top

def check_brackets(statement):
    stack = Stack()
    left_brackets = ['(', '[', '{']
    right_brackets = [')', ']', '}']
    for c in statement:
        if c in left_brackets:
            stack.push(c)
        if c in right_brackets:
            top = stack.pop()
            if top == '(' and c == ')':
                continue
            elif top == '[' and c == ']':
                continue
            elif top == '{' and c == '}':
                continue
            else:
                return False
    return stack.size == 0

sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)

for s in sl:
    m = check_brackets(s)
    print(f'{s}: {m}')
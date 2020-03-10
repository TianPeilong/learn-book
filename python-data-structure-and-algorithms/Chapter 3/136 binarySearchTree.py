class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current

    # different with book
    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            while current:
                if current.data > data:
                    if current.left_child is None:
                        current.left_child = node
                        break
                    else:
                        current = current.left_child
                else:
                    if current.right_child is None:
                        current.right_child = node
                        break
                    else:
                        current = current.right_child

    def get_node_with_parent(self, data):
        if self.root_node is None:
            return (None, None)
        parent = None
        current = self.root_node
        while current: # different
            if current.data == data:
                return (parent, current)
            elif data < current.data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (None, None)

    def remove(self, data):
        parent, current = self.get_node_with_parent(data)
        if current is None:
            return False
        count = 0
        if current.left_child:
            count += 1
        if current.right_child:
            count += 1
        if count == 0:
            if parent:
                if parent.left_child is current:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None
        elif count == 1:
            next_node = None
            if current.left_child:
                next_node = current.left_child
            else:
                next_node = current.right_child
            if parent:
                if parent.left_child is current:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_right_min_node = current
            right_min_node = current.right_child
            while right_min_node.left_child:
                parent_of_right_min_node = right_min_node
                right_min_node = right_min_node.left_child
            current.data = right_min_node.data
            if parent_of_right_min_node.left_child == right_min_node:
                parent_of_right_min_node.left_child = right_min_node.right_child
            else:
                parent_of_right_min_node.right_child = right_min_node.right_child
        return True

    def search(self, data):
        current = self.root_node
        if current is None:
            return None
        while current:
            if current.data == data:
                return current
            elif data < current.data:
                current = current.left_child
            else:
                current = current.right_child
        return current

tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)    
tree.insert(1)

for i in range(1, 10):
    found = tree.search(i)
    print(f'{i}: {found}')

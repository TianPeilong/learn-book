from collections import deque
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def breadth_first_travesal(self):
        list_of_nodes = []
        travesal_queue = deque([self.root_node])
        while len(travesal_queue) > 0:
            current = travesal_queue.popleft()
            list_of_nodes.append(current.data)
            if current.left_child:
                travesal_queue.append(current.left_child)
            if current.right_child:
                travesal_queue.append(current.right_child)
        return list_of_nodes
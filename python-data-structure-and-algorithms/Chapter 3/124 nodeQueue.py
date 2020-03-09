class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count  = 0

    def enqueue(self, data):
        node = Node(data)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        data = None
        if self.head:
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.count -= 1
        return data

        
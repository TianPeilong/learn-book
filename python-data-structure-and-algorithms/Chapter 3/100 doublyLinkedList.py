class Node:
    def __init__(self, data=None, next=None, pre=None):
        self.data = data
        self.next = next
        self.pre = pre

class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        # different with book
        elif current == self.tail:
            if current.data == data:
                self.head = None
                self.tail = None
                node_deleted = True
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.pre.next = current.next
                    current.next.pre = current.pre
                    node_deleted = True
                    break
                current = current.next
        if node_deleted:
            self.count -= 1

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def contain(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False # different with book

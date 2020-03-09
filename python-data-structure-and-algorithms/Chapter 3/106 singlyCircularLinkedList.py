class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1

    def size(self):
        '''
        count = 0
        current = self.tail
        while current:
            current = current.next
            count += 1
        return count
        '''
        return self.size

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val
    
    # different with book
    def delete(self, data):
        current = self.tail
        pre = self.tail
        while current:
            if current.data == data:
                if self.tail == self.head:
                    self.tail = None
                    self.head = None
                elif current == self.tail:
                    self.tail = current.next
                    self.head = self.tail
                elif current == self.head:
                    self.head = pre
                    self.head.next = self.tail
                else:
                    pre.next = current.next
                self.size -= 1
                break
            if current == self.tail:
                break
            else:
                current = current.next
                pre = current

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
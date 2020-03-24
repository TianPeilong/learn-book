class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class SequentialSearchST:
    def __init__(self, head=None):
        self.head = None
    
    def get(self, key):
        cur = self.head
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return None

    def put(self, key, val):
        cur = self.head
        while cur:
            if cur.key == key:
                cur.val = val
                return
            cur = cur.next
        self.head = Node(key, val, self.head)

class SeperateChainingHashST:
    def __init__(self, m=997):
        self.m = m
        self.st = [SequentialSearchST() for i in range(m)]

    def _hash(self, key):
        return (hash(key) & 0x7fffffff) % self.m
    
    def get(self, key):
        return self.st[self._hash(key)].get(key)
    
    def put(self, key, val):
        self.st[self._hash(key)].put(key, val)

st = SeperateChainingHashST()
for i in range(2000):
    st.put(i, str(i))

for i in range(2000):
    print(st.get(i))
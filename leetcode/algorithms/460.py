class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.count = 0
        self.dic = {}

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            node.count += 1
            self._check(node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            node.count += 1
            self._check(node)
        else:
            node = Node(key, value=value)
            self.dic[key] = node
            self.count += 1
            if not self.head:
                self.head = node
                self.tail = node
            else:
                if self.count <= self.capacity:
                    node.pre = self.tail
                    self.tail.next = node
                    self.tail = node
                    self._check(node)
                else:
                    del self.dic[self.tail.key]
                    if not self.tail.pre:
                        self.head = node
                        self.tail = node
                    else:
                        pre = self.tail.pre
                        node.pre = pre
                        pre.next = node
                        self.tail = node
                        self._check(node)
                    self.count -= 1

    def _check(self, node):
        while node.pre:
            pre = node.pre
            if pre.count <= node.count:
                self._switch(pre, node)
            else:
                break

    def _switch(self, pre, cur):
        if not cur.next:
            self.tail = pre
        cur.pre = pre.pre
        pre.pre = cur
        pre.next = cur.next
        cur.next = pre
        if cur.pre:
            cur.pre.next = cur
        else:
            self.head = cur
        if pre.next:
            pre.next.pre = pre

class Node:
    def __init__(self, key, value=None, count=1, pre=None, next=None):
        self.key = key
        self.value = value
        self.count = count
        self.pre = None
        self.next = None

# 
#["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
#[[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]

cache = LFUCache(3)

cache.put(2,2)
cache.put(1,1)
cache.get(2)
cache.get(1)
cache.get(2)
cache.put(3,3)
cache.put(4,4)
cache.get(3)
cache.get(2)
cache.get(1)
cache.get(4)

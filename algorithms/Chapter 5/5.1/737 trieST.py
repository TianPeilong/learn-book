R = 26
ord_a = ord('a')

class Node:
    def __init__(self, val=None):
        self.val = None
        self.next = [None] * R

class TrieST:
    def __init__(self):
        self.root = Node()
    
    def put(self, s, val):
        self._put(self.root, s, val, 0)
    
    def _put(self, node, s, val, d):
        if node is None:
            node = Node()
        if d >= len(s):
            node.val = val
        else:
            pos = ord(s[d])-ord_a
            node.next[pos] = self._put(node.next[pos], s, val, d+1)
        return node

    def get(self, s):
        node = self._get(self.root, s, 0)
        if node is None:
            return None
        return node.val
    
    def _get(self, node, s, d):
        if node is None:
            return None
        if d == len(s):
            return node
        pos = ord(s[d])-ord_a
        return self._get(node.next[pos], s, d+1)

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        count = 0
        if node.val:
            count += 1
        for child in node.next:
            count += self.size(child)
        return count

    def collect(self, node, pre, result):
        if node is None:
            return
        if node.val:
            result.append(pre)
        for i,child in enumerate(node.next):
            if child:
                next_pre = pre + chr(i)
                self.collection(child, next_pre, result)
    
    def keysWithPrefix(self, pre):
        arr = []
        node = self._get(self.root, pre, 0)
        self.collect(node, pre, arr)
        return arr

    def keys(self):
        return self.keysWithPrefix('')

    def longestPrefixOf(self, s):
        l = self._search(self.root, s, 0, 0)
        return s[:l]

    def _search(self, node, s, d, length):
        if node is None:
            return length
        if node.val:
            length = d
        if len(s) == d:
            return length
        pos = ord(s[d])-ord_a
        return self._search(node.next[pos], s, d+1, length)
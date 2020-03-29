from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'
        q = deque()
        q.append([root])
        result = []
        while q:
            hasChild = False
            nodes = q.popleft()
            next_nodes = []
            for cur in nodes:
                if cur is None:
                    result.append('null')
                else:
                    result.append(str(cur.val))
                    next_nodes.append(cur.left)
                    next_nodes.append(cur.right)
                    if cur.left or cur.right:
                        hasChild = True
            if hasChild:
                q.append(next_nodes)
        while result[-1] == 'null':
            result.pop()
        s = ','.join(result)
        return '[' + s + ']'
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:len(data)-1]
        vals = []
        for s in data.split(','):
            if s != 'null':
                vals.append(int(s))
            else:
                vals.append(None)
        root = TreeNode(vals[0])
        i = 0
        q = deque()
        q.append(root)
        n = len(vals)
        while q:
            p = q.popleft()
            i += 1
            if i >= n:
                break
            l = vals[i]
            if l:
                p.left = TreeNode(l)
                q.append(p.left)
            i += 1
            if i >= n:
                break
            r = vals[i]
            if r:
                p.right = TreeNode(r)
                q.append(p.right)
        return root
            
# Your Codec object will be instantiated and called as such:
codec = Codec()

#### code here
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        def get(s1, s2):
            if len(s1) == 1:
                return ord(s2) - ord(s1) + 1
            if s2[0] == s1[0]:
                return get(s1[1:], s2[1:])
            a1 = s1[0]
            for c in range(len(s1)-1):
                a1 += 'z'
            a2 = s2[0]
            for i in range(len(s2)-1):
                a2 += 'a'
            return get(s1, a1) + (ord(s2) - ord(s1) - 1)*((26**(len(s1)-1))%(10**9 + 7)) + get(a2,s2)

        if len(evil) == n:
            if evil < s1 or evil > s2:
                return get(s1, s2) % (10**9 + 7)
            else:
                return (get(s1,evil) + get(evil,s2)-2) % (10**9 + 7)
        else:
            eN = len(evil)
            eCount = 0
            if evil < s1[:eN] or evil > s2[eN]:
                return (ord(s2[0])-ord(s1[0])) * self.findGoodStrings(n-1, s1[1:n], s2[1:n], evil)
        
        eN = len(s1) - len(evil)
        eCount = 1 if eN == 0 else (eN + 1) * (26 ** eN)
    


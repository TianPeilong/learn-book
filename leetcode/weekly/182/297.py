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
s = '[1,2,3,null,null,4,5]'
#codec.deserialize(codec.serialize(root))
print(codec.serialize(codec.deserialize(s)))
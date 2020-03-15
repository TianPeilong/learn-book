# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        data = []
        self.pre(root, data)
        new_root = self.re_order(data)
        q = deque([new_root])
        result = []
        while q:
            cur = q.popleft()
            if cur:
                result.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                result.append(None)
        return result
        
    
    def pre(self, root, data):
        if root is None:
            return
        if root.left:
            self.pre(root.left, data)
        data.append(root.val)
        if root.right:
            self.pre(root.right, data)
            
    def re_order(self, data):
        if not data:
            return None
        if len(data) < 2:
            node = TreeNode(data[0])
            return node
        mid = len(data) // 2
        root = TreeNode(data[mid])
        left = self.re_order(data[:mid])
        right = self.re_order(data[mid+1:])
        root.left = left
        root.right = right
        return root

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
t = Solution()
print(t.balanceBST(root))
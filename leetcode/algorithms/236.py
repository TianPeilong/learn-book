# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node:
                return 0, None
            ln,lp = dfs(node.left,p,q)
            if lp:
                return ln, lp
            rn,rp = dfs(node.right,p,q)
            if rp:
                return rn,rp
            cur = ln + rn
            if node.val == p:
                cur += 1
            if node.val == q:
                cur += 2
            if cur == 3:
                return 3,node.val
            else:
                return cur,None
        v,re = dfs(root,p,q)
        return re

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
s = Solution()
print(s.lowestCommonAncestor(root, 5,1))
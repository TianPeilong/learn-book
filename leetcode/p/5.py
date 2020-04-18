from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        c,b = self.dfs(root)
        return c + b
    
    def dfs(self, root):
        if not root:
            return 0,0
        cl,bl = self.dfs(root.left)
        cr,br = self.dfs(root.right)
        if cl < cr:
            cl, bl, cr, br = cr, br, cl, bl
        b = bl + cr
        c = 0
        if br >= (cl - cr) / 2:
            b += (br + (cl - cr) / 2)
        else:
            c = cl - cr - 2 * br
            b += 2 * br
        return c+root.val,b


root = TreeNode(47)
root.left = TreeNode(74)
root.right = TreeNode(31)


'''
root = TreeNode(15)
root.left = TreeNode(21)
root.left.left = TreeNode(24)
root.left.left.right = TreeNode(26)
root.left.left.left = TreeNode(27)
'''
'''
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(4)
'''
s = Solution()
m = s.minimalExecTime
cases = [
    [root]
]

for case in cases:
    print(m(*case))
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        nodes  = [root]
        while nodes:
            post = []
            vals = []
            for n in nodes:
                if n is None:
                    vals.append(None)
                else:
                    vals.append(n.val)
                    post.append(n.left)
                    post.append(n.right)
            i = 0
            j = len(vals) - 1
            while i <= j:
                if vals[i] != vals[j]:
                    return False
                i += 1
                j -= 1
            nodes= post
        return True

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

print(s.isSymmetric(root))
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        depth = self.get_depth(root)
        width = 2 ** depth - 1
        result = [[''] * width] * depth
        self.fill(root, 0, width-1, result, 0)
        return result

    def get_depth(self, root):
        if root is None:
            return 0
        lw = self.get_depth(root.left)
        rw = self.get_depth(root.right)
        return lw+1 if lw > rw else rw+1

    def fill(self, root, l, r, result, d):
        if root is None:
            return
        mid = (l+r)//2
        result[d][mid] = root.val
        self.fill(root.left, l, mid-1, result, d+1)
        self.fill(root.right, mid+1, r, result, d+1)

root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

s = Solution()
print(s.printTree(root))
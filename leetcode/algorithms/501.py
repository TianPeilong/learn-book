# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.result = []
        self.last_count  = 0
        self.count = 0
        self.last = None
        cur = root
        while cur:
            if cur.left is None:
                self.process(cur)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right is not None and pre.right != cur:
                    pre = pre.right
                if pre.right == cur:
                    pre.right = None
                    self.process(cur)
                    cur = cur.right
                else:
                    pre.right = cur
                    cur = cur.left
        if self.count > self.last_count:
            self.result = [self.last]
        elif self.count == self.last_count:
            self.result.append(self.last)
        return self.result

    def process(self, curNode):
        if curNode.val == self.last:
            self.count += 1
        else:
            if self.count > self.last_count:
                self.result = [self.last]
                self.last_count = self.count
            elif self.count == self.last_count:
                self.result.append(self.last)
            self.last = curNode.val
            self.count = 1

s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

print(s.findMode(root))
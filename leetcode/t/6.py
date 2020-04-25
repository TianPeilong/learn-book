from typing import List

class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        if len(value) < 3:
            return 0
        les = [set() for i in range(len(value))]
        for edge in edges:
            les[edge[0]].add(edge[1])
            les[edge[1]].add(edge[0])
        d = {i:v for i,v in enumerate(value)}
        d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        m = 0
        maxm = 0
        for j in range(len(d)):
            find = False
            if j < 5:
                if len(d) < 5:
                    maxm = sum([item[1] for item in d])
                else:
                    maxm = sum([item[1] for item in d[:5]])
            else:
                maxm = sum([item[1] for item in d[:4]]) + d[j][1]
            i = d[j][0]
            if len(les[i]) < 2:
                continue
            curs = []
            for j in les[i]:
                s = les[i] & les[j]
                for k in s:
                    curs.append(set([j,k]))
            lcurs = len(curs)
            if lcurs == 0:
                continue
            elif lcurs == 1:
                c = lcurs[0]
                m = max(m,value[i] + value[c[0]] + value[c[1]])
                if m >= maxm:
                    find = True
                    break
            else:
                for j in range(lcurs-1):
                    if find:
                        break
                    for k in range(j+1,lcurs):
                        s = curs[j] | curs[k]
                        sumv = value[i]
                        for ind in s:
                            sumv += value[ind]
                        m = max(m, sumv)
                        if m >= maxm:
                            find = True
                            break
            if find:
                break
        return m

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
m = s.maxWeight

cases = [
    [[[0,1],[1,2],[0,2]],[1,2,3]],
    [[[0,2],[2,1]], [1,2,5]],
    [[[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]], [7,8,6,8,9,7]]
]
'''
cases = [
    [[[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]], [7,8,6,8,9,7]]
]
'''
for case in cases:
    print(m(*case))
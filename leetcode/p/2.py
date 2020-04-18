from typing import List

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        re = [[] for i in range(n)]
        for r in relation:
            re[r[0]].append(r[1])
        pre = {}
        for i in re[0]:
            pre[i] = 1
        k -= 1
        while k > 0:
            k -= 1
            cur = {}
            for ke, count in pre.items():
                for i in re[ke]:
                    if i not in cur:
                        cur[i] = count
                    else:
                        cur[i] += count
            pre = cur
        t = n -1 
        if t in pre:
            return pre[t]
        else:
            return 0 
s = Solution()
m = s.numWays
cases = [
    [5,[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3],
    [3, [[0,2],[2,1]], 2]
]

for case in cases:
    print(m(*case))
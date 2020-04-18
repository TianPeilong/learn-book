from typing import List

class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        n = len(requirements)
        day = 0
        reqs = [[i,val] for i, val in enumerate(requirements)]
        reqa = [None] * 3
        m = 0
        while m < 3:
            reqa[m] = sorted([[i,val[m]] for i, val in enumerate(requirements)], key=lambda x:x[1])
            m += 1
        re = [-1] * len(requirements)
        pty = [0, 0, 0]
        sa = [set(), set(), set()]
        cur = [0,0,0]
        j = 0
        while j < 3:
            while cur[j] < n:
                if pty[j] >= reqa[j][cur[j]][1]:
                    sa[j].add(reqa[j][cur[j]][0])
                    cur[j] += 1
                else:
                    break
            j += 1
        curre = sa[0] & sa[1] & sa[2]
        for s in curre:
            i = 0
            while i < 3:
                sa[i].discard(s)
                i += 1
            re[s] = day
        for inc in increase:
            day += 1
            i = 0
            while i < 3:
                pty[i] += inc[i]
                i += 1
            j = 0
            while j < 3:
                while cur[j] < n:
                    if pty[j] >= reqa[j][cur[j]][1]:
                        sa[j].add(reqa[j][cur[j]][0])
                        cur[j] += 1
                    else:
                        break
                j += 1
            curre = sa[0] & sa[1] & sa[2]
            for s in curre:
                i = 0
                while i < 3:
                    sa[i].discard(s)
                    i += 1
                re[s] = day
        return re
            

s = Solution()
m = s.getTriggerTime
cases = [
    [[[2,8,4],[2,5,0],[10,9,8]], [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]],
    [[[0,4,5],[4,8,8],[8,6,1],[10,10,0]], [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]],
    [[[0,0,0]], [[0,0,0]]]
]

for case in cases:
    print(m(*case))
from typing import List

class Solution:
    def minJump(self, jump: List[int]) -> int:
        if len(jump) < 2:
            return 1
        dic = {}
        n = len(jump)
        for i, val in enumerate(jump):
            next = i + val
            if next > n:
                next = n
            if next not in dic:
                dic[next] = [i]
            else:
                dic[next].append(i)
        count = 0
        cur = [0] * (n+1)
        mv = n
        premv = n + 1
        while True:
            if cur[0] == 1 or mv == 0:
                break
            nmv = mv
            count += 1
            for i,v in enumerate(cur[:mv]):
                if v == 1:
                    if i < nmv:
                        nmv = i
                    if i in dic:
                        pre = dic[i]
                        for p in pre:
                            cur[p] = 1
            for i in range(mv, premv):
                if i in dic:
                    pre = dic[i]
                    for p in pre:
                        cur[p] = 1
            premv = mv
            mv = nmv
        return count

s = Solution()
m = s.minJump
cases = [
[[2, 5, 1, 1, 1, 1]],
[[1, 1, 1, 1, 1, 1]]
]

for case in cases:
    print(m(*case))
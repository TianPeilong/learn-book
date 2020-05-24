from typing import List

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        i = 0
        full = 0
        while i < 40:
            full |= (1 << i)
            i += 1
        hs = []
        for h in hats:
            rh = 0
            for c in h:
                rh |= (1 << (c-1))
            hs.append(rh)
        def ways(hs):
            if not hs:
                return 1
            if len(hs) == 1:
                count = 0
                cur = hs[0]
                while cur:
                    if cur & 1 == 1:
                        count += 1
                    cur = (cur >> 1)
                return count
            f = hs[0]
            if f & full == 0:
                return 0
            i = 0
            cur = 0
            count = 0
            while i < 40:
                cur = (1 << i)
                if f & cur != 0:
                    lefts = [(l | cur) ^ cur for l in hs[1:]]
                    count += ways(lefts)
                i += 1
            return count
            
        return ways(hs)

s = Solution()
m = s.numberWays
cases = [
    [[3,4],[4,5],[5]],
     [[3,5,1],[3,5]],
     [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]],
     [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]],
     [[1,2,3,4,5,7,9,11,12,13,17,18,19,20,21,22,23,24,25],[1,2,3,4,5,6,7,8,9,12,13,14,15,16,18,20,21,22,24,25],[2,3,7,12,13,15,19,22,23,24],[6,9,11,12,14,15,16,17,20,22,24,25],[10],[19,21,24],[1,3,5,6,8,10,11,13,14,15,16,17,18,20,22,24,25],[3,7,9]]
]

# 8808050
for case in cases:
    print(m(case))
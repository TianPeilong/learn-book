from typing import List

class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        def sa(a, b, c):
            return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0])
        s = [set() for i in range(len(points))]
        d = []
        left = set([i for i in range(len(points))])
        p = 0
        while p < len(points):
            if p < 2:
                for i in left:
                    if i not in s[p]:
                        d.append(i)
                        s[p].add(i)
                        left.discard(i)
                        p += 1
                        break
            else:
                curDir = direction[p-2]
                success = False
                for i in left:
                    if i not in s[p]:
                        lrs = sa(points[d[p-2]], points[d[p-1]], points[i])
                        if (lrs > 0 and curDir == 'L') or (lrs < 0 and curDir == 'R'):
                            s[p].add(i)
                            d.append(i)
                            left.discard(i)
                            p += 1
                            success = True
                            break
                if not success:
                    s[p] = set()
                    p -= 1
                    left.add(d.pop())
        return d


s = Solution()
m = s.visitOrder
cases = [
    [[[1,1],[1,4],[3,2],[2,1]], "LL"],
    [[[1,3],[2,4],[3,3],[2,1]], "LR"]
]

for case in cases:
    print(m(*case))
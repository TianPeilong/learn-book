from typing import List

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        f = 0
        a = []
        for r in mat:
            f += r[0]
            a.append(r[0])
        if len(mat[0]) < 2:
            return f
        re = []
        for r, row in enumerate(mat):
            pre = row[0]
            for v in row[1:]:
                re.append((v-pre,r,v))
        s = sorted(re, key=lambda x:x[0])
        i = 0
        while k > 1:
            cur = s[i]
            a[cur[1]] = cur[2]
            k -= 1
            i += 1
        return sum(a)

s = Solution()
m = s.kthSmallest
cases = [
    [[[1,3,11],[2,4,6]],5],
]

# 8808050
for case in cases:
    print(m(*case))
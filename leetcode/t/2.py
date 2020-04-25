from typing import List

class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        mt = [[0 for j in range(len(time)+1)] for i in range(len(time)+1)]
        for e in range(1, len(time)+1):
            mt[0][e] = max(mt[0][e-1], time[e-1])
        for s in range(1,len(time)+1):
            for e in range(s, len(time)+1):
                mt[s][e] = max(mt[s][e-1], time[e-1])

        t = [[] for i in range(m+1)]
        for i in range(m+1):
            for j in range(len(time)+1):
                t[i].append(0)
        s = []
        s.append(0)
        ma = []
        ma.append(0)
        for i in range(1, len(time)+1):
            s.append(s[i-1]+time[i-1])
            ma.append(max(ma[i-1], time[i-1]))
        for i in range(1,len(time)+1):
            t[1][i] = s[i] - ma[i]
        for i in range(2,m+1):
            for j in range(1,len(time)+1):
                mi = float('inf')
                for k in range(j):
                    mi = min(mi, max(t[i-1][k], s[j]-s[k]-mt[k+1][j]))
                t[i][j] = mi
        return t[m][len(time)]


s = Solution()
m = s.minTime
cases = [
    [[1,2,3,3], 2],
    [[999,999,999], 4]
]

for case in cases:
    print(m(*case))
from typing import List

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > m:
            return 0
        count = 0
        curc = 1
        for i in range(k,m):
            curc = 1
            j = m
            while i >= 1:



s = Solution()
m = s.minCount
cases = [
    
]

for case in cases:
    print(m(case))
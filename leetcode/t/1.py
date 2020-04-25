from typing import List



s = Solution()
m = s.minCount
cases = [
    [4,2,1],
    [2,3,10]
]

for case in cases:
    print(m(case))
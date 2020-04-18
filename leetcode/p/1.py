from typing import List
class Solution:
    def minCount(self, coins: List[int]) -> int:
        count = 0
        if not coins:
            return count
        for c in coins:
            count += ((c // 2) + (c % 2))
        return count

s = Solution()
m = s.minCount
cases = [
    [4,2,1],
    [2,3,10]
]

for case in cases:
    print(m(case))
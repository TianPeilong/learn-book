from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        st = 0
        sr = 0
        sc = 0
        n = len(grid)
        for r in grid:
            pre = 0
            for c in r:
                sr += abs(c - pre)
                pre = c
                if c != 0:
                    st += 1
            sr += r[-1]
        for col in range(n):
            pre = 0
            for row in range(n):
                sc += abs(grid[row][col]-pre)
                pre = grid[row][col]
            sc += grid[n-1][col]
        return 2*st + sr + sc

s = Solution()
grid = [[2,2,2],[2,1,2],[2,2,2]]
print(s.surfaceArea(grid))
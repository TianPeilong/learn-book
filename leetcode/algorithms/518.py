from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for am in range(coin, amount+1):
                dp[am] += dp[am-coin]
        return dp[-1]

s = Solution()
print(s.change(5, [5,2,1]))